import re,sys,os
import logging
from Bio.SeqIO import parse
from Bio.Seq import Seq,translate
from Bio.SeqIO import parse

seqs = {}
#fid = open('gene.fa','w')

for ret in parse('/home/db/genomes/human/GCF_000001405.39_GRCh38.p13_genomic.fna','fasta'):
    seqs[ret.id] = str(ret.seq)

seq_s = set()  
gene_id = {} 

for rem in open('table2.gff').readlines():
    if rem[0] != '#':
        allinf = re.split('\t',rem)

        if allinf[4] == 'CDS':
            if len(re.findall('gene=(.+?);',allinf[10])) != 0:
                geneid = re.findall('gene=(.+?);',allinf[10])[0]
		
                if geneid not in gene_id.keys():
                    gene_id[geneid] = 1
                    st1 = int(allinf[5]) - 1
                    st2 = int(allinf[6])
                    if allinf[8] == "-":
                        print(allinf[0] + '\t' + allinf[1] + '\t' + allinf[2] + '\t' + allinf[3] + '\t' 
                            + allinf[4] + '\t'+ allinf[5] +  '\t'+ allinf[6] + '\t'+ allinf[7] + '\t' +
                                allinf[8] + '\t' +  allinf[9] + '\t' +  allinf[10].rstrip('\n') + '\t' +
                                str(Seq(seqs[allinf[2]][st1:st2]).reverse_complement()).upper())
                    else:
                        print(allinf[0] + '\t' + allinf[1] + '\t' + allinf[2] + '\t' + allinf[3] + '\t'
                            + allinf[4] + '\t'+ allinf[5] +  '\t'+ allinf[6] + '\t'+ allinf[7] + '\t' +
                             allinf[8] + '\t' +  allinf[9] + '\t' +  allinf[10].rstrip('\n') + '\t'
                             + seqs[allinf[2]][st1:st2].upper())
                else:
                    gene_id[geneid] += 1
                    st1 = int(allinf[5]) - 1
                    st2 = int(allinf[6])
                    if allinf[8] == "-":
                        print(allinf[0] + '\t' + allinf[1] + '\t' + allinf[2] + '\t' + allinf[3] + '\t'+
                        allinf[4] + '\t'+ allinf[5] +  '\t'+ allinf[6] + '\t'+ allinf[7] + '\t' +
                        allinf[8] + '\t' +  allinf[9] + '\t' +  allinf[10].rstrip('\n') + '\t' +
                        str(Seq(seqs[allinf[2]][st1:st2]).reverse_complement()).upper())
                    else:
                        print(allinf[0] + '\t' + allinf[1] + '\t' + allinf[2] + '\t' + allinf[3] + '\t'
                        + allinf[4] + '\t'+ allinf[5] +  '\t'+ allinf[6] + '\t'+ allinf[7] + '\t' +
                        allinf[8] + '\t' +  allinf[9] + '\t' +  allinf[10].rstrip('\n') + '\t' +
                        seqs[allinf[2]][st1:st2].upper())

#fid.close()

                    
