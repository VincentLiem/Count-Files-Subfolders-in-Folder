import os

path = input("Enter path >> ")
try:
    exclude_under = int(input("Exclude folders with less than this many files >> "))
except ValueError:
    print ('Number not entered, including all')
    exclude_under = 0
save_file = input("Save to text file? (Y/N) >> ")
def CheckYes(x):
    return x.lower() == "y" or x.lower() == "yes"
if CheckYes(save_file):
    with open('File count.txt', 'w') as save:
        save.write(path + '\n')
total_files = 0
total_dir = 0
exclude_count = 0
for base, dirs, files in os.walk(path):
    dirs = sorted(dirs)
    file_count = 0
    for directories in dirs:
        total_dir += 1
    for Files in files:
        total_files += 1
        file_count += 1
    if file_count >= exclude_under:
        if CheckYes(save_file):
            with open('File count.txt', 'a') as save:
                save.write(base + ' : ' + str(file_count) + ' files \n')
        print(base, " : ", file_count, " files")
    if file_count < exclude_under:
        exclude_count += 1
if exclude_under > 0:
    print(exclude_count, "directories hidden")
print("Total files: ", total_files)
print("Total directories: ", total_dir)
if CheckYes(save_file):
    with open('File count.txt', 'a') as save:
        if exclude_under > 0:
            save.write(str(exclude_count) + ' directories hidden' + '\n')
        save.write("Total files: " + str(total_files) + '\n')
        save.write("Total directories: " + str(total_dir) + '\n')
