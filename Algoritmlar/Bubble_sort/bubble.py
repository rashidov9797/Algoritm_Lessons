from  random import randrange

def bubbleSort(list_a):
  length = len(list_a) -1
  sorted=False

  while not sorted:
    sorted = True
    for i in range(0,length):
      if list_a[i] > list_a[i+1]:
        sorted=False
        list_a[i],list_a[i+1] = list_a[i+1], list_a[i]
    return list_a

