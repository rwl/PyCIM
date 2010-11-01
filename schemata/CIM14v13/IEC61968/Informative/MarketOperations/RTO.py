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

from CIM14v13.IEC61968.Informative.InfERPSupport.ErpOrganisation import ErpOrganisation

class RTO(ErpOrganisation):
    """Regional transmission operator.
    """

    def __init__(self, Pnodes=None, SecurityConstraints=None, SecurityConstraintsLinear=None, ResourceGroupReqs=None, Markets=None, *args, **kw_args):
        """Initializes a new 'RTO' instance.

        @param Pnodes:
        @param SecurityConstraints:
        @param SecurityConstraintsLinear:
        @param ResourceGroupReqs:
        @param Markets:
        """
        self._Pnodes = []
        self.Pnodes = [] if Pnodes is None else Pnodes

        self._SecurityConstraints = []
        self.SecurityConstraints = [] if SecurityConstraints is None else SecurityConstraints

        self._SecurityConstraintsLinear = []
        self.SecurityConstraintsLinear = [] if SecurityConstraintsLinear is None else SecurityConstraintsLinear

        self._ResourceGroupReqs = []
        self.ResourceGroupReqs = [] if ResourceGroupReqs is None else ResourceGroupReqs

        self._Markets = []
        self.Markets = [] if Markets is None else Markets

        super(RTO, self).__init__(*args, **kw_args)

    def getPnodes(self):
        
        return self._Pnodes

    def setPnodes(self, value):
        for x in self._Pnodes:
            x._RTO = None
        for y in value:
            y._RTO = self
        self._Pnodes = value

    Pnodes = property(getPnodes, setPnodes)

    def addPnodes(self, *Pnodes):
        for obj in Pnodes:
            obj._RTO = self
            self._Pnodes.append(obj)

    def removePnodes(self, *Pnodes):
        for obj in Pnodes:
            obj._RTO = None
            self._Pnodes.remove(obj)

    def getSecurityConstraints(self):
        
        return self._SecurityConstraints

    def setSecurityConstraints(self, value):
        for x in self._SecurityConstraints:
            x._RTO = None
        for y in value:
            y._RTO = self
        self._SecurityConstraints = value

    SecurityConstraints = property(getSecurityConstraints, setSecurityConstraints)

    def addSecurityConstraints(self, *SecurityConstraints):
        for obj in SecurityConstraints:
            obj._RTO = self
            self._SecurityConstraints.append(obj)

    def removeSecurityConstraints(self, *SecurityConstraints):
        for obj in SecurityConstraints:
            obj._RTO = None
            self._SecurityConstraints.remove(obj)

    def getSecurityConstraintsLinear(self):
        
        return self._SecurityConstraintsLinear

    def setSecurityConstraintsLinear(self, value):
        for x in self._SecurityConstraintsLinear:
            x._RTO = None
        for y in value:
            y._RTO = self
        self._SecurityConstraintsLinear = value

    SecurityConstraintsLinear = property(getSecurityConstraintsLinear, setSecurityConstraintsLinear)

    def addSecurityConstraintsLinear(self, *SecurityConstraintsLinear):
        for obj in SecurityConstraintsLinear:
            obj._RTO = self
            self._SecurityConstraintsLinear.append(obj)

    def removeSecurityConstraintsLinear(self, *SecurityConstraintsLinear):
        for obj in SecurityConstraintsLinear:
            obj._RTO = None
            self._SecurityConstraintsLinear.remove(obj)

    def getResourceGroupReqs(self):
        
        return self._ResourceGroupReqs

    def setResourceGroupReqs(self, value):
        for p in self._ResourceGroupReqs:
            filtered = [q for q in p.RTOs if q != self]
            self._ResourceGroupReqs._RTOs = filtered
        for r in value:
            if self not in r._RTOs:
                r._RTOs.append(self)
        self._ResourceGroupReqs = value

    ResourceGroupReqs = property(getResourceGroupReqs, setResourceGroupReqs)

    def addResourceGroupReqs(self, *ResourceGroupReqs):
        for obj in ResourceGroupReqs:
            if self not in obj._RTOs:
                obj._RTOs.append(self)
            self._ResourceGroupReqs.append(obj)

    def removeResourceGroupReqs(self, *ResourceGroupReqs):
        for obj in ResourceGroupReqs:
            if self in obj._RTOs:
                obj._RTOs.remove(self)
            self._ResourceGroupReqs.remove(obj)

    def getMarkets(self):
        
        return self._Markets

    def setMarkets(self, value):
        for x in self._Markets:
            x._RTO = None
        for y in value:
            y._RTO = self
        self._Markets = value

    Markets = property(getMarkets, setMarkets)

    def addMarkets(self, *Markets):
        for obj in Markets:
            obj._RTO = self
            self._Markets.append(obj)

    def removeMarkets(self, *Markets):
        for obj in Markets:
            obj._RTO = None
            self._Markets.remove(obj)

