import os
#Hello world 指令
printf = "Notepad.exe"

#定義參數
Robocopy = "robocopy"
#來源路徑，使用者請修改它
Source = "D:\Source folder path"
#目的地路徑
Destination = "D:\Destination folder path"

#鏡像複製
#注意：此指令會造成目的地資料遺失
Mirrors_Copy = "/mir"

os.system(printf)
