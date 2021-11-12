

from random import randrange

# def qsort(array):
#   if len(array)<2:
#     return array
#   else:
#       pivot = array.pop(randrange(len(array)))
#       kichik = [i for i in array if i<=pivot]
#       #agar i katta bo'lsa tanlangan sondan
#       katta = [i for i in array if i>pivot]
#       #agar i kichik bolsa tanlangan sondan
#       return qsort(kichik) + [pivot] + qsort(katta)



def qsort(array):
  if len(array)<2:
    return array
  else:
    pivot_tayanch_nuqta = array.pop()
    kichik = [i for i in array if i<= pivot_tayanch_nuqta]
    katta = [i for i in array if i>pivot_tayanch_nuqta]

    print(f"{kichik} + [pivot_tayanch_nuqta] + qsort(katta)")

    return qsort(kichik) + [pivot_tayanch_nuqta] + qsort(katta)


if __name__ == '__main__':
  # array1=[1,5,7,88,-8,889]
  # print(array1)    
  array2 =list(range(20))
  print(qsort(array2))
