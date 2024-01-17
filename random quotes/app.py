from flask import Flask, jsonify
import random

app = Flask(__name__)

# Sample quotes list
quotes = [
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Do not wait to strike till the iron is hot, but make it hot by striking. - William Butler Yeats",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "It always seems impossible until it’s done. - Nelson Mandela",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only source of knowledge is experience. - Albert Einstein",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The purpose of our lives is to be happy. - Dalai Lama",
]

@app.route('/random-quote', methods=['GET'])
def get_random_quote():
    random_quote = random.choice(quotes)
    return jsonify({'quote': random_quote})

if __name__ == '__main__':
    app.run(debug=True)
