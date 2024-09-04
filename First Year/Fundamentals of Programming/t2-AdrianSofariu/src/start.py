from src.repository import Repository
from src.services import Service
from src.ui import UI

repository = Repository("students.txt")
service = Service(repository)
ui = UI(service)
ui.start()
