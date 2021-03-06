#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 SWIPO Project
#
# Authors (this file):
#   Stefan Schinkel <stefan.schinkel@gmail.com>
"""
Weave tests to check that python and weave implementations give the same
results
"""

from pyunicorn import ResNetwork


res = ResNetwork.SmallTestNetwork()
resC = ResNetwork.SmallComplexNetwork()


def testVCFB():
    for i in range(5):
        vcfbPython = res._vertex_current_flow_betweenness_python(i)
        vcfbWeave = res._vertex_current_flow_betweenness_weave(i)
        assert vcfbPython == vcfbWeave


def testECFB():
    ecfbPython = res._edge_current_flow_betweenness_python()
    ecfbWeave = res._edge_current_flow_betweenness_weave()
    l = len(ecfbPython)
    for i in range(l):
        for j in range(l):
            assert ecfbPython[i][j] == ecfbWeave[i][j]
