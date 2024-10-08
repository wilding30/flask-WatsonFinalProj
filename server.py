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
def emotionDectector():
    ''' Uses Watson AI to determine the
        relevant emptions
    '''
    textToAnalyze = request.args.get('textToAnalyze')
    response = emotion_detector(textToAnalyze)
    try:
        dominant_emotion = response['dominant_emotion']
        if dominant_emotion == None:
            return 'Invalid text! Please try again!'
    except:
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
    ''' This functions executes the flask
        app and deploys it on localhost:5000
    '''
    app.run(debug=True, host='0.0.0.0')