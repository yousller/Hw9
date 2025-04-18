class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            instance = super().__new__(cls)
            cls._instance = instance
        return cls._instance
    
akbar = Singleton()
asqar = Singleton()
print(akbar is asqar)
print(id(akbar) == id(asqar))