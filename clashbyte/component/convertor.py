# -*- coding: utf-8 -*-
# Time       : 2022/5/22 10:43
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import urlparse

from clashbyte.scheme import Hysteria
from clashbyte.scheme import Scheme
from clashbyte.scheme import Tuic


@dataclass
class Toolkit:
    @staticmethod
    def from_link_to_scheme(link: str) -> Scheme | None:
        parser = urlparse(link)
        if not parser:
            return
        if parser.scheme == "hysteria":
            return Hysteria.from_urlparser(parser)
        if parser.scheme == "tuic":
            return Tuic.from_urlparser(parser)

    @staticmethod
    def from_clash_to_links():
        pass
