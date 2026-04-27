s=input('Enter a string ==> ')
print('The string is: ' + s)
print('After Manipulation : ',end='')
for i in s[::-1]:
    if i not in 'aeiouAEIOU':
        print(i, end='')