class Add(int):
    def __init__(self, num):
        self.num = num
        
    def __call__(self, number):
        self.num += number
        return self.num
    
print(Add(10)(11))
print(Add(10)(11)(12))