class Shape:
    def calculateArea(self, length, breadth=-1):
        if breadth != -1:
            return length * breadth
        else:
            return length * length

class Sum:
    def addition(self, a, b, c=0):
        return a+b+c

class Sum2:
    def addition(self, *args):
        if not args:
            return 0
        val = 0
        for value in args:
            val += value
        return val

def main():
    area = Shape()
    print(f"Area of Rectangle: {area.calculateArea(10, 15)}")
    print(f"Area of Squre: {area.calculateArea(15)}")

    sum = Sum()
    print(f"Sum1: {sum.addition(2,3,4)}")
    print(f"Sum2: {sum.addition(3,4)}")

    sum2 = Sum2()
    print(f"Sum1: {sum2.addition(2,3,4,5,1,4,5,13,4)}")
    print(f"Sum2: {sum2.addition(3,4,1,7,9)}")

if __name__ == "__main__":
    main()
        