inport json

config = 
	{
		"//":"sourcePath左邊為來源位置，引號內請填入要複製的來源，請勿移除雙引號",
		"sourcePath":"",
		"//":"targetPath右邊為目標位置，引號內請填入複製目標的路徑，請勿移除雙引號",
		"targetPath":"",
		"//":"OS Type需要使用者判斷自己的作業系統，如果是Windows請填W、MacOS請填M、Linux無論是Ubuntu或其他發行版都填L，讓程式識別模式",
		"OS Type":"W"
	}

print json.dumps()