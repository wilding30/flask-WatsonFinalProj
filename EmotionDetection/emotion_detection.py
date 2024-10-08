# Import requests and json to pass the request and interpret the response
import requests
import json

def emotion_detector(text_to_analyse):
    ''' Action to determine emotion for some given text '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    status_code = response.status_code
    emotion_scores = {
        'anger': 0,
        'disgust': 0,
        'fear': 0,
        'joy': 0,
        'sadness': 0,
        'dominant_emotion': 0
        }

    if status_code == 200:
        formatted_response = json.loads(str(response.text))
        emotion_scores['anger'] = formatted_response['emotionPredictions'][0]['emotion']['anger']
        emotion_scores['disgust'] = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        emotion_scores['fear'] = formatted_response['emotionPredictions'][0]['emotion']['fear']
        emotion_scores['joy'] = formatted_response['emotionPredictions'][0]['emotion']['joy']
        emotion_scores['sadness'] = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)

    elif status_code == 400:
        emotion_scores['anger'] = None
        emotion_scores['disgust'] = None
        emotion_scores['fear'] = None
        emotion_scores['joy'] = None
        emotion_scores['sadness'] = None
        emotion_scores['dominant_emotion'] = None
      
    else:
        return 'Server error'

    # Return the response as text
    return emotion_scores
