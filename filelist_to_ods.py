import os, collections, sys 
from pyexcel_ods import save_data

reload(sys)
sys.setdefaultencoding('utf8')

youarehere = os.path.dirname(os.path.realpath(__file__))
data = collections.OrderedDict()
filelist = [["Type","Extension","Filename","Path"]]

def extensionChecker (name, ext):
	if ext.lower() == ".jpg" or ext.lower() == ".jpeg" or ext.lower() == ".png" or ext.lower() == ".svg":
		f.append ("Image")
	elif ext.lower() == ".txt" or ext.lower() == ".doc" or ext.lower() == ".docx" or ext.lower() == ".odf" or ext.lower() == ".ods":
		f.append ("Document")
	elif ext.lower() == ".avi" or ext.lower() == ".mkv" or ext.lower() == ".mp4":
		f.append ("Video")
	elif ext.lower() == ".mp3" or ext.lower() == ".ogg":
		f.append ("Audio")
	elif ext.lower() == ".dll" or ext.lower() == ".exe":
		f.append ("Program files")
	else:
		f.append ("Other")

for root, directories, filenames in os.walk(youarehere):
	for filename in filenames: 
		f = []
		name, ext = os.path.splitext(filename)
		extensionChecker(name, ext)
		#if f != ["Other"]:   # 2 lines to make loop go to the next iteration in case of discovery the cathegrised file extention already 
		#	continue          # it's useful to see what kinds of exts are not cathegorised yet
		f.append (ext.lower())
		f.append (filename)
		f.append (os.path.join(root,filename))
		filelist.append(f)

data.update({"Sheet 1":filelist})
save_data("your_file.ods", data)

