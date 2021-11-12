
# def sort(array=[12,4,5,6,7,3,1,15]):
#     """Sort the array by using quicksort."""

#     less = []
#     equal = []
#     greater = []

#     if len(array) > 1:
#         pivot = array[0]
#         for x in array:
#             if x < pivot:
#                 less.append(x)
#             elif x == pivot:
#                 equal.append(x)
#             elif x > pivot:
#                 greater.append(x)
#         # Don't forget to return something!
#         return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
#     # Note that you want equal ^^^^^ not pivot
#     else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
#         return array


# print(sort())


# def taxla(array=[33,555,6667,2,3,1,4,56,8,9.7,6,77,5]):
#   chap=[]
#   ong=[]
#   tanla=[]

#   if len(array) > 1:
#     pivot = array[0]
    
#     for x in array:
#       if x < pivot:
#         chap.append(x)
#       elif x == pivot:
#         ong.append(x)
#       elif x> pivot:
#         tanla.append(x)
#         print(f"{taxla(chap)} + {ong}+ {taxla(tanla)}")
#       else:
#         print(array)     

# print(taxla())


from  random import  randrange

def qsort(array):
  if len(array)<2:
    return array
  else:
    pivot =array.pop(0)
    kichik = [i for i in array if i <=pivot]
    katta =[i for i in array if i>pivot]
    print(f"{qsort(kichik)} + {pivot}+ {qsort(katta)}")  
    return qsort(kichik)+[pivot]+qsort(katta)


if __name__ == "__main__":
  # array1 = [222,1,4,55,6,22]    
  # print(array1)
  # print(qsort(array1))
  array2 = list(range(20))
  print(array2)
  print(qsort(array2))
 
