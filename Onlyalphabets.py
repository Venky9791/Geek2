'''
Given a string consisting of alphabets and others characters, remove all the characters other than alphabets and print the string so formed.
Examples:

Input : str = "$Gee*k;s..fo, r'Ge^eks?"
Output : GeeksforGeeks

'''

str1 = "$Gee*k;s..fo, r'Ge^eks?"

#for i in str1:
   # print(i, end='')
    #if ord(i) in range(ord('A'),ord('Z')) or ord(i) in range(ord('a'),ord('z')):
        #pass
       # print()
       #print(i,end='')

res = [x for x in str1 if  ord(x) in range(ord('A'),ord('Z')) or ord(x) in range(ord('a'),ord('z')) ]

print(''.join(res))