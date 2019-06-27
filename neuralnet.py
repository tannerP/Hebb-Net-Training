import json
import sys

if(len(sys.argv) < 2):
  print("ERROR need a file")
  exit()

try:
  json_file = open(sys.argv[1], 'r') #getting filename from command line
  data = json.load(json_file)
except IOError as e:
    print("ERROR file not found")
    exit()

t = data['target']
x = data['training']

# initialize weights
w = [0] * (len(x) // 2) #integer division
b = 0

for row in range(len(x)):
  y = t[row]
  x_1 = x[row][0]
  x_2 = x[row][1]
  w[0] += x_1*y
  w[1] += x_2*y
  b = b + y

print("w", w)
print("b", b)
