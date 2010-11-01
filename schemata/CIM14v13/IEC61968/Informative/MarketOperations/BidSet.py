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

class BidSet(IdentifiedObject):
    """As set of mutually exclusive bids for which a maximum of one may be scheduled. Of these generating bids, only one generating bid can be scheduled at a time.
    """

    def __init__(self, GeneratingBids=None, *args, **kw_args):
        """Initializes a new 'BidSet' instance.

        @param GeneratingBids:
        """
        self._GeneratingBids = []
        self.GeneratingBids = [] if GeneratingBids is None else GeneratingBids

        super(BidSet, self).__init__(*args, **kw_args)

    def getGeneratingBids(self):
        
        return self._GeneratingBids

    def setGeneratingBids(self, value):
        for x in self._GeneratingBids:
            x._BidSet = None
        for y in value:
            y._BidSet = self
        self._GeneratingBids = value

    GeneratingBids = property(getGeneratingBids, setGeneratingBids)

    def addGeneratingBids(self, *GeneratingBids):
        for obj in GeneratingBids:
            obj._BidSet = self
            self._GeneratingBids.append(obj)

    def removeGeneratingBids(self, *GeneratingBids):
        for obj in GeneratingBids:
            obj._BidSet = None
            self._GeneratingBids.remove(obj)

