class Calculator:
    calculation_type = "Arithmetic Operations"
    def __init__(self):
        pass

    @staticmethod
    def add(a,b):
        return a + b
    
    @classmethod
    def multiply(cls, a ,b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
