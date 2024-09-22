class ComplexNumber:
    def __init__(self) -> None:
        self.real = 0
        self.imaginary = 0
    
    def set_values(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def display_result(self):
        print("(", self.real, " + ", self.imaginary, "i )")

    def __add__(self, *args):
        result = ComplexNumber()
        for arg in args:
            result.real = self.real + arg.real
            result.imaginary = self.imaginary + arg.imaginary
        return result

def main():
    c1 = ComplexNumber()
    c2 = ComplexNumber()
    c3 = ComplexNumber()
    c1.set_values(10, 15)
    c2.set_values(15, 20)
    c3.set_values(12, 11)
    c = c1 + c2 + c3
    c.display_result()

if __name__ == "__main__":
    main()
    