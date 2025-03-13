#!/usr/bin/python3
from models.state import State
from models.engine.db_storage import DBStorage
from models import storage

state = State()

# print(State)
# print(state)
# print(state.id)
print(storage.all())
print()

print(storage.count(State))