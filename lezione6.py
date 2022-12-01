class CSVFile:
  def __init__(self, name):
    if not isinstance(name, str):
      raise Exception('Eccezione con name: {}'.format(name))
    self.name = name

  def is_range_correct(start, end, min, max):
    if start  != None and end != None:
      if start < 0 and end < 0:
        raise IndexError('Errore ottenuto con start: {}, end:{}'.format(start,end))
      if end < start:
        raise IndexError('Errore ottenuto con start: {}, end:{}'.format(start,end))
    elif start == None:
      start = min
    elif end == None:
      end = max
    
    
  # funzione che legge i dati di un csv
  def get_data(self, start=None, end=None):
    elements = []
    try:   
      my_file = open(self.  name, 'r')
    except OSError as e:
      print("Errore: {}".format(e))
    # leggo tutte le righe del file e le salvo in elements
    for line in my_file:
      values = line.split(',')
      if values[0] != 'Date':
        temp = []
        index = 0
        for item in values:
          index += 1
          temp.append(item.strip())
        elements.append(temp)
    # eseguo un controllo sulla correttezza degli indici
    if start == None and end == None:
      return elements
    else:
      try:
        is_range_correct(start, end, 0, index)
        sliced = elements[start:end]
        return sliced
      except IndexError as e:
        print("Errore ottenuto: {} con indici start {} e end {}".format(e, start, end))
        return new
      except Exception as e:
        print("Errore ottenuto: {} con indici start {} e end {}".format(e, start, end))


class NumericalCSVFile(CSVFile):
  
  def get_data(self, *args, **kwargs):
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


csv_file = CSVFile("shampoo_sales.csv")
rows = csv_file.get_data(-1, -5)
print(rows)