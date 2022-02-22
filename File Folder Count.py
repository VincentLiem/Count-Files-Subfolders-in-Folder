import os

path = input("Enter path >> ")
exclude_under = int(input("Exclude folders with less than this many files >> "))
save_file = input("Save to text file? (Y/N) >> ")
def CheckYes(x):
    return x == "Y" or x == "y"
if CheckYes(save_file):
    with open('File count.txt', 'w') as save:
        save.write(path + '\n')
total_files = 0
total_dir = 0
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
print("Total files: ", total_files)
print("Total directories: ", total_dir)
if CheckYes(save_file):
    with open('File count.txt', 'a') as save:
        save.write("Total files: " + str(total_files) + '\n')
        save.write("Total directories: " + str(total_dir) + '\n')
    save.close()
