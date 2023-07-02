def gugu():
    for i in range(1, 10):
        for j in range (1, 10):
            print(str(i) + "*" + str(j) + "=" + str(i*j))

    return


def gugu1():
        
    for j in [1,4,7]:
        for i in range(1, 10):

            # print(str(i) + "*" + str(j) + "=" + str(i*j))
            print("{} * {} = {} {} * {} = {}  {} * {} = {}".format (j, i, i * j, j + 1, i , (j + 1) * i, j + 2, i , (j + 2) * i))
        print("\n")
    return

def gugu2():
    # for j in range():
    n = 3
    m = 6
    b = 9
    for i in range (1, n+1):
        for j in range (1,n+1):
            print("{} * {} = {} {} * {} = {}  {} * {} = {}".format (j, i, i * j, j + 1, i , (j + 1) * i, j + 2, i , (j + 2) * i))
    print("\n\n")
    for i in range (4, m+1):
        for j in range (1,m+1):
            print("{} * {} = {} {} * {} = {}  {} * {} = {}".format (j, i, i * j, j + 1, i , (j + 1) * i, j + 2, i , (j + 2) * i))
    print("\n\n")
    for i in range (7, b+1):
        for j in range (1,b+1):
            print("{} * {} = {} {} * {} = {}  {} * {} = {}".format (j, i, i * j, j + 1, i , (j + 1) * i, j + 2, i , (j + 2) * i))


        # for i in range(1, 10):
        #     j = 1
            
        #     print("{} * {} = {} {} * {} = {} {} * {} = {}".format (j, i, i * j, j + 1, i , (j + 1) * i, j + 2, i , (j + 2) * i))
    
    


#gugu()

gugu1()

#gugu2()


# {} * {} = {}  {} * {} = {}"
# 