
# def search(list,n):
#   i=0
#   while i<len(list):
#     if list[i] == n:
#       print(f'Nihoyat biz {n} sonini topdik hehehehe')
#       return True
#     i=i+1  
#   return False



# list = [443,33,6,7,88,9,21]

# n=21
# if search(list,n):
#   print(f'Biz {n} sonini topdik')
# else:
#   print('Error!') 

# print(search)   


# LINEAR SEARCH

def linear_search(list,item):
  for n in range(len(list)):
    if list[n] == item:
      return n
  return None



def binary_search(list,item):
  low=0
  heigh = len(list)-1
  while low <= heigh:
    mid = (low+heigh)//2
    # -- //2 ---> Pastki va quyi chegarani ikkiga bo'lib uni butun qismini olamiz
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      heigh = mid -1  
    else:
      low = mid +1
  return None      


# mylist=[1,2,3,5,7,8,9,14,23,24,33,77]  
# print(linear_search(mylist,7))
# print(binary_search(mylist,7))

# mylist=[1,233,533,5,67,8,99,4,3,2,333,77]
# mylist.sort()
# print(linear_search(mylist,2))
# print(binary_search(mylist,2))


mevalar = ['olma','anor','nok','behi']
# mevalar.sort()
print(binary_search(mevalar,'behi'))