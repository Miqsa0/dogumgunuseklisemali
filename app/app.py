from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Şarkıların YouTube video ID'leri
PLAYLIST = [
    {
        
        "id": "8uxt-FnNy2I",
        "title": "Coldplay - Don't Panic",
        "uploader": "Coldplay",
        "url": "https://www.youtube.com/watch?v=8uxt-FnNy2I"
    },

    {
        "id": "egQqHqad_UM",
        "title": "Son Feci Bisiklet - Beni Rahatta Dinleyin",
        "uploader": "Son Feci Bisiklet",
        "url": "https://www.youtube.com/watch?v=egQqHqad_UM"
    },

    {
        "id": "q7mlB-adMBc",
        "title": "Coldplay - Yellow",
        "uploader": "Coldplay",
        "url": "https://www.youtube.com/watch?v=q7mlB-adMBc"
    },
    {
        "id": "PFW2uSCZ0uE",
        "title": "Coldplay - Clocks",
        "uploader": "Coldplay",
        "url": "https://www.youtube.com/watch?v=PFW2uSCZ0uE"
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/playlist')
def get_playlist():
    return jsonify(PLAYLIST)

if __name__ == '__main__':
    app.run(debug=True, port=5000)