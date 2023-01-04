#File I/O
#01 - Samples and coordinates
print("PART 01- Samples and coordinates")
file1=[]
filedic={}
with open("/to_use_01.txt", "r") as gff: #analyze the file to_use_01.txt
    for lines in gff:
        if lines.startswith("Sample"):
            continue  
        data1=lines.split() 
        print(data1)
        key,value=data1[0],str(data1[1])+" "+str(data1[1])
        filedic[key]=value
    filedic["Var"]="43.13 6.25"
    filedic["Tun"]="36.95 8.85"
    print(filedic)
with open("/to_use_01_new.txt", "w") as gff: #analyze the file to_use_01.txt
    for key in filedic: 
        gff.write("\n")  
        gff.write(key)
        gff.write("\n") 
        gff.write(filedic[key])
#2
print("02 - Basic data filtering")
filedic2={}
with open("/to_use_02.txt", "r") as gff:#analyze the file to_use_02.txt
    for lines in gff:
        if lines.startswith("Sample"):
            continue
        degrees=(72-32)/1.8
        data2=lines.split()
        key,value=data2[0],str(data2[1:14])
        filedic2[key]=value
    print(filedic2)
with open("/to_use_02_new.txt", "w") as gff:#analyze the file to_use_02.txt
    for key in filedic2:
        gff.write(key)
        gff.write("\n")
        gff.write(filedic2[key])
        if key=="Bio3":
            print(key)
        gff.write("\n") 
