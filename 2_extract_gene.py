import xlrd

data = xlrd.open_workbook('tcga.xlsx')
table = data.sheets()[3]
row = table.nrows
#print(row)

dict1 = {}
for i in range(1, row):
#    print(table.cell_value(i, 0) + '\t' + table.cell_value(i, 1))
    dict1.update({table.cell_value(i, 0):table.cell_value(i, 1)})
#print(len(dict1))
#print(dict1)
with open('cds.gff') as f:
    for line in f:
        line_list = line.rstrip('\n').split('\t')
        #print(line_list)
        if line_list[1] not in dict1:
            continue
        print(line.rstrip('\n')) 

