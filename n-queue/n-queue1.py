import time
start_time = time.time()
from itertools import permutations


def print_table():
    for row in range(11):
        print(table[row])

def put_queen(x,y):
    if table[y][x] == 0:
        for m in range(11):
            table[y][m] = 1
            table[m][x] = 1
            table[y][x] = 2
            if y+m <= 10 and x+m <= 10:
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= 10:
                table[y-m][x+m] = 1
            if y+m <= 10 and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1
        return True
    else:
        return False

table = [[0]*11 for _ in range(11)]
perms = permutations([0,1,2,3,4,5,6,7,8,9,10])


num_comb = 0

for perm in perms:
    if put_queen(perm[0], 0) == True:
        if put_queen(perm[1], 1) == True:
            if put_queen(perm[2], 2) == True:
                if put_queen(perm[3], 3) == True:
                    if put_queen(perm[4], 4) == True:
                        if put_queen(perm[5], 5) == True:
                            if put_queen(perm[6], 6) == True:
                                if put_queen(perm[7], 7) == True:
                                    if put_queen(perm[8], 8) == True:
                                        if put_queen(perm[9], 9) == True:
                                            if put_queen(perm[10], 10) == True:
                                                print_table()
                                                num_comb += 1
                                                print(f"solution{num_comb}")
                                                print(" ")
    table = [[0] * 11 for _ in range(11)]
print("--- %s seconds ---" % (time.time() - start_time))
'''//////////////////////////////////////////////////////////////////////////////////////////////////////'''
start_time = time.time()
N = 11			 # N x N Board
numSol = 0  			# number of solutions

b = N*[-1]  			# indices = rows, b[index] = coloumn, first init to -1
colFree = N*[1] 			# all N col are free at first
upFree = (2*N - 1)*[1] 		# all up diagonals are free at first
downFree = (2*N - 1)*[1]    		# all down diagonals are free at first

def printBoard(b):
    print(b)

def putQueen(r, b, colFree, upFree, downFree):
    global N
    global numSol
    for c in range(N): # ใล่ใส่ไปทีละ column ทุก col.
        if colFree[c] and upFree[r+c] and downFree[r-c+N-1]: #ใส่ได้?
            b[r] = c    # ใส่ ที่ r, c

            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0 # เปลี่ยน data struct ไม่ให้ใส่แนวนี้

            if r == N-1:       # ถ้าใส่ควีนครบแล้ว
                printBoard(b)  #print(b)
                numSol += 1
            else:
                putQueen(r+1, b, colFree, upFree, downFree)  # ใส่ควีนแถวถัดไป
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1 #เอา Queen ออกเพื่อให้ได้ solution อื่น
                                                             # หรือ เพราะ queen ตัวนี้แม้ใส่ได้แต่ไม่ทำให้เกิด solution
putQueen(0, b, colFree, upFree, downFree)   #  first add at 1st  (ie. row 0)
print('number of solutions = ', numSol)
print("--- %s seconds ---" % (time.time() - start_time))
