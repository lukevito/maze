from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship
from diagrams.onprem.queue import Kafka

graph_attr = {
    "splines": "spline",
}

with Diagram("Diagram Architektury C4 systemu Maze Solver poziom Containers (C2)", direction="TB", graph_attr=graph_attr, filename="diagrams/architecture-c2", show=True):
    customer = Person(
        name="Szukający drogi", description="Osoba zainteresowan rozwiązaniem labiryntu."
    )

    with SystemBoundary("System Aplikacji Maze Solver"):
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

    kafka = Kafka("Kafka")


    customer >> Relationship("1. Wchodzi na strone dająca możliwoś rozwiązania labiryntu [HTTP]") >> webapp
    webapp >> Relationship("2. Wysyła komunikat na topik 'maze' ") >> kafka
    solver << Relationship("3. Pobiera prośbę o rozwiązanie z topicku 'maze'") << kafka
    solver >> Relationship("4. Wysyła rozwiązanie na topick 'result'") >> kafka
    webapp << Relationship("5. pobiera komunikat z topicku 'result i prezentuje wynik' ") << kafka