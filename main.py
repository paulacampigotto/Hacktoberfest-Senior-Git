from Triangle import *
from Square import *
from Circle import *

def main():
    print(Triangle(3,5).area() == 7.5)
    print(Square(3,5).area() == 15)
    print(Circle(3).area() == 28.274333882308138)

if __name__ == "__main__":
    main()