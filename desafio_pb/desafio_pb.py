file1=open("/here is the file with the name sequence_ncbi.fasta", "r")
i=0
for lines in file1:
    if lines.startswith(">"):
        i+=1
x=["k",]*i
i=0
file1=open("here is the file with the name equence_ncbi.fasta", "r")
for lines in file1:
    if lines.startswith(">"):
        x[i]=lines
        i+=1
file1.close()
file2=open("here is the file with the name sequence_ena.fasta", "r")
i=0
for lines in file2:
    if lines.startswith(">"):
        i+=1
y=["k",]*i
i=0
file2=open("here is the file with the name sequence_ena.fasta", "r")
for lines in file2:
    if lines.startswith(">"):
        y[i]=lines
        i+=1
file2.close()
print(len(x))
print(len(y))
i=0
x=sorted(x)
y=sorted(y)
for x in y:
    print("", end="")
else:
   print(x)