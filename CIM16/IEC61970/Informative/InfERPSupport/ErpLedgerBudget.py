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

class ErpLedgerBudget(Document):
    """Information for utility Ledger Budgets. They support the transfer budget amounts between all possible source applications throughout an enterprise and a general ledger or budget application.Information for utility Ledger Budgets. They support the transfer budget amounts between all possible source applications throughout an enterprise and a general ledger or budget application.
    """

    def __init__(self, ErpLedBudLineItems=None, *args, **kw_args):
        """Initialises a new 'ErpLedgerBudget' instance.

        @param ErpLedBudLineItems:
        """
        self._ErpLedBudLineItems = []
        self.ErpLedBudLineItems = [] if ErpLedBudLineItems is None else ErpLedBudLineItems

        super(ErpLedgerBudget, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpLedBudLineItems"]
    _many_refs = ["ErpLedBudLineItems"]

    def getErpLedBudLineItems(self):
        
        return self._ErpLedBudLineItems

    def setErpLedBudLineItems(self, value):
        for x in self._ErpLedBudLineItems:
            x.ErpLedgerBudget = None
        for y in value:
            y._ErpLedgerBudget = self
        self._ErpLedBudLineItems = value

    ErpLedBudLineItems = property(getErpLedBudLineItems, setErpLedBudLineItems)

    def addErpLedBudLineItems(self, *ErpLedBudLineItems):
        for obj in ErpLedBudLineItems:
            obj.ErpLedgerBudget = self

    def removeErpLedBudLineItems(self, *ErpLedBudLineItems):
        for obj in ErpLedBudLineItems:
            obj.ErpLedgerBudget = None

