from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API route
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')

    # Logic
    word_count = len(text.split())
    char_count = len(text)

    # Very basic sentiment
    sentiment = "Positive" if "good" in text.lower() else "Neutral"

    return jsonify({
        "words": word_count,
        "characters": char_count,
        "sentiment": sentiment
    })

if __name__ == '__main__':
    app.run(debug=True)