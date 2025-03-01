# Thomas Safago
# 02/28/2025


from Variable import Variable
from Function import Function
from Class import Class


def main():
    shape = Class("Shape", [Variable("name"), Variable("sides")], [Function("calc_area")])
    quadrilateral = Class("Quadrilateral", [Variable("skew")], [Function("calc_area"), Function("to_tris")])
    rectangle = Class("Rectangle", [Variable("length"), Variable("width")], [Function("get_diagonal")])
    square = Class("Square", [], [Function("get_square")])

    quadrilateral.inherits(shape)
    rectangle.inherits(quadrilateral)
    square.inherits(rectangle)

    print(shape.generate())
    print("\n\n")
    print(quadrilateral.generate())
    print("\n\n")
    print(rectangle.generate())
    print("\n\n")
    print(square.generate())


if __name__ == '__main__':
    main()
