from flask import render_template, current_app as app

@app.route("/")
def index():
    return render_template("index.html", content="yt_video_downloader.html")

@app.route("/yt_video_downloader")
def yt_video_downloader():
    return render_template("index.html", content="yt_video_downloader.html")

@app.route("/yt_video_downloader_progress")
def yt_video_downloader_progress():
    return render_template("index.html", content="yt_video_downloader_progress.html")

@app.route("/yt_playlist_downloader")
def yt_playlist_downloader():
    return render_template("index.html", content="yt_playlist_downloader.html")

@app.route("/transcribe_video")
def transcribe_video():
    return render_template("index.html", content="transcribe_video.html")

@app.route("/extract_text_from_image")
def extract_text_from_image():
    return render_template("index.html", content="extract_text_from_image.html")