import os
import filecmp

file1 = "output.bin"
file2 =  "output_sorted.bin"

x = input("Enter full path to the directory with files need to compare or just press 'Enter' key to compare files in the current folder:\n")
if(x == ""):
	x = os.curdir

os.chdir(x)
print("U can define filenames at the beginnig of this script. Now we compare: ", file1, " and ", file2)

if filecmp.cmp(file1, file2):
	print("\nFiles are equal!")
else:
        print("\nFiles aren't equal :(")
