
import json
from urllib import request
import time

import pprint

import re

def main():
  text="女性アイドルグループとしては珍しく長い下積みを経て、2007年から2008年にかけてブレイク。以降も長く人気を保つ女性アイドルグループである。独特の音楽性やダンス、舞台演出等に特徴がある。"
  result=make_furigana(text,grade=3)
  pprint.pprint(result)

def make_furigana(text,grade):
  # print(text,grade)

  str_json = get_json(text,grade)

  obj=json.loads(str_json)
  words=obj["result"]["word"]
  parts=[]
  for word in words:
    if "furigana" in word:
      temp=furigana_just(word["surface"], word["furigana"])
      parts.append(temp)
    else:
      parts.append(word["surface"])
  sentence="".join(parts)
  return sentence

def furigana_just(surface,furigana):
  # 長い（ながい）となるので 長（なが）い にする。
  ms=re.search(r"([^ぁ-ん]+)([ぁ-ん]*)$",surface)
  temps=ms.groups()
  mae=temps[0]
  ato=temps[1]
  kana_ato=re.sub(ato+"$","",furigana)
  result= mae+"（"+kana_ato+"）"+ato
  return result


def get_json(text,grade):
  URL = "https://jlp.yahooapis.jp/FuriganaService/V2/furigana"
  appid="dj00aiZpPW9mUXI0NFRYZktLMCZzPWNvbnN1bWVyc2VjcmV0Jng9YTA-"
  headers = {
    "Content-Type": "application/json",
    "User-Agent": f"Yahoo AppID: {appid}",
  }
  param_dic = {
    "id": int(time.time()%1000*1000),
    "jsonrpc" : "2.0",
    "method" : "jlp.furiganaservice.furigana",
    "params" : {
      "q" : text,
      "grade" : grade
    }
  }
  params = json.dumps(param_dic).encode()
  req = request.Request(URL, params, headers)
  with request.urlopen(req) as res:
    body = res.read()
  return body.decode()

if __name__ == "__main__":
  main()
