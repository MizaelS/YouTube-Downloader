from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

def format_number(number):
    if number >= 10**9:
        return f"{number / 10**9:.1f}B"
    elif number >= 10**6:
        return f"{number / 10**6:.1f}M"
    elif number >= 10**3:
        return f"{number / 10**3:.1f}K"
    else:
        return str(number)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        url = url.split('?')[0]
        yt = YouTube(url)
        video_streams = yt.streams.filter(only_video=True, file_extension='mp4').all()
        audio_streams = yt.streams.filter(only_audio=True, file_extension='mp4').all()
        thumbnail_url = yt.thumbnail_url

        # calcular el tamaño de cada stream de video y audio
        for stream in video_streams:
            stream.size = round(stream.filesize / (1024 * 1024), 2)  # convertir a MB y redondear a 2 decimales

        for stream in audio_streams:
            stream.size = round(stream.filesize / (1024 * 1024), 2)  # convertir a MB y redondear a 2 decimales

        title = yt.title
        views = format_number(yt.views)

        return render_template('index.html', video_streams=video_streams, audio_streams=audio_streams, url=url, thumbnail_url=thumbnail_url, title=title, views=views)
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        url = request.form['url']
        video_itag = request.form['video']
        audio_itag = request.form['audio']
        yt = YouTube(url)
        video_stream = yt.streams.get_by_itag(video_itag)
        audio_stream = yt.streams.get_by_itag(audio_itag)
        video_filename = video_stream.download(output_path='temp', filename='video')
        audio_filename = audio_stream.download(output_path='temp', filename='audio')
        
        output_filename = os.path.join('temp', f"{yt.title}.mp4")
        os.system(f'ffmpeg -i "{video_filename}" -i "{audio_filename}" -c:v copy -c:a aac "{output_filename}"')
        
        os.remove(video_filename)
        os.remove(audio_filename)
        
        response = send_file(output_filename, as_attachment=True, download_name=f"{yt.title}.mp4")
        os.remove(output_filename)
        return response
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
