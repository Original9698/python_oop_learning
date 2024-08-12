class Dog:
    def __init__(self, name_dog, age_dog):
        self.name = name_dog
        self.age = age_dog
    def description(self):
        return f'{self.name} is {self.age} years old'
    def speak(self,sound:str):
        return f'{self.name} says {sound}'

