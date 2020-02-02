# generating sudoku grid filled with numbers


def showgrid():

    print("grid")
    for l in grid:
        print(l)

def clear(num,x,y):
    print("clear")
    modx = int(x/3)
    mody = int(y/3)
    for a in range(len(grid)):
        moda = int(a/3)
        for b in range(len(grid[a])):
            if grid[a][b] == "":
                showgrid()
                print("eradsa")
                quit()

            modb = int(b/3)
            if not (x == a and y == b):
                sqr = ((modx == moda) and (mody == modb))
                row = (x == a)
                cul = (y == b)
                if (sqr or row or cul) and type(grid[a][b]) == str:
                    grid[a][b] = grid[a][b].replace(str(num),"")
    showgrid()
    print(nums)

def generate(l):
    print("gen")
    if len(l) == 0:
        print("error on the way")
        showgrid()
        quit()
        return
    num = l[0]
    l.pop(0)
    print(l)
    count = 0
    global grid
    bckp = grid
    skip = 0
    while bckp == grid:
        skipped = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if type(grid[x][y]) == str:
                    if str(num) in grid[x][y]:
                        if skip == skipped:
                            grid[x][y] = num
                            count+=1
                            clear(num,x,y)
                        elif skipped < skip:
                            skipped +=1
                            grid[x][y] = grid[x][y].replace(str(num),"")
                        if skipped > skip:
                            print("waaat")
        if count != 9:
            print(f"{num} , {count}")
            print("ERRRRROR")
            skip+=1
            if skip > (9-num):
                print("errrrrerrrrrrr")
            grid = bckp

    return l

def done():
    print("done")
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if type(grid[x][y]) != int:
                return False
    return True

def main():
    print("main")
    global nums
    nums = [i for i in range(1,10)]
    while not done():
        nums = generate(nums)
        print(nums)
        showgrid()
        input()

if __name__ == "__main__":
    grid = [["123456789" for i in range(9)] for i in range(9)]

    main()
