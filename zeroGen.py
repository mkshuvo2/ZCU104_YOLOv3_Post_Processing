
fileID = open('Filler.txt','w')
for i in range(4):
   print(i)
   for j in range(75):
      txt = "0 "
      fileID.write(txt)
   txt = '\n'
   fileID.write(txt)
fileID.close()
print("Data written to File")