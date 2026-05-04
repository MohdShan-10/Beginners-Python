dic = {'Aman': 76,'Mukesh':65,'Deepak':97,'Rohit':93}
mod_dic = {}

# Interchange The Keys and Values pair for ease if code...

for i in dic:
    mod_dic[dic[i]] = i

marks = max(mod_dic.keys())
print(f'Topper is  {mod_dic[marks]}')