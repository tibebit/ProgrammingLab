class CSVFile:
  def __init__(self, name):
      self.name = name
    
  def get_data(self):
    elements = []
    try:   
      my_file = open(self.  name, 'r')
    except OSError as e:
      print("Errore: {}".format(e))
      return None
    for line in my_file:
      values = line.split(',')
      
      if values[0] != 'Date':
        temp = []
        
        for item in values:
            temp.append(item.strip())
          
        elements.append(temp)

    return elements


class NumericalCSVFile(CSVFile):
  
  def get_data(self, *args, *kwargs):
    elements = super().get_data(*args, **kwargs);
    parsed_values = []
    for element in elements:
      new_row = []
      for i, column in enumerate(element):
        if i == 0:
          new_row.append(column)
        else:
          try:
            new_row.append(float(column))
          except:
            print('Errore!')
      parsed_values.append(new_row)
    return parsed_values