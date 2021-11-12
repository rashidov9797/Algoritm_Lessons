

class pilus:
  """Tugun"""

  def __init__(self,data):
    self.data = data
    self.next = None


class  Listlar:
  """Obyeklar"""
  def __init__(self):
    self.head = None    


  def consolga_chiqar(self):
    cons=self.head
    while cons:
      print(cons.data)
      cons=cons.next 

  def push(self,new_element):
    new_list = pilus(new_element)
    new_list.next = pilus(new_element)
    self.head = new_list     

