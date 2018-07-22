# textmod.py 的字串
textmod_sourcePath = "輸入來源位置："
textmod_targetPath = "輸入目標位置："
textmod_recheck = """請再次確認是否輸入正確。

來源位置：{sP}
目標位置：{tP}

如果輸入錯誤，輸入 A 關閉程式之後重新開啟輸入。
如果輸入正確，直接按下 Enter 即可。
"""

# getjson.py 的字串
jsonContent = """{
	"//": "自動填入 recopy_exe.py，適合給固定不變的複製。",
	"//": "sourcePath：設定來源位置，引號內請填入想複製的來源，請勿移除雙引號。",
	"sourcePath": "",
	"//": "targetPath：設定目標位置，引號內請填入複製目標的路徑，請勿移除雙引號",
	"targetPath": ""
}"""

# 主函式字串
main_recheck = """開始時間：{h} 時 {m} 分 {s} 秒
來源位置：{source}
目標位置：{target}

若沒有問題，請直接輸入 Enter
若有問題，請輸入 A 後重新開啟程式。"""

# 通用字串 general strings
gen_input = "請輸入："

# 通用錯誤字串
generr_module = "Can't run as module!"