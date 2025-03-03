# Thomas Safago
# 02/28/2025


from Program import Program
from helpers import Functions, Variables
from Variable import Variable
from Function import Function
from Class import Class


def main():
    p1 = Program("Trollz", "Anna Gettinger")

    c1 = Class("Troll", Variables("nose_length", "chin_hairs_count", "moles_count"), Functions("groan", "eat_stew", "turn_into_rock", Function("chin_hair_collection", Variables("chin_hairs", "collection_basket"))))
    c2 = Class("Gremlin", Variables("bed_time", "water_exposure_level"), Functions("explode"))
    c3 = Class("Goblin", Variables("number_of_sherpan_spears", "stew_pot_count"), Functions("make_food"))
    c4 = Class("BabyGremlin", Variables("baby_age"), Functions("grow"))

    p1.add_class(c1)
    p1.add_class(c2)
    p1.add_class(c3)
    p1.add_class(c4)

    c2.inherits(c1)
    c3.inherits(c1)
    c4.inherits(c2)

    p1.generate()


if __name__ == '__main__':
    main()
