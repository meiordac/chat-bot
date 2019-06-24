from flask import Flask, jsonify, request
import bot

app = Flask(__name__)


@app.route('/bot', methods=['GET'])
def get_response():
    message = request.args.get('message')
    print(message)
    response = bot.response(message)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
