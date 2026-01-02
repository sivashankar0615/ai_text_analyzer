from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    polarity = 0
    word_count = 0
    char_count = 0

    if request.method == "POST":
        text = request.form["text"]

        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😟"
        else:
            sentiment = "Neutral 😐"

        word_count = len(text.split())
        char_count = len(text)

    return render_template(
        "index.html",
        sentiment=sentiment,
        polarity=polarity,
        word_count=word_count,
        char_count=char_count
    )

if __name__ == "__main__":
    app.run(debug=True)
