import itertools
from math import sqrt

def dist(x,y):
    # res = 0
    cal = ((x[1]-x[0])**2)+((y[1]-y[0])**2) # Euclidean distance
    return sqrt(cal)

def is_rect(a,b,c,d):
    a,b,c,d = sorted([a,b,c,d]) # complexity O(nCr)
    if a[0] == b[0] and c[0] == d[0] and a[1] == c[1] and b[1] == d[1]: # condition to check if the co-ordinates form a quadrilateral
        # if dist(a,b) == dist(b,d): # condition to check if it's a square
        if dist(a,b) != dist(b,d): # condition to check if it's a rectangle
            # print('unsorted')
            # print(a,b,c,d)
            # a,b,c,d = sorted([a,b,c,d])
            # print('sorted')
            # print(a,b,c,d)
            # print('yes')
            # print(dist(a,b))
            # print(dist(b,d))
            return True

    else:
        return False


def num_rect(coordinates):
    # temp_list = []
    count = 0
    # check = 0
    for a,b,c,d in itertools.combinations(coordinates, 4):
        # check+=1
        flag = is_rect(a,b,c,d)
        if flag:
            count+=1
    # print(f'check is -> {check}')
    return count

ans = num_rect([[1,1],[0,1],[0,0],[1,0],[2,0],[2,1]])
print(f'{ans} rectangle(s) can be extracted from these co-ordinates')