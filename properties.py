class Property:
    def __init__(self, var_name: str, name: str, clazz, **kwargs):
        self.var_name = var_name
        self.name = name
        self.property = clazz(name=name, **kwargs)