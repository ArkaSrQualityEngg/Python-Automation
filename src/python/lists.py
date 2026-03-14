from fontTools.merge.util import avg_int

myList = ['Nancy','Bhola','Janu','Jeffrey','Nangu',0,57]

print(len(myList))

print(myList.pop())
myList.append('Raandwa')
print(myList)
myList.insert(1,'Phallus')
print(myList)
myList.remove('Jeffrey')
print(myList)
myList.reverse()
print(myList)
print(myList[3:])
print(myList[:])

yourList = [2,4,4,6,7,9,0]
print(min(yourList))
print(max(yourList))
print(avg_int(yourList))