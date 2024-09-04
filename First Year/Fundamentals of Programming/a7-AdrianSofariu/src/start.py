"""
This is the entrypoint of our app
"""
from src.ui.ui import UI
from src.repository.binary_file_repository import BinaryFileRepository
from src.repository.text_file_repository import TextFileRepository
from src.repository.memory_repository import MemoryRepository

if __name__ == "__main__":
    repo_type = BinaryFileRepository()
    my_ui = UI(repo_type)
    my_ui.start()
