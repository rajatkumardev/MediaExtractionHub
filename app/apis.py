import os, pytesseract
from flask import request, send_file, Response, current_app as app, render_template
from pytube import YouTube
from tqdm import tqdm
from PIL import Image
from docx import Document

@app.route('/download_yt_video', methods=['POST'])
def download_yt_video():
    video_url = request.form['url']

    try:
        yt = YouTube(video_url)
        main_title = yt.title
        main_title = main_title + '.mp4'
        main_title = main_title.replace('|', '') 
    except:
        print('connection problem..unable to fetch video info')
    
    try:
        stream = yt.streams.filter(progressive=True).get_highest_resolution()
        video_file = stream.download()
        
        return send_file(video_file, as_attachment=True)
    except:
        print('This video could not be downloaded')
        pass

@app.route('/download_yt_playlist', methods=['POST'])
def download_yt_playlist():
    video_url = request.form['url']

    try:
        yt = YouTube(video_url)
        main_title = yt.title
        main_title = main_title + '.mp4'
        main_title = main_title.replace('|', '') 
    except:
        print('connection problem..unable to fetch video info')
    
    try:
        stream = yt.streams.filter(progressive=True).get_highest_resolution()
        video_file = stream.download()
        
        return send_file(video_file, as_attachment=True)
    except:
        print('This video could not be downloaded')
        pass

def download_video(video_url):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        video_file = stream.download()

        return video_file
    except Exception as e:
        return str(e)

@app.route('/download_progressive', methods=['POST'])
def download_progressive():
    video_url = request.form['url']
    video_file = download_video(video_url)

    def generate():
        with open(video_file, 'rb') as f:
            pbar = tqdm(total=os.path.getsize(video_file), unit='B', unit_scale=True)
            while True:
                # Read the file in chunks
                chunk = f.read(1024)
                if not chunk:
                    break

                pbar.update(len(chunk))

                # Yield the chunk to the response
                yield chunk

        pbar.close()
        os.remove(video_file)

    # Set the appropriate headers for the response
    headers = {
        'Content-Disposition': 'attachment',
        'filename': 'video.mp4'
    }

    # Create the response object with the generator function
    response = Response(generate(), headers=headers, mimetype='video/mp4')
    response.headers['Content-Length'] = os.path.getsize(video_file)
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Pragma'] = 'no-cache'

    return response

@app.route('/extract_text', methods=['POST'])
def extract_text():
    # Get the uploaded image file
    image = request.files['image']

    # Read the image using PIL
    img = Image.open(image)

    # Extract text from the image using pytesseract
    extracted_text = pytesseract.image_to_string(img)

    # Create a new Word document
    document = Document()

    # Add the extracted text to the document
    document.add_paragraph(extracted_text)

    # Save the document as a Word file
    document.save('extracted_text.docx')
