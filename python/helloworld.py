def main():
    print('Hello World')
    testList()
    testPlural()
    testTuple()
    getAddress()
    
##list
def testList():
    x = [1,2,3]
    print(type(x))
    print(x)
    x[1] = 0   ##列表是数组
    print(x)

##plural
def testPlural():
    a = 1 + 2j
    b = 2 + 3j
    print(type(a))
    print(a+b)

##元组和字符串不可以修改
def testTuple():
    x = (1,2,3)
    print(type(x))

def getAddress():
    A = 123;
    B = 456;
    C = (1,2,3)
    print(id(A))
    print(id(B))
    print(id(C))
    print(id(C[0]))
    print(id(C[1]))
    print(id(C[2]))
    print(id(getAddress))
    
main()

