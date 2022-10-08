#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2011-2013, Nigel Small
# Copyright 2011-2013, Fabian Yamaguchi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="py2neo-gremlin",
    version="0.1",
    description="Gremlin support for py2neo.",
    
    author= "Nigel Small, Fabian Yamaguchi",
    author_email="nigel@nigelsmall.com, fabs@goesec.de",
    
    install_requires = ["py2neo >= 1.6.1"],

    packages=[
        "py2neo_gremlin",
    ],
    license="Apache License 2.0",
)
