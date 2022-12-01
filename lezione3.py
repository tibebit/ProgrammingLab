def sum_list(my_list):
  if not len(my_list):
      return None
  total = 0
  for item in my_list:
    total += item
    
  return total

  
def read_csv(file_name):
  elements = []
  my_file = open(file_name, 'r')
  for line in my_file:
      values = line.split(',')
      if values[0] != 'Date':
        elements.append(values[1])

  return elements


def parse_csv(elements):
  values = []
  for element in elements:
    try:
      values.append(float(element))
    except:
      None

  return values

  
def sum_csv(file_name):
  elements = read_csv(file_name)
  values = parse_csv(elements)
  
  return sum_list(values)