from pypinyin  import pinyin, Style

def getFirsLetter(province):
    py =pinyin(province, style=Style.FIRST_LETTER)
    name=''
    for p  in py:
        name += p[0]
    return name