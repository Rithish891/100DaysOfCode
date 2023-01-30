import os

FOLDER_PATH = "C:\\Users\\rreddyja\\PycharmProjects\\100DaysOfCode"


folders = ["Day{}".format(i) for i in range(1, 101)]

for folder in folders:
    if os.path.isdir("./{}".format(folder)):
        print("Exists")
    else:
        os.mkdir("./{}".format(folder))
