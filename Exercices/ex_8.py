#Exercices 08
#01 - DNA Sequences
import sys
file,with_start,file_reverse,with_start_reverse={},{},{},{}
exists=[0,]
def reverse(sequence,key):
    if "U" in sequence:
        print("U inputed a RNA")
    else:
        sequence=sequence[::-1]
        sequence=sequence.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()
        file_reverse[(key.replace("\n",""))]=(sequence).replace("\n","")
def codon(sequence_codon):
    new=""
    for letter in sequence_codon:
        new+=letter
        if len(new)==5:
            if "ATG" in new:
                exists[0]=1
            else:
                exists[0]=0
def fasta(fasta):
    with open(fasta, "r") as gff:
        key,total="",""
        for lines in gff:
            if lines.startswith(">"):
                file[key.replace("\n","")]=total.replace("\n","")
                key=lines.replace(">","")
                total=""
            else:
                total+=lines
def main(which):
    fasta(which)
    for key in file:
        codon(file[key])
        if exists[0]==1:
            with_start[key]=file[key]
    for key in file:
        reverse(file[key],key)
    for key,values in file_reverse.items():
        codon(values)
        if exists[0]==1:
            with_start_reverse[key.replace('\n','')+"-RC"]=(file[key]).replace("\n","")
            print("a")
    for key in with_start:
        print(key,with_start[key])
    for key in with_start_reverse:
        print(key,with_start_reverse[key])
main(sys.argv[1])