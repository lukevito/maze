from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("Diagram Architektury C4 systemu Maze Solver poziom Context (C1)", direction="TB", graph_attr=graph_attr, filename="diagrams/architecture-c1", show=True):
    
    customer = Person(
        name="Szukający drogi", description="Osoba zainteresowan rozwiązaniem labiryntu."
    )


    webapp = Container(
        name="Aplikacja Maze Solver",
        technology="Dostępna przez przeglądarkę WWW",
        description="Rozwiązuje labirynty",
    )

    customer >> Relationship("Ma możliwość rozwiązania labiryntu") >> webapp