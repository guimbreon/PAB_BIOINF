bases,total,all,names,count=["A","T","G","C"],"",[],[],0
with open((input("Which file are you going to analyze?/n>>")).replace("'",""), "r") as gff: #with the replace method it can now read any file u drag to the terminal
    search=input("Which sequence do u want to search for?/n>>").upper()
    if set(search).difference(bases) == set() and len(search)>=5: #Store the names and all the sequences
        for lines in gff:
            if lines.startswith(">"):
                names.append(lines.replace(">","").replace("\n",""))
                all.append(total.replace("\n",""))
                total=""
            else:
                total+=lines
    else:
        print("\n\nDon't forget:\n-The motif you want to search for has to be DNA {A,T,G,C}\n-Have atleast 5bp")
    for seq2 in all: #Analizes the reverse-complement
        seq2=(seq2[::-1].replace("A","t").replace("T","a").replace("C","g").replace("G","c")).upper() #Transforms it into a reverse complement
        for i, _ in enumerate(seq2):
            if seq2[i:i+len(search)] == search:
                if (i+3)%3==0:
                    print(f"{names[count]}\t{len(seq2)}\t{i}\t-1")
                if (i+4)%3==0:
                    print(f"{names[count]}\t{len(seq2)}\t{i}\t-3")
                if (i+5)%3==0:
                    print(f"{names[count]}\t{len(seq2)}\t{i}\t-2")
        count+=1
    count=0
    for seq in all:#Analizes the sequence
        for i, _ in enumerate(seq):
            if seq[i:i+len(search)] == search: #I THINK I MANAGED TO FIND THE FRAME FINDER!!!!!!!!
                if (i+3)%3==0:
                    print(f"{names[count]}\t{len(seq)}\t{i}\t1")
                if (i+4)%3==0:
                    print(f"{names[count]}\t{len(seq)}\t{i}\t3")
                if (i+5)%3==0:
                    print(f"{names[count]}\t{len(seq)}\t{i}\t2")
        count+=1