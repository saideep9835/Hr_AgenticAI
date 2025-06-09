from threading import Lock
from .base import BaseMemory

class InMemoryStore(BaseMemory):
    def __init__(self):
        self.store = {}
        self.lock = Lock()

    def get(self, key: str):
        with self.lock:
            return self.store.get(key)

    def put(self, key: str, value):
        with self.lock:
            self.store[key] = value

    def clear(self):
        with self.lock:
            self.store.clear()