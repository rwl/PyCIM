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

class ErpJournal(Document):
    """Book for recording accounting transactions as they occur. Transactions and adjustments are first recorded in a journal, which is like a diary of instructions, advising which account to be charged and by how much. A journal represents a change in the balances of a business's financial accounts. Many tasks or transactions throughout an enterprise will result in the creation of a journal. Some examples are creating a customer invoice, paying a vendor, transferring inventory, or paying employees.
    """

    def __init__(self, ErpJournalEntries=None, *args, **kw_args):
        """Initializes a new 'ErpJournal' instance.

        @param ErpJournalEntries:
        """
        self._ErpJournalEntries = []
        self.ErpJournalEntries = [] if ErpJournalEntries is None else ErpJournalEntries

        super(ErpJournal, self).__init__(*args, **kw_args)

    def getErpJournalEntries(self):
        
        return self._ErpJournalEntries

    def setErpJournalEntries(self, value):
        for x in self._ErpJournalEntries:
            x._ErpJournal = None
        for y in value:
            y._ErpJournal = self
        self._ErpJournalEntries = value

    ErpJournalEntries = property(getErpJournalEntries, setErpJournalEntries)

    def addErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            obj._ErpJournal = self
            self._ErpJournalEntries.append(obj)

    def removeErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            obj._ErpJournal = None
            self._ErpJournalEntries.remove(obj)

