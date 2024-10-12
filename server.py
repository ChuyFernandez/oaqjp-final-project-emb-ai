from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def sent_analyzer():
    if request.method == "GET":
        text_to_analyze = request.args.get('textToAnalyze')
        response = emotion_detector(text_to_analyze)
        anger,disgust,fear,joy,sadness,dominant_emotion=list(response.values())

        if dominant_emotion is None: 
            return "Invalid text! Please try again!"
            
        return "For the given statement, the system response is \
                'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}." .format(anger, disgust, fear, joy, sadness, dominant_emotion)

@app.route("/", methods=["GET"])
def render_index_page():
    if request.method == "GET":
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

