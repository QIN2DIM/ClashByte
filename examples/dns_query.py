# -*- coding: utf-8 -*-
# Time       : 2023/8/9 14:20
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import json
import os
from pathlib import Path

from clashbyte.apis import ClashMetaAPI

# Fill in your Clash.Meta's external control field
os.environ["CLASH_URL"] = "http://127.0.0.1:9090"
os.environ["CLASH_SECRET"] = ""

answers = Path("dns_answers")
answers.mkdir(exist_ok=True, parents=True)

for query_domain in [
    "www.baidu.com",
    "www.bilibili.com",
    "github.com",
    "zh.wikipedia.org"
]:
    sp = answers.joinpath(f"{query_domain}.json")
    result = ClashMetaAPI().dns_query(name=query_domain, dns_type="A")
    sp.write_text(json.dumps(result, indent=4))
