# Exercises 02
# Variables and type casting
# 1-My first strings
plant_species=["Pteridophytes", "Bryophytes", "Angiosperms"]
animal_species=["Amorphea", "Obazoa", "Filozoa"]
print(plant_species[0], plant_species[1], plant_species[2], sep=" | ")
print(animal_species[0], animal_species[1], animal_species[2], sep="|")
print("\nTESTING STRINGS:(extra)\n")
#Join the "|" to the string itself on the list
print("|".join(animal_species[0:3]))
print("|".join(plant_species[0:3]))

# 2-Count

print("\n\n")
TXID1=1415635
TXID2=1524889
TXID3=8818
print(type(TXID1), type(TXID2), type(TXID3),sep="   ")
TXID1=str(TXID1)
TXID2=str(TXID2)
TXID3=str(TXID3)
print("The species is: Anas chathamica. It's txid is "+TXID1,
"\nThe species is: Caloenas maculata. It's txid is "+TXID2,
"\nThe species is: Dinornis novaezealandiae. It's txid is "+TXID3)
print(type(TXID1))

# 3-Lists and tuples

print("\n\n")
life1=["Moho bishopi", "Ficus dugandii", "Streptococcus pneumoniae"] #Change the stuff on the list to species names
life2={
    "Moho bishopi":572099,
    "Ficus dugandii":323847,
    "Streptococcus pneumoniae":1313

}
life3=["Pteridophytes", "Obazoa", "Angiosperms"]
life4={
    "Anas chathamica":1415635,
    "Caloenas maculata":1524889,
    "Dinornis novaezealandiae":8818
}
print(life1)
print(life2)
print(life3)
print(life4)
print(life2["Ficus dugandii"])

teste=[life1,life3]
print(teste)


# 4-Dictionaries

print("\n\n")
animals = {
    "Animalia":["Treponema_pallidum", "Raphus_cucullatus", "Gallinula_aleata"],
    "Fungi":["Amanita_muscaria", "Sarcoscypha", "Coccinea"],
    "Protista":["Amoeba", "Paramecium", "Euglena"]
}
print(animals)
print(animals["Animalia"])
print(animals["Fungi"])
print(animals["Protista"])

# 5-Sets

print("\n\n")
list=[13,13,420,13,13]
print(list)
list=set(list)
print(list)
