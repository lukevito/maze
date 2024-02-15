from kafka import KafkaProducer, KafkaConsumer
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import json
import logging
import multiprocessing

app = Flask(__name__)
socketio = SocketIO(app)
producer = KafkaProducer(bootstrap_servers=["kafka:9092"])

def consume_messages():
    consumer = KafkaConsumer("rozwiazania", bootstrap_servers=["kafka:9092"])

    for message in consumer:
        try:
            rozwiazanie = get_kafka_message(message)
            
            log(f"Pobrałem wiadomość z topiku 'rozwiazania': {rozwiazanie}")
# todo to dziadostwo nie działa bo proces i inny miejsce niz socketio czy cos w każdym razie lipa
            socketio.emit("prezentuj_rozwiazanie", rozwiazanie)

        except Exception as e:
            errorExc(e)

@socketio.on("prezentuj_rozwiazanie")
def on_prezentuj_rozwiazanie(rozwiazanie):
    app.logger.info(f"Prezentowanie rozwiązania: {rozwiazanie}")
    emit("redirect", "/success")

@socketio.on("zadanie_do_rozwiazania")
def on_zadanie_do_rozwiazania(message):
    app.logger.info(f"Otrzymano zadanie do rozwiązania: {message}")
    producer.send("zadania", json.dumps(message).encode("utf-8"))

@socketio.on("connect")
def on_connect():
    app.logger.info("Klient podłączony")

@app.route("/success")
def success():
    return "<h1>Wiadomość otrzymana!</h1>"

@app.route("/", methods = ['POST', 'GET'])
def hello():
    return render_template("index.html")

def log(new_var):
    app.logger.info(new_var)

def get_kafka_message(message):
    return json.loads(message.value.decode("utf-8"))

def errorExc(e):
    app.logger.error(f"Wystąpił błąd: {e}")

def configure_flask():
    """Configures Flask logging and settings."""
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

if __name__ == "__main__":
    configure_flask()

    process = multiprocessing.Process(target=consume_messages, args=())
    process.start()
    
    app.run(host="0.0.0.0", port=5000)
