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

from CIM16.IEC61968.Common.Document import Document

class ErpReceivable(Document):
    """Transaction representing an invoice, credit memo or debit memo to a customer. It is an open (unpaid) item in the Accounts Receivable ledger.Transaction representing an invoice, credit memo or debit memo to a customer. It is an open (unpaid) item in the Accounts Receivable ledger.
    """

    def __init__(self, ErpRecLineItems=None, *args, **kw_args):
        """Initialises a new 'ErpReceivable' instance.

        @param ErpRecLineItems:
        """
        self._ErpRecLineItems = []
        self.ErpRecLineItems = [] if ErpRecLineItems is None else ErpRecLineItems

        super(ErpReceivable, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpRecLineItems"]
    _many_refs = ["ErpRecLineItems"]

    def getErpRecLineItems(self):
        
        return self._ErpRecLineItems

    def setErpRecLineItems(self, value):
        for x in self._ErpRecLineItems:
            x.ErpReceivable = None
        for y in value:
            y._ErpReceivable = self
        self._ErpRecLineItems = value

    ErpRecLineItems = property(getErpRecLineItems, setErpRecLineItems)

    def addErpRecLineItems(self, *ErpRecLineItems):
        for obj in ErpRecLineItems:
            obj.ErpReceivable = self

    def removeErpRecLineItems(self, *ErpRecLineItems):
        for obj in ErpRecLineItems:
            obj.ErpReceivable = None

