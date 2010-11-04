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

class RegisteredResource(IdentifiedObject):
    """A resource that is registered through the RTO participant registration system. Examples include generating unit, customer meter, and a non-physical generator or load.
    """

    def __init__(self, rtoID='', Meters=None, Markets=None, ResourceGroups=None, MarketProducts=None, Pnode=None, Organisation=None, **kw_args):
        """Initializes a new 'RegisteredResource' instance.

        @param rtoID: Unique name obtained via RTO registration 
        @param Meters:
        @param Markets:
        @param ResourceGroups:
        @param MarketProducts: A registered resource is eligible to bid market products
        @param Pnode: A registered resource injects power at one or more connectivity nodes related to a pnode
        @param Organisation:
        """
        #: Unique name obtained via RTO registration
        self.rtoID = rtoID

        self._Meters = []
        self.Meters = [] if Meters is None else Meters

        self._Markets = []
        self.Markets = [] if Markets is None else Markets

        self._ResourceGroups = []
        self.ResourceGroups = [] if ResourceGroups is None else ResourceGroups

        self._MarketProducts = []
        self.MarketProducts = [] if MarketProducts is None else MarketProducts

        self._Pnode = None
        self.Pnode = Pnode

        self._Organisation = None
        self.Organisation = Organisation

        super(RegisteredResource, self).__init__(**kw_args)

    def getMeters(self):
        
        return self._Meters

    def setMeters(self, value):
        for x in self._Meters:
            x._RegisteredResource = None
        for y in value:
            y._RegisteredResource = self
        self._Meters = value

    Meters = property(getMeters, setMeters)

    def addMeters(self, *Meters):
        for obj in Meters:
            obj._RegisteredResource = self
            self._Meters.append(obj)

    def removeMeters(self, *Meters):
        for obj in Meters:
            obj._RegisteredResource = None
            self._Meters.remove(obj)

    def getMarkets(self):
        
        return self._Markets

    def setMarkets(self, value):
        for p in self._Markets:
            filtered = [q for q in p.RegisteredResources if q != self]
            self._Markets._RegisteredResources = filtered
        for r in value:
            if self not in r._RegisteredResources:
                r._RegisteredResources.append(self)
        self._Markets = value

    Markets = property(getMarkets, setMarkets)

    def addMarkets(self, *Markets):
        for obj in Markets:
            if self not in obj._RegisteredResources:
                obj._RegisteredResources.append(self)
            self._Markets.append(obj)

    def removeMarkets(self, *Markets):
        for obj in Markets:
            if self in obj._RegisteredResources:
                obj._RegisteredResources.remove(self)
            self._Markets.remove(obj)

    def getResourceGroups(self):
        
        return self._ResourceGroups

    def setResourceGroups(self, value):
        for p in self._ResourceGroups:
            filtered = [q for q in p.RegisteredResources if q != self]
            self._ResourceGroups._RegisteredResources = filtered
        for r in value:
            if self not in r._RegisteredResources:
                r._RegisteredResources.append(self)
        self._ResourceGroups = value

    ResourceGroups = property(getResourceGroups, setResourceGroups)

    def addResourceGroups(self, *ResourceGroups):
        for obj in ResourceGroups:
            if self not in obj._RegisteredResources:
                obj._RegisteredResources.append(self)
            self._ResourceGroups.append(obj)

    def removeResourceGroups(self, *ResourceGroups):
        for obj in ResourceGroups:
            if self in obj._RegisteredResources:
                obj._RegisteredResources.remove(self)
            self._ResourceGroups.remove(obj)

    def getMarketProducts(self):
        """A registered resource is eligible to bid market products
        """
        return self._MarketProducts

    def setMarketProducts(self, value):
        for p in self._MarketProducts:
            filtered = [q for q in p.RegisteredResources if q != self]
            self._MarketProducts._RegisteredResources = filtered
        for r in value:
            if self not in r._RegisteredResources:
                r._RegisteredResources.append(self)
        self._MarketProducts = value

    MarketProducts = property(getMarketProducts, setMarketProducts)

    def addMarketProducts(self, *MarketProducts):
        for obj in MarketProducts:
            if self not in obj._RegisteredResources:
                obj._RegisteredResources.append(self)
            self._MarketProducts.append(obj)

    def removeMarketProducts(self, *MarketProducts):
        for obj in MarketProducts:
            if self in obj._RegisteredResources:
                obj._RegisteredResources.remove(self)
            self._MarketProducts.remove(obj)

    def getPnode(self):
        """A registered resource injects power at one or more connectivity nodes related to a pnode
        """
        return self._Pnode

    def setPnode(self, value):
        if self._Pnode is not None:
            filtered = [x for x in self.Pnode.RegisteredResources if x != self]
            self._Pnode._RegisteredResources = filtered

        self._Pnode = value
        if self._Pnode is not None:
            self._Pnode._RegisteredResources.append(self)

    Pnode = property(getPnode, setPnode)

    def getOrganisation(self):
        
        return self._Organisation

    def setOrganisation(self, value):
        if self._Organisation is not None:
            filtered = [x for x in self.Organisation.RegisteredResources if x != self]
            self._Organisation._RegisteredResources = filtered

        self._Organisation = value
        if self._Organisation is not None:
            self._Organisation._RegisteredResources.append(self)

    Organisation = property(getOrganisation, setOrganisation)

