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

from CIM14v13.IEC61970.Core.Curve import Curve

class LoadReductionPriceCurve(Curve):
    """This is the price sensitivity that bidder expresses for allowing market load interruption.  Relationship between price (Y1-axis) vs. MW (X-axis).
    """

    def __init__(self, LoadBids=None, *args, **kw_args):
        """Initializes a new 'LoadReductionPriceCurve' instance.

        @param LoadBids:
        """
        self._LoadBids = []
        self.LoadBids = [] if LoadBids is None else LoadBids

        super(LoadReductionPriceCurve, self).__init__(*args, **kw_args)

    def getLoadBids(self):
        
        return self._LoadBids

    def setLoadBids(self, value):
        for x in self._LoadBids:
            x._LoadReductionPriceCurve = None
        for y in value:
            y._LoadReductionPriceCurve = self
        self._LoadBids = value

    LoadBids = property(getLoadBids, setLoadBids)

    def addLoadBids(self, *LoadBids):
        for obj in LoadBids:
            obj._LoadReductionPriceCurve = self
            self._LoadBids.append(obj)

    def removeLoadBids(self, *LoadBids):
        for obj in LoadBids:
            obj._LoadReductionPriceCurve = None
            self._LoadBids.remove(obj)

