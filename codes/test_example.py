# pip install -U pytest

def greet(person):
    return "hi {name}".format(**person)
def test():
    bob = {"name": "Bob"}           # arrange
    greeting = greet(bob)           # act
    assert greeting == "hi Bob"     # assert