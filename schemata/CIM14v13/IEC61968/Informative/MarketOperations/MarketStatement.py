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

from CIM14v13.IEC61968.Common.Document import Document

class MarketStatement(Document):
    """A statement is a roll up of statement line items. Each statement along with its line items provide the details of specific charges at any given time.
    """

    def __init__(self, tradeDate='', referenceNumber='', start='', end='', transactionDate='', MarketStatementLineItem=None, **kw_args):
        """Initializes a new 'MarketStatement' instance.

        @param tradeDate: The date of which Settlement is run. 
        @param referenceNumber: The version number of previous statement (in the case of true up). 
        @param start: The start of a bill period. 
        @param end: The end of a bill period. 
        @param transactionDate: The date of which this statement is issued. 
        @param MarketStatementLineItem:
        """
        #: The date of which Settlement is run.
        self.tradeDate = tradeDate

        #: The version number of previous statement (in the case of true up).
        self.referenceNumber = referenceNumber

        #: The start of a bill period.
        self.start = start

        #: The end of a bill period.
        self.end = end

        #: The date of which this statement is issued.
        self.transactionDate = transactionDate

        self._MarketStatementLineItem = []
        self.MarketStatementLineItem = [] if MarketStatementLineItem is None else MarketStatementLineItem

        super(MarketStatement, self).__init__(**kw_args)

    def getMarketStatementLineItem(self):
        
        return self._MarketStatementLineItem

    def setMarketStatementLineItem(self, value):
        for x in self._MarketStatementLineItem:
            x._MarketStatement = None
        for y in value:
            y._MarketStatement = self
        self._MarketStatementLineItem = value

    MarketStatementLineItem = property(getMarketStatementLineItem, setMarketStatementLineItem)

    def addMarketStatementLineItem(self, *MarketStatementLineItem):
        for obj in MarketStatementLineItem:
            obj._MarketStatement = self
            self._MarketStatementLineItem.append(obj)

    def removeMarketStatementLineItem(self, *MarketStatementLineItem):
        for obj in MarketStatementLineItem:
            obj._MarketStatement = None
            self._MarketStatementLineItem.remove(obj)

