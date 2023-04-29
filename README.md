# Programming Applied to Bioinformatics Projects

This repository contains the code for the projects completed in the Programming Applied to Bioinformatics (PAB) classes. All the code in this repository is written in Python.

## Getting Started

To get started with this project, you'll need to have Python installed on your computer. You can download it from the official website [here](https://www.python.org/downloads/).

Once you have Python installed, you can clone this repository to your local machine using the following command:

	git clone https://github.com/Guimbreon/pab_22-23.git

## Contents

The repository contains the following projects:

### Assignment 1: Motif Finder in DNA Sequences

The code reads in a file containing DNA sequences in FASTA format and prompts the user to input a motif to search for. It then searches for the motif in both the forward and reverse complement sequences of each DNA sequence in the file, and outputs the positions where the motif is found along with some additional information, such as the sequence name, length, and frame. The code also includes some error handling to ensure that the input motif is valid and has a length of at least 5 base pairs.


### Assignment 2: File Converter

This is a Python code for a program that can convert files between different formats (Nexus, Fasta, and Phylip). It uses the argparse library to accept command-line arguments for the input and output files. Here is a breakdown of what the program does:

    Imports the required modules (sys and argparse) and defines an ArgumentParser object.
    Adds two arguments to the parser object for the input and output files.
    Parses the arguments using the parse_args() method and assigns the values to the file1 and file2 variables.
    Defines a data class to hold the sequence data.
    Defines a function know_type_input() to determine the format of the input file based on its content.
    Defines a function know_type_output() to determine the format of the output file based on its extension.
    Defines a function reading() to read the input file and store its data in the data class.
    Defines a function writing() to write the data from the data class to the output file in the desired format.
    Calls the functions in the order defined above to perform the file conversion.

Overall, this code is an example of how to use command-line arguments, object-oriented programming, and file input/output operations in Python to create a simple file conversion program.

### Desafio_pb: Sequence Comparator

The Sequence Comparator is a Python program that compares two fasta files containing sequences from the NCBI and ENA databases. The program first reads in the fasta files and extracts the sequence names from each file. The sequence names are then sorted in alphabetical order. The program then compares the sorted sequence names from both files and prints out any names that are in one file but not the other.

### Exercices

This file contains all the exercises covered in the practical classes of PAB.

### Fasta_files

This pasta contains all the fasta_files that are available for use in any project.

### Working_codons: Gene Sequence Finder

The Gene Sequence Finder is a Python program that reads a FASTA-formatted file of DNA sequences and identifies potential coding regions. The program extracts the sequence from the start codon (ATG) to the stop codon (TAG, TAA, or TGA) and reports the length of the sequence and its start and stop positions. It also appends the identified coding regions to a list. The program is useful for identifying genes of interest and analyzing DNA sequences.


## Contributing

If you find any issues or have suggestions for improving this repository, please feel free to submit a pull request or create an issue.

## License

This repository is licensed under the [GNU License](LICENSE).

