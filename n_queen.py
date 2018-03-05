import copy
import sys
import heapq
import random

# N Queen Pazzle


def heuristic(N, put_pos, position):
    if not position:
        return 0
    for i in position:
        x = put_pos  % N
        y = put_pos // N
        ix = i  % N
        iy = i // N
        if ix == x or iy == y:
            return 1
        elif ix > x and iy > y:
            while x <= N and y <= N:
                if ix == x and iy == y:
                    return 1
                x += 1
                y += 1
        elif ix < x and iy < y:
            while x >= 0 and y >= 0:
                if ix == x and iy == y:
                    return 1
                x -= 1
                y -= 1
        elif ix > x and iy < y:
            while x <= N and y >= 0:
                if ix == x and iy == y:
                    return 1
                x += 1
                y -= 1
        elif ix < x and iy > y:
            while x >= 0 and y <= N:
                if ix == x and iy == y:
                    return 1
                x -= 1
                y += 1
    return 0

class node:
    def __init__(self, N, position, q_position, depth, prev_heu):
        self.depth = depth            
        self.q_position = copy.deepcopy(q_position)
        self.cost = 0
        if position != None:
            self.position = position
            self.depth = depth
            self.heu = heuristic(N, self.position, self.q_position) + prev_heu
            self.cost = depth + self.heu
            self.q_position.append(self.position)
            self.q_position.sort()
        else:
            self.heu = 0     
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) == type(other):
            return False
        else:
            return self.heu == other.heu
    def __lt__(self, other):
        return self.heu < other.heu


def printState(N, q_position):
    for i in range(N * N):
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
        

def aStar(N):
    open = []
    ans = []
    close = {}
    q_position = []
    open.append(node(N, None, q_position, 0, 0))
    close[tuple(q_position)] = True
    extracted = 0
    while True:
        sys.stdout.write("\033[2K\033[G%d" % extracted)
        sys.stdout.flush()
        if not open:
            #print('Search finished.')
            return ans
        n = heapq.heappop(open)
        #printState(N, n.q_position)
        if len(n.q_position) == N and n.heu == 0:
            ans.append(n)
            #print("Search successed.")
        elif len(n.q_position) >= N:
            pass
        elif n.heu > 0:
            pass
        else:
            for position in range(N * N):
                if not (position in n.q_position):
                    child = node(N, position, n.q_position, n.depth + 1, n.heu)
                    key = tuple(child.q_position)
                    if (not key in close) and n.heu == 0:
                        heapq.heappush(open, child)
                        close[key] = True                
                        extracted += 1        
N = int(input('> input N : '))
i = 1
for ans in aStar(N):
    print('ans' + str(i))
    #print(ans.q_position)
    printState(N, ans.q_position)
    i += 1
