def printState(n, position):
    for i in range(n * n):
        if i % n == n - 1:
            if i in position:
                print('Q')
            else:
                print('-')
        else:
            if i in position:
                print('Q', end = '')
            else:
                print('-', end = '')

def isCapturable(n, put_pos, position):
    if not position:
        return True
    for i in position:
        x = put_pos  % n
        y = put_pos // n
        ix = i  % n
        iy = i // n
        if ix == x or iy == y:
            return False
        elif ix > x and iy > y:
            while x <= n and y <= n:
                if ix == x and iy == y:
                    return False
                x += 1
                y += 1
        elif ix < x and iy < y:
            while x >= 0 and y >= 0:
                if ix == x and iy == y:
                    return False
                x -= 1
                y -= 1
        elif ix > x and iy < y:
            while x <= n and y >= 0:
                if ix == x and iy == y:
                    return False
                x += 1
                y -= 1
        elif ix < x and iy > y:
            while x >= 0 and y <= n:
                if ix == x and iy == y:
                    return False
                x -= 1
                y += 1
    return True

def nQueenPazzle(n):
    position = []
    while True:
        printState(n, position)
        if len(position) == n:
            print('pazzle completed.')
            break
        x, y =  map(int, input('> input x y : ').split())
        put_pos = x + y * n
        if isCapturable(n, put_pos, position):
            print('success')
            position.append(put_pos)
        else:
            print('it\'ll be captured.')

nQueenPazzle(int(input('> input n: ')))
