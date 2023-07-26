# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import os
import re
import pandas as pd


#获取控制台传入的文件名
params = sys.argv
sourceRoot = params[1]
print sourceRoot
outputRoot = params[2]
files = os.listdir(sourceRoot)

# def outputJson(path,data):
	

def readExcel(path,outPath):
	print "读取" + path
	df = pd.read_excel(io=nowPath)
	lines = len(df)
	names = df.columns.values
	finalJson = []
	for line in range(0,lines):
		lineMap = {}
		for title in names:
			value = df.iloc[line][title]
			ns = title.split("/") #name split
			realValue = ""
			if not pd.isna(value):
				if type(value) == unicode:
					# 是文本
					realValue = value
				else:
					realValue = int(value)
			else:
				realValue = value
			if len(ns) > 1: #存在/
				if lineMap.has_key(ns[0]):
					lineMap[ns[0]][ns[1]] = realValue
				else:
					if ns[1] == "0":
						lineMap[ns[0]] = [realValue]
					else:
						lineMap[ns[0]] = {ns[1]:realValue}
			else:
				lineMap[ns[0]] = realValue
		finalJson.append(lineMap)
	jf = pd.DataFrame(finalJson)
	file_path = outputRoot  + "/"+ outPath
	jf.to_json(file_path, orient="records", lines=False, force_ascii=False)

for f in files:
    if not os.path.isdir(f): #判断是否是文件夹   
    	if re.search(r".*\.xlsx$", f, re.M|re.I):
    		nowPath = sourceRoot + '/' + f
    		sourceData = readExcel(nowPath,re.sub(".xlsx", ".json", f))

