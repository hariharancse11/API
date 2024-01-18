from flask import Flask, jsonify
import random

app = Flask(__name__)

# Sample quotes list
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Get busy living or get busy dying. - Stephen King",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "Don't cry because it's over, smile because it happened. - Dr. Seuss",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison",
    "The best way to predict the future is to create it. - Peter Drucker",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "It is our choices that show what we truly are, far more than our abilities. - J.K. Rowling",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "The more I want to get something done, the less I call it work. - Richard Bach",
    "If you are not willing to risk the usual, you will have to settle for the ordinary. - Jim Rohn",
    "You can't cross the sea merely by standing and staring at the water. - Rabindranath Tagore",
    "I find that I get most creative when I'm the most physically active. - Albert Einstein",
    "Don't count the days, make the days count. - Muhammad Ali",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
    "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
    "You don't have to be rich to travel well. - Eugene Fodor",
    "The first step toward success is taken when you refuse to be a captive of the environment in which you first find yourself. - Mark Caine",
    "Challenges are what make life interesting and overcoming them is what makes life meaningful. - Joshua J. Marine",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "It is not the strongest of the species that survive, nor the most intelligent, but the one most responsive to change. - Charles Darwin",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "Twenty years from now, you will be more disappointed by the things that you didn't do than by the ones you did do. - Mark Twain",
    "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King, Jr.",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Don't count the days, make the days count. - Muhammad Ali",
    "The more I want to get something done, the less I call it work. - Richard Bach",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "I find that I get most creative when I'm the most physically active. - Albert Einstein",
    "It is our choices that show what we truly are, far more than our abilities. - J.K. Rowling",
    "If you want to achieve greatness stop asking for permission. - Anonymous",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"]


@app.route('/', methods=['GET'])
def get_random_quote():
    random_quote = random.choice(quotes)
    return jsonify({'quote': random_quote})

if __name__ == '__main__':
    app.run(debug=True)
