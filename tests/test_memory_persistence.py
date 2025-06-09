def test_memory_persistence():
    from memory.in_memory import InMemoryStore
    mem = InMemoryStore()
    mem.put("key", "value")
    assert mem.get("key") == "value"
