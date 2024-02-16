from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship
from diagrams.programming.framework import Flask
from diagrams.programming.language import Python

graph_attr = {
    "splines": "spline",
}

with Diagram("Diagram Architektury C4 systemu Maze Solver poziom Code (C4)", direction="TB", graph_attr=graph_attr, filename="diagrams/architecture-c4", show=True):

    flask = Flask("Flask")
    pyt = Python("Python")

    webComponent = Container(
        name="Controler aplikacji webowej '/'",
        technology="Python with Flask and SocketIO",
        description="Przyjmuje labirynty do rozwiązania. (używa webscoketów do komunikacji z klientem)",
    )

    mazeComponent = Container(
        name="Moduł rozwiązujący labirynt",
            technology="Python",
            description="Rozwiązuje lairynt",
        )


    with SystemBoundary("elementy aplikacji webowej"):
        appWebPY = Container(
            name="app.py",
            technology="Skrytp Python",
            description="Skrypt labiryntu oraz komunikacji z kafka",
        )

    with SystemBoundary("elementy aplikacji rozwiązującej labirynt"):
        appKafkaPY = Container(
            name="app.py",
            technology="Python",
            description="Skrypt labiryntu oraz komunikacji z kafka",
        )
    
   


    webComponent >> Relationship("1. Wchodzi na strone dająca możliwoś rozwiązania labiryntu [HTTP]") >> appWebPY
    mazeComponent >> Relationship("1. Wchodzi na strone dająca możliwoś rozwiązania labiryntu [HTTP]") >> appKafkaPY

    appWebPY >> Relationship() >> flask
    appWebPY >> Relationship() >> pyt

    appKafkaPY >> Relationship() >> pyt