import csv

def get_data_from_csv(filename):
    
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = []
    for row in reader:
      data.append(row[0])
  arrays = []
  for i in range(0, len(data), 28):
    array = data[i:i + 28]
    if len(array) == 28:
      arrays.append(array)
  return arrays

def main():
  """Gets the arrays from the CSV file and prints them."""

  filename = 'numbers-entertainment.csv'
  arrays = get_data_from_csv(filename)
  for array in arrays:
    print(array)

if __name__ == "__main__":
  main()
