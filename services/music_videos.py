import random

import random

# Videos con música bonita y EMBED PERMITIDO
VIDEOS = [
    # lofi / chill
    "jfKfPfyJRdk",   # lofi hip hop radio
    "5qap5aO4i9A",   # chillhop
    "DWcJFNfaw9c",   # coffee shop music

    # canciones tranquilas
    "2OEL4P1Rz04",   # indie acoustic
    "hHW1oY26kxQ",   # relaxing music
    "zbxAB7rTpDc",   # calm piano

    # vibes bonitas
    "rUxyKA_-grg",   # soft pop
    "xNN7iTA57jM",   # aesthetic playlist
]

def get_video():
    return random.choice(VIDEOS)