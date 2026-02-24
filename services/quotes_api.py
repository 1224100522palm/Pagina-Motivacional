import requests
import random

FALLBACK_QUOTES = [
    {
        "text": "Avanza a tu ritmo, no es una carrera.",
        "author": "Anónimo"
    },
    {
        "text": "Haz lo mejor que puedas con lo que tienes.",
        "author": "Theodore Roosevelt"
    },
    {
        "text": "Confía en ti, lo estás haciendo mejor de lo que crees.",
        "author": "Anónimo"
    },
    {
        "text": "Descansar también es una forma de avanzar.",
        "author": "Anónimo"
    },
    {
        "text": "No tienes que tener todo resuelto hoy.",
        "author": "Anónimo"
    },
    {
        "text": "Cada paso pequeño también cuenta.",
        "author": "Anónimo"
    },
    {
        "text": "Sé paciente contigo, estás aprendiendo.",
        "author": "Anónimo"
    },
    {
        "text": "Incluso los días difíciles forman parte del progreso.",
        "author": "Anónimo"
    },
    {
        "text": "Respira, este momento también pasará.",
        "author": "Anónimo"
    },
    {
        "text": "Lo que sientes es válido.",
        "author": "Anónimo"
    },
    {
        "text": "Hoy hiciste lo que pudiste, y eso es suficiente.",
        "author": "Anónimo"
    },
    {
        "text": "No te compares, cada proceso es distinto.",
        "author": "Anónimo"
    },
    {
        "text": "La calma también es una fortaleza.",
        "author": "Anónimo"
    },
    {
        "text": "Paso a paso sigue siendo avance.",
        "author": "Anónimo"
    },
    {
        "text": "Está bien ir despacio.",
        "author": "Anónimo"
    }
]
def get_quote():
    try:
        url = "https://api.quotable.io/random"
        response = requests.get(url, timeout=5)
        data = response.json()

        text = data.get("content")
        author = data.get("author")

        if text and author:
            return {
                "text": text,
                "author": author
            }

    except Exception as e:
        print("Error quotes API:", e)

    # 🔥 respaldo SIEMPRE
    return random.choice(FALLBACK_QUOTES)