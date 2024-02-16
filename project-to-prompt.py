from pathlib import Path
from git import Repo
import pyperclip
import chardet

text_output = {}

list_output = ""

def list_repo(path):
    """
    Wyświetla listę plików i folderów w repozytorium Git z zachowaniem struktury drzewa.

    Args:
        path: Ścieżka do katalogu zawierającego repozytorium Git.
    """

    repo = Repo(path, search_parent_directories=True)

    def print_tree(tree, indent=""):
        global list_output
        for entry in tree.blobs + tree.trees:
            if entry.type == "blob":
                list_output += f"{indent}Plik: {entry.name}\n"
            elif entry.type == "tree":
                list_output += f"{indent}Katalog: {entry.name}\n"
                print_tree(entry, indent + "  ")

    print_tree(repo.tree(), "")

def list_repo_file_content(path):
    repo = Repo(path, search_parent_directories=True)

    def print_tree(tree, indent=""):
        global text_output
        for entry in tree.blobs + tree.trees:
            if entry.type == "blob":
                f = entry.data_stream
                try:
                    raw_content = f.read()
                    detected_encoding = chardet.detect(raw_content)["encoding"]
                    if detected_encoding:
                        content = raw_content.decode(detected_encoding)[:200]
                    else:
                        content = "(Nie udało się wykryć kodowania)"
                    text_output[entry.name] = content
                except UnicodeDecodeError:
                    content = f"(Nie udało się odczytać zawartości pliku w kodowaniu {detected_encoding})"
                text_output[entry.name] = content
            elif entry.type == "tree":
                print_tree(entry, indent + "  ")

    print_tree(repo.tree(), "")

if __name__ == "__main__":
    # Użyj bieżącego katalogu
    path = Path(".")

    # Wyświetl listę plików i folderów
    list_repo(path)
    print(list_output)
    
    # Wyświetl zawartość plików
    list_repo_file_content(path)

    text = "\n".join([f"{key}: {value}" for key, value in text_output.items()])
    
    print(text)

    # pyperclip.copy("Mam taką strukture projektu python: \n" + text_output)
