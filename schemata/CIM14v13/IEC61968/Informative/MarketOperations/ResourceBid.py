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

from CIM14v13.IEC61968.Informative.MarketOperations.Bid import Bid

class ResourceBid(Bid):
    """Energy bid for generation, load, or virtual type for the whole of the market-trading period (i.e., one day in day ahead market or one hour in the real time market)
    """

    def __init__(self, startUpsMaxDay=0, energyMinDay=0.0, energyMaxDay=0.0, virtual=False, startUpsMaxWeek=0, commodityType='', shutDownsMaxWeek=0, shutDownsMaxDay=0, **kw_args):
        """Initializes a new 'ResourceBid' instance.

        @param startUpsMaxDay: Maximum number of startups per day. 
        @param energyMinDay: Minimum amount of energy per day which has to be produced during the trading period in MWh 
        @param energyMaxDay: Maximum amount of energy per day which can be produced during the trading period in MWh 
        @param virtual: True if bid is virtual.  Bid is assumed to be non-virtual if attribute is absent 
        @param startUpsMaxWeek: Maximum number of startups per week. 
        @param commodityType: Energy product (commodity) type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve 
        @param shutDownsMaxWeek: Maximum number of shutdowns per week. 
        @param shutDownsMaxDay: Maximum number of shutdowns per day. 
        """
        #: Maximum number of startups per day.
        self.startUpsMaxDay = startUpsMaxDay

        #: Minimum amount of energy per day which has to be produced during the trading period in MWh
        self.energyMinDay = energyMinDay

        #: Maximum amount of energy per day which can be produced during the trading period in MWh
        self.energyMaxDay = energyMaxDay

        #: True if bid is virtual.  Bid is assumed to be non-virtual if attribute is absent
        self.virtual = virtual

        #: Maximum number of startups per week.
        self.startUpsMaxWeek = startUpsMaxWeek

        #: Energy product (commodity) type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve
        self.commodityType = commodityType

        #: Maximum number of shutdowns per week.
        self.shutDownsMaxWeek = shutDownsMaxWeek

        #: Maximum number of shutdowns per day.
        self.shutDownsMaxDay = shutDownsMaxDay

        super(ResourceBid, self).__init__(**kw_args)

