# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61968.Informative.MarketOperations.RegisteredResource import RegisteredResource

class RegisteredLoad(RegisteredResource):

    def __init__(self, LoadArea=None, LoadBids=None, **kw_args):
        """Initializes a new 'RegisteredLoad' instance.

        @param LoadArea:
        @param LoadBids:
        """
        self._LoadArea = None
        self.LoadArea = LoadArea

        self._LoadBids = []
        self.LoadBids = [] if LoadBids is None else LoadBids

        super(RegisteredLoad, self).__init__(**kw_args)

    def getLoadArea(self):
        
        return self._LoadArea

    def setLoadArea(self, value):
        if self._LoadArea is not None:
            filtered = [x for x in self.LoadArea.RegisteredLoads if x != self]
            self._LoadArea._RegisteredLoads = filtered

        self._LoadArea = value
        if self._LoadArea is not None:
            self._LoadArea._RegisteredLoads.append(self)

    LoadArea = property(getLoadArea, setLoadArea)

    def getLoadBids(self):
        
        return self._LoadBids

    def setLoadBids(self, value):
        for x in self._LoadBids:
            x._RegisteredLoad = None
        for y in value:
            y._RegisteredLoad = self
        self._LoadBids = value

    LoadBids = property(getLoadBids, setLoadBids)

    def addLoadBids(self, *LoadBids):
        for obj in LoadBids:
            obj._RegisteredLoad = self
            self._LoadBids.append(obj)

    def removeLoadBids(self, *LoadBids):
        for obj in LoadBids:
            obj._RegisteredLoad = None
            self._LoadBids.remove(obj)

