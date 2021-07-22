def func13(n):
    a,b = 0,1 
    while a<n:
        print(a , end=" ")
        a,b = b,a+b
    print()

def func14(n):
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b,a+b
    return result

if __name__ == "__main__":
    import sys
    func13(int(sys.argv[1]))