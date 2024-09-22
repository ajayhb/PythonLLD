class Circle:
    PI = 3.142857

    def __init__(self, radius) -> None:
        self.radius = radius

    def get_area(self):
        return Circle.PI * (self.radius**2)

    def get_perimeter(self):
        return 2 * Circle.PI * self.radius

def main():
    circle1 = Circle(10)
    print(f"Circle1 Area: {circle1.get_area()}")
    print(f"Circle1 Perimeter: {circle1.get_perimeter()}")

if __name__ == "__main__":
    main()