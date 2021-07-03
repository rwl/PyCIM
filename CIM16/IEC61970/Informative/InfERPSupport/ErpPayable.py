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

class ErpPayable(Document):
    """A transaction that represents an invoice from a supplier. A payable (or voucher) is an open item, approved and ready for payment, in the Accounts Payable ledger.A transaction that represents an invoice from a supplier. A payable (or voucher) is an open item, approved and ready for payment, in the Accounts Payable ledger.
    """

    def __init__(self, ContractorItems=None, ErpPayableLineItems=None, *args, **kw_args):
        """Initialises a new 'ErpPayable' instance.

        @param ContractorItems:
        @param ErpPayableLineItems:
        """
        self._ContractorItems = []
        self.ContractorItems = [] if ContractorItems is None else ContractorItems

        self._ErpPayableLineItems = []
        self.ErpPayableLineItems = [] if ErpPayableLineItems is None else ErpPayableLineItems

        super(ErpPayable, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ContractorItems", "ErpPayableLineItems"]
    _many_refs = ["ContractorItems", "ErpPayableLineItems"]

    def getContractorItems(self):
        
        return self._ContractorItems

    def setContractorItems(self, value):
        for p in self._ContractorItems:
            filtered = [q for q in p.ErpPayables if q != self]
            self._ContractorItems._ErpPayables = filtered
        for r in value:
            if self not in r._ErpPayables:
                r._ErpPayables.append(self)
        self._ContractorItems = value

    ContractorItems = property(getContractorItems, setContractorItems)

    def addContractorItems(self, *ContractorItems):
        for obj in ContractorItems:
            if self not in obj._ErpPayables:
                obj._ErpPayables.append(self)
            self._ContractorItems.append(obj)

    def removeContractorItems(self, *ContractorItems):
        for obj in ContractorItems:
            if self in obj._ErpPayables:
                obj._ErpPayables.remove(self)
            self._ContractorItems.remove(obj)

    def getErpPayableLineItems(self):
        
        return self._ErpPayableLineItems

    def setErpPayableLineItems(self, value):
        for x in self._ErpPayableLineItems:
            x.ErpPayable = None
        for y in value:
            y._ErpPayable = self
        self._ErpPayableLineItems = value

    ErpPayableLineItems = property(getErpPayableLineItems, setErpPayableLineItems)

    def addErpPayableLineItems(self, *ErpPayableLineItems):
        for obj in ErpPayableLineItems:
            obj.ErpPayable = self

    def removeErpPayableLineItems(self, *ErpPayableLineItems):
        for obj in ErpPayableLineItems:
            obj.ErpPayable = None

