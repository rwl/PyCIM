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

class ErpLedger(Document):
    """In accounting transactions, a ledger is a book containing accounts to which debits and credits are posted from journals, where transactions are initially recorded. Journal entries are periodically posted to the ledger. Ledger Actual represents actual amounts by account within ledger within company or business area. Actual amounts may be generated in a source application and then loaded to a specific ledger within the enterprise general ledger or budget application.In accounting transactions, a ledger is a book containing accounts to which debits and credits are posted from journals, where transactions are initially recorded. Journal entries are periodically posted to the ledger. Ledger Actual represents actual amounts by account within ledger within company or business area. Actual amounts may be generated in a source application and then loaded to a specific ledger within the enterprise general ledger or budget application.
    """

    def __init__(self, ErpLedgerEntries=None, *args, **kw_args):
        """Initialises a new 'ErpLedger' instance.

        @param ErpLedgerEntries:
        """
        self._ErpLedgerEntries = []
        self.ErpLedgerEntries = [] if ErpLedgerEntries is None else ErpLedgerEntries

        super(ErpLedger, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpLedgerEntries"]
    _many_refs = ["ErpLedgerEntries"]

    def getErpLedgerEntries(self):
        
        return self._ErpLedgerEntries

    def setErpLedgerEntries(self, value):
        for x in self._ErpLedgerEntries:
            x.ErpLedger = None
        for y in value:
            y._ErpLedger = self
        self._ErpLedgerEntries = value

    ErpLedgerEntries = property(getErpLedgerEntries, setErpLedgerEntries)

    def addErpLedgerEntries(self, *ErpLedgerEntries):
        for obj in ErpLedgerEntries:
            obj.ErpLedger = self

    def removeErpLedgerEntries(self, *ErpLedgerEntries):
        for obj in ErpLedgerEntries:
            obj.ErpLedger = None

