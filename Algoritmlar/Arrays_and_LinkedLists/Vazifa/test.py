
from vazifa import pilus, Listlar
my_list = Listlar()

my_list.head = pilus("Kechki rejalarim :")

plan1 = pilus('Kopiya qilish')
plan2 = pilus('Kechki ovqat')
plan3= pilus('Bozorlik')

my_list.head.next = plan1
plan1.next = plan3
plan3.next =plan2 

# print(my_list.head.next.next.data)

print(my_list.consolga_chiqar())
print(my_list.push('Xohlasam borib yotaman'))