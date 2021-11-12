
class Node:
    """ Tugun (node) obyekti"""
    def __init__(self,data):
        self.data =data
        self.next = None
        
class LinkedList:
    """LinkedList obyekti"""
    def __init__(self):
        self.head = None 
        
        
##Consolga chiqaruvchi funksiya
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next

    #Ro'yxatga element qo'shish
    def push(self,new_data):
        """List boshiga tugun qo'shish"""

        #Yangi Node yaratamiz
        new_node = Node(new_data)

        #List boshini keyingi o'ringa suramiz
        new_node.next = Node(new_data)

        #Yangi modelni list boshiga qo'yamiz

        self.head = new_node


    #Biror tugundan keyin qo'shish

    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        #Yangi yugun qo'shamiz
        new_node = Node(new_data)
        #Yangi tugunni keyingi tugunga bog'laymiz
        new_node.next = prev_node.next
        #Avvalgi tugunni yangi tugunga bog'laymiz
        prev_node.next = new_node

    #Oxiriga element qo'shish

    def append(self,new_data):
        """List oxiriga tugun qo'shish"""
        #Yangi tugun yaratamiz
        new_node = Node(new_data)
        #List bo'sh emasligini tekshiramiz
        if self.head is None:
            #List bo'sh bo'lsa ro'yxatning boshiga qo'shamiz
            self.head = new_node
            return
        #Aks holda list oxiriga boramiz
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node   

    #Listdan qiymatni o'chirish  

    def deleteNode(self,key):
        #List boshini topamiz
        temp = self.head
        #Birinchi tugunni tekshiramiz
        if (temp and temp.data == key):
            self.head = temp.next
            temp=None
            return
        #Aks holda keyingi tugunlarni qarab chiqamiz
        while temp:
            if temp.data == key:
                break
            prev=temp
            temp=temp.next
        #Agar qiymat topilmasa
        if temp==None:
            return
        #Tugunni listdan o'chiramiz
        prev.next = temp.next
        temp = None                    







    
        
                
        