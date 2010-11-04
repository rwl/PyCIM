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

class ErpLedgerBudget(Document):
    """Information for utility Ledger Budgets. They support the transfer budget amounts between all possible source applications throughout an enterprise and a general ledger or budget application.
    """

    def __init__(self, ErpLedBudLineItems=None, **kw_args):
        """Initializes a new 'ErpLedgerBudget' instance.

        @param ErpLedBudLineItems:
        """
        self._ErpLedBudLineItems = []
        self.ErpLedBudLineItems = [] if ErpLedBudLineItems is None else ErpLedBudLineItems

        super(ErpLedgerBudget, self).__init__(**kw_args)

    def getErpLedBudLineItems(self):
        
        return self._ErpLedBudLineItems

    def setErpLedBudLineItems(self, value):
        for x in self._ErpLedBudLineItems:
            x._ErpLedgerBudget = None
        for y in value:
            y._ErpLedgerBudget = self
        self._ErpLedBudLineItems = value

    ErpLedBudLineItems = property(getErpLedBudLineItems, setErpLedBudLineItems)

    def addErpLedBudLineItems(self, *ErpLedBudLineItems):
        for obj in ErpLedBudLineItems:
            obj._ErpLedgerBudget = self
            self._ErpLedBudLineItems.append(obj)

    def removeErpLedBudLineItems(self, *ErpLedBudLineItems):
        for obj in ErpLedBudLineItems:
            obj._ErpLedgerBudget = None
            self._ErpLedBudLineItems.remove(obj)

