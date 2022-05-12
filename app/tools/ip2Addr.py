# -*- coding: utf-8 -*-
import os
from app.tools.ip2Region import Ip2Region


def ip2addr(ip):
    ipdb_path = os.path.join(
        os.path.dirname(
            os.path.dirname(
                __file__
            )
        ), "static/ip2region/data/ip2region.db"
    )
    i2a = Ip2Region(ipdb_path)
    ipinfo = i2a.memorySearch(ip)
    return ipinfo
