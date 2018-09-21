#!/usr/bin/python3
#-*- coding: utf-8 -*-
# 匯入內部模組
import datetime
import json
import os
import shutil
import sys
import time

# 匯入程式所需模組
import settings as options
import theStrings as i18n
from getjson import jsonReader
from textmod import tui

# 定義前置變數
config = "config.json"
sysname = sys.platform

if sysname != "win32":
    rsyncExists = False

    for rsync_path in options.rsyncPossiblePath:
        if os.path.exists(rsync_path):
            rsyncExists = True
            break

    if rsyncExists == False:
        raise Exception(i18n.err_rsyncNotFound)

################
## 主程式部份 ##
################
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

if __name__ == "__main__":
    ntime = datetime.datetime.now()
    print(i18n.main_recheck.format(h = ntime.hour, m = ntime.minute, s = ntime.second, \
source = sourcePath, target = targetPath))
    if input(i18n.gen_input) == "A":
        exit()
    else:
        if sysname == "win32":
            if recursive:
                os.system(options.rm_win32.format(Path))
            else:
                raise Exception(i18n.err_windowsdir)
        else:
            if recursive:
                os.system(options.rm_linux.format(Path))
            else:
                os.system(options.cp_linux.format(Path))
else:
    print(i18n.generr_module)

# 清理垃圾程式檔案
shutil.rmtree("__pycache__")
exit(0)
