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

class ErpLedger(Document):
    """In accounting transactions, a ledger is a book containing accounts to which debits and credits are posted from journals, where transactions are initially recorded. Journal entries are periodically posted to the ledger. Ledger Actual represents actual amounts by account within ledger within company or business area. Actual amounts may be generated in a source application and then loaded to a specific ledger within the enterprise general ledger or budget application.
    """

    def __init__(self, ErpLedgerEntries=None, **kw_args):
        """Initializes a new 'ErpLedger' instance.

        @param ErpLedgerEntries:
        """
        self._ErpLedgerEntries = []
        self.ErpLedgerEntries = [] if ErpLedgerEntries is None else ErpLedgerEntries

        super(ErpLedger, self).__init__(**kw_args)

    def getErpLedgerEntries(self):
        
        return self._ErpLedgerEntries

    def setErpLedgerEntries(self, value):
        for x in self._ErpLedgerEntries:
            x._ErpLedger = None
        for y in value:
            y._ErpLedger = self
        self._ErpLedgerEntries = value

    ErpLedgerEntries = property(getErpLedgerEntries, setErpLedgerEntries)

    def addErpLedgerEntries(self, *ErpLedgerEntries):
        for obj in ErpLedgerEntries:
            obj._ErpLedger = self
            self._ErpLedgerEntries.append(obj)

    def removeErpLedgerEntries(self, *ErpLedgerEntries):
        for obj in ErpLedgerEntries:
            obj._ErpLedger = None
            self._ErpLedgerEntries.remove(obj)

