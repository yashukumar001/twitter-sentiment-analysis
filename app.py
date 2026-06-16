from flask import Flask, render_template, request

app = Flask(__name__)

def predict_sentiment(text):
    text = text.lower()

    positive_words = [
        "love",
        "great",
        "awesome",
        "excellent",
        "happy"
    ]

    negative_words = [
        "bad",
        "worst",
        "terrible",
        "hate",
        "awful"
    ]

    positive_score = sum(
        word in text
        for word in positive_words
    )

    negative_score = sum(
        word in text
        for word in negative_words
    )

    if positive_score >= negative_score:
        return "Positive 😊"

    return "Negative 😞"

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        text = request.form["tweet"]

        result = predict_sentiment(text)

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)