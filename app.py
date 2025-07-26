from flask import Flask, render_template, request, redirect, session
import requests
import html
import random

app = Flask(__name__)
app.secret_key = 'vihu3232'
leaderboard_data = []  


@app.route('/')
def index():
    # Fetch available categories dynamically
    try:
        response = requests.get('https://opentdb.com/api_category.php')
        categories = response.json().get('trivia_categories', [])
    except Exception:
        categories = []

    return render_template('index.html', categories=categories)


@app.route('/question', methods=['POST', 'GET'])
def question():
    if request.method == 'POST':
        if 'difficulty' in request.form:
            difficulty = request.form.get('difficulty')
            category = request.form.get('category')

            session['difficulty'] = difficulty
            session['category'] = category

            # Build the API URL
            api_url = f'https://opentdb.com/api.php?amount=10&type=multiple&difficulty={difficulty}'
            if category:
                api_url += f'&category={category}'

            # Fetch questions
            response = requests.get(api_url)
            data = response.json()

            questions = []
            for item in data['results']:
                question = {
                    'question': html.unescape(item['question']),
                    'correct': html.unescape(item['correct_answer']),
                    'choices': [html.unescape(ans) for ans in item['incorrect_answers']] + [html.unescape(item['correct_answer'])]
                }
                random.shuffle(question['choices'])
                questions.append(question)

            session['questions'] = questions
            session['current'] = 0
            session['score'] = 0

            # Get category name for display
            cat_list = requests.get('https://opentdb.com/api_category.php').json().get('trivia_categories', [])
            category_name = next((c['name'] for c in cat_list if str(c['id']) == category), 'Any Category')
            session['category_name'] = category_name

        elif 'answer' in request.form:
            selected = request.form.get('answer')
            index = session.get('current', 0)
            correct = session['questions'][index]['correct']

            if selected == correct:
                session['score'] += 1

            session['current'] += 1

            if session['current'] >= len(session['questions']):
                return redirect('/result')

    if 'questions' not in session or 'difficulty' not in session:
        return redirect('/')

    index = session['current']
    question = session['questions'][index]

    return render_template(
        'question.html',
        question=question,
        index=index + 1,
        total=len(session['questions']),
        difficulty=session['difficulty'],
        category_name=session.get('category_name', 'Any Category')
    )

@app.route('/result')
def result():
    if 'score' not in session or 'questions' not in session:
        return redirect('/')

    score = session['score']
    total = len(session['questions'])
    difficulty = session.get('difficulty', 'Unknown').capitalize()
    category_name = session.get('category_name', 'Any Category')
    percentage = (score / total) * 100

    if percentage == 100:
        message = "🎉 Perfect score! You're a trivia master!"
    elif percentage >= 80:
        message = "👏 Great job! You really know your stuff."
    elif percentage >= 50:
        message = "👍 Not bad! Keep practicing and you'll ace it."
    else:
        message = "📚 Don't worry, try again and learn something new!"

    return render_template(
        'result.html',
        score=score,
        total=total,
        message=message,
        difficulty=difficulty,
        category_name=category_name
    )

@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    global leaderboard_data
    if request.method == 'POST':
        name = request.form.get('player')
        score = int(request.form.get('score'))
        total = int(request.form.get('total'))
        difficulty = request.form.get('difficulty')
        category = request.form.get('category')

        leaderboard_data.append({
            'name': name,
            'score': score,
            'total': total,
            'difficulty': difficulty,
            'category': category
        })
        leaderboard_data = sorted(leaderboard_data, key=lambda x: x['score'], reverse=True)
    return render_template('leaderboard.html', leaderboard=leaderboard_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
