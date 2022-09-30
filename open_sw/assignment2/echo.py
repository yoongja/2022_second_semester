import sys

file_path = sys.argv[1]

if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

print(file_path)