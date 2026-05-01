S=input('Enter any string ==> ')
S=S.replace(' ','')
S=S.lower()
count={}
for ch in S:
    count[ch]=count.get(ch,0)+1
for i in count:
    print(i,'-->',count[i])