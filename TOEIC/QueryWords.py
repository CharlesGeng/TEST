import http.client
import os
from bs4 import BeautifulSoup


def QueryWord(word: str):
    conn = http.client.HTTPSConnection("dictionary.cambridge.org")
    conn.request(
        "GET", "/dictionary/english-chinese-simplified/" + word.replace(" ", "-")
    )
    res = conn.getresponse()
    original_html = ""
    while not res.closed:
        b = res.read(1000)
        # 忽略解码错误
        data = b.decode("utf-8", errors="ignore")
        if len(data) == 0:
            break
        original_html = original_html + data

    soup = BeautifulSoup(original_html, "html.parser")

    # 根据HTML元素的class名称获取解释块
    meanings = soup.select(".def-block.ddef_block")
    i = 0
    glossary = ''
    while i < len(meanings):
        l = word+':'
        # 英语解释
        en_glossary = meanings[i].select(".def.ddef_d.db")
        l = l + "\t" + en_glossary[0].get_text()
        # 中文解释
        cn_glossary = meanings[i].select(".trans.dtrans.dtrans-se.break-cj")
        l = l + "." + cn_glossary[0].get_text()
        # 例句
        for translation in meanings[i].select(".examp.dexamp"):
            l = l + '\n    ' + translation.get_text().replace("\n", "")
        glossary = glossary + l + '\n'
        i += 1
    return glossary


word = "word"
while len(word) > 0:
    word = input()
    glossary = QueryWord(word)
    print(glossary)