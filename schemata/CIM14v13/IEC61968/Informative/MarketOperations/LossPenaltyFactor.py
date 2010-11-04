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

from CIM14v13.IEC61968.Informative.MarketOperations.MarketFactors import MarketFactors

class LossPenaltyFactor(MarketFactors):
    """Loss penalty factor applied to a ConnectivityNode for a given time interval.
    """

    def __init__(self, lossFactor=None, ConnectivityNodes=None, **kw_args):
        """Initializes a new 'LossPenaltyFactor' instance.

        @param lossFactor: Loss penalty factor. 
        @param ConnectivityNodes:
        """
        #: Loss penalty factor.
        self.lossFactor = lossFactor

        self._ConnectivityNodes = []
        self.ConnectivityNodes = [] if ConnectivityNodes is None else ConnectivityNodes

        super(LossPenaltyFactor, self).__init__(**kw_args)

    def getConnectivityNodes(self):
        
        return self._ConnectivityNodes

    def setConnectivityNodes(self, value):
        for p in self._ConnectivityNodes:
            filtered = [q for q in p.LossPenaltyFactors if q != self]
            self._ConnectivityNodes._LossPenaltyFactors = filtered
        for r in value:
            if self not in r._LossPenaltyFactors:
                r._LossPenaltyFactors.append(self)
        self._ConnectivityNodes = value

    ConnectivityNodes = property(getConnectivityNodes, setConnectivityNodes)

    def addConnectivityNodes(self, *ConnectivityNodes):
        for obj in ConnectivityNodes:
            if self not in obj._LossPenaltyFactors:
                obj._LossPenaltyFactors.append(self)
            self._ConnectivityNodes.append(obj)

    def removeConnectivityNodes(self, *ConnectivityNodes):
        for obj in ConnectivityNodes:
            if self in obj._LossPenaltyFactors:
                obj._LossPenaltyFactors.remove(self)
            self._ConnectivityNodes.remove(obj)

