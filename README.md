# 🌸 MoodMap

MoodMap es una aplicación web sencilla que integra distintas APIs para mostrar información contextual y emocional del día, combinando clima, frases motivacionales y música, con el objetivo de crear un espacio agradable y sin presión para el usuario.

---

## 🧠 Descripción del proyecto

MoodMap permite visualizar:
- El **clima actual** según la ubicación
- Una **frase motivacional** que cambia automáticamente
- **Música o videos** para acompañar el estado de ánimo
- Publicaciones con estados emocionales y reacciones

La aplicación busca relacionar el estado emocional con el contexto del día, ofreciendo una experiencia visual sencilla y agradable.

---

## 🛠️ Tecnologías utilizadas

- **Python**
- **Flask**
- **Jinja2**
- **HTML5**
- **CSS3**
- **APIs externas**
- **YouTube Embed**

---

## 🔌 APIs integradas

El proyecto integra al menos **tres APIs**, cumpliendo con el objetivo de la práctica:

1. 🌤 **API del Clima**
   - Obtiene temperatura y descripción del clima
   - Ejemplo: OpenWeatherMap

2. 💬 **API de Frases**
   - Muestra frases motivacionales
   - Incluye frases de respaldo (fallback) en español

3. 🎵 **API de Videos/Música**
   - Integra videos musicales desde YouTube
   - Selección aleatoria de canciones relajantes o bonitas


## ▶️ Cómo ejecutar el proyecto

1. Clona el repositorio o descarga el proyecto
2. Crea y activa el entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate

Instala las dependencias:

pip install -r requirements.txt

Ejecuta la aplicación:

python app.py

Abre en el navegador:

http://127.0.0.1:5000
🎨 Diseño

Estilo minimalista

Tarjetas con sombras suaves

Colores relajantes

Emojis para reforzar emociones

Diseño responsive

🎯 Objetivo académico

Este proyecto fue desarrollado como parte de una práctica escolar para:

Integrar múltiples APIs

Aplicar conocimientos de Flask y Jinja2

Diseñar una aplicación funcional y útil

Manejar errores con valores de respaldo (fallback)

