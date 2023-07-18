# -*- coding: utf-8 -*-
# Time       : 2022/5/22 10:43
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict
from urllib.parse import urlparse

from clashbyte.scheme.hysteria import Hysteria


@dataclass
class Toolkit:
    @staticmethod
    def parse_hysteria_sharelink(links: List[str] | str) -> Dict[str, Hysteria | None]:
        if isinstance(links, str):
            links = [links]
        response = {}
        for link in links:
            u = urlparse(link)
            if u and u.scheme == "hysteria":
                hysteria = Hysteria.from_sharelink(u)
                response[link] = hysteria
            else:
                response[link] = None
        return response
