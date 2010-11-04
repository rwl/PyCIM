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

class BilateralTransaction(Element):
    """Bilateral transaction
    """

    def __init__(self, scope='', curtailTimeMax=0, curtailTimeMin=0, marketType='', purchaseTimeMin=0, purchaseTimeMax=0, totalTranChargeMax=0.0, transactionType='', **kw_args):
        """Initializes a new 'BilateralTransaction' instance.

        @param scope: Transaction scope: 'Internal' 'External' 
        @param curtailTimeMax: Maximum curtailment time in number of trading intervals 
        @param curtailTimeMin: Minimum curtailment time in number of trading intervals 
        @param marketType: Market type (default=DA) DA - Day Ahead RT - Real Time HA - Hour Ahead 
        @param purchaseTimeMin: Minimum purchase time in number of trading intervals 
        @param purchaseTimeMax: Maximum purchase time in number of trading intervals 
        @param totalTranChargeMax: Maximum total transmission (congestion) charges in monetary units 
        @param transactionType: Transaction type (default 1)  1 - Fixed  2 - Dispatchable continuous  3 - Dispatchable block-loading 
        """
        #: Transaction scope: 'Internal' 'External'
        self.scope = scope

        #: Maximum curtailment time in number of trading intervals
        self.curtailTimeMax = curtailTimeMax

        #: Minimum curtailment time in number of trading intervals
        self.curtailTimeMin = curtailTimeMin

        #: Market type (default=DA) DA - Day Ahead RT - Real Time HA - Hour Ahead
        self.marketType = marketType

        #: Minimum purchase time in number of trading intervals
        self.purchaseTimeMin = purchaseTimeMin

        #: Maximum purchase time in number of trading intervals
        self.purchaseTimeMax = purchaseTimeMax

        #: Maximum total transmission (congestion) charges in monetary units
        self.totalTranChargeMax = totalTranChargeMax

        #: Transaction type (default 1)  1 - Fixed  2 - Dispatchable continuous  3 - Dispatchable block-loading
        self.transactionType = transactionType

        super(BilateralTransaction, self).__init__(**kw_args)

