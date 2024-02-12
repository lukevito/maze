# Maze
Dokumentacja architektury systemu do rowiązywania labiryntów

zobacz plik -> [zadanie.pdf](doc/presentations/export/zadanie.pdf)

## Setup projektu

### Wymagane oprogramowanie

* Python <https://www.python.org/>
* Visual Studio Code <https://code.visualstudio.com/>
* Marp for VS Code <https://github.com/marp-team/marp-vscode>
* Visual Studio Community <https://visualstudio.microsoft.com/pl/> (ze względu na jedną z bibliotek)

### Utwórz projekt w vscode na podstawie tego repozytorium
<https://github.com/lukevito/maze>

### Następnie będąc głównym katalogu projektu otwórz konsole i utwórz srodowisko

```
python -m venv myenv
```

### Aktywuj srodowisko

```
myenv\Scripts\activate
```

### Zainstaluj biblioteki

```
python -m pip install -r .\requirements.txt
```

## Generowanie diagramów architektury

```
python.exe .\architecture.py
```

## Generowanie wpisu w Architecture Decision Record

```
adr-new create equal animals
```

listowanie decyzji

```
adr-list
doc/adr/0001-record-architecture-decisions.md
doc/adr/0002-create-equal-animals.md
```


## Generowanie prezentacji (Visual Studio Code)
![alt text](diagrams/images/export.gif) 