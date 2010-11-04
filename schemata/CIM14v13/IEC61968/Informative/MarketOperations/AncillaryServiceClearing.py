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

class AncillaryServiceClearing(MarketFactors):
    """Ancillary services clearing results are posted for a given settlement period.
    """

    def __init__(self, clearedMW=0.0, mcp=0.0, commodityType='', MarketCaseClearing=None, *args, **kw_args):
        """Initializes a new 'AncillaryServiceClearing' instance.

        @param clearedMW: Cleared MWs. 
        @param mcp: Market clearing price (MCP) in monetary units. 
        @param commodityType: Requirement type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve 
        @param MarketCaseClearing:
        """
        #: Cleared MWs.
        self.clearedMW = clearedMW

        #: Market clearing price (MCP) in monetary units.
        self.mcp = mcp

        #: Requirement type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve
        self.commodityType = commodityType

        self._MarketCaseClearing = None
        self.MarketCaseClearing = MarketCaseClearing

        super(AncillaryServiceClearing, self).__init__(*args, **kw_args)

    def getMarketCaseClearing(self):
        
        return self._MarketCaseClearing

    def setMarketCaseClearing(self, value):
        if self._MarketCaseClearing is not None:
            filtered = [x for x in self.MarketCaseClearing.AncillaryServiceClearing if x != self]
            self._MarketCaseClearing._AncillaryServiceClearing = filtered

        self._MarketCaseClearing = value
        if self._MarketCaseClearing is not None:
            self._MarketCaseClearing._AncillaryServiceClearing.append(self)

    MarketCaseClearing = property(getMarketCaseClearing, setMarketCaseClearing)

