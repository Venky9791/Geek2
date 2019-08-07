'''
# Python3 code to demonstrate working of
# Converting String content to dictionary
# Using dictionary comprehension + split()

# initializing string
test_str = "Gfg = 1, Good = 2, CS = 3, Portal = 4"
'''

test_str = "Gfg = 1, Good = 2, CS = 3, Portal = 4"
test_str_lst = test_str.split(',')
res = {key:int(val) for key,val in (item.split('=') for item in test_str.split(','))}
print(res)
test_str_lst1 = [lis1 for lis1 in [item.split('=') for item in test_str.split((','))]]

tup1 = (tup1 for tup1 in tuple(item.split('=') for item in test_str.split((','))))
tup1 = tuple(test_str_lst1)
print(tup1)


print()
print('*'*50)
print(test_str_lst1)
res = eval('dict(% s)' %test_str)

print(res)