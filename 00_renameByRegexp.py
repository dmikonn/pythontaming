import os, re, shutil

path = os.path.dirname(os.path.realpath(__file__))
newpath = path + "/done"
if not os.path.exists(newpath):
    os.makedirs("done")

files = os.listdir(path)
files.remove("rename.py")
files.remove("done")


i = 0
for file in files:
    match1 = re.search(r"\-\d\d\d\_", str(file))
    match2 = re.search(r"page\d\d\d", str(file))
    if match1 == True and match2 == False:
        page = str(match1.group(0))[1:4]
    elif match1 == False and match2 == True:
        page = str(match2.group(0))[4:7]
    elif match1 and match2:
        print("problem: double page numeration")
        break
    else:
        print("problem: page numeration not found")
        break

    if int(page) < 10:
        shutil.copy2(
            os.path.join(path, file), os.path.join(newpath, str("00" + page) + ".jpg")
        )
    elif int(page) < 100:
        shutil.copy2(
            os.path.join(path, file), os.path.join(newpath, str("0" + page) + ".jpg")
        )
    else:
        shutil.copy2(os.path.join(path, file), os.path.join(newpath, page + ".jpg"))
    i = i + 1
