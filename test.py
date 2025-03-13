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

print(storage.count(State))