# Import requests and json to pass the request and interpret the response
import requests
import json

def emotion_detector(text_to_analyse):
    ''' Action to determine emotion for some given text '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    # Return the response as text
    return response.text
