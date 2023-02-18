from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.post('/calculate')
def calculate():
    data = request.json
    if request.is_json:
        num1 = data['num1']
        num2 = data['num2']
        result = int(num1) + int(num2)
        return {'result': result}, 200

    return {'error': 'Invalid input'}, 400

if __name__ == '__main__':
    app.run()