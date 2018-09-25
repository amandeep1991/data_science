class dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color


def bark(bark1):
    return bark1


fido = dog("Fido", "brown")
print(fido.name)
print(bark("woof"))