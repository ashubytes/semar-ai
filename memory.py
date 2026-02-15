# memory.py

import json

FILE = "memory.json"

def save(problem, winner):
    """
    Save a memory entry as JSON: { "problem": ..., "winner": ... } on each line.
    """
    entry = {"problem": problem, "winner": winner}
    with open(FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

def load():
    """
    Load all memory entries from the file.
    """
    memories = []
    try:
        with open(FILE, "r") as f:
            for line in f:
                memories.append(json.loads(line))
    except FileNotFoundError:
        pass
    return memories
def clear():
    with open(FILE, "w") as f:
        pass
