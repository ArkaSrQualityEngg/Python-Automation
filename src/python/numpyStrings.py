import numpy as np

ch_name = "India AI Production"
str1 = " Learning Python Numpy"

print(np.char.add(ch_name,str1))
print(np.char.lower(ch_name))
print(np.char.upper(ch_name))
print(np.char.center(str1,60,fillchar="*"))
print(np.char.split(str1))
print(np.char.splitlines("Hello\nIndia"))
str4 = "ddmmyyyy"
str5 ="ddmmyyyy"
print(np.char.join(["-","/"],[str4,str5]))
print(np.char.replace(ch_name,"AI","Artificial Intelligence"))
print(np.char.equal(str4,str5))
print(np.char.count(ch_name,'o'))
print(np.char.find(ch_name,"AI"))




