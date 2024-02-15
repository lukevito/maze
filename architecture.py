from diagrams import Diagram, Node, Edge

# Komponenty
interfejs_uzytkownika = Node("Interfejs użytkownika")
modul_logiki = Node("Moduł logiki")
modul_danych = Node("Moduł danych")
silnik_graficzny = Node("Silnik graficzny")

# Komunikacja
interfejs_uzytkownika >> modul_logiki
modul_logiki >> modul_danych
modul_logiki >> silnik_graficzny

with Diagram("Web Service", show=False, strict=True, filename="doc/diagrams/maze_arch", outformat="png", ):
# Diagram
    diagram = Diagram(
        fontsize=12,
        node_width=2,
        node_height=2,
    )

    diagram.add(interfejs_uzytkownika)
    diagram.add(modul_logiki)
    diagram.add(modul_danych)
    diagram.add(silnik_graficzny)

    diagram.connect(interfejs_uzytkownika, modul_logiki)
    diagram.connect(modul_logiki, modul_danych)
    diagram.connect(modul_logiki, silnik_graficzny)

    diagram.show()