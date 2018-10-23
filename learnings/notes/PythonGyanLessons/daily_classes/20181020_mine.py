

# import sys
# ll = sys.argv # returns a list whose first element(0-indexed element) is actually a file name (which we ran) (with absolute path) and from 2nd element onwards it gives command-line arguments
#
# print(ll[0])
# print(ll[1])
# print(ll[2])
# print(ll[3])

# 4


# n = 5
# space = " "
# star = "*"
#
# for i in range(1,2*n+1):
#     v1 = space * (n - (i% n))
#     v2 = star * ((2 * (i% n) - 1) )
#     print(v1 + v2)




# for i in range(1,n+1):
#     print(space*(n-i), end='')
#     print(star*(2*i-1))
#
# for i in range(n-1,0,-1):
#     print(space*(n-i), end='')
#     print(star*(2*i-1))


import os
import numpy as np
os.chdir("C:\\ML\\downloads")
import pandas as pd
df = pd.read_excel("sahilfile.xlsx")
df.columns = [column_name.replace(' ', '') for column_name in df.columns]

employee_id_1 = 'JS 1005'
employee_id_2 = 'JS 1001'
employee_id_3 = 'JS 1011'
employee_id_4 = 'JS 1008'

employee_ids = np.array([employee_id_1, employee_id_2, employee_id_3, employee_id_4])

df[df.Employeeid.isin(employee_ids)].to_excel('output.xls')


n = "12121"
if n[::-1] == n:
    print('YEss')
else:
    print('No')


n = "121321"
is_palindrome = True
for i in range(len(n)//2):
    if n[i] ==  n[len(n)-i-1]:
        pass
    else:
        is_palindrome = False
        break

if is_palindrome:
    print('Yess')
else:
    print('NO..')