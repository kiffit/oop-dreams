# Thomas Safago
# 02/28/2025


from Node import Node


class BaseElement(Node):
    # Attributes
    __name = None
    __element_type = None


    # Constants
    __INDENT = "\t"


    # Constructors
    def __init__(self, name, element_type="BaseElement"):
        super().__init__()
        self.set_name(name)
        self.set_element_type(element_type)


    # Methods
    def indent(self, string, custom=-1):
        prefix = self.__INDENT * self.depth()

        if custom != -1:
            prefix = self.__INDENT * custom

        return "\n".join(prefix + line for line in string.splitlines())

    def string_header(self):
        return f"[{self.get_element_type()}] {self.get_name()}"


    # Getters
    def get_name(self):
        return self.__name

    def get_element_type(self):
        return self.__element_type


    # Setters
    def set_name(self, name):
        self.__name = name

    def set_element_type(self, element_type):
        self.__element_type = element_type


    # Tostring
    def __str__(self):
        string = self.string_header()

        for child in self.get_children():
            string += "\n\t" + child.__str__()

        return self.indent(string)
