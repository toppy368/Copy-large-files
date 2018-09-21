# 《複製大檔案 Copy Large File》程式設定檔案
# 此工具與 config.json 性質不同！

# [Linux] 偵測 rsync 的可能位置
rsyncPossiblePath = ['/usr/bin/rsync', '/bin/rsync', '/usr/sbin/rsync', '/sbin/rsync']

# [Windows] [Linux] 檔案與目錄複製指令
# {} = 來源位置 + 目標位置
# e.g recopy_exe.py recopy2.py
## Linux 的檔案複製變數
cp_linux = 'rsync -h --progress {}'
## Windows 的資料夾複製變數
rm_win32 = 'robocopy {} /e /mir /eta /mt:100'
## Linux 的資料夾複製變數
rm_linux = 'rsync -hr --progress {}'
