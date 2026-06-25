
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        user_age = request.form.get('user_age')
        user_choice = request.form.get('choice')

        if int(user_age) < 18:
            print(f"Извините, {username},регистрация только для лиц старше 18 лет.")
        else:
            print(f"Поздравляем, {username}! Вы успешно записаны на поток {user_choice}")
    return render_template('register.html')

task_list = []

@app.route('/todo', methods = ['POST', 'GET'])
def todo():
    if request.method == 'POST':

        any_task = request.form.get('task')

        if any_task:
            task_list.append(any_task)

    return render_template('todo.html', tasks = task_list)

@app.route('/IMT', methods = ['POST', 'GET'])
def IMT():
    if request.method == 'POST':
        height = request.form.get('height')
        weight = request.form.get('weight')
        IMT_user = float(weight) / (float(height) * 2)
        return render_template('IMT.html', IMT_user = IMT_user)
    return render_template('IMT.html')


@app.route('/register_acc', methods = ['GET', 'POST'])
def register_acc():
    if request.method == 'POST':
        name_acc = request.form.get('name_acc')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')

        if password != password_confirm:
            print(f'Пароли не совпадают!')
        else:
            print(f'Поздравляем {name_acc}! Вы успешно зарегистрировались!')
    return render_template('register_acc.html')

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    if request.method == 'POST':
        pass_admin = request.form.get('pass_admin')
        if int(pass_admin) == 1234:
            print(f'Добро пожаловать!')
            return render_template('admin.html', correct="Добро пожаловать!")
        else:
            return render_template('admin.html', error='Доступ запрщен!')

    return render_template('admin.html')





@app.route('/feedback', methods = ['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        username = request.form.get('username')
        user_mes = request.form.get('messege')

        print(f'username: {username} Messege: {user_mes}')
        return (f"<h1> Спасибо {username}</h1> <p>ваше сообщение получено: {user_mes}</p>"
                f"<a href='/'>назад</a>")
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug= True)



