# Exercises 02
# Variables and type casting
# 1- String operations
dna_seq = "GTAGCTGATGCTAGCTGTGATTATTCGTACGATTTGTCGTAGTGTCGTATGCGTAGCTGATGCGTAT"
print(dna_seq)

dna_seq_length = len(dna_seq)
print(dna_seq_length)

adenines_in_seq = dna_seq.count("A")

base_counts = {"A": adenines_in_seq,
               "C": dna_seq.count("C"),
               "G": dna_seq.count("G"),
               "T": dna_seq.count("T")}

print(base_counts)

percent_gc = (base_counts["G"] + base_counts["C"]) / dna_seq_length

print(f"The DNA sequence GC content is ~ {round(percent_gc * 100, 1)}%.")

rna_seq = dna_seq.replace("T", "U")
print(rna_seq)


#02-List operations
dna_fragments = dna_seq.split("GAT")
print(f"Digesting the DNA sequence with the mentioned restriction enzyme would result in the following: {dna_fragments}")
print(f"The DNA sequence was cut in {len(dna_fragments)} fragments. The last fragment is {len(dna_fragments[-1])} base pairs long.")

dna_fragments.append("TACGGCATT")

middle_dna_fragments = dna_fragments[1:5]

rebuilt_dna_plus = "GAT".join(dna_fragments)  # The 'GAT' motif had been digested and needs to be added back!
print(rebuilt_dna_plus)


# Tuple operation
primers = ("AGCTGATG", "TTATTCGT", "TAGTGTCG", "ATGCGTAT")  # My order may not be the same as yours but it should no take any difference to solve the exercise
print(primers)
print(primers[::-1])

#Challenge 
indeces = []
indeces.append(dna_seq.find(primers[0]))
indeces.append(dna_seq.find(primers[1]))
indeces.append(dna_seq.find(primers[2]))
indeces.append(dna_seq.find(primers[3]))