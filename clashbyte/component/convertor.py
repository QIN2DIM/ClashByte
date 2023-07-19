# -*- coding: utf-8 -*-
# Time       : 2022/5/22 10:43
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from __future__ import annotations

import os
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import List
from urllib.parse import urlparse

import yaml

from clashbyte.scheme import Hysteria
from clashbyte.scheme import Scheme
from clashbyte.scheme import Tuic
from scheme import path_clash_config


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

    @staticmethod
    def gen_clash_config_from_links(links: str | List[str], sp: Path | str | None = None):
        if isinstance(links, str):
            links = links.split("\n")
        proxies = [Toolkit.from_link_to_scheme(link) for link in links]
        proxies = [p.to_clash_node() for p in proxies if p]
        proxy_groups = [
            {"name": "PROXY", "type": "select", "proxies": [p["name"] for p in proxies]}
        ]

        if sp is None:
            sp = Path("clash_configs")
        elif isinstance(sp, str):
            sp = Path(sp)
        os.makedirs(sp, exist_ok=True)

        t = yaml.safe_load(path_clash_config.read_text(encoding="utf8"))
        t.update({"proxies": proxies, "proxy-groups": proxy_groups})
        fn = "runtime.yaml"
        fp = sp.joinpath(fn)
        if fp.exists():
            shutil.move(fp, sp.joinpath(f"{int(fp.stat().st_mtime)}.yaml"))
        Path(fn).write_text(yaml.safe_dump(t, allow_unicode=True, sort_keys=False))
        shutil.copy(fn, fp)

        return t
