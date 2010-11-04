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

from CIM14v13.Element import Element

class BidClearing(Element):
    """Bid clearing results posted for a given settlement period.
    """

    def __init__(self, noLoadCost=0.0, startUpCost=0.0, lostOpCost=0.0, Bid=None, **kw_args):
        """Initializes a new 'BidClearing' instance.

        @param noLoadCost: No-load cost in monetary units. 
        @param startUpCost: Start up cost in case of energy commodity in monetary units. 
        @param lostOpCost: Energy lost opportunity cost in monetary units. 
        @param Bid:
        """
        #: No-load cost in monetary units.
        self.noLoadCost = noLoadCost

        #: Start up cost in case of energy commodity in monetary units.
        self.startUpCost = startUpCost

        #: Energy lost opportunity cost in monetary units.
        self.lostOpCost = lostOpCost

        self._Bid = None
        self.Bid = Bid

        super(BidClearing, self).__init__(**kw_args)

    def getBid(self):
        
        return self._Bid

    def setBid(self, value):
        if self._Bid is not None:
            self._Bid._BidClearing = None

        self._Bid = value
        if self._Bid is not None:
            self._Bid._BidClearing = self

    Bid = property(getBid, setBid)

