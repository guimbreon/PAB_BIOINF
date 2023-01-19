#Exercises 7
#File I/O

#01 - Samples and coordinates
print("PART 01- Samples and coordinates")
file1=[]
filedic={}
#with open(input("Which file do you want to analize?/n>>"), "r") as gff:
with open("~/to_use_01.txt", "r") as gff:
    for lines in gff:
        if lines.startswith("Sample"):
            first1=lines
            continue  
        data1=lines.split() 
        print(data1)
        key,value=data1[0],str(data1[1])+" "+str(data1[1])
        filedic[key]=value
filedic["Var"]="43.13 6.25"
filedic["Tun"]="36.95 8.85"
for key in filedic:
    filedic[key]=str(filedic[key]).replace(" ","\t")
filedic=sorted(filedic.items(), key=lambda x:x[0])
filedic=dict(filedic)
#with open(input("Which file do you want to save the program?/nCan't use the same file has the last used!/n>>"), "r") as gff:
with open("~/to_use_01_new.txt", "w") as gff:
    gff.write(f"{first1}\n")
    for key in filedic:
        gff.write(f"{key}\t{filedic[key]}\n")
#02- Basic daata filtering
print("#02- Basic daata filtering")
filedic2,filedic2_new={},[]
#with open(input("Which file do you want to analize?/n>>"), "r") as gff:
with open("~/to_use_02.txt", "r") as gff:#analyze the file to_use_02.txt
    for lines in gff:
        value=[]
        if lines.startswith("Sample"):
            first2=lines
            continue
        data2=lines.split() #divides the line
        for item in data2[1:3]:
            value.append(item)
        for item in data2[3:4]:
            degrees=(int(item)-32)/1.8
            value.append(int(round(degrees)))
        for item in data2[4:15]:
            value.append(item)
        key=data2[0] #the data[0] is the key and the rest are values
        filedic2[key]=value
filedic2=sorted(filedic2.items(), key=lambda x:x[0])
filedic2=dict(filedic2)

#with open(input("Which file do you want to save the program?/nCan't use the same file has the last used!/n>>"), "r") as gff:
with open("~/to_use_02_new.txt", "w") as gff:#analyze the file to_use_02.txt
    gff.write(f"{first2}\n")
    for key in filedic2:
        gff.write(f"{key}")
        for item in filedic2[key]:
            gff.write(f"\t{item}")
        gff.write("\n")
print(filedic["Tun"])
with open("~/to_use_02_new2.txt", "w") as gff:#analyze the file to_use_02.txt
    gff.write(f"{first2}\tLat\tLong".replace("\n",""))
    for key in filedic2:
        gff.write(f"\n{key}")
        for item in filedic2[key]:
            gff.write(f"\t{item}")
        gff.write(f"\t{filedic[key]}")
        print(filedic[key])

#03 - VCF parsing
missing,total=0,0
with open("~/ex07_genotypes.vcf", "r") as gff:
    for lines in gff:
        if lines.startswith("locus"):
            missing=lines.count(".")
            total=len(lines)
            lines=lines.split()
            if missing!=0:
                perc=(missing/total)*100
                print(f"{lines[0]}\t{round(perc,2)}")     
            else:
                print(f"{lines[0]}\t0")

seperate=["teste"]
i=0
print("\n\n\n\n\n")
with open("~/ex07_genotypes.vcf", "r") as gff:
    for lines in gff:
        i=0
        if lines.startswith("#CHROM"):
            size=len(lines.split())
        if lines.startswith("locus"):
            lines=lines.split()
            if seperate[0]=="teste":
                seperate=[0,]*(len(lines)-10)
            for thing in lines[9:size-1]:
                seperate[i]=seperate[i]+thing.count(".")
                i+=1    
print(seperate)