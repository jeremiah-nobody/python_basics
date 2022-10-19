import sys

#this is a comment

if len(sys.argv) > 2:
     sys.exit("Too many command line arguments.")
elif len(sys.argv) < 2:
     sys.exit("Too few command line arguments.")


file_name = sys.argv[1]
a = len(file_name) - 1

lines = []

try:
     with open(sys.argv[1]) as file:
          for line in file:
               lines.append(line.rstrip())
     with open(sys.argv[1], 'w') as file:
          for line in lines:
               file.writelines(f"{line}", end="\n")

except:
     sys.exit("File does not exit.")

convert = lambda: os.system(f"dos2unix {sys.argv[1]}")
convert()
