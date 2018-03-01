import copy
import sys
import heapq
import random

# N Queen Pazzle
N = 4

def heuristic(position, q_position):
    if position == None:
        return 0
    if len(q_position) < 2:
        return 0
    posx = position % N
    posy = position // N
    pos = [posx, posy]
    x = (posx + 1) % N
    y = (posy + 1) // N
    xy = [x, y]
    cnt = 0
    q_pos_lst = [] # capturable candidates on oblique line
    for q in q_position:
        qx = q % N
        qy = q // N
        if posx == qx or posy == qy:
            cnt += 1 # count queen captured vartical or horizonal line
        else:
            q_pos_lst.append([qx, qy])   
    while not pos == xy:
        if xy in q_pos_lst :
            cnt += 1
        x = (x + 1) % N
        y = (y + 1) // N
        xy = [x, y]
    x = (posx + 1) % N
    y = (posy + 1) // N
    xy = [x, y]
    while not pos == xy:
        if xy in q_pos_lst :
            cnt += 1
        x = (x - 1) % N if x - 1 >= 0 else N - 1
        y = (y - 1) // N if y - 1 >= 0 else N - 1
        xy = [x, y]
    return cnt

class node:
    def __init__(self, position, q_position, depth):
        self.depth = depth            
        self.q_position = copy.deepcopy(q_position)
        self.cost = 0
        if position != None:
            self.position = position
            self.depth = depth
            self.cost = depth + heuristic(self.position, self.q_position)
            self.q_position.append(self.position)       
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) == type(other):
            return False
        else:
            return self.cost == other.cost
    def __lt__(self, other):
        return self.cost < other.cost


def printState(q_position):
    for i in range(N*N):
        if i in q_position:
            if i % N == N-1:
                print('Q')
            else:
                print('Q ', end = '')
        else:
            if i % N == N-1:
                print('- ')
            else:
                print('- ', end = '')
    print('')
        

def aStar():
    open = []
    close = {}
    q_position = []
    open.append(node(None, q_position, 0))
    close[tuple(q_position)] = True
    extracted = 0
    while True:
        if not open:
            print('Search failed.')
            return (999, 0, 0)
        n = heapq.heappop(open)
        printState(n.q_position)
        if len(n.q_position) == N:
            print("Search successed.")
            return (n.depth, extracted, float(format(extracted ** (1 / n.depth), '.3f'))) if n.depth else (0, 0, 0)
        else:
            for position in range(N*N):
                if not (position in n.q_position):
                    child = node(position, n.q_position, n.depth + 1)
                    key = tuple(child.q_position)
                    if not key in close:
                        heapq.heappush(open, child)
                        close[key] = True                
                        extracted += 1        

aStar()
