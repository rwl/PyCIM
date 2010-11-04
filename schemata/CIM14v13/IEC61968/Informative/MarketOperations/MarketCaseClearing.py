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

class MarketCaseClearing(MarketFactors):
    """Market case clearing results are posted for a given settlement period.
    """

    def __init__(self, modifiedDate='', postedDate='', caseType='', AncillaryServiceClearing=None, *args, **kw_args):
        """Initializes a new 'MarketCaseClearing' instance.

        @param modifiedDate: Last time and date clearing results were manually modified. 
        @param postedDate: Bid clearing results posted time and date. 
        @param caseType: Settlement period:  'DA - Bid-in'  'DA - Reliability'  'DA - Amp1'  'DA - Amp2'  'RT - Ex-Ante'  'RT - Ex-Post'  'RT - Amp1'  'RT - Amp2' 
        @param AncillaryServiceClearing:
        """
        #: Last time and date clearing results were manually modified.
        self.modifiedDate = modifiedDate

        #: Bid clearing results posted time and date.
        self.postedDate = postedDate

        #: Settlement period:  'DA - Bid-in'  'DA - Reliability'  'DA - Amp1'  'DA - Amp2'  'RT - Ex-Ante'  'RT - Ex-Post'  'RT - Amp1'  'RT - Amp2'
        self.caseType = caseType

        self._AncillaryServiceClearing = []
        self.AncillaryServiceClearing = [] if AncillaryServiceClearing is None else AncillaryServiceClearing

        super(MarketCaseClearing, self).__init__(*args, **kw_args)

    def getAncillaryServiceClearing(self):
        
        return self._AncillaryServiceClearing

    def setAncillaryServiceClearing(self, value):
        for x in self._AncillaryServiceClearing:
            x._MarketCaseClearing = None
        for y in value:
            y._MarketCaseClearing = self
        self._AncillaryServiceClearing = value

    AncillaryServiceClearing = property(getAncillaryServiceClearing, setAncillaryServiceClearing)

    def addAncillaryServiceClearing(self, *AncillaryServiceClearing):
        for obj in AncillaryServiceClearing:
            obj._MarketCaseClearing = self
            self._AncillaryServiceClearing.append(obj)

    def removeAncillaryServiceClearing(self, *AncillaryServiceClearing):
        for obj in AncillaryServiceClearing:
            obj._MarketCaseClearing = None
            self._AncillaryServiceClearing.remove(obj)

