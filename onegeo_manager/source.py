# Copyright (c) 2017-2018 Neogeo-Technologies.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from abc import ABCMeta
from abc import abstractmethod
from importlib import import_module
import inspect
import os.path
from re import search


__all__ = ['Source']


class AbstractSource(metaclass=ABCMeta):

    def __init__(self, uri, name):

        self.protocol = os.path.basename(
            inspect.getmodule(inspect.stack()[1][0]).__file__[:-3])
        self.uri = uri

        s = search('^[a-z0-9_]{2,100}$', name)
        if not s:
            raise ValueError("Malformed value for 'name'.")
        self.name = name

    @abstractmethod
    def get_resources(self, *args, **kwargs):
        raise NotImplementedError(
            "This is an abstract method. You can't do anything with it.")

    @abstractmethod
    def get_collection(self, *args, **kwargs):
        raise NotImplementedError(
            "This is an abstract method. You can't do anything with it.")


class Source(object):

    def __new__(self, uri, name, protocol, **kwargs):

        ext = import_module(
            'onegeo_manager.protocol.{0}'.format(protocol), __name__)

        self = object.__new__(ext.Source)
        self.__init__(uri, name, **kwargs)
        return self
