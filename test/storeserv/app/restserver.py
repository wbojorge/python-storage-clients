#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   (C) Copyright 2017-2019 Hewlett Packard Enterprise Development LP
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

"""
.. module:: test.storeserv
    :synopsis: Flask server for testing hpestorapi.StoreServ

.. moduleauthor:: Ivan Smirnov <ivan.smirnov@hpe.com>, HPE Pointnext DACH & Russia
"""


from flask import Flask
from flask_restful import Api
from resources.credentials import Credentials
from resources.hosts import Hosts
from resources.system import System


class ApiInstance:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(Credentials,
                              '/api/v1/credentials',
                              '/api/v1/credentials/<string:key>')
        self.api.add_resource(System,
                              '/api/v1/system')
        self.api.add_resource(Hosts,
                              '/api/v1/hosts')

    def run(self):
        self.app.run(debug=False, host='0.0.0.0', port=8008)


if __name__ == "__main__":
    server = ApiInstance()
    server.run()
