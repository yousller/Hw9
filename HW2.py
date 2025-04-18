class Ersbary:
    def __init__(self):
        self.numbers = []
        
    def add_number(self, number):
        if not isinstance(number, int):
            raise ValueError('ValueError. Give an integer.')
        self.numbers.append(number)
    
    def res(self):
        print(self.numbers)
        print(sum(self.numbers))
        
class Add(Ersbary):
    def __call__(self, number):
        self.add_number(number)
        return self
    
add = Add()
add(10)(11)
print(add.res())
add(10)(11)(12)
print(add.res())