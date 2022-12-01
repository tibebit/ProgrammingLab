class CSVFile:
  def __init__(self, name):
    self.name = name
    
  def get_data(self):
    elements = []
    try:   
      my_file = open(self.name, 'r')
    except OSError as e:
      print("Errore: {}".format(e))
    for line in my_file:
      values = line.split(',')
      if values[0] != 'Date':
        elements.append([values[0], values[1].strip()])

    return elements
