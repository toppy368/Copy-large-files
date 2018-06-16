import os
#Hello world 指令
printf = "Notepad.exe"

#定義指令與主要路徑

#來源路徑，使用者請修改來源路徑，這是要同步的「來源」
Source = 'D:\TEST\A' + ' '
#目的地路徑，使用者請修改它，這是指定要複製的「目的地」
Destination = 'D:\TEST\B' + ' '

#路徑變數(方便維護所以先將路徑組合成一個變數)
Path = Source + Destination

#定義參數
#鏡像複製
#注意：此指令會先清除目的地資料夾的資料
Mirrors_Copy = 'robocopy '+ Path +'/mir /mt:100'

#遞迴複製(含空資料夾)
#說明：此指令也會複製子資料夾
Recursive_Mode = 'robocopy ' + Path + '/e /mt:100'


os.system('robocopy '+  Path + '/mir /mt:100')
