The second assignment from pab_22-23



Rules:

    The program must be written in Python 3.
    The program cannot be linear -> Most of your code (more than 90%) has to be inside functions and classes.
    All functions must take at least one parameter, but not all of them have to return something.
    You can import modules from Python's standard library (those included with Python), but not from third party packages (like BioPython).
    The input file must be provided to the program as a command line argument.
    The output file must be provided to the program as a command line argument.
    The program can use the file extension to infer the output format, but not the input format.
    The sequences from the input file must be read into an "intermediate representation": an instance of a class called Sequence. This class can have as many proprieties as you want, but needs to have at least one method for obtaining the sequence's length.
    The Nexus and Phylip formats have two variants - "leave" and "interleave". For this assignment, you only need to worry about the "leave" variant, and can safely ignore that the "interleave" variant even exists (both for input and output).
    When reading or writing a nexus file, you only need to read/write the "data" block. Any other blocks can be safely ignored.
    For this exercise you can also assume that the "DATATYPE" is always DNA, the "MISSING" character is always "N", and the "GAP" character is always "-" (relevant only for Nexus files).
    When writing Nexus or Phylip files, you don't have to worry about aligning sequence names.

