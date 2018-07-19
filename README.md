# Copy Large File for Windows / macOS / Linux
## 說明 Description
這是大量複製檔案的程式，使用python做成的小程式，
簡單來說這個python檔案可以直接對Windowws執行DOS指令robocopy，
做資料夾之間的複製，可以做資料夾的大量檔案複製，可以取代傳統的複製貼上功能(Ctrl + C、Ctrl+V)。

## 特點 Features
- 自動判斷是否需要進行 Recursive (是否為資料夾)。
- 自動偵測是否為 Windows 或 macOS / Linux 環境，<br />
  Windows 使用 robocopy、macOS / Linux 使用 rsync。

## 準備 Prepare
1. 安裝 Python。Linux 通常各發行版本已經內建，macOS / Windows 需要至 [Python 官方網站](https://www.python.org) 下載最新版本的 Python。
2. 安裝完成之後，下載 recopy_exe.py 即可。

## 使用 Using
### 參數
Usage: `recopy_exe.py [原始檔案 / 資料夾位置] [目標檔案 / 資料夾位置]`<br />
如果是包含特殊符號或包含空格，請用 `""` 雙引號包住。

### JSON
如果不指定參數，recopy_exe.py 會自動從 config.json 取得來源與目標路徑。

這是 config.json 的原始檔案，供隨時復原到原始狀態：

```
{
	"//": "自動填入 recopy_exe.py，適合給固定不變的複製。",
	"//": "sourcePath：設定來源位置，引號內請填入想複製的來源，請勿移除雙引號。",
	"sourcePath": "",
	"//": "targetPath：設定目標位置，引號內請填入複製目標的路徑，請勿移除雙引號",
	"targetPath": ""
}
```

在 sourcePath 填入來源路徑、targetPath 填入目標路徑，效果等同於從參數中輸入路徑。

### 開啟並使用
1. 如果是 Windows，請開啟命令提示字元之後輸入：
   ```
   python recopy_exe.py (參數)
   ```
2. 如果是 macOS / Linux，請開啟終端器之後輸入：
   ```
   python3 recopy_exe.py (參數)
   ```

# 文件 Documents
- [MSDN robocopy](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Robocopy Wikipedia](https://en.wikipedia.org/wiki/Robocopy)
- [Rsync Man Manual](https://linux.die.net/man/1/rsync)
- [Rsync Wikipedia](https://zh.wikipedia.org/wiki/Rsync)
