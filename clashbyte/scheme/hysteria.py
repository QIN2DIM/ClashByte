# -*- coding: utf-8 -*-
# Time       : 2023/7/18 16:45
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal
from urllib.parse import ParseResult

from clashbyte.scheme._scheme import Scheme
from clashbyte.utils import from_dict_to_cls


@dataclass
class Hysteria(Scheme):
    # hostname or IP address of the server to connect to (required)
    host: str

    # port of the server to connect to (required)
    port: int

    # upstream bandwidth in Mbps (required)
    upmbps: int

    # downstream bandwidth in Mbps (required)
    downmbps: int

    # multiport skip (optional)
    mport: str = ""

    # protocol to use ("udp", "wechat-video", "faketcp") (optional, default: "udp")
    protocol: Literal["udp", "wechat-video", "faketcp"] = "udp"

    # authentication payload (string) (optional)
    auth: str = ""

    # SNI for TLS (optional)
    peer: str = ""

    # insecure: ignore certificate errors (optional)
    insecure: str = ""

    # QUIC ALPN (optional)
    alpn: str = "h3"

    # Obfuscation mode (optional, empty or "xplus")
    obfs: Literal["", "xplus"] = ""

    # Obfuscation password (optional)
    obfsParam: str = ""

    # remarks alias (optional)
    remarks: str = ""

    @classmethod
    def from_urlparser(cls, parser: ParseResult):
        """
        从节点分享链接反序列化节点对象

        https://hysteria.network/zh/docs/uri-scheme/

        :param parser: Hysteria URL Scheme Parser
        :return:
        """
        host, port = parser.netloc.split(":")
        data = {"host": host, "port": port, "remarks": parser.fragment}
        for e in parser.query.split("&"):
            k, v = e.split("=")
            data[k] = v
        return from_dict_to_cls(cls, data)

    def to_sharelink(self) -> str:
        t = "hysteria://{netloc}?{query}#{fragment}"
        netloc = f"{self.host}:{self.port}"
        queries = []
        for k in self.__dict__:
            if not self.__dict__[k]:
                continue
            v = self.__dict__[k]
            queries.append(f"{k}={v}")
        query = "&".join(queries)
        fragment = self.remarks
        sharelink = t.format(netloc=netloc, query=query, fragment=fragment)
        return sharelink

    def to_clash_node(self, **kwargs):
        self.remarks = self.remarks or self.host
        node = {
            "name": self.remarks,
            "type": "hysteria",
            "server": self.host,
            "port": self.port,
            "ports": self.mport,
            "alpn": [self.alpn],
            "protocol": self.protocol,
            "up": self.upmbps,
            "down": self.downmbps,
            "sni": self.peer,
            "skip-cert-verify": self.insecure,
            "auth_str": self.auth,
            "obfs": self.obfsParam,  # auto fill
        }
        if kwargs:
            node.update(**kwargs)
        return node
