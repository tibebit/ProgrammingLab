class CSVFile:
  def __init__(self, name):
    self.name = name
    
  def get_data(self):
    elements = []
    my_file = open(self.name, 'r')
    for line in my_file:
      values = line.split(',')
      if values[0] != 'Date':
        elements.append([values[0], values[1].strip()])

    return elements