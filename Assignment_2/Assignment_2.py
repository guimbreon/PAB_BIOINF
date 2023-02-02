import sys
import argparse
parser= argparse.ArgumentParser(description="Program made to convert files!")
parser.add_argument("-i","--input_file",help="The input file!\nHas to be Nexus, Fasta or Phylip")
parser.add_argument("-o","--output_file",help="The input file!\nHas to be Nexus, Fasta or Phylip")
args = parser.parse_args()
file1,file2=sys.argv[2],sys.argv[4]
class data():
    def __init__(self,names,seq):
        self.name=names
        self.sequence=seq
    def lenght(self):
        self.sizes=len(self.sequence)
        return self.sizes
def know_type_input(files):
    file_type_1,number="",0
    with open(files,"r") as input_file:
        for lines in input_file:
            if file_type_1=="":
                if lines.startswith(">"):
                    file_type_1=".fasta"
                elif lines.startswith("#NEXUS"):
                    file_type_1=".nexus"
                elif file_type_1=="":
                    try:
                        int(lines.replace("\n","").replace(" ",""))
                    except ValueError:
                        print("The input file you have entered is not valid\nIs not Fasta or Nexus or Phylips.")
                        quit()
                    else:
                        file_type_1=".phy"
    return file_type_1
def know_type_output(files): #to know the output type
    file_type_2=""
    if files.endswith(".fasta"):
        file_type_2=".fasta"
    if files.endswith(".phy"):
        file_type_2=".phy"
    if files.endswith(".nexus"):
        file_type_2=".nexus"
    elif file_type_2=="":
        print("The output file you have entered is not valid\nIs not Fasta or Nexus or Phylips.")
        quit()
    return file_type_2

def reading(file_type,files):
    total,name,sequence="",[],[]
    if file_type==".fasta":
        with open(files,"r") as file:
            for lines in file:
                if lines.startswith(">"): 
                    name.append(lines.replace(">","").replace("\n",""))
                    if total=="":
                        continue
                    sequence.append(total.replace("\n",""))
                    total=""
                else:
                    total+=lines
    if file_type==".nexus":
        data=1
        with open(files,"r") as file:
            for lines in file:
                    dados=[]
                    if data>=8 and lines!=";\n" and lines!="\n" and lines!="END;":
                        dados=lines.split("     ")
                        print(dados)
                        name.append(dados[0])
                        if total!="":
                            sequence.append(total.replace("\n",""))
                            total=""
                        else:
                            total+=dados[1]
                    data+=1
    if file_type==".phy":
        i=0
        with open(files,"r") as file:
            for lines in file:
                try:
                    1/int(lines.split()[0])
                    continue
                except ValueError:
                    dados=lines.split("   ")
                    name.append(dados[0])
                    sequence.append(dados[1].replace("\n",""))
    return name,sequence
def writing(file_type_1,file_type_2,files):
    i,k=0,0
    if file_type_1==file_type_2:
        print("\nThe input and output file are the same format!\n")
        quit()
    if file_type_2==".nexus":
        with open(files, "w") as file:
            for seq in thing.sequence:
                if i==0:
                    file.write(f"#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX={thing.lenght()} NCHAR={len(seq)};\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n")
                file.write(f"\n{thing.name[i]}     {seq}")
                i+=1
            file.write("\n;\n\nEND;")
    if file_type_2==".fasta":
        with open(files,"w") as file:
            for seq in thing.sequence:
                k=0
                file.write(f">{thing.name[i]}\n")
                for character in seq:
                    if k<=79:
                        file.write(f"{character}")
                        print(k)
                        k+=1
                    if k==79:
                        print("a")
                        file.write(f"\n")
                        k=0
                    
                file.write("\n")
                               
                i+=1

    if file_type_2==".phy":
        with open(files,"w") as file:
            for seq in thing.sequence:
                if i==0:
                    file.write(f"{thing.lenght()} {len(seq)}")
                file.write(f"\n{thing.name[i]}   {seq}")
                i+=1
file_type_1,file_type_2=know_type_input(file1),know_type_output(file2)
reading(file_type_1,file1)
name,sequence=reading(file_type_1,file1)
thing=data(name,sequence)
print(thing.sequence)
writing(file_type_1,file_type_2,file2)
print(f"\nThe program converted a {file_type_1} file to a {file_type_2} file SUCESSFULLY!")