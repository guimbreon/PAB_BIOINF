import sys
#01- Species names again
sp_list01 = ["Antaresia childreni", "Antaresia maculosa", "Antaresia perthensis", "Antaresia stimsoni", "Apodora papuana", "Aspidites melanocephalus", "Aspidites ramsayi", "Bothrochilus boa", "Leiopython albertisii", "Morelia viridis", "Morelia imbricata", "Python brongersmai"]
sp_list02 = ["Liasis fuscus", "Liasis mackloti", "Liasis olivaceus", "Malayopython reticulatus", "Malayopython timoriensis", "Morelia azurea", "Morelia bredli", "Morelia carinata", "Morelia spilota", "Morelia viridis", "Python anchietae", "Python bivittatus", "Python curtus"]
print("\n".join(sp_list01))#1
print("\n\n")#2
sp_list01.sort()
print(sp_list01)
print("\n\n")#3
total=set(sp_list01) & set(sp_list02) 
for snake in sp_list01 + sp_list02:
    if snake not in total:
        print(f"{snake}")
    else:
        print(f"Multiple «{snake}» found. That's a lot of snakes.\n")
print("\n\n") #4
changed=[]
for snake in sp_list01 + sp_list02:
    space = snake.index(" ")
    snake= f"{snake[0]}. {snake[space +1:]}"
    changed.append(snake) #use this to add things to a list
print(changed)
print("\n\n")
print("\n\n")
#02- Basic data filtering
blast_out = """SNPName  ScaffoldName    SequeceLength   eValue  IdentityMatch   Length  ScaffoldStart   ScaffoldEnd
vcf_locus981    scaffold3209    51  8.20e-13    49  53  56022   56074
vcf_locus15697  scaffold1024    65  2.08e-20    60  63  161458  161396
vcf_locus15857  scaffold8324    52  1.09e-16    49  51  23136   23086
vcf_locus18446  scaffold10473   68  2.22e-25    66  68  6142    6075
vcf_locus21054  scaffold12844   111 2.00e-38    103 112 8489    8600
vcf_locus21240  scaffold7935    75  4.24e-23    70  76  25769   25694
vcf_locus39196  scaffold2600    110 3.40e-16    50  52  73764   73815
vcf_locus40555  scaffold8149    90  1.52e-33    83  87  190104  190190
vcf_locus41736  C399953 74  1.15e-28    72  74  154549  154622
vcf_locus47292  scaffold1118    103 5.00e-44    100 103 250562  250664"""

for lines in blast_out.split("\n"): #separation in \n(enter)
    if lines.startswith("SNP"): #prints the first line
        print(lines)
    elif float(lines.split()[3]) < 1e-25: # 3 in 3
        print(lines)
print("\n\n")
for lines in blast_out.split("\n"):
    if lines.startswith("SNP"):
        print(lines)
    elif int(lines.split()[2]) > 100:
        print(lines)
        break
else:
    print("There is no sequence with SequenceLenght larger than 100bp",file=sys.stderr)
#03- DNA sequences
sequences = {'Ib8': 'GGATTGTGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAATACGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCATATCGGACGGGGCCTATACTATGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTTCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTCTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATTTTAGGGACATCACTAATACACCTAATATTTTTACACGAAACAGGGTCAAACAACCCAACAGGGTTAAACTCAAACTCAGATAAAATCCCGTTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTACTCTTATACCTCTCACTATTTTCCCCATTGCTCCTAGGAGACCCAGAAAACTTCA', 'Ib9': 'GGATTGTGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAATACGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCATATCGGACGGGGCCTATACTATGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTTCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTCTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATTTTAGGGACATCACTAATACACCTAATATTTTTACACGAAACAGGGTCAAACAACCCAACAGGGTTAAACTCAAACTCAGATAAAATCCCGTTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTACTCTTATACCTCTCACTATTTTCCCCATTGCTCCTAGGAGACCCAGAAAACTTCA', 'Ib1': 'GGATTGTGCCTAATTACTCAAATTGTTACCGGATTATTTTTAGCAATACACTATAATGCAGATATTAACTCCGCATTCTCATCAGTCGCACACATTCACCGTGATGTACAACATGGATGACTAATCCGAAATATCCATGCCAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGGGGCCTATACTATGGGTCCTACTTATTTACTGAAACATGAAACATTGGAGTTCTACTCCTCCTCCTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCATTTTGAGGGGCCACTGTCATTACTAATCTCTTATCTGCCATCCCATACATTGGAAACACCCTAGTTGAGTGAGTTTGAGGCGGATTCGCAATTGATAGCGCAACCCTAACTCGATTCTTCACACTACACTTCCTCCTACCTTTTCTGATCCTAGGAACATCACTAATTCACTTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGATTGAATTCAAACTCAGACAAAATTCCATTCCACCCTTACTACTCATATAAAGATGCCCTTGGAGCCCTATTATTTGTAGCCCTGCTCTTATACCTTTCACTATTTTCACCCCTACTCCTAGGGGACCCAGAAAACTTTA', 'Ib2': 'GGATTGTGCCTAATTACTCAAATTGTTACCGGATTATTTTTAGCAATACACTATAATGCAGATATTAACTCCGCATTCTCATCAGTCGCACACATTCACCGTGATGTACAACATGGGTGACTAATCCGAAATATCCATGCCAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGGGGCCTATACTATGGGTCCTACTTATTTACTGAAACATGAAACATTGGAGTTCTACTCCTCCTCCTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCATTTTGAGGGGCCACTGTCATTACTAATCTCTTATCTGCCATCCCATACATTGGAAACACCCTAGTTGAGTGAGTTTGAGGCGGATTCGCAATTGATAGCGCAACCCTAACTCGATTCTTCACACTACACTTCCTCCTACCTTTTCTGATCCTAGGAACATCACTAATTCACTTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGATTGAATTCAAACTCAGACAAAATTCCATTCCACCCTTACTACTCATATAAAGATGCCCTTGGAGCCCTATTATTTGTAGCCCTGCTCTTATACCTTTCACTATTTTCACCCCTACTCCTAGGGGACCCAGAAAACTTTA', 'Ib3': 'GGATTGTGCCTAATTACTCAAATTGTTACCGGATTATTTTTAGCAATACACTATAATGCAGATATTAACTCCGCATTCTCATCAGTCGCACACATTCACCGTGATGTACAACATGGATGACTAATCCGAAATATTCATGCCAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGGGGCCTATACTATGGGTCCTACTTATTTACTGAAACATGAAACATTGGGGTTCTACTCCTCCTCCTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCATTTTGAGGGGCCACTGTCATTACTAATCTCTTATCTGCCATCCCATACATTGGAAACACCCTAGTTGAATGAGTTTGAGGCGGATTCGCAATTGATAGCGCAACCCTAACTCGATTCTTCACACTACACTTCCTCCTACCTTTTCTGATCCTAGGAACATCACTAATTCACTTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGGTTGAATTCAAACTCAGACAAAATTCCATTCCACCCTTACTACTCATATAAAGATGCCCTTGGAGCCCTATTATTTGTAGCCCTGCTCTTATACCTTTCACTATTTTCACCCCTACTCCTAGGGGACCCAGAAAACTTTA', 'Ib4': 'GGATTGTGCCTAATTACTCAAATTGTTACCGGACTATTTTTAGCAATACACTATAATGCAGATATTAACTCCGCATTCTCATCAGTCGCACACATTCACCGTGATGTACAACATGGCTGACTAATCCGAAATATCCATGCTAACGGCGCATCACTATTCTTTATTTGCATCTATATGCACATCGGACGGGGCCTATACTACGGGTCCTACTTATTTACTGAAACATGAAACATTGGAGTTCTCCTCCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTACGTCCTCCCATGAGGACAAATATCATTTTGAGGGGCCACTGTCATCACCAATCTCTTATCTGCCATCCCATACATTGGAAACACCTTAGTTGAATGAATTTGAGGTGGATTCGCAATTGATAACGCAACCCTAACTCGATTCTTCACACTACACTTCCTCCTACCTTTTCTGATCCTAGGAACATCACTAATTCACTTAATATTTTTACACGAAACCGGATCAAACAACCCAACAGGATTAAATTCAAACTCAGACAAAATTCCATTCCACCCTTACTACTCATATAAAGATGCCCTTGGAGCCCTATTATTTATAGCCCTGCTCTTATTCCTTTCACTATTTTCACCCCTACTCCTAGGGGACCCCGAAAACTTTA', 'Ib5': 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNACTATTTTTAGCAATACACTATAATGCAGATATTAACTCCGCATTCTCATCAGTCGCACACATTCACCGTGATGTACAACATGGCTGACTAATCCGAAATATCCATGCTAACGGCGCATCACTATTCTTTATTTGCATCTATATGCACATCGGACGAGGCCTATACTACGGGTCCTACTTATTTACTGAAACATGAAACATTGGAGTTCTCCTCCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTACGTCCTCCCATGAGGACAAATATCATTTTGAGGGGCCACTGTCATCACTAATCTCTTATCTGCCATCCCATACATTGGAAACACCTTAGTTGAATGAATTTGAGGTGGATTCGCAATTGATAACGCAACCCTAACTCGATTCTTCACACTACACTTCCTCCTACCTTTTCTGATCCTAGGAACATCACTAATTCACTTAATATTTTTACACGAAACCGGATCAAACAACCCAACAGGATTAAATTCAAACTCAGACAAAATTCCATTCCACCCTTACTACTCATATAAAGATGCCCTTGGAGCCCTATTATTTATAGCCCTGCTCTTATTCCTTTCACTATTTTCACCCCTACTCCTAGGGGACCCCGAAAACTTTA', 'Ib6': 'GGATTGTGCCTAATTACTCAAATTGTTACCGGACTATTTTTAGCAATACACTATAATGCAGATATTAACTCCGCATTCTCATCAGTCGCGCACATTCACCGTGATGTGCAACATGGCTGACTAATCCGAAACATTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTATACGCACATCGGACGGGGCCTATACTACGGGTCCTACTTATTCACTGAAACATGAAACATTGGAGTTCTTCTCCTCCTCTTAGTAATAGCTACAGCCTTCATAGGTTATGTACTCCCATGGGGACAAATATCATTTTGAGGAGCCACTGTCATTACTAATCTCTTATCTGCCATCCCATACATTGGAAACACTCTAGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACCCTAACTCGATTCTTCACACTACACTTCCTCCTACCTTTTCTGATCCTAGGAACATCACTAATTCACTTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGATTAAATTCAAACTCAGACAAAATTCCATTCCACCCTTACTACTCATACAAAGATGCCCTTGGAGCCCTATTATTTATAACTCTACTCTTATACCTTTCACTATTTTCACCCTTACTCCTAGGAGACCCCGAAAACTTTA', 'Ib7': 'GGATTGTGCCTAATTACTCAAATTGTTACCGGACTATTTTTAGCAATACACTATAATGCAGATATTAACTCCGCATTCTCATCAGTCGCGCACATTCACCGTGATGTGCAACATGGCTGACTAATCCGAAATATCCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGGGGCCTATACTACGGGTCCTACTTATTCACTGAAACATGAAACATTGGAGTTCTTCTCCTCCTCTTAGTAATAGCTACAGCCTTCATAGGTTATGTACTCCCATGGGGACAAATATCATTTTGAGGAGCCACTGTCATTACTAATCTCTTATCTGCCATCCCATACATTGGAAACACTCTAGTTGAGTGAGTTTGAGGTGGATTCGCAATCGATAACGCAACCCTAACTCGATTCTTCACACTACACTTCCTCCTACCTTTTCTGATCCTAGGAACATCACTAATTCACTTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGATTAAATTCAAACTCAGACAAAATTCCATTCCACCCTTACTACTCATACAAAGATGCCCTTGGAGCCCTATTATTTATAACTCTACTCTTATACCTTTCACTATTTTCACCCTTACTCCTAGGAGACCCCGAAAACTTTA', 'Outgroup': 'GGCCTCTGTTTAATTATTCAAACCGTTACAGGCCTTTTTCTAGCCATACACTACACCCCAGACATCTCTTCAGCATTTTCATCCGTCGCTCACATTCACCGAGACGTTCAATACGGGTGACTTATCCGCAATCTGCATGCCAACGGTGCTTCTATGTTCTTTGTCTGTATTTATCTACACATCGGACGAGGTTTATATTATGGCTCTTATATATTTATTGAGACCTGAAATATTGGAGTTATTCTCCTACTTCTCGTTATAGCTACAGCCTTTATAGGATACGTATTACCCTGAGGCCAAATATCATTCTGAGGGGCCACTGTTATTACCAACCTTCTCTCCGCAATCCCCTACATTGGTACCTCCCTTGTTGAGTGAATCTGAGGCGGATTTGCAGTAGATAACGCAACCCTAACTCGATTCTTTACCTTCCATTTTCTTTTACCCTTCCTCATTATAGGTACCTCTATAGTCCACCTACTCTTTCTACACGAAACAGGATCAAACAACCCAACAGGTTTGAACTCCAACACTGATAAAATCCCCTTCCACCCATACTACTCTTATAAAGATCTATTAGGTGTTATAATAATCATTACCCTTCTCCTATTTCTCGCCCTTTTTGCACCCAACCTCCTAGGCGACCCCGAAAACTTCT', 'Ib24': 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGNAGCACACATTCACCGCGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATNATGCACATCGGACGGGGCCTATACTACGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCNCTCTTAGTAATAGCTNCAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCATTCTGAGGGGCCACNGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAGCACCTTGGTTGAGTGNGTTTGAGGTGGATTCGCAATTGATAACGCAACACNAACTCGATTCTTCACACTACACTTCCTCCTACCCTTTTTAATCCTAGGAACATCATTAATTCACCTNATATTTTTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTGCTCTTATACCTCTCACTATTCTCCCCGTTACTCCTGGGAGACCCAGAAAACTTCA', 'Ib23': 'GGATTATGCCTAATTACTCAAATTGTTACAGGGTTATTTTTAGCAATACACTACAACGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGTGATGTCCAACATGGCTGACTTATCCGAAATGTTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTACATGCACATTGGGCGGGGCCTATACTATGGATCCTACTTATTCACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGAGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACTCTAGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTCTGATCTTAGGAACATCACTAATTCACCTAATATTTCTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAATTCAGATAAAATCCCGTTCCACCCATACTACTCGTATAAAGACGCCCTTGGAGCCCTATTATTCATAACCCTRCTCTTGTACCTATCACTATTTTCTCCATTACTCCTGGGAGACCCAGAAAACTTTA', 'Ib22': 'GGATTGTGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTTTCATCAGTAGCACACATTCACCGCGATGTCCAACATGGCTGACTTATTCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATTTATATGCACATCGGGCGGGGCCTATACTATGGATCCTACTTATTCACTGAAACATGAAACATTGGAGTTCTACTTCTCCTCTTAGTAATAGCCACAGCTTTCATAGGTTATGTCCTCCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCCGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACACTTCCTCCTACCCTTTTTAATTCTAGGAGCATCACTAATTCACCTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAGCCCTGCTCTTATACCTCTCACTATTCTCCCCATTACTCCTGGGAGACCCAGAAAACTTTA', 'Ib21': 'GGATTATGCCTAGTTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCACATCGGACGGGGCCTATACTACGGATCCTACTTATTCACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGCTATGTCCTCCCATGAGGACAAATATCATTTTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAGCACCTTGGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATCCTAGGAACATCATTAATTCACCTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGATTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTGCTCTTRTACCTCTCACTATTCTCCCCATTACTCCTGGGAGACCCAGAAAACTTCA', 'Ib20': 'GGAATATGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATATGCATCTATATGCACATCGGACGGGGCCTATACTACGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAGCACCTTGGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATCCTAGGAACATCATTAATTCACCTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTGCTCTTATACCTCTCACTATTCTCCCCATTACTCCTGGGAGACCCAGAAANNNNNN', 'Mo12': 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGTGATGTCCAACATGGCTGACTTATCCGAAATATCCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGGGGCCTATACTATGGATCTTACTTATTTACTGAAACATGGAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGTGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCCTAGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTCTGATCTTAGGAACATCATTAATTCACCTAATATTTCTACACGAAACAGGATCAAACAACCCTACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTCATAACCCTACTCTTGTACCTATCACTATTCTCTCCATTACTCCTAGGAGACCCAGAAAACTTTA', 'Mo11': 'GGATTGTGCCTAATTACTCAAATTGTCACAGGGTTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGTGATGTTCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGGGGCCTATACTATGGATCCTACTTATTCACTGAAACATGGAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGGGCCACCGTCATTACTAACCTTTTATCCGCCATCCCATACATTGGAAACACCCTAGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACACTTCCTCCTACCCTTTCTGATCTTAGGAACATCACTAATTCACCTAATATTTCTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTACTCATACAAAGACGCCCTTGGAGCCCTATTATTCATAACCCTACTCTTGTACCTATCACTATTCTCTCCATTACTCCTAGGAGACCCAGAAAACTTTA', 'Mo10': 'GGACTGTGCCTAATTACTCAAATTGTTACAGGGTTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGTGATGTCCAACATGGCTGACTTATCCGAAATATCCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGGGGCCTATACTATGGATCCTACTTATTTACTGAAACATGGAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGTGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCCTAGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTCTGATCTTAGGAGCATCATTAATTCACCTAATATTTCTACACGAAACAGGATCAAACAACCCTACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTCATAACCCTACTCTTGTACCTATCACTATTCTCTCCATTACTCCTAGGAGACCCAGAAAACTTTA', 'Mo9': 'GGACTATGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCTGCATTCTCATCAGTAGCACACATTCATCGTGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGAGGCCTATACTATGGATCCTACTTATTCACTGAAACATGGAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGCTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGGGCCACTGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCCTAGTCGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTCTGATCTTAGGAACATCATTAATTCACCTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTACTATTCATAACCCTACTCTTGTACCTATCACTATTCTCTCCATTACTCTTAGGAGACCCAGAAAACTTTA', 'Mo8': 'GGACTATGCCTAATCACTCAAATTGTTACAGGATTGTTTTTAGCAATACACTACAATGCGGATATTAACTCCGCATTCTCATCAGTAGCACACATTCATCGTGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGAGGCCTATACTATGGATCCTACTTATTCACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGCTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGGGCCACTGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCCTAGTCGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTATGATCTTAGGAACATCATTAATTCACCTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTATTCATATAAAGACGCCCTTGGAGCCCTACTATTCATAACCCTACTCTTGTATCTATCACTATTCTCTCCATTACTCTTAGGGGACCCAGAAAACTTTA', 'Mo3': 'GGATTATGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAACGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGTGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTACATGCACATTGGGCGGGGCCTATACTATGGATCCTACTTATTCACTGAAACATGGAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGAGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACTTTAGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTCTGATCTTAGGAACATCACTAATTCACCTAATATTTCTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAATTCAGATAAAATCCCGTTCCACCCATACTACTCGTATAAAGACGCCCTTGGAGCCCTATTATTCATAACCCTACTCTTGTACCTATCACTATTTTCTCCATTACTCCTAGGAGACCCAGAAAACTTTA', 'Mo2': 'GGATTATGCCTAATTACTCAAATTGTTACAGGGTTATTTTTAGCAATACACTACAACGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGTGATGTCCAACATGGCTGACTTATCCGAAATGTTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTACATGCACATTGGGCGGGGCCTATACTATGGATCCTACTTATTCACTGAAACATGGAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGAGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACTCTAGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTCTGATCTTAGGAACATCACTAATTCACCTAATATTTCTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAATTCAGATAAAATCCCGTTCCACCCATACTACTCGTATAAAGACGCCCTTGGAGCCCTATTATTCATAACCCTACTCTTGTACCTATCACTATTTTCTCCATTACTCCTAGGAGACCCAGAAAACTTTA', 'Mo1': 'GGATTATGCCTAATTACTCAAATTGTTACAGGGTTATTTTTAGCAATACACTACAACGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGTGATGTCCAACATGGCTGACTTATCCGAAATGTTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTACATGCACATTGGGCGGGGCCTATACTATGGATCCTACTTATTCACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGAGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACTCTAGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTCTGATCTTAGGAACATCACTAATTCACCTAATATTTCTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAATTCAGATAAAATCCCGTTCCACCCATACTACTCGTATAAAGACGCCCTTGGAGCCCTATTATTCATAACCCTACTCTTGTACCTATCACTATTTTCTCCATTACTCCTAGGAGACCCAGAAAACTTTA', 'Mo7': 'GGACTATGCCTAATCACTCAAATTGTTACAGGATTGTTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCATCGTGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGAGGCCTATACTATGGATCCTACTTATTCACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGCTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGGGCCACTGTCATTACTAACCTTTTATCTGCCATCCCATACATCGGAAACACCCTAGTCGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTATGATCTTAGGAACATCATTAATTCACCTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTATTCATATAAAGACGCCCTTGGAGCCCTACTATTCATAACCCTACTCTTGTACCTATCACTATTCTCTCCATTACTCTTAGGGGACCCAGAAAACTTTA', 'Mo6': 'GGACTATGCCTAATCACTCAAATTGTTACAGGATTGTTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCATCGTGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGAGGCCTATACTATGGATCCTACTTATTCACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGCTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGGGCCACTGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCCTAGTCGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTATGATCTTAGGAACATCATTAATTCACCTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTATTCATATAAAGACGCCCTTGGAGCCCTACTATTCATAACCCTACTCTTGTACCTATCACTATTCTCTCCATTACTCTTAGGGGACCCAGAAAACTTTA', 'Mo5': 'GGACTATGCCTAATCACTCAAATTGTTACAGGATTGTTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCATCGTGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTATATGCACATCGGACGAGGCCTATACTATGGATCCTACTTATTCACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGCTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGGGCCACTGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCCTAGTCGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTATGATCTTAGGAACATCATTAATTCACCTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTATTCATATAAAGACGCCCTTGGAGCCCTACTATTCATAACCCTACTCTTGTACCTATCACTATTCTCTCCATTACTCTTAGGGGACCCAGAAAACTTTA', 'Mo4': 'GGATTATGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAACGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGTGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTTATTTGCATTTACATGCACATTGGGCGGGGCCTATACTATGGATCCTACTTATTCACTGAAACATGGAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCGTTTTGAGGAGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACTTTAGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACGCTACATTTCCTCCTACCCTTTCTGATCTTAGGAACATCACTAATTCACCTAATATTTCTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAATTCAGATAAAATCCCGTTCCACCCATATTACTCGTATAAAGACGCCCTTGGAGCCCTATTATTCATAACCCTACTCTTGTACCTATCACTATTTTCTCCATTACTCCTAGGAGACCCAGAAAACTTTA', 'Ib18': 'GGATTATGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCACATCGGACGGGGCCTATACTATGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTCTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATCTTAGGAACATCACTAATTCACCTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGATTAAACTCAAACTCAGATAAAATCCCGTTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTGCTCTTATACCTCTCACTATTCTCCCCATTACTCCTGGGAGACCCAGAAAACTTCA', 'Ib19': 'GGATTATGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAACATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCACATCGGACGGGGCCTATACTACGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCTACAGCCTTCATAGGTTATGTCCTCCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAGCACCTTGGTTGAGTGAGTTTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACACTTCCTCCTACCCTTTTTAATCCTAGGAACATCATTAATTCACCTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGACTAAACTCAAACTCAGATAAAATCCCATTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTACTCTTATACCTCTCACTATTCTCCCCGTTACTCCTGGGAGACCCAGAAAACTTNN', 'Ib12': 'GGATTGTGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAATACGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCATATCGGACGGGGCCTATACTATGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTTCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTCTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATTTTAGGGACATCACTAATACACCTAATATTTTTACACGAAACAGGGTCAAACAACCCAACAGGGTTAAACTCAAACTCAGATAAAATCCCGTTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTACTCTTATACCTCTCACTATTTTCCCCATTGCTCCTAGGAGACCCAGAAAACTTCA', 'Ib13': 'GGATTGTGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAATACGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCATATCGGACGGGGCCTATACTATGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTTCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTCTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATTTTAGGGACATCACTAATACACCTAATATTTTTACACGAAACAGGGTCAAACAACCCAACAGGGTTAAACTCAAACTCAGATAAAATCCCGTTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTACTCTTATACCTCTCACTATTTTCCCCATTGCTCCTAGGAGACCCAGAAAACTTCA', 'Ib10': 'GGATTGTGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAATACGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCATATCGGACGGGGCCTATACTATGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTTCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTCTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATTTTAGGGACATCACTAATACACCTAATATTTTTACACGAAACAGGGTCAAACAACCCAACAGGGTTAAACTCAAACTCAGATAAAATCCCGTTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTACTCTTATACCTCTCACTATTTTCCCCATTGCTCCTAGGAGACCCAGAAAACTTCA', 'Ib11': 'GGATTGTGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAATACGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCATATCGGACGGGGCCTATACTATGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTTCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTCTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATTTTAGGGACATCACTAATACACCTAATATTTTTACACGAAACAGGGTCAAACAACCCAACAGGGTTAAACTCAAACTCAGATAAAATCCCGTTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTACTCTTATACCTCTCACTATTTTCCCCATTGCTCCTAGGAGACCCAGAAAACTTCA', 'Ib16': 'GGATTATGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAATACGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCATATCGGACGGGGCCTATACTATGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTTCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTCTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATTTTAGGGACATCACTAATACACCTAATATTTTTACACGAAACAGGGTCAAACAACCCAACAGGGCTAAACTCAAACTCAGATAAAATCCCGTTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTACTCTTATACCTCTCACTATTTTCCCCATTGCTCCTAGGAGACCCAGAAAACTTCA', 'Ib17': 'GGATTGTGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAATATGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCATATCGGACGGGGCCTATACTATGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTTCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTCTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATTTTAGGAACATCACTAATACACCTAATATTTTTACACGAAACAGGATCAAACAACCCAACAGGGTTAAACTCAAACTCAGATAAAATCCCGTTCCACCCATACTACTCATACAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTACTCTTATACCTCTCACTATTTTCCCCATTGCTCCTAGGAGACCCAGAAAACTTCA', 'Ib14': 'GGATTGTGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAATACGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCATATCGGACGGGGCCTATACTATGGATCCTACTTATTTACTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTTCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTCTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATTTTAGGGACATCACTAATACACCTAATATTTTTACACGAAACAGGGTCAAACAACCCAACAGGGTTAAACTCAAACTCAGATAAAATCCCGTTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTACTCTTATACCTCTCACTATTTTCCCCATTGCTCCTAGGAGACCCAGAAAACTTCA', 'Ib15': 'GGATTGTGCCTAATTACTCAAATTGTTACAGGATTATTTTTAGCAATACACTACAATGCAGATATTAACTCCGCATTCTCATCAGTAGCACACATTCACCGCGATGTCCAATACGGCTGACTTATCCGAAATATTCATGCTAACGGCGCATCACTATTCTTCATTTGCATCTATATGCATATCGGACGGGGCCTATACTATGGATCCTACTTATTTATTGAAACATGAAACATTGGAGTACTACTTCTCCTCTTAGTAATAGCCACAGCCTTCATAGGTTATGTCCTTCCATGAGGACAAATATCATTCTGAGGGGCCACCGTCATTACTAACCTTTTATCTGCCATCCCATACATTGGAAACACCTTGGTTGAGTGAGTCTGAGGTGGATTCGCAATTGATAACGCAACACTAACTCGATTCTTCACACTACATTTCCTCCTACCCTTTTTAATTTTAGGGACATCACTAATACACCTAATATTTTTACACGAAACAGGGTCAAACAACCCAACAGGGTTAAACTCAAACTCAGATAAAATCCCGTTCCACCCATACTACTCATATAAAGACGCCCTTGGAGCCCTATTATTTATAACCCTACTCTTATACCTCTCACTATTTTCCCCATTGCTCCTAGGAGACCCAGAAAACTTCA'}
x=sequences.items()
for keys, value in sequences.items(): #n entendi lá muito bem oque eu fiz mas funcionou ig (ele separa para a primeira variavel que eu criar as keys e para a segunda a value)
    print(f"{keys}-{value}\n") #put \n for some organization reasons
print("\n\n#1.1")#1.1
for keys, value in sequences.items(): #> in FAST
    print(f">{keys}\n{value}") 
print("\n\n#1.2")#1.2
for keys, value in sequences.items():
    if value.startswith("N"):
        continue
    else:
        print(f">{keys}\n{value}")
print("\n\n#1.3")#1.3
for keys, value in sequences.items(): #> in FAST
    print(f">{keys}\n{value[::-1]}") #reversed(é isso só?)

print("\n\n\n")
#EXTREME CHALLENGE AHHHHHHHHHHHHHHHHH
new_sequences = {}
mult_names = set()  # Stores sequence names that have already been collapsed
for keys, value in sequences.items():
    if keys in mult_names:
        continue
    mult_names.add(keys)
    for keys2, value2 in sequences.items():
        if keys2 not in mult_names and keys2 == keys:
            new_sequences.add(keys2)
            mult_names.add(keys2)
            new_sequences += f"\n{keys2}"
            
        


print(new_sequences)

