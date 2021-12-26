from collections import deque

if __name__ == '__main__':
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []


    def person_is_seller(name):
        return name[-1] == 'm'


    def search(name):
        # create a queue
        search_queue = deque()
        # add all the neighbors to the search queue. graph["you"] = ['alice', 'bob', 'claire']
        search_queue += graph[name]
        searched = []
        while search_queue:  # while there are still people in the queue
            person = search_queue.popleft()  # Grab the first person off the queue
            if person_is_seller(person):  # if the person is a mango seller
                print(person + ' is a mango seller!')  # Yes, he/she is a mango seller!
                return True
            else:
                search_queue += graph[person]  # No, they are not a mango seller. Add their friends to the search queue
        return False


    search('you')
