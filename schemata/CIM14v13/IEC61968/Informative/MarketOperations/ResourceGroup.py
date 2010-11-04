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

class ResourceGroup(IdentifiedObject):
    """A logical grouping of resources that are used to model location of types of requirements for ancillary services such as spinning reserve zones, regulation zones, etc.
    """

    def __init__(self, RegisteredResources=None, ResourceGroupReqs=None, **kw_args):
        """Initializes a new 'ResourceGroup' instance.

        @param RegisteredResources:
        @param ResourceGroupReqs:
        """
        self._RegisteredResources = []
        self.RegisteredResources = [] if RegisteredResources is None else RegisteredResources

        self._ResourceGroupReqs = []
        self.ResourceGroupReqs = [] if ResourceGroupReqs is None else ResourceGroupReqs

        super(ResourceGroup, self).__init__(**kw_args)

    def getRegisteredResources(self):
        
        return self._RegisteredResources

    def setRegisteredResources(self, value):
        for p in self._RegisteredResources:
            filtered = [q for q in p.ResourceGroups if q != self]
            self._RegisteredResources._ResourceGroups = filtered
        for r in value:
            if self not in r._ResourceGroups:
                r._ResourceGroups.append(self)
        self._RegisteredResources = value

    RegisteredResources = property(getRegisteredResources, setRegisteredResources)

    def addRegisteredResources(self, *RegisteredResources):
        for obj in RegisteredResources:
            if self not in obj._ResourceGroups:
                obj._ResourceGroups.append(self)
            self._RegisteredResources.append(obj)

    def removeRegisteredResources(self, *RegisteredResources):
        for obj in RegisteredResources:
            if self in obj._ResourceGroups:
                obj._ResourceGroups.remove(self)
            self._RegisteredResources.remove(obj)

    def getResourceGroupReqs(self):
        
        return self._ResourceGroupReqs

    def setResourceGroupReqs(self, value):
        for x in self._ResourceGroupReqs:
            x._ResourceGroup = None
        for y in value:
            y._ResourceGroup = self
        self._ResourceGroupReqs = value

    ResourceGroupReqs = property(getResourceGroupReqs, setResourceGroupReqs)

    def addResourceGroupReqs(self, *ResourceGroupReqs):
        for obj in ResourceGroupReqs:
            obj._ResourceGroup = self
            self._ResourceGroupReqs.append(obj)

    def removeResourceGroupReqs(self, *ResourceGroupReqs):
        for obj in ResourceGroupReqs:
            obj._ResourceGroup = None
            self._ResourceGroupReqs.remove(obj)

