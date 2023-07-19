# -*- coding: utf-8 -*-
# Time       : 2023/7/18 16:47
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any
from urllib.parse import ParseResult

from clashbyte.scheme._scheme import Scheme


@dataclass
class Tuic(Scheme):
    @classmethod
    def from_urlparser(cls, parser: ParseResult):
        pass

    def to_sharelink(self) -> str:
        pass

    def to_clash_node(self, **kwargs) -> Dict[str, Any]:
        pass
