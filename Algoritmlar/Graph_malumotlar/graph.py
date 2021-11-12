from collections import deque



def search(start_node, target='jobs'):
  search_que = deque()
  # deque malumotlar tuzilmasi

  search_que += graph[start_node]

  searched = set()


  while  search_que:
    person = search_que.popleft()

    if person not in searched:
      if person == target:
        print("f{target} ni topdik")
        return True
      else:
        search_que += graph[person]
        searched.add(person)
    return False

if __name__ == '__main__':
  graph={
    'siz':['ali','vali','shali'], 'ali':['aziza','bahodir','akbar'], 'vali':['ahmad','alibobo'],'shali':['jobs','musk','mark'], 'botir':[], 'jobs':['stiv'],'mamur':[]
  }

  search('siz','mamur')

