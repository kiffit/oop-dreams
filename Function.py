# Thomas Safago
# 02/28/2025


from Variable import Variable


class Function(Variable):
    # Constructors
    def __init__(self, name, parameters=None, return_type="Any", element_type="Function"):
        super().__init__(name, return_type, element_type)

        if parameters is not None:
            for parameter in parameters:
                self.add_child(parameter)

    # Methods
    def get_children_names(self):
        children_names = []

        for child in self.get_children():
            children_names.append(child.get_name())

        return children_names

    def generate_function(self):
        return (
            f"def {self.get_name()}({", ".join(self.get_children_names())}):"
            f"\n\tpass"
        )

    def generate_method(self):
        return (
            f"def {self.get_name()}({", ".join(["self"] + self.get_children_names())}):"
            f"\n\tpass"
        )
