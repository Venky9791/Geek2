vow = ['a','e','i','o','u']

iter_vow = iter(vow)

# try:
#     print(iter_vow.__next__())
#     print(iter_vow.__next__())
#     print(iter_vow.__next__())
#     print(iter_vow.__next__())
#     print(iter_vow.__next__())
#     print(iter_vow.__next__())
# except:
#     print("I cant Iter any more")


try:
    for i in iter_vow:
        print(i)
except:
    print("I cant Iter Any more")

arr1 = [10,11,20,30,40,50]
iter_vow1 =  iter(arr1)

while True:
    try:
        print(iter_vow1.__next__())
    except:
        print("I can print any more ")
        break


class Counter:

    def __init__(self,start,end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num+=1
            return self.num-1

if __name__ == '__main__':
    a,b = 2,5
    c1 = Counter(a,b)
    c2 = Counter(a,b)

    print("Way 1 Printing without using Iter")
    print("*" *50)
    for i in c1:
        print("Eating more Pizza's ",i)

    print("Way2 Printing using Iter Object")

    obj = iter(c2)
    try:
        while True:
            print("Eating more Pizza's using Iter",next(obj))
    except:
        print("Eating more food , GAME Over")





