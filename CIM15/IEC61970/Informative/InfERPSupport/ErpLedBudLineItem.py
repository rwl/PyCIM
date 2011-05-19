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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ErpLedBudLineItem(IdentifiedObject):
    """Individual entry of a given Ledger Budget, typically containing information such as amount, accounting date, accounting period, and is associated with the applicable general ledger account.Individual entry of a given Ledger Budget, typically containing information such as amount, accounting date, accounting period, and is associated with the applicable general ledger account.
    """

    def __init__(self, ErpLedBudLineItem=None, ErpLedgerBudget=None, status=None, *args, **kw_args):
        """Initialises a new 'ErpLedBudLineItem' instance.

        @param ErpLedBudLineItem:
        @param ErpLedgerBudget:
        @param status:
        """
        self._ErpLedBudLineItem = None
        self.ErpLedBudLineItem = ErpLedBudLineItem

        self._ErpLedgerBudget = None
        self.ErpLedgerBudget = ErpLedgerBudget

        self.status = status

        super(ErpLedBudLineItem, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpLedBudLineItem", "ErpLedgerBudget", "status"]
    _many_refs = []

    def getErpLedBudLineItem(self):
        
        return self._ErpLedBudLineItem

    def setErpLedBudLineItem(self, value):
        if self._ErpLedBudLineItem is not None:
            self._ErpLedBudLineItem._ErpLedgerEntry = None

        self._ErpLedBudLineItem = value
        if self._ErpLedBudLineItem is not None:
            self._ErpLedBudLineItem.ErpLedgerEntry = None
            self._ErpLedBudLineItem._ErpLedgerEntry = self

    ErpLedBudLineItem = property(getErpLedBudLineItem, setErpLedBudLineItem)

    def getErpLedgerBudget(self):
        
        return self._ErpLedgerBudget

    def setErpLedgerBudget(self, value):
        if self._ErpLedgerBudget is not None:
            filtered = [x for x in self.ErpLedgerBudget.ErpLedBudLineItems if x != self]
            self._ErpLedgerBudget._ErpLedBudLineItems = filtered

        self._ErpLedgerBudget = value
        if self._ErpLedgerBudget is not None:
            if self not in self._ErpLedgerBudget._ErpLedBudLineItems:
                self._ErpLedgerBudget._ErpLedBudLineItems.append(self)

    ErpLedgerBudget = property(getErpLedgerBudget, setErpLedgerBudget)

    status = None

