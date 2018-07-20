#!/usr/bin/python3
#-*- coding: utf-8 -*-
import datetime
import json
import os
import sys
import time
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


# TUI 函式
def tui():
    global sourcePath, targetPath
    sourcePath = input("輸入來源位置：")
    targetPath = input("輸入目標位置：")
    print("""請再次確認是否輸入正確。

來源位置：{sP}
目標位置：{tP}

如果輸入錯誤，輸入 A 關閉程式之後重新開啟輸入。
如果輸入正確，直接按下 Enter 即可。
""".format(sP=sourcePath, tP=targetPath))
    if input("請輸入：") == "A":
        exit()
    else:
        return


# 讀取 config.json 的內容
if os.path.exists("config.json"):
    jsonExist = True
    jsonInit = os.open("config.json", os.O_RDONLY)
    jsonRaw = str(os.read(jsonInit, 4096), encoding="UTF-8")
    jsonContent = json.loads(jsonRaw)
    jsonContent.pop('//')
else:
    jsonExist = False
    print("[WARN] config.json not found!")

# 接收指令列參數
if len(sys.argv) > 2:
    sourcePath = sys.argv[1]
    targetPath = sys.argv[2]
else:
    if jsonExist:
        if jsonContent.get("sourcePath", "") == "" or jsonContent.get(
                "targetPath", "") == "":
            tui()
        else:
            sourcePath = jsonContent.get("sourcePath")
            targetPath = jsonContent.get("targetPath")
    else:
        tui()

if os.path.isfile(sourcePath):
    recursive = False
else:
    recursive = True

#路徑變數(方便維護所以先將路徑組合成一個變數)
Path = sourcePath + " " + targetPath + " "

#定義參數
#鏡像複製 (win32)
#注意：此指令會先清除目的地資料夾的資料
cp_win32 = 'robocopy ' + Path + '/mir /mt:100'

# 複製 (linux / mac)
cp_linux = 'rsync -h --progress ' + Path

#遞迴複製(含空資料夾) (win32)
#說明：此指令也會複製子資料夾
rm_win32 = 'robocopy ' + Path + '/e /mt:100'

# 遞迴複製 (linux / mac)
rm_linux = 'rsync -hr --progress ' + Path

if __name__ == "__main__":
    ntime = datetime.datetime.now()
    deltatime = datetime.timedelta(seconds=3)
    ntime += deltatime
    print("""
開始時間：{h} 時 {m} 分 {s} 秒
來源位置：{source}
目標位置：{target}

若沒有問題，請直接輸入 Enter
若有問題，請輸入 A 後重新開啟程式。""".format(h = ntime.hour, m = ntime.minute, s = ntime.second, \
source = sourcePath, target = targetPath))
    if input("請輸入：") == "A":
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
    print("Can't run as module!")
