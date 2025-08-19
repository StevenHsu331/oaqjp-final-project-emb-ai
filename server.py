"""
Flask server for the Emotion Detection API.

This module exposes a REST API endpoint `/emotionDetector`
which accepts JSON input with a "text" field and returns
the detected emotions and the dominant emotion.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    API endpoint to detect emotions from input text.

    Expected input:
        {
            "text": "I love this!"
        }

    Returns:
        - 400 if input is not valid JSON or missing "text"
        - 500 if an internal error occurs
        - String summary of the detected emotions and dominant emotion
    """
    if not request.is_json:
        return jsonify({"error": "Input has to be JSON."}), 400

    input_data = request.get_json()

    if "text" not in input_data:
        return jsonify({"error": "Missing 'text' in JSON."}), 400

    text = input_data["text"]

    try:
        result = emotion_detector(text)
    except (ValueError, KeyError, TypeError):
        return jsonify({"error": "Failed to process the result."}), 500

    if any(value is None for value in result.values()):
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}"
    )


if __name__ == "__main__":
    app.run(debug=True)
