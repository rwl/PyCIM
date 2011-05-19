# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61968.Common.Document import Document

class ErpQuote(Document):
    """Document describing the prices of goods or services provided by a supplier. It includes the terms of the purchase, delivery proposals, identification of goods or services ordered, as well as their quantities.Document describing the prices of goods or services provided by a supplier. It includes the terms of the purchase, delivery proposals, identification of goods or services ordered, as well as their quantities.
    """

    def __init__(self, ErpQuoteLineItems=None, *args, **kw_args):
        """Initialises a new 'ErpQuote' instance.

        @param ErpQuoteLineItems:
        """
        self._ErpQuoteLineItems = []
        self.ErpQuoteLineItems = [] if ErpQuoteLineItems is None else ErpQuoteLineItems

        super(ErpQuote, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpQuoteLineItems"]
    _many_refs = ["ErpQuoteLineItems"]

    def getErpQuoteLineItems(self):
        
        return self._ErpQuoteLineItems

    def setErpQuoteLineItems(self, value):
        for x in self._ErpQuoteLineItems:
            x.ErpQuote = None
        for y in value:
            y._ErpQuote = self
        self._ErpQuoteLineItems = value

    ErpQuoteLineItems = property(getErpQuoteLineItems, setErpQuoteLineItems)

    def addErpQuoteLineItems(self, *ErpQuoteLineItems):
        for obj in ErpQuoteLineItems:
            obj.ErpQuote = self

    def removeErpQuoteLineItems(self, *ErpQuoteLineItems):
        for obj in ErpQuoteLineItems:
            obj.ErpQuote = None

