# -*- coding: utf-8 -*-

"""
pip install elasticsearch
"""

from elasticsearch import Elasticsearch

es = Elasticsearch(
    # ['192.168.10.10', '192.168.10.11', '192.168.10.12'],
    ['10.135.0.19:9200'],
    sniff_on_start=True,
    sniff_on_connection_fail=True,
    sniff_timeout=60
)






