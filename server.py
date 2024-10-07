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
@app.route('/emotionDectector')
def emotionDectector():
    ''' Uses Watson AI to determine the
        relevant emptions
    '''
    textToAnalyze = request.args.get('textToAnalyze')
    response = emotion_detection('textToAnalyze')
    return response

if __name__ == "__main__":
    ''' This functions executes the flask
        app and deploys it on localhost:5000
    '''
    app.run(debug=True, host='0.0.0.0')