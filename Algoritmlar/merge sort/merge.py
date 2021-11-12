from colorama import Fore, Back, Style

# def mergeSort(arr = [33,44,55,2,66]):
#   if len(arr) >1:
#     mid = len(arr) //2


#     l = arr[: mid]
#     print(Back.GREEN + str(l))


#     r = arr[:mid]
#     print(Back.RED + str(r))


#     mergeSort((l))

#     mergeSort((r))

#     i=j=k=0


a = [3,555,67,8,1,33,6]
b=[55,6,78,34,2,222]
print(a)
print(b)
def merge(list1,list2,m,n):
  i=0
  j=0
  o=[]

  while (i<m and j <n):
    if list1[i] <= list2[j]:
      o.append(list1[i])
      i += 1
    else:
      o.append(list2[j])
      j += 1
  for p in range(i,m):
    o.append(list1[p])
  for q in range(j,n):
    o.append(list2[q])

  print(o)

merge(a,b, len(a), len(b))            