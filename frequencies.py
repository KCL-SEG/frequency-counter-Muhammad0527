"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if str(item) in frequencies:
            frequencies[str(item)] = frequencies[str(item)] + 1
        else:
            frequencies[str(item)] = 1
    return frequencies

print(frequencies(['a', 'a', 'b', 'b', 'b', 'c']))
print(frequencies([100, 'Hello', '100', '100', 100]))