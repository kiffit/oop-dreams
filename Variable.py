# Thomas Safago
# 02/28/2025


from BaseElement import BaseElement


class Variable(BaseElement):
    # Attributes
    __data_type = None


    # Constructors
    def __init__(self, name, data_type="Any", element_type="Variable"):
        super().__init__(name, element_type)
        self.set_data_type(data_type)

    # Methods
    def string_header(self):
        return f"{super().string_header()} -> {self.get_data_type()}"

    def generate_getter(self):
        return (
            f"def get_{self.get_name()}(self):"
            f"\n\treturn self.__{self.get_name()}"
        )

    def generate_setter(self):
        return (
            f"def set_{self.get_name()}(self, {self.get_name()}):"
            f"\n\tself.__{self.get_name()} = {self.get_name()}"
        )


    # Getters
    def get_data_type(self):
        return self.__data_type


    # Setters
    def set_data_type(self, data_type):
        self.__data_type = data_type
