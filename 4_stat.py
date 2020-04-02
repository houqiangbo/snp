from Bio.Seq import Seq

'''
set1= set()
with open("gene.fa") as f:
    for line in f:
        line_list = line.rstrip('\n').split('\t')
        print(line_list)
#        set1.add(line_list[1])
#print(len(set1))

'''
li = open("table2.seq").readlines()
length = len(li) 
#print(li)
index = []
for i,seq in enumerate(li):
    if i + 1 < length:
        if li[i].split('\t')[0] != li[i + 1].split('\t')[0]:
            index.append(i+1)
index.insert(0,0)
index.append(length)

#print(index)
le = len(index)
total = []
for i in range(le):
    if i + 1 < le:
        tran = li[index[i]:(index[i + 1])]
        str1 = ""
        str2 = ""
        str3 = ""
        list1 = []
        list2 = []
        list3 = []
        for item in tran:
#            print(item)
            item_list = item.split('\t')
            str1 += item_list[-1].rstrip('\n')
            str2 += str(len(item_list[-1].rstrip('\n'))) + '|'
            str3 += str(item_list[5]) + '_' + str(item_list[6]) + '|'
            list1.append(item_list[0] + '|' + item_list[1])
            list2.append(item_list[2])
            list3.append(item_list[8])
#        print(str1)
        total.append(list1[0] + '\t' + list2[0] + '\t' + list3[0] + '\t' + str1 + '\t' + str(Seq(str1).translate()))
        print(list1[0] + '\t' + list2[0] + '\t' + list3[0] + '\t' + str1 + '\t' + str(Seq(str1).translate()) + '\t' + str2 + '\t' + str3)
#print(total[0:10])
'''
import xlrd
data = xlrd.open_workbook('tcga.xlsx')
table = data.sheets()[0]
row = table.nrows
print(total)
'''









