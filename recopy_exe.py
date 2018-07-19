#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os, sys, json

'''
從 Source 複製資料至目標位置
可接受指令列的參數。

Usage: recopy.py Source Target

Source
    來源位址。使用 "" 包住。
Target
    目標位址。使用 "" 包住。

Example:
    recopy.py "./abc" "./123"
    recopy.py "./abc.py" "./123/abc.py"
'''

# 讀取 config.json 的內容
if os.path.exists("config.json"):
    jsonExist = True
    jsonInit = os.open("config.json", os.O_RDONLY)
    jsonRaw = str(os.read(jsonInit, 4096), encoding="UTF-8")
    jsonContent = json.loads(jsonRaw)
    jsonContent.pop('//')
else:
    print("[WARN] config.json not found!")

# 接收指令列參數
if len(sys.argv) > 2:
    sourcePath = sys.argv[1]
    targetPath = sys.argv[2]
else:
    if jsonExist:
        sourcePath = jsonContent.get('sourcePath', ":errcode:1")
        targetPath = jsonContent.get('targetPath', ":errcode:2")
    else:
        print("[ERR] 參數輸入錯誤！")

if os.path.isfile(sourcePath):
    recursive = False
else:
    recursive = True

#路徑變數(方便維護所以先將路徑組合成一個變數)
Path = sourcePath + " " + targetPath + " "

#定義參數
#鏡像複製 (win32)
#注意：此指令會先清除目的地資料夾的資料
cp_win32 = 'robocopy '+ Path +'/mir /mt:100'

# 複製 (linux / mac)
cp_linux = 'rsync -h --progress ' + Path

#遞迴複製(含空資料夾) (win32)
#說明：此指令也會複製子資料夾
rm_win32 = 'robocopy ' + Path + '/e /mt:100'

# 遞迴複製 (linux / mac)
rm_linux = 'rsync -hr --progress ' + Path

if __name__ == "__main__":
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
    print("Can't run as module!")