class Robot:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    
    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I am a {self.model} model robot built in {self.year}.")
    
    def abilities(self):
        print("I can walk, talk, and assist you with simple tasks.")
    
    def farewell(self):
        print(f"It was nice meeting you. Goodbye from {self.name}!")

# Create a robot object
robot1 = Robot("RoboRoy", "XJ-9", 2025)

# Introduce the robot
robot1.introduce()
robot1.abilities()
robot1.farewell()
