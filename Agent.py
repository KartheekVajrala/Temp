class Agent:
  """Class for declaring Agent Object
  Takes 3 params
  dep : department
  year and hall currently in.
  """
  def __init__(self, dep, year, hall):
    self.dep = dep
    self.year = year
    self.hall = hall

  def get_year(self):
    return self.year
  def get_dep(self):
    return self.dep
  def get_hall(self):
    return self.hall
