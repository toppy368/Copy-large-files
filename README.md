# Copy Large File for Windows / macOS / Linux
## 說明 Description
這是個可以大量複製檔案的程式，利用 Python 製作出的小程式。
簡單來說，這個 Python 檔案可以節省您輸入 `robocopy` 或 `rsync`
指令的困擾，在 Windows 環境下可以複製資料夾，在 Linux 環境可以複製
檔案以及資料夾，讓大檔案與目錄的備份更加簡單。

## 特點 Features
- 自動判斷是否需要進行 Recursive (是否為目錄)。
- 自動偵測是否為 Windows 或 macOS / Linux 環境，<br />
  Windows 使用 robocopy、macOS / Linux 使用 rsync。

## 準備 Prepare
1. 安裝 Python。Linux 通常各發行版本已經內建，macOS / Windows 需要至 [Python 官方網站](https://www.python.org) 下載最新版本的 Python。
2. python 安裝完成後，請下載本專案，可透過Git工具Clone下來，如果使用瀏覽器訪問本頁，可以點選 `Clone or download` 下載本專案的 zip 檔。
3. 下載好之後，將zip解壓縮，執行此資料夾的 recopy_exe.py 即可。

## 使用 Using
提供了三種方法，讓這個程式更活用。
**Windows 不支援複製檔案，僅可複製資料夾！**

### 參數
Usage: `recopy_exe.py [原始檔案 / 資料夾位置] [目標檔案 / 資料夾位置]`<br />
如果是包含特殊符號或包含空格，請用 `""` 雙引號包住。

### JSON
如果不指定參數，recopy_exe.py 會自動從 config.json 取得來源與目標路徑。

在 sourcePath 填入來源路徑、targetPath 填入目標路徑，效果等同於從參數中輸入路徑。

若要重設 json，只須把 config.json 刪除，程式將會自動建立。

### 文字介面
當參數未輸入、JSON 未設定或是不存在，則使用 TUI 介面。
照著畫面上的指示操作即可。

### 開啟並使用
1. 如果是 Windows，請開啟命令提示字元之後輸入：(開啟方法：搜尋與執行 (Win-R) cmd.exe)
   ```
   python recopy_exe.py (參數)
   ```
2. 如果是 macOS / Linux，請開啟終端器之後輸入：
   ```
   python3 recopy_exe.py (參數)
   ```

## 文件 Documents
- [MSDN robocopy](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Robocopy Wikipedia](https://en.wikipedia.org/wiki/Robocopy)
- [Rsync Man Manual](https://linux.die.net/man/1/rsync)
- [Rsync Wikipedia](https://zh.wikipedia.org/wiki/Rsync)
