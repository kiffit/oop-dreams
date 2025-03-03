# Thomas Safago
# 02/28/2025


from BaseElement import BaseElement


class Class(BaseElement):
    # Attributes
    __attributes = None
    __methods = None
    __base_class = None

    # Separators
    __FUNCTION_SEPARATOR = "\n\n"
    __CATEGORY_SEPARATOR = "\n\n"

    # Constructors
    def __init__(self, name, attributes=None, methods=None, base_class=None, element_type="Class"):
        super().__init__(name, element_type)
        self.set_attributes(attributes)
        self.set_methods(methods)
        self.set_base_class(base_class)

    # Methods
    def generate(self):
        return (
            f"{self.generate_header()}"
            f"\n{self.indent(self.generate_attributes(), 1)}"
            f"{self.__CATEGORY_SEPARATOR}{self.indent(self.generate_init(), 1)}"
            f"{self.__CATEGORY_SEPARATOR}{self.indent(self.generate_methods(), 1)}"
            f"{self.__CATEGORY_SEPARATOR}{self.indent(self.generate_getters(), 1)}"
            f"{self.__CATEGORY_SEPARATOR}{self.indent(self.generate_setters(), 1)}"
            f"{self.__CATEGORY_SEPARATOR}{self.indent(self.generate_tostring(), 1)}"
        )

    def get_attribute_names(self):
        attribute_names = []

        for attribute in self.get_attributes():
            attribute_names.append(attribute.get_name())

        return attribute_names

    def get_inherited_attribute_names(self):
        inherited_attribute_names = []
        curr = self.get_base_class()

        while curr is not None:
            inherited_attribute_names = curr.get_attribute_names() + inherited_attribute_names
            curr = curr.get_base_class()

        return inherited_attribute_names

    def generate_imports(self):
        if self.get_base_class() is None:
            return ""

        return (
            f"from {self.get_base_class().get_name()} import {self.get_base_class().get_name()}"
        )

    def generate_header(self):
        header = f"class {self.get_name()}:"

        if len(self.get_inherited_attribute_names()) > 0:
            header = f"class {self.get_name()}({self.get_base_class().get_name()}):"

        return header

    def generate_attributes(self):
        attributes = f"# Attributes"

        for attribute_name in self.get_attribute_names():
            attributes += f"\n__{attribute_name} = None"

        return attributes

    def generate_init(self):
        attribute_names = self.get_attribute_names()
        inherited_attribute_names = self.get_inherited_attribute_names()
        all_attribute_names = inherited_attribute_names + attribute_names

        init = (
            f"# Constructor"
            f"\ndef __init__(self, {", ".join(all_attribute_names)}):"
        )

        if len(inherited_attribute_names) > 0:
            init += f"\n\tsuper().__init__({", ".join(inherited_attribute_names)})"

        for attribute_name in attribute_names:
            init += f"\n\tself.set_{attribute_name}({attribute_name})"

        return init

    def generate_methods(self):
        methods = f"# Methods\n"

        for method in self.get_methods():
            methods += f"{method.generate_method()}" + self.__FUNCTION_SEPARATOR

        return methods[:-len(self.__FUNCTION_SEPARATOR)]

    def generate_getters(self):
        getters = f"# Getters\n"

        for attribute in self.get_attributes():
            getters += attribute.generate_getter() + self.__FUNCTION_SEPARATOR

        return getters[:-len(self.__FUNCTION_SEPARATOR)]

    def generate_setters(self):
        setters = f"# Setters\n"

        for attribute in self.get_attributes():
            setters += attribute.generate_setter() + self.__FUNCTION_SEPARATOR

        return setters[:-len(self.__FUNCTION_SEPARATOR)]

    def generate_tostring(self):
        tostring = (
            f"# Tostring"
            f"\ndef __str__(self):"
            f"\n\treturn ("
            f"\n\t\t" + r'f"' + self.get_name() + r':"'
        )

        if len(self.get_inherited_attribute_names()) > 0:
            tostring += "\n\t\t" + r'f"\n\t{' + "super().__str__()" + r'}"'

        for attribute_name in self.get_attribute_names():
            tostring += "\n\t\t" + r'f"\n\t' + f"{attribute_name}: " + r'{' + f"self.get_{attribute_name}()" + r'}' + r'"'

        tostring += "\n\t)"

        return tostring

    # Getters
    def get_attributes(self):
        return self.__attributes

    def get_methods(self):
        return self.__methods

    def get_base_class(self):
        return self.__base_class

    # Setters
    def set_attributes(self, attributes):
        self.__attributes = attributes

        for attribute in attributes:
            self.add_child(attribute)

    def set_methods(self, methods):
        self.__methods = methods

        for method in methods:
            self.add_child(method)

    def set_base_class(self, base_class):
        self.__base_class = base_class

    # Alias for set_base_class
    def inherits(self, base_class):
        self.set_base_class(base_class)
