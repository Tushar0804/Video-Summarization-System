import os
import subprocess
import time
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'sharma-tushar-008'

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/loading', methods=['POST'])
def process():
    video = request.files['video']
    accent = request.form["accent"]
    session['accent'] = accent

    video_file_path = "/Users/tusharsharma/B Tech/RESEARCH PROJECTS/Video Summariser Project/videos/video.mp4"

    video.save(video_file_path)

    return render_template('loading.html')

@app.route('/result', methods=['GET'])
def result(): 

    video_file_path = "/Users/tusharsharma/B Tech/RESEARCH PROJECTS/Video Summariser Project/videos/video.mp4"
    accent = session.get('accent')
    print(accent)

    # start the processing asynchronously using a subprocess
    process = subprocess.Popen(['python', '/Users/tusharsharma/B Tech/RESEARCH PROJECTS/Video Summariser Project/module/model.py', video_file_path, accent], stdout=subprocess.PIPE)
    
    # Wait for the process to finish and capture the output
    process.wait()

    output, error = process.communicate()
    if error:
        return f"An error occurred: {error.decode('utf-8')}"

    # Return the output
    return render_template('result.html', summary=output.decode('utf-8'))

if __name__ == '__main__':
    app.run()