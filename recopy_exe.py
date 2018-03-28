import os
#Hello world 指令
printf = "Notepad.exe"

#定義指令與主要路徑
Robocopy = "robocopy"
#來源路徑，使用者請修改它
Source = "<Source folder path：Please paste the source path to this line !>"
#目的地路徑
Destination = "<Destination folder path：Please paste the destination path to this line ! >"

#定義參數
#鏡像複製
#注意：此指令會造成目的地資料遺失
Mirrors_Copy = "/mir"

#遞迴複製(含空資料夾)
#說明：此指令也會複製子資料夾
Recursive_Mode = "/e"

#多線城複製設定(此指令適用於Win7以上)
Multi_threaded_set = "/mt:100"

os.system("robocopy D:\TEST1 D:\TEST2 /mir /mt:100")
