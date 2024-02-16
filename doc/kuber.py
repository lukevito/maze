from diagrams import Diagram
from diagrams.c4 import Container, SystemBoundary, Relationship

from diagrams.onprem.container import Docker
from diagrams.onprem.queue import Kafka

graph_attr = {
    "splines": "spline",
}

with Diagram("Diagram infrastruktury systemu Maze Solver", direction="TB", graph_attr=graph_attr, filename="diagrams/infra", show=True):
    
    docker = Docker("Docker")

    docker_compose = Docker("Docker Compose")
    

    with SystemBoundary("siec virtualna zwenętrza  dla frontu aplikacji'/"):
        webComponent = Container(
            name="Controler aplikacji webowej '/'",
            technology="Python with Flask and SocketIO",
            description="Przyjmuje labirynty do rozwiązania. (używa webscoketów do komunikacji z klientem)",
        )

    with SystemBoundary("siec virtualna wewnętrza Kontener  dla Backoffice'"):
        mazeComponent = Container(
            name="Moduł rozwiązujący labirynt",
            technology="Python",
            description="Rozwiązuje lairynt",
        )   

        kafka = Kafka("Kafka")

    docker >> Relationship("1. Używa docker compose 'docker-compose.yml'") >> docker_compose
    docker_compose >> Relationship("2. Uruchamia kontenery dla frontu aplikacji kożystając z Dockerfile w app-web") >> webComponent
    docker_compose >> Relationship("3. Uruchamia kontenery dla backoffice aplikacji kożystając z Dockerfile w app-kafka") >> mazeComponent
    docker_compose >> Relationship("3. Uruchamia kontenery dla backoffice") >> kafka



       