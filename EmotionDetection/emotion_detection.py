import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        data = json.loads(response.text)
        emotions = data["emotionPredictions"][0]["emotion"]
        return {
            'anger': emotions["anger"],
            'disgust': emotions["disgust"],
            'fear': emotions["fear"],
            'joy': emotions["joy"],
            'sadness': emotions["sadness"],
            'dominant_emotion': max(emotions, key=emotions.get)
        }
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
