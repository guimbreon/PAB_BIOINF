print("Exercicses 08")
print("01 - DNA Sequences")
def reverse(sequence):
    if "U" in sequence:
        print("U inputed a RNA")
    else:
        sequence=sequence[::-1]
        sequence=sequence.replace("A","t").replace("T","a").replace("C","g").replace("G","c")
        print(sequence.upper())
def codon(sequence_codon):
    new=""
    for letter in sequence_codon:
        new+=letter
        if len(new)==5:
            print(new)
            if "ATG" in new:
                print("SIM")
reverse(sequence=input("Which sequence do you want to analyze:\n>>"))
codon(sequence_codon=input("Which sequence do you want to analyze:\n>>"))
with open(input("Which file do you want to analyze:\n>>")), "r") as gff:
    def fasta(gff):
        keys,values=[],[]
        for lines in gff:
            if lines.startswith(">"):
                lines=lines.replace(">","")
                key=lines
        print(*keys) 
fasta(gff)
