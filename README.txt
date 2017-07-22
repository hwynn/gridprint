Bioinformatics project 1: protein sequence alignment software

This project has 2 versions. One version is written in python and the other is written in c++. Functionality is identical.

I. Python version (compiled and tested in windows 7)
Python 3 must be installed on the system to compile and run it.
instructions: navigate to the project folder and run "py align.py"
This will show a demo of the program functionality without requiring FASTA.txt files from the user.
If you do have two FASTA formatted text files and want to run a sequence alignment, use the command "py align.py filename1.fasta.txt filename2.fasta.txt". The alignment will be printed in the console window.


II. C++ version (compiled and tested in fedora 22)
g++ Must be installed on the system.
instructions: navigate to the project folder and run "make".
After the program compiles, run with "./l". This will show a demo of the program functionality without requiring FASTA.txt files from the user.
If you do have two FASTA formatted text files and want to run a sequence alignment, use the command "./l filename1.fasta.txt filename2.fasta.txt". The alignment will be printed in the console window.
