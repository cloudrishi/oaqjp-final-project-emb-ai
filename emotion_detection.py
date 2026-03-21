import requests
import json

# Function that calls Watson AI's Emotion Detector
def emotion_detector(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
    payload = {
        "raw_document": { 
            "text": text_to_analyze 
        } 
    }
    
    response = requests.post(url, json=payload, headers=headers)

    # convert response to disctionary
    response_dictionary = json.loads(response.text) 

    # gets first item → {"emotion": {...} 
    emotions = response_dictionary['emotionPredictions'][0]['emotion']

    emotion_scores = {
        'anger':    emotions['anger'],
        'disgust':  emotions['disgust'],
        'fear':     emotions['fear'],
        'joy':      emotions['joy'],
        'sadness':  emotions['sadness']
    }

    emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)


    return emotion_scores

if __name__ == "__main__":
    result = emotion_detector("I love this new technology")
    print(json.dumps(result, indent=4))