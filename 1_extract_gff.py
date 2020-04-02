import re

with open("/home/db/genomes/human/GCF_000001405.39_GRCh38.p13_genomic.gff") as f:
    for line in f:
        if line.startswith('#'):
            continue
        line_list = line.rstrip('\n').split('\t')
        #print(line_list)
        if line_list[2] == "CDS":
            tran = re.findall(";protein_id=(.*?)$",line_list[8])   
            genename = re.findall("gene=(.*?);",line_list[8])
        #    print(genename)
            if len(tran) == 1 and len(genename) == 1:
                print(tran[0].split(';')[0] + '\t' + genename[0] + '\t' + line.rstrip('\n'))
