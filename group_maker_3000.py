import random

print('Group Maker 3000')

table1 = []
table2 = []
table3 = []
table4 = []
table5 = []
table6 = []

classList = []

tableNumber = 1

randomPick = []

while len(classList) > 0:
  randomPick = random.choice(classList)
  if tableNumber == 1:
    table1.append(randomPick)
  if tableNumber == 2:
    table2.append(randomPick)
  if tableNumber == 3:
    table3.append(randomPick)
  if tableNumber == 4:
    table4.append(randomPick)
  if tableNumber == 5:
    table5.append(randomPick)
  if tableNumber == 6:
    table6.append(randomPick)
  classList.remove(randomPick)
  tableNumber = tableNumber + 1
  if tableNumber == 7:
    tableNumber = 1

print("Table 1: ", table1)
print("Table 2: ", table2)
print("Table 3: ", table3)
print("Table 4: ", table4)
print("Table 5: ", table5)
print("Table 6: ", table6)
