from flask import Flask, render_template
from services.weather_api import get_weather
from services.quotes_api import get_quote
from services.music_videos import get_video

app = Flask(__name__)

@app.route("/")
def index():
    weather = get_weather()
    quote = get_quote()
    video_id = get_video()

    moods = [
        {
            "title": "Me siento tranquila 🌿",
            "body": "Hoy decidí ir con calma.",
            "reactions": 120
        },
        {
            "title": "Día pesado 😵‍💫",
            "body": "No fue fácil, pero aquí sigo.",
            "reactions": 89
        }
    ]

    return render_template(
        "index.html",
        weather=weather,
        quote=quote,
        video_id=video_id,
        moods=moods
    )

if __name__ == "__main__":
    app.run(debug=True)