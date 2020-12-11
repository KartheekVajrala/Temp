class Agent:
  def __init__(self, name, RollNo, currentYear):
    self.name = name
    self.RollNo = RollNo
    self.currentYear = currentYear

p1 = Agent("Jhon", "50", 3)

print(p1.__dict__)
