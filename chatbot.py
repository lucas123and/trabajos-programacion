import gradio as gr
import requests

# --- Funciones que consultan OpenLigaDB ---

def obtener_partidos_actuales():
    """Obtiene los partidos más recientes de la Premier League desde OpenLigaDB."""
    try:
        url = "https://api.openligadb.de/getmatchdata/bl1/2024"  # 'bl1' es Bundesliga (ejemplo)
        # ⚠️ OpenLigaDB no tiene siempre la Premier League, así que usamos Bundesliga como demostración
        # pero se puede cambiar a otra liga si se agrega.
        r = requests.get(url)
        data = r.json()

        if not data:
            return "No hay datos disponibles por el momento."

        partidos = []
        for match in data[:5]:  # Mostramos solo los 5 más recientes
            home = match["Team1"]["TeamName"]
            away = match["Team2"]["TeamName"]
            goals_home = match.get("MatchResults", [{}])[-1].get("PointsTeam1", "?")
            goals_away = match.get("MatchResults", [{}])[-1].get("PointsTeam2", "?")
            partidos.append(f"{home} {goals_home} - {goals_away} {away}")

        return "🏟️ Últimos partidos (ejemplo Bundesliga):\n" + "\n".join(partidos)

    except Exception as e:
        return f"Error al obtener datos: {e}"

# --- Lógica del chatbot ---

def responder(mensaje):
    mensaje = mensaje.lower()

    # Datos reales desde API
    if "partidos" in mensaje or "resultados" in mensaje:
        return obtener_partidos_actuales()

    # Respuestas sobre equipos
    elif "manchester united" in mensaje:
        return "El Manchester United es uno de los clubes más grandes de Inglaterra, con 20 títulos de liga."
    elif "manchester city" in mensaje:
        return "El Manchester City ha dominado la Premier League en los últimos años bajo Pep Guardiola."
    elif "liverpool" in mensaje:
        return "El Liverpool FC es uno de los clubes más exitosos del mundo, con seis Champions League."
    elif "arsenal" in mensaje:
        return "El Arsenal FC es conocido por su estilo ofensivo y su historia en la Premier League."
    elif "chelsea" in mensaje:
        return "El Chelsea FC ha ganado múltiples títulos de Premier League y Champions League."
    elif "tottenham" in mensaje or "spurs" in mensaje:
        return "El Tottenham Hotspur es un club de Londres con un estadio moderno y gran tradición."

    # Preguntas generales
    elif "tabla" in mensaje or "posiciones" in mensaje:
        return "Por ahora, OpenLigaDB no ofrece una tabla actualizada de la Premier League sin autenticación."
    elif "premier league" in mensaje or "liga inglesa" in mensaje:
        return "La Premier League es la liga más competitiva del mundo, con 20 clubes y jugadores de élite."

    else:
        return "Puedo hablarte de equipos o mostrarte resultados recientes. ¡Probá escribiendo 'partidos recientes'!"

# --- Interfaz con Gradio ---

with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align:center; color:#1e90ff;'>🏴 Chatbot del Fútbol Inglés (sin API key)</h1>")
    chatbot = gr.Chatbot(height=400)
    mensaje = gr.Textbox(placeholder="Escribí tu pregunta...", label="")
    enviar = gr.Button("Enviar")

    def enviar_mensaje(mensaje, chat):
        respuesta = responder(mensaje)
        chat.append((mensaje, respuesta))
        return chat, ""

    enviar.click(enviar_mensaje, [mensaje, chatbot], [chatbot, mensaje])
    mensaje.submit(enviar_mensaje, [mensaje, chatbot], [chatbot, mensaje])

demo.launch(share=True)