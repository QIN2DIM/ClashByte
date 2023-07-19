# -*- coding: utf-8 -*-
# Time       : 2023/7/7 3:10
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from __future__ import annotations

import os
import socket
from dataclasses import dataclass
from typing import Literal
from urllib.parse import urlparse

import httpx
from loguru import logger


@dataclass
class Clash:
    """https://dreamacro.github.io/clash/runtime/external-controller.html#restful-api-documentation"""


@dataclass
class ClashMetaAPI:
    """https://wiki.metacubex.one/api/"""

    secret: str = ""
    controller_url: str = ""

    _client = None

    def __post_init__(self):
        if not self.controller_url:
            self.controller_url = os.environ.get("CLASH_URL", "http://127.0.0.1:9090")
        if not self.secret:
            self.secret = os.environ.get("CLASH_SECRET", "")

        headers = {"Authorization": f"Bearer {self.secret}"}
        if not self.secret:
            logger.warning(
                "Please set your external secret key. \n"
                'python -c "import secrets;print(secrets.token_hex())"',
                documentation="https://wiki.metacubex.one/api/#_1",
            )
            del headers["Authorization"]
        self._client: httpx.Client = httpx.Client(base_url=self.controller_url, headers=headers)

    @property
    def is_alive(self):
        u = urlparse(self.controller_url)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                host, port = u.netloc.split(":")
                s.bind((host, int(port)))
                raise OSError
        except socket.gaierror:
            return False
        except OSError:
            return True

    @property
    def logs(self):
        return self._client.get("/logs").json()

    @property
    def traffic(self):
        return self._client.get("/traffic").json()

    @property
    def memory(self):
        return self._client.get("/memory").json()

    @property
    def version(self):
        return self._client.get("/version").json()

    @property
    def connections(self):
        return self._client.get("/connections").json()

    @property
    def configs(self):
        return self._client.get("/configs").json()

    @property
    def proxies(self):
        return self._client.get("/proxies").json()

    def put_configs(self):
        """https://wiki.metacubex.one/api/#configs"""
        return self._client.put("/configs?force=true")

    def patch_configs(self, new_config: dict):
        return self._client.patch("/configs", json=new_config)

    def restart(self):
        """重启内核"""
        return self._client.post("/restart").json()

    def upgrade(self):
        """更新内核"""
        return self._client.post("/upgrade")

    def flush_fakeip_cache(self):
        self._client.post("/cache/fakeip/flush")

    def get_proxy(self, name: str):
        return self._client.get(f"/proxies/:{name}").json()

    def select_proxy(self, name: str):
        return self._client.put(f"/proxies/:{name}").json()

    def get_proxy_delay(self, name: str):
        return self._client.get(f"/proxies/:{name}/delay").json()

    @property
    def rules(self):
        """获取规则信息"""
        return self._client.get("/rules").json()

    def drop_all_connections(self):
        """关闭所有连接"""
        return self._client.delete("/connections")

    def drop_connection(self, conn_id: str):
        """关闭特定连接"""
        return self._client.delete(f"/connections/:{conn_id}").json()

    @property
    def providers_proxies(self):
        return self._client.get("/providers/proxies").json()

    def get_provider_proxies(self, name: str):
        return self._client.get(f"/providers/proxies/:{name}").json()

    def put_provider_proxies(self, name: str):
        raise NotImplementedError

    def healthcheck_provider_proxies(self, name: str):
        return self._client.get(f"/providers/proxies/:{name}/healthcheck").json()

    @property
    def providers_rules(self):
        """获取所有规则集合的所有信息"""
        return self._client.get("/providers/rules").json()

    def upgrade_providers_rules(self, provider_name: str):
        """更新规则集合"""
        return self._client.get(f"/providers/rules/:{provider_name}").json()

    def dns_query(self, name: str, dns_type: Literal["A", "CNAME", "MX", "AAAA"] | None = ""):
        params = {"name": name, "type": dns_type}
        return self._client.get("/dns/query", params=params).json()

    def delete_connection(self, conn_id: str | None = ""):
        api = "/connections" if not conn_id else "/connections/:{conn_id}"
        return self._client.delete(api)
