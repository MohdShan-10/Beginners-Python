sentence = input('Enter any sentence ==>  ')
sentence = sentence.lower()
count = {}
words = sentence.split()
for i in words:
    count[i] = count.get(i,0) + 1
for i in count:
    print(f' {i} : {count[i]}')