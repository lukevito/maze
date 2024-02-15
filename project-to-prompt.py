from pathlib import Path
from git import Repo

def list_repo_contents(path):
    """
    Wyświetla listę plików i folderów w repozytorium Git z zachowaniem struktury drzewa.

    Args:
        path: Ścieżka do katalogu zawierającego repozytorium Git.
    """

    repo = Repo(path, search_parent_directories=True)

    def print_tree(tree, indent=""):
        for entry in tree.blobs + tree.trees:
            if entry.type == "blob":
                print(f"{indent}Plik: {entry.name}")
            elif entry.type == "tree":
                print(f"{indent}Katalog: {entry.name}")
                print_tree(entry, indent + "  ")

    print_tree(repo.tree(), "")

if __name__ == "__main__":
    # Użyj bieżącego katalogu
    path = Path(".")

    # Wyświetl listę plików i folderów
    list_repo_contents(path)
