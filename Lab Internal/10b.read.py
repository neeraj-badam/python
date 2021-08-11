#ReadStringAndDisplay
class ReadPrint:
    def __init__(self) -> None:
        self.a = ''
    def read(self):
        self.a = input()
    def write(self):
        return self.a

rp = ReadPrint()
rp.read()
print(rp.write())