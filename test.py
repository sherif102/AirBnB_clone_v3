#!/usr/bin/python3
from models.state import State
from models.engine.file_storage import FileStorage

storage = FileStorage()
state = State()

# print(State)
# print(state)
# print(state.id)
print(storage.all())
print()

print(storage.get(State, 'd8a745d6-72b9-45b0-a3a1-67f0d53c987a'))