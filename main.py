from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que tu página web se conecte desde otro dominio

@app.route("/ia", methods=["POST"])
def responder_emocion():
    datos = request.get_json()
    mensaje = datos.get("mensaje", "").lower()

    if "triste" in mensaje or "deprimida" in mensaje:
        respuesta = "Siento que estés así corazón. Respira profundo y escucha algo de música. Estoy aquí para ti siempre que me necesites. No soy la mejor contando chistes pero a lo mejor esto te anima un rato, ¿Cuál es el café más peligroso del mundo? El ex-preso... Jijiji ¿Te cuento otro?😊"
    
    elif "cansada" in mensaje or "agotada" in mensaje:
        respuesta = "Debes estar muy cansad@, lo lamento tanto. 🥺 No sé si es la mejor opción darte consejos de cómo mejorar, pero estaré aquí para escucharte y entenderte. Puedes seguir comentándome cómo te sientes y cómo has llevado las cosas. Si puedes llorar, intenta hacerlo, no es bueno cargar con tantas emociones. Pero si no quieres, toma algo de agua y trata de respirar profundo. Me importas 😊"
    
    elif "ansiosa" in mensaje or "estresada" in mensaje:
        respuesta = "Parece que estás estresad@ 😥. Tengo muchas ideas para que te relajes un rato. ¿Te tica ver unas pelis? También podrías tomar una pequeña siesta, respirar, bailar o cantar. ¡Me encantaría que me comentaras algunas de tus canciones favoritas :3! Siempre estaré para escucharte."
    
    elif "feliz" in mensaje or "contenta" in mensaje:
        respuesta = "¡Bakan! 😄 Me encanta que te sientas bien. ¡Sigue brillando como sol!😎"
    
    else:
        respuesta = "Gracias por contarme cómo te sientes cariño. Está súper duper hablar de tus emociones 💜!"

    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
