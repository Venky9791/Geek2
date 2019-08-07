from collections import  Counter
'''
Given three arrays sorted in non-decreasing order, print all common elements in these arrays.

Examples:

Input:  ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output: [80, 20]

Input:  ar1 = [1, 5, 5]
        ar2 = [3, 4, 5, 5, 10]
        ar3 = [5, 5, 10, 20]
Output: [5, 5]
'''

#ar1 = [1, 5, 5]
#ar2 = [3, 4, 5, 5, 10]
#ar3 = [5, 5, 10, 20]

ar1 = [1, 20, 9, 12, 14, 89]
ar2 = [6, 7, 20, 80,80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

s1 = set(ar1)
s2=set(ar2)
s3=set(ar3)
print(s1.intersection(s2).intersection(s3))


''' Another Soultion using Dict Counters'''

f1 = Counter(ar1)
f2 = Counter(ar2)
f3 = Counter(ar3)



resultDict = dict(f1.items() & f2.items() & f3.items())
#print(resultDict)


#print(f1)
#print(f2)
#print(f3)

for key,value in f1.items():
    if key in f2 and key and f3:
        print (key,end= " ")


