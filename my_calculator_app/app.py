from flask import Flask, render_template, request

app = Flask(__name__)

# Головна сторінка з HTML-формою для введення даних
@app.route('/')
def index():
    return render_template('index.html')

# Маршрут для обробки операції калькулятора
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Отримуємо дані з форми
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        # Виконуємо арифметичну операцію
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                result = 'Помилка! Ділення на нуль.'
            else:
                result = num1 / num2
        else:
            result = 'Неправильна операція!'
    except Exception as e:
        result = f"Помилка: {e}"

    # Повертаємо результат
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
