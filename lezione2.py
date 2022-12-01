def sum_list(my_list):
  if not len(my_list):
      return None
  total = 0
  for item in my_list:
    total += item
  return total

my_list = []
print(sum_list(my_list))