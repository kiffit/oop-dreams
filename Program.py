# Thomas Safago
# 02/28/2025


from datetime import date
from os import makedirs, path

from BaseElement import BaseElement
from Class import Class


class Program(BaseElement):
    # Attributes
    __author_name = None

    # Separators
    __CATEGORY_SEPARATOR = "\n\n\n"
    __EOF = "\n"

    # Constructors
    def __init__(self, name, author_name, element_type="Program"):
        super().__init__(name, element_type)
        self.set_author_name(author_name)

    # Methods
    def generate(self):
        # Make new project directory
        makedirs(self.get_name(), exist_ok=True)

        # Generate driver
        with open(path.join(self.get_name(), "driver.py"), "w") as driver:
            driver.write(self.generate_driver_contents())

        # Generate classes
        for element in self.get_children():
            if type(element) is Class:
                with open(path.join(self.get_name(), f"{element.get_name()}.py"), "w") as class_file:
                    class_file.write(self.generate_class_contents(element))

        print("Project generated!")

    def generate_header(self):
        return (
            f"# {self.get_author_name()}"
            f"\n# {date.strftime(date.today(), "%m/%d/%Y")}"
        )

    def generate_driver_contents(self):
        return (
            f"{self.generate_header()}"
            f"{self.__CATEGORY_SEPARATOR}"
            f"def main():"
            f"\n\tpass"
            f"{self.__CATEGORY_SEPARATOR}"
            f"if __name__ == '__main__':"
            f"\n\tpass"
            f"{self.__EOF}"
        )

    def generate_class_contents(self, class_object):
        imports = class_object.generate_imports()
        if len(imports) > 0:
            imports += self.__CATEGORY_SEPARATOR

        return (
            f"{self.generate_header()}"
            f"{self.__CATEGORY_SEPARATOR}"
            f"{imports}"
            f"{class_object.generate()}"
            f"{self.__EOF}"
        )

    # Interactive methods
    def add_class(self, class_object):
        self.add_child(class_object)

    # Getters
    def get_author_name(self):
        return self.__author_name

    # Setters
    def set_author_name(self, author_name):
        self.__author_name = author_name
