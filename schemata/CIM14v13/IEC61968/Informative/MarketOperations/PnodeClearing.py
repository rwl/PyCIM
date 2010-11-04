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

class PnodeClearing(MarketFactors):
    """Pricing node clearing results posted for a given settlement period.
    """

    def __init__(self, congestLMP=0.0, lossLMP=0.0, costLMP=0.0, Pnode=None, **kw_args):
        """Initializes a new 'PnodeClearing' instance.

        @param congestLMP: Congestion component of Location Marginal Price (LMP) in monetary units per MW. 
        @param lossLMP: Loss component of Location Marginal Price (LMP) in monetary units per MW. 
        @param costLMP: Cost component of Locational Marginal Pricing (LMP) in monetary units per MW. 
        @param Pnode:
        """
        #: Congestion component of Location Marginal Price (LMP) in monetary units per MW.
        self.congestLMP = congestLMP

        #: Loss component of Location Marginal Price (LMP) in monetary units per MW.
        self.lossLMP = lossLMP

        #: Cost component of Locational Marginal Pricing (LMP) in monetary units per MW.
        self.costLMP = costLMP

        self._Pnode = None
        self.Pnode = Pnode

        super(PnodeClearing, self).__init__(**kw_args)

    def getPnode(self):
        
        return self._Pnode

    def setPnode(self, value):
        if self._Pnode is not None:
            self._Pnode._PnodeClearing = None

        self._Pnode = value
        if self._Pnode is not None:
            self._Pnode._PnodeClearing = self

    Pnode = property(getPnode, setPnode)

