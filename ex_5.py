#01- Species names

sp_list01 = ["Antaresia childreni", "Antaresia maculosa", "Antaresia perthensis", "Antaresia stimsoni", "Apodora papuana", "Aspidites melanocephalus", "Aspidites ramsayi", "Bothrochilus boa", "Leiopython albertisii", "Morelia viridis", "Morelia imbricata", "Python brongersmai"]
sp_list02 = ["Liasis fuscus", "Liasis mackloti", "Liasis olivaceus", "Malayopython reticulatus", "Malayopython timoriensis", "Morelia azurea", "Morelia bredli", "Morelia carinata", "Morelia spilota", "Morelia viridis", "Python anchietae", "Python bivittatus", "Python curtus"]

if "Malayopython timoriensis" in sp_list01:
    print("Timor Python exists in list 1.\n")
else:
    print("Timor Python doesn't exist in list 1\n")
if "Malayopython timoriensis" in sp_list02:
    print("Timor Python exists in list 2.\n")
else:
    print("Timor Python doesn't exist in list 2\n")
if "Liasis olivaceus" in sp_list01:
    print("The Olive Python exists in the first list but not on the second\n")
elif "Liasis olivaceus" in sp_list02:
    print("The Olive Python exists in the second list but not on the first\n")
else:
    print("The Olive Python is absent from either lists\n")
a=set(sp_list01)
b=set(sp_list02)
common=0
print("\n$Testing the common values from the lists$\n")
for value in sp_list01:
    if value in sp_list02:
        print(value)
        common+=1
        which=value #equals which value is in both lists
print(f"There are {common} species in common\n")

if which in (sp_list01 and sp_list02):
    print(f"The {which} species exists in the first list and on the second\n")


#02- DNA translation
orf=0
my_sequences = ("ATGATGCATGCTAGTCTGATGCGCTGTTGA")
if len(my_sequences)%3==0:# if the rest of the division by 3 is 0, it means that the len is divisible by 3
    print("It's divisible by 3.")
    orf+=1  
else:
    print("It's value isn't divisible by 3")
if my_sequences.startswith("ATG"):
    print("It starts with the start codon 'ATG'\n")
    orf+=1 
else:
    print("It doesn't start with the start codon 'ATG'\n")
if my_sequences.endswith(("UAG","UAA","UGA")):
    print("The sequence ends with one of the stop codons.\n")
    orf+=1 
else:
    print("It doesn't start with the start codon 'ATG'\n")
if orf==3:
    print("The sequence is not ORF")
else:
    print("The sequence is not an ORF sequence")

#challenge
sequence_with_f1_orf = "TTTATGAGTCGATCGAGCTAGCATCGATAGCTCGATCGATCATGATTT"  # Start codon on [3]
sequence_with_fminus2_orf = "GTTGTATCGATCGATCTACGGTCAGTATTAG"  # Start codon on [-5]
my_seq=sequence_with_f1_orf.find("ATG")
