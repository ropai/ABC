import random
aList = 1
def main():
    print('Python List')
    print(id(aList))
    ListTest1()
    ListTest2()
    MapTest()

def ListTest1():
    aList=[x * x for x in range(10)]
    print(id(aList))
    print(aList)
    print('min:', min(aList),'max:',max(aList), sep=' ', end='\n')
    random.shuffle(aList)
    print(aList)

def ListTest2():
    ##random.shuffle(aList)
    print(id(aList))


    
def MapTest():
    bList = list(range(2,20,2))
    print(bList)
    def add3(v):##嵌套定义
        return v + 3
    print(list(map(add3, range(10))))
    

    def add(x,y):##dual parameter
        return x+y
    print(list(map(add, range(10),range(10,20))))

    print(list(map(lambda x,y:x+y, range(10), range(10,20))))
    
main()
