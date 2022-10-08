#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json

from py2neo import neo4j


class Gremlin(neo4j.Resource):

    def __init__(self, graph_db):
        ext = graph_db.__metadata__["extensions"]
        if "GremlinPlugin" not in ext:
            raise NotImplementedError("Gremlin plugin not available")
        self._resources = dict(
            (name, neo4j.Resource(uri))
            for name, uri in ext["GremlinPlugin"].items()
        )
        
    def execute_script(self, script):
        rs = self._resources["execute_script"]._post({"script": script})
        return neo4j._hydrated(rs.content)

