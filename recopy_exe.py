#!/usr/bin/python3
#-*- coding: utf-8 -*-
# 匯入內部模組
import datetime
import json
import os
import sys
import time
import shutil

# 匯入程式所需模組
from textmod import tui
from getjson import jsonReader
import theStrings as i18n

# 定義前置變數
config = "config.json"

###############
## 主程式部份 ##
##############
# 載入 json
jsonContent = jsonReader(config)

# 接收指令列參數
if len(sys.argv) > 2:
    sourcePath = sys.argv[1]
    targetPath = sys.argv[2]
else:
    if jsonContent == 255 or jsonContent == 250:
        tuilist = tui()
        sourcePath = tuilist[0]
        targetPath = tuilist[1]
    else:
        sourcePath = jsonContent[0]
        targetPath = jsonContent[1]

if os.path.isfile(sourcePath):
    recursive = False
else:
    recursive = True

# 路徑變數 (方便維護所以先將路徑組合成一個變數)
Path = sourcePath + " " + targetPath + " "

# 定義後置變數
## Windows 的檔案複製變數
cp_win32 = 'robocopy ' + Path + '/mir /eta /mt:100'
## Linux 的檔案複製變數 
cp_linux = 'rsync -h --progress ' + Path
## Windows 的資料夾複製變數
rm_win32 = 'robocopy ' + Path + '/e /eta /mt:100'
## Linux 的資料夾複製變數
rm_linux = 'rsync -hr --progress ' + Path

if __name__ == "__main__":
    ntime = datetime.datetime.now()
    dtime = datetime.timedelta(seconds=1)
    ntime += dtime
    print(i18n.main_recheck.format(h = ntime.hour, m = ntime.minute, s = ntime.second, \
source = sourcePath, target = targetPath))
    if input(i18n.gen_input) == "A":
        exit()
    else:
        if sys.platform == "win32":
            if recursive:
                os.system(rm_win32)
            else:
                os.system(cp_win32)
        else:
            if recursive:
                os.system(rm_linux)
            else:
                os.system(cp_linux)
else:
    print(i18n.generr_module)

# 清理垃圾程式檔案
shutil.rmtree("__pycache__")
exit(0)

'''
@ Still developing, DO NOT REMOVE IT!
#錯誤處理 try except
#try:
	
#except Exception as err:
	#顯示錯誤訊息並另存errorlog.txt
	#print("Can't run as module!")
	#將錯誤訊息另存errorlog.txt
	#errfile = open("errorlog.txt","w")
	#errfile.write(err)
#else:
'''
