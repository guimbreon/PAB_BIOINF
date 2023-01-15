This is our first Assignment( the first "big" project we did).

Objectives:

	Create a program that reads a FASTA file, finds DNA motifs in it and reports its findings.


Rules:

	    The program must be written in Python 3
	    The program must be linear -> Do not write any functions or classes (leave that for the next assignment)
	    You can import modules from Python's standard library (those included with Python), but not from third party packages (like BioPython)
	    The FASTA file must be provided to the program as a command line argument
	    The motif must be read from STDIN
		The motif must be at least 5bp long
		The motif must contain only the 4 DNA bases IUPAC codes (A, T, G, or C)
		    Ambiguities can be ignored for this assignment
	    If the motif is present multiple times in the same sequence, your program must report this
		Motifs must be reported in the order they are found: a motif in position 3 must be reported before a motif in position 29
	    The sequence length must be reported
	    The frame where the motif was found must be reported as well
		If this is the case, the positive frames in which the motif was found must be reported before negative ones.
	    Your program must write the results to STDOUT, similar to the example below:
		If your output does not respect this scheme you will automatically fail the assignment
		The field separator character must be a TAB (\t in Python)

