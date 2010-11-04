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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ResourceGroupReq(IdentifiedObject):
    """Ancillary service requirements for a market.
    """

    def __init__(self, ResourceGroup=None, RTOs=None, **kw_args):
        """Initializes a new 'ResourceGroupReq' instance.

        @param ResourceGroup:
        @param RTOs:
        """
        self._ResourceGroup = None
        self.ResourceGroup = ResourceGroup

        self._RTOs = []
        self.RTOs = [] if RTOs is None else RTOs

        super(ResourceGroupReq, self).__init__(**kw_args)

    def getResourceGroup(self):
        
        return self._ResourceGroup

    def setResourceGroup(self, value):
        if self._ResourceGroup is not None:
            filtered = [x for x in self.ResourceGroup.ResourceGroupReqs if x != self]
            self._ResourceGroup._ResourceGroupReqs = filtered

        self._ResourceGroup = value
        if self._ResourceGroup is not None:
            self._ResourceGroup._ResourceGroupReqs.append(self)

    ResourceGroup = property(getResourceGroup, setResourceGroup)

    def getRTOs(self):
        
        return self._RTOs

    def setRTOs(self, value):
        for p in self._RTOs:
            filtered = [q for q in p.ResourceGroupReqs if q != self]
            self._RTOs._ResourceGroupReqs = filtered
        for r in value:
            if self not in r._ResourceGroupReqs:
                r._ResourceGroupReqs.append(self)
        self._RTOs = value

    RTOs = property(getRTOs, setRTOs)

    def addRTOs(self, *RTOs):
        for obj in RTOs:
            if self not in obj._ResourceGroupReqs:
                obj._ResourceGroupReqs.append(self)
            self._RTOs.append(obj)

    def removeRTOs(self, *RTOs):
        for obj in RTOs:
            if self in obj._ResourceGroupReqs:
                obj._ResourceGroupReqs.remove(self)
            self._RTOs.remove(obj)

