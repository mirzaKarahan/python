adet = 0
for element in range(1,999999):
  for item in str(element):
    a = int(item)**len(str(element)) 
    if a == element:
      print(element)
      adet +=1
print("\n",adet)
