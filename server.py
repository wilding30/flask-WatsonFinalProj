''' Application to use the emotion
    detection service from watson AI
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate the server
app = Flask('Emotion Detector')

# Set the homepage
@app.route('/')
def home():
    ''' Returns the index as the homepage '''
    return render_template('index.html')

# Create the emotion detection API
@app.route('/emotionDetector')
def emotion_dectector():
    ''' Uses Watson AI to determine the
        relevant emptions
    '''
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)
    try:
        dominant_emotion = response['dominant_emotion']
        if dominant_emotion is None:
            return 'Invalid text! Please try again!'
    except KeyError:
        return 'Something went wrong. Please contact the system administrator.'
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return f'''For the given statement, the system
        response is 'anger': {anger}, 'disgust': {disgust},
        'fear': {fear}, 'joy': {joy}, and 'sadness'
        : {sadness}. The dominant emotion is {dominant_emotion}'''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
