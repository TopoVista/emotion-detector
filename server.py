"""Emotion Detector Flask application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Render main page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze emotion from text."""
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        "'anger': {anger}, "
        "'disgust': {disgust}, "
        "'fear': {fear}, "
        "'joy': {joy}, "
        "'sadness': {sadness}. "
        "The dominant emotion is {dominant_emotion}."
    ).format(**response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
