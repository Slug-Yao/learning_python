class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def update_name(self,name):
        self.name=name