import json
import sys

if(len(sys.argv) < 2):
  print("ERROR need a file")
  exit(1)

try:
  json_file = open(sys.argv[1], 'r') #getting filename from command line
  data = json.load(json_file)
  json_file.close()
except IOError as e:
    print("ERROR file input")
    exit(1)

target = data['target']
training = data['training']

# initialize weights
w = [0] * (len(training) // 2) #integer division
b = 0

for row in range(len(training)):
  y = target[row]
  x_1 = training[row][0]
  x_2 = training[row][1]
  w[0] += x_1*y
  w[1] += x_2*y
  b = b + y

print("w", w)
print("b", b)
