import theStrings as i18n
import os
import json
import sys

'''
回傳 dict：正常運作。
回傳 250：兩值中一值為空
回傳 255：檔案不存在
'''

# 讀取 config.json 的內容
def jsonReader(config):
    try:
        if os.path.exists(config):
            jsonInit = os.open(config, os.O_RDONLY)
            jsonRaw = str(os.read(jsonInit, 4096), encoding="UTF-8")
            jsonContent = json.loads(jsonRaw)
            jsonContent.pop('//')
            if jsonContent.get("sourcePath") == "" or jsonContent.get("targetPath") == "":
                return 250
            return (jsonContent.get("sourcePath"), jsonContent.get("targetPath"))
        else:
            initJson = os.open(config, os.O_WRONLY|os.O_CREAT)
            os.write(initJson, bytes(i18n.jsonContent, encoding="UTF-8"))
            os.close(initJson)
            return 255
    except:
        raise Exception(i18n.err_bugreport.format(sys.exc_info()))