# app.py
# This is a test commit 1
def add(a, b):
    print("hi")
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
