class Animal:
    def animalVoice1(self):
        print("Hello")
    
    def animalVoice2(self):
        print("Dickhead")

class Lion(Animal):
    def animalVoice1(self):
        Animal.animalVoice1(self)
    def animalVoice2(self):
        print("Asshole")

def main():
    lion = Lion()
    lion.animalVoice1()
    lion.animalVoice2()

if __name__ == "__main__":
    main()
