#!/usr/bin/python
import re
import pdb 
import os
import sys

def filterFile(filepath,word):
	sourcefiles = open(filepath,'r')
	arr = sourcefiles.readlines()
	for index in range(len(arr)):
		line = arr[index]
		if line.find(word) != -1:
			sourcefiles.close()
			# print(filepath.split("/")[-1],index,word)
			return True
	sourcefiles.close()

def allfiles(filepath,word):
	for dirpath,dirnames,filenames in os.walk(filepath):
		for file in filenames:
			if file.find('Localizable.strings') != -1:
				continue
			if file.find('.m') == -1:
				continue
			child = os.path.join('%s/%s' % (dirpath, file))
			rst = filterFile(child,word)
			if rst:
				return True
	return False

def allwords(filepath,wordpath):
	if os.path.exists(filepath) == False:
		print("%s not exist !!!"%(filepath));
		return
	if os.path.exists(wordpath) == False:
		print("%s not exist !!!"%(wordpath));
		return

	arr = []
	linearr = []
	wordsfile = open(wordpath,'r')
	for word in wordsfile.readlines():
		pattern = re.compile(r'"(.*?)"')
		match = pattern.match(word)
		if match:
			childs = match.group()
			if allfiles(filepath,childs) == False:
				arr.append(childs)
			else:
				linearr.append(word)
		else:
			linearr.append(word)
	print("unused string: %s"%(arr))
	output = open('outputLocalizable.strings', 'w')
	for word in linearr:
		output.write(word)
	output.close()
	print("new strings file:%s/%s"%(cur_file_dir(),'outputLocalizable.strings'))


def cur_file_dir():
	path = sys.path[0]
	if os.path.isdir(path):
		return path
	elif os.path.isfile(path):
		return os.path.dirname(path)

# allwords('/Users/yangbo/Desktop/gitlab/DidaShipper-iOS','/Users/yangbo/Desktop/gitlab/DidaShipper-iOS/DidaShipper/Resources/Base.lproj/Localizable.strings')
# allwords('/Users/yangbo/Desktop/py_tools','/Users/yangbo/Desktop/py_tools/Localizable.strings')

if len(sys.argv) < 3 :
	print('please input argv !!!')
else:
	allwords(sys.argv[1],sys.argv[2])


