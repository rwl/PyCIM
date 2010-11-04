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

class ErpQuote(Document):
    """Document describing the prices of goods or services provided by a supplier. It includes the terms of the purchase, delivery proposals, identification of goods or services ordered, as well as their quantities.
    """

    def __init__(self, ErpQuoteLineItems=None, **kw_args):
        """Initializes a new 'ErpQuote' instance.

        @param ErpQuoteLineItems:
        """
        self._ErpQuoteLineItems = []
        self.ErpQuoteLineItems = [] if ErpQuoteLineItems is None else ErpQuoteLineItems

        super(ErpQuote, self).__init__(**kw_args)

    def getErpQuoteLineItems(self):
        
        return self._ErpQuoteLineItems

    def setErpQuoteLineItems(self, value):
        for x in self._ErpQuoteLineItems:
            x._ErpQuote = None
        for y in value:
            y._ErpQuote = self
        self._ErpQuoteLineItems = value

    ErpQuoteLineItems = property(getErpQuoteLineItems, setErpQuoteLineItems)

    def addErpQuoteLineItems(self, *ErpQuoteLineItems):
        for obj in ErpQuoteLineItems:
            obj._ErpQuote = self
            self._ErpQuoteLineItems.append(obj)

    def removeErpQuoteLineItems(self, *ErpQuoteLineItems):
        for obj in ErpQuoteLineItems:
            obj._ErpQuote = None
            self._ErpQuoteLineItems.remove(obj)

