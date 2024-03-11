class MyClass:
    all_instances = []

    def __init__(self, name):
        self.name = name
        MyClass.all_instances.append(self)

    @classmethod
    def print_all_instance(cls):
        '''
        class method
        '''
        for instance in cls.all_instances:
            print(instance.name)


# Creating instances
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")
obj3 = MyClass("Object 3")

# Accessing all instances through the class attribute
MyClass.print_all_instance()
