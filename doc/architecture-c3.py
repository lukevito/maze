from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship
from diagrams.onprem.container import Docker

from diagrams.onprem.queue import Kafka

graph_attr = {
    "splines": "spline",
}

with Diagram("Diagram Architektury C4 systemu Maze Solver poziom Components (C3)", direction="TB", graph_attr=graph_attr, filename="diagrams/architecture-c3", show=True):

    webapp = Container(
            name="App WEB",
            technology="Python with Flask and SocketIO",
            description="Przyjmuje labirynty do rozwiązania.",
        )

    solver = Container(
            name="Maze Solver",
            technology="Python",
            description="Aplikacja rozwiązuje labirynty.",
        )
    
    docker = Docker("Docker")

    with SystemBoundary("Componenty aplikacji webowej '/"):
        webComponent = Container(
            name="Controler aplikacji webowej '/'",
            technology="Python with Flask and SocketIO",
            description="Przyjmuje labirynty do rozwiązania. (używa webscoketów do komunikacji z klientem)",
        )

        kafkaProducer = Container(
            name="Kafka Producer",
            technology="Python",
            description="Wysyła komunikaty do kolejki Kafka.",
        )

        kafkaConsumer = Container(
            name="Kafka Consumer",
            technology="Python",
            description="Pobiera komunikaty z kolejki Kafka.",
        )
    
    with SystemBoundary("Componenty aplikacji rozwiązywania labiryntu '/"):
        mazeComponent = Container(
            name="Moduł rozwiązujący labirynt",
            technology="Python",
            description="Rozwiązuje lairynt",
        )

        mazeKafkaProducer = Container(
            name="Kafka Producer",
            technology="Python",
            description="Wysyła komunikaty do kolejki Kafka.",
        )

        mazeKafkaConsumer = Container(
            name="Kafka Consumer",
            technology="Python",
            description="Pobiera komunikaty z kolejki Kafka.",
        )

    kafka = Kafka("Kafka")


    webapp >> Relationship("1. Aplikacja wywołuje żądanie http używając websocketów") >> webComponent
    webComponent >> Relationship("2. używa producenta komunikatów") >> kafkaProducer
    kafkaProducer >> Relationship("3. Wysyła prośbę o rozwiązanie na topick 'maze'") >> kafka
    webComponent >> Relationship("4. używa konsumera do pobrania") >> kafkaConsumer
    kafkaConsumer >> Relationship("5.pobiera z topicu 'result'") >> kafka
    kafkaConsumer >> Relationship("7. Zwraca do kontrolera'") >> webComponent
    webComponent >> Relationship("8. Prezentuje wynik używając websocketów") >>  webapp

    solver >> Relationship("1. rozwiązuje labirynty ") >> mazeComponent
    mazeComponent >> Relationship("2. używa consumera komunikatów ") >> mazeKafkaConsumer
    mazeKafkaConsumer >> Relationship("3. pobiera z topicu 'maze'") >> kafka
    mazeComponent >> Relationship("4. rozwiązuje labirynt ") >> mazeComponent
    mazeComponent >> Relationship("5. używa producenta komunikatów ") >> mazeKafkaProducer
    mazeKafkaProducer >> Relationship("6. Wysyła rozwiązanie na topick 'result'") >> kafka


