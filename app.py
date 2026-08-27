from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

PLAYLIST = [
    {"file": "falanfilan.mp3", "title": "Falan Filan", "display_title": "Redd - Falan Filan", "uploader": "Redd"},
    {"file": "dontpanic.mp3", "title": "Don't Panic", "display_title": "Coldplay - Don't Panic", "uploader": "Coldplay"},
    {"file": "benirahattadinleyin.mp3", "title": "Beni Rahatta Dinleyin", "display_title": "Son Feci Bisiklet - Beni Rahatta Dinleyin", "uploader": "Son Feci Bisiklet"},
    {"file": "yellow.mp3", "title": "Yellow", "display_title": "Coldplay - Yellow", "uploader": "Coldplay"},
    {"file": "instantcrush.mp3", "title": "Instant Crush", "display_title": "Daft Punk - Instant Crush", "uploader": "Daft Punk"},
    {"file": "clocks.mp3", "title": "Clocks", "display_title": "Coldplay - Clocks", "uploader": "Coldplay"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/playlist')
def get_playlist():
    return jsonify(PLAYLIST)

@app.route('/api/photos')
def get_photos():
    photos_dir = os.path.join(app.root_path, 'photos')
    if not os.path.exists(photos_dir):
        return jsonify([])
    
    valid_extensions = ('.jpeg', '.jpg', '.png', '.webp')
    files = [f for f in os.listdir(photos_dir) if f.lower().endswith(valid_extensions)]
    files.sort()
    return jsonify(files[:4])

@app.route('/musics/<path:filename>')
def serve_musics(filename):
    return send_from_directory('musics', filename)

@app.route('/photos/<path:filename>')
def serve_photos(filename):
    return send_from_directory('photos', filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
