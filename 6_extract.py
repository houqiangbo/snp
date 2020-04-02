from Bio.Seq import Seq


with open("table2_final.txt") as f:
    for line in f:
        line_list = line.rstrip('\n').split('\t')
        #print(line_list)
        index = int(line_list[0].split("|")[1][1:-1])
        
        if ((index - 1) * 3 - 36 >= 0) and \
            (len(line_list[4]) - (index - 1) * 3 - 36) >= 0:
            seq1 = line_list[4][((index - 1) * 3 - 36) : (index - 1) * 3].lower()
            seq2 = line_list[4][(index - 1) * 3 : ((index - 1) * 3 + 3)].upper()
            seq3 = line_list[4][((index - 1) * 3 + 3) : ((index - 1) * 3 + 3 + 36)].lower()
            seq = seq1 + seq2 + seq3
            print(line_list[0].split('|')[0] + '\t' + line_list[0].split('|')[1] + '\t' + 
                line_list[1].split('|')[0] + '\t' + line_list[2] + '\t' + line_list[3] + '\t' +
                seq + '\t' + str(Seq(seq1).translate()).lower() + str(Seq(seq2).translate()).upper() + 
                str(Seq(seq3).translate()).lower())
        
        if ((index - 1) * 3 - 36 < 0) and (len(line_list[4]) - (index - 1) * 3 - 36) >=0:
            seq1 = line_list[4][0 : (index - 1) * 3].lower()
            seq2 = line_list[4][(index - 1) * 3 : ((index - 1) * 3 + 3)].upper()
            seq3 = line_list[4][((index - 1) * 3 + 3) : 75].lower()
            seq = seq1 + seq2 + seq3
            print(line_list[0].split('|')[0] + '\t' + line_list[0].split('|')[1] + '\t' +
                line_list[1].split('|')[0] + '\t' + line_list[2] + '\t' + line_list[3] + '\t' +
                seq + '\t' + str(Seq(seq1).translate()).lower() + str(Seq(seq2).translate()).upper() +
                str(Seq(seq3).translate()).lower())
        
        if ((index - 1) * 3 - 36 >= 0) and \
            (len(line_list[4]) - (index - 1) * 3 - 36) < 0:
            seq1 = line_list[4][-75:(index - 1) * 3].lower() 
            seq2 = line_list[4][(index - 1) * 3 : ((index - 1) * 3 + 3)].upper()
            seq3 = line_list[4][((index - 1) * 3 + 3):].lower()
            seq = seq1 + seq2 + seq3
            print(line_list[0].split('|')[0] + '\t' + line_list[0].split('|')[1] + '\t' +
                  line_list[1].split('|')[0] + '\t' + line_list[2] + '\t' + line_list[3] + '\t' +
                  seq + '\t' + str(Seq(seq1).translate()).lower() + str(Seq(seq2).translate()).upper() +
                  str(Seq(seq3).translate()).lower())
