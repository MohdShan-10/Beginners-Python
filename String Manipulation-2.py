sen=input('Enter a sentence ==> ')
words=sen.split()
longest=''
for i in words:
    if len(i) > len(longest):
        longest = i
print('The longest word is:', longest)