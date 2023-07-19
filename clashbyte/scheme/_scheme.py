# -*- coding: utf-8 -*-
# Time       : 2023/7/18 17:26
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any
from urllib.parse import ParseResult

path_clash_config = Path(__file__).parent.joinpath("_default.yaml")


@dataclass
class Scheme(ABC):
    @classmethod
    @abstractmethod
    def from_urlparser(cls, parser: ParseResult):
        ...

    @abstractmethod
    def to_sharelink(self) -> str:
        ...

    @abstractmethod
    def to_clash_node(self, **kwargs) -> Dict[str, Any]:
        ...
