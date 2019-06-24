from flask import Flask, jsonify, request
import bot

app = Flask(__name__)


@app.route('/bot', methods=['GET'])
def get_response():
    message = request.args.get('message')
    print(message)
    response = bot.response(message)
    return jsonify(response)


@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
