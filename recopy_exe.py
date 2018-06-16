import os
#Hello world 指令
printf = "Notepad.exe"

#定義指令與主要路徑

#來源路徑，使用者請修改它
Source = 'D:\TEST\A' + ' '
#目的地路徑
Destination = 'D:\TEST\B' + ' '

#路徑變數(方便維護所以先將路徑組合成一個變數)
Path = Source + Destination

#定義參數
#鏡像複製
#注意：此指令會先清除目的地資料夾的資料
#Mirrors_Copy = '/mir'

#遞迴複製(含空資料夾)
#說明：此指令也會複製子資料夾
#Recursive_Mode = '/e'

#多線城複製設定(此指令適用於Win7以上)
#Multi_threaded_set = '/mt:100'

os.system('robocopy '+  Source + Destination + '/mir /mt:100')
