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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ErpLedBudLineItem(IdentifiedObject):
    """Individual entry of a given Ledger Budget, typically containing information such as amount, accounting date, accounting period, and is associated with the applicable general ledger account.
    """

    def __init__(self, ErpLedgerBudget=None, ErpLedBudLineItem=None, status=None, **kw_args):
        """Initializes a new 'ErpLedBudLineItem' instance.

        @param ErpLedgerBudget:
        @param ErpLedBudLineItem:
        @param status:
        """
        self._ErpLedgerBudget = None
        self.ErpLedgerBudget = ErpLedgerBudget

        self._ErpLedBudLineItem = None
        self.ErpLedBudLineItem = ErpLedBudLineItem

        self.status = status

        super(ErpLedBudLineItem, self).__init__(**kw_args)

    def getErpLedgerBudget(self):
        
        return self._ErpLedgerBudget

    def setErpLedgerBudget(self, value):
        if self._ErpLedgerBudget is not None:
            filtered = [x for x in self.ErpLedgerBudget.ErpLedBudLineItems if x != self]
            self._ErpLedgerBudget._ErpLedBudLineItems = filtered

        self._ErpLedgerBudget = value
        if self._ErpLedgerBudget is not None:
            self._ErpLedgerBudget._ErpLedBudLineItems.append(self)

    ErpLedgerBudget = property(getErpLedgerBudget, setErpLedgerBudget)

    def getErpLedBudLineItem(self):
        
        return self._ErpLedBudLineItem

    def setErpLedBudLineItem(self, value):
        if self._ErpLedBudLineItem is not None:
            self._ErpLedBudLineItem._ErpLedgerEntry = None

        self._ErpLedBudLineItem = value
        if self._ErpLedBudLineItem is not None:
            self._ErpLedBudLineItem._ErpLedgerEntry = self

    ErpLedBudLineItem = property(getErpLedBudLineItem, setErpLedBudLineItem)

    status = None

