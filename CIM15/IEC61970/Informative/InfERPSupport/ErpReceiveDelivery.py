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

class ErpReceiveDelivery(Document):
    """Transaction for an Organisation receiving goods or services that may be used to indicate receipt of goods in conjunction with a purchase order. A receivable is an open (unpaid) item in the Accounts Receivable ledger.Transaction for an Organisation receiving goods or services that may be used to indicate receipt of goods in conjunction with a purchase order. A receivable is an open (unpaid) item in the Accounts Receivable ledger.
    """

    def __init__(self, ErpRecDelvLineItems=None, *args, **kw_args):
        """Initialises a new 'ErpReceiveDelivery' instance.

        @param ErpRecDelvLineItems:
        """
        self._ErpRecDelvLineItems = []
        self.ErpRecDelvLineItems = [] if ErpRecDelvLineItems is None else ErpRecDelvLineItems

        super(ErpReceiveDelivery, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpRecDelvLineItems"]
    _many_refs = ["ErpRecDelvLineItems"]

    def getErpRecDelvLineItems(self):
        
        return self._ErpRecDelvLineItems

    def setErpRecDelvLineItems(self, value):
        for x in self._ErpRecDelvLineItems:
            x.ErpReceiveDelivery = None
        for y in value:
            y._ErpReceiveDelivery = self
        self._ErpRecDelvLineItems = value

    ErpRecDelvLineItems = property(getErpRecDelvLineItems, setErpRecDelvLineItems)

    def addErpRecDelvLineItems(self, *ErpRecDelvLineItems):
        for obj in ErpRecDelvLineItems:
            obj.ErpReceiveDelivery = self

    def removeErpRecDelvLineItems(self, *ErpRecDelvLineItems):
        for obj in ErpRecDelvLineItems:
            obj.ErpReceiveDelivery = None

