# -*- coding: utf-8 -*-
# Time       : 2023/7/18 16:43
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from __future__ import annotations

from dataclasses import dataclass

import pywebio
from pywebio.input import *
from pywebio.output import *

pywebio.config(theme="minty")


@dataclass
class Panel:
    TITLE = "云彩姬@订阅转换"

    def startup(self):
        """
        actions("\n", buttons=[
                {"label": "生成订阅链接", "value": "生成订阅链接", "color": "secondary"},
                {"label": "生成短链接", "value": "生成短链接", "color": "secondary"},
            ], name="action_link"),
        actions("\n", buttons=[
                {"label": "上传配置", "value": "上传配置", "color": "info"},
                {"label": "一键导入Clash", "value": "一键导入Clash", "color": "info"},
            ], name="action_inner")
        """
        toast("Just a demo", position="right", duration=3, color="##78c2ad")

        data = input_group(
            label=self.TITLE,
            inputs=[
                textarea(
                    label="订阅链接",
                    placeholder="支持 hysteria 链接，多个链接每行一个或用 | 分隔",
                    rows=4,
                    name="sharelink",
                ),
                select(label="客户端", options=["NekoRay", "Clash Verge"], name="client"),
                actions(
                    label="label",
                    buttons=[
                        {"label": "上传配置", "value": "上传配置", "color": "info"},
                        {"label": "一键导入 Clash", "value": "一键导入 Clash", "color": "info"},
                    ],
                    name="clash_config",
                ),
            ],
        )

        put_text(data)


if __name__ == "__main__":
    panel = Panel()
    panel.startup()
