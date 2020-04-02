set1 = set()
gene_SNP = []
with open('re_table2_genename.txt') as f:
    for line in f:
        line_list = line.rstrip('\n').split('\t')
        gene_SNP.append(line_list[0] + '|' + line_list[1])
#print(len(gene_SNP))
        set1.add(line_list[0] + '|' + line_list[1])
#print(len(set1))

gene_inf = []
with open('re_table2.inf') as f:
    for line in f:
        gene_inf.append(line.rstrip('\n'))

dict1 = {}
set2 = set()
for inf in gene_inf:
    #print(inf)
    for snp in gene_SNP:
        if inf.split('\t')[0].split('|')[1] == snp.split('|')[0]:
            if len(inf.split('\t')[4]) > int(snp.split('|')[1][1:-1])-1:
                if (inf.split('\t')[4][int(snp.split('|')[1][1:-1]) - 1]) == snp.split('|')[1][0]:   
                    dict1.update({snp:inf})  
                    set2.add(snp)
#                    print(snp + '\t' + inf)
print(set1 - set2)
#for i in set1 - set2:
#    print(i.split('|')[0] + '\t' + i.split('|')[1])
#print(len(dict1))
#for key in dict1:
#    print(key + '\t' + dict1[key])





#        print(line_list)
        #print(line_list)
#        for ge_snp in gene_SNP:
#            if (line_list[0].split('|')[1] == ge_snp.split('|')[0]):
            #print(line_list[4][int(ge_snp.split('|')[1][1:-1]) + 1] == ge_snp.split('|')[1][1])
            #print(line_list[4][int(ge_snp.split('|')[1][1:-1])])    
#                if (line_list[4][int(ge_snp.split('|')[1][1:-1])+1] == ge_snp.split('|')[1][0]):
#                    print(line_list)
            #    print(ge_snp)
#print(gene_inf)
#dict1 = {}
#list1 = []
#set1 = set()
#for ge in gene_SNP:
#    ge_list = ge.split('|')
#    for inf in gene_inf:
#        if ge_list[0] == inf.split('\t')[0].split('|')[1]:
#            print(inf)
#            if len(inf.split('\t')[4]) > (int(ge_list[1][1:-1]) + 1):
#                if (inf.split('\t')[4][int(ge_list[1][1:-1]) + 1]) == ge_list[1][0]:
                    #print(ge_list[0] + '\t' + ge_list[1] + '\t' + inf)
#                    dict1.update({ge_list[0] + '|' + ge_list[1]:inf})
#                    break
#                    list1.append(ge_list[0] + '|' + ge_list[1])
#                else:
#                    set1.add(ge_list[0] + '|' + ge_list[1])

#print(set1)
#print(len(set1))
#print(dict1)
#print(len(dict1))
#print(list1)
#print(len(list1))
