class Agent:
  def __init__(self, name, RollNo, currentYear):
    self.name = name
    self.RollNo = RollNo
    self.currentYear = currentYear

p1 = Agent("Kartheek", "18ME10027", 3)

print(p1.__dict__)