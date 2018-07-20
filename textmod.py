import theStrings as istr

# Text Mode 介面
def tui():
    sourcePath = input(istr.textmod_sourcePath)
    targetPath = input(istr.textmod_targetPath)
    print(istr.textmod_recheck.format(sP=sourcePath, tP=targetPath))
    if input(istr.gen_input) == "A":
        exit()
    return (sourcePath, targetPath)