import reader

reader.ReaderTips()

list=[]
sum = reader.Loader('monday.csv', list)

list1=[]
s = reader.JudegeAttack(list, list1)
#reader.show_all(list1)
print("the number of records:",s)
f=open('./list.txt','w')
for i in list1:
    i=str(i).strip('[').strip(']').replace("'","").replace(' ','')
    print(i)
    f.write(i+'\n')
f.close()
#s = reader.merge_length_2(list, list1)
#reader.show_all(list1)
#print("the number of records:", s)
#av = reader.get_average(list1)
#print("average:", av)
