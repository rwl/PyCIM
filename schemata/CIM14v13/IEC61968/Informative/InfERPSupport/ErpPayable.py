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

class ErpPayable(Document):
    """A transaction that represents an invoice from a supplier. A payable (or voucher) is an open item, approved and ready for payment, in the Accounts Payable ledger.
    """

    def __init__(self, ContractorItems=None, ErpPayableLineItems=None, *args, **kw_args):
        """Initializes a new 'ErpPayable' instance.

        @param ContractorItems:
        @param ErpPayableLineItems:
        """
        self._ContractorItems = []
        self.ContractorItems = [] if ContractorItems is None else ContractorItems

        self._ErpPayableLineItems = []
        self.ErpPayableLineItems = [] if ErpPayableLineItems is None else ErpPayableLineItems

        super(ErpPayable, self).__init__(*args, **kw_args)

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
            x._ErpPayable = None
        for y in value:
            y._ErpPayable = self
        self._ErpPayableLineItems = value

    ErpPayableLineItems = property(getErpPayableLineItems, setErpPayableLineItems)

    def addErpPayableLineItems(self, *ErpPayableLineItems):
        for obj in ErpPayableLineItems:
            obj._ErpPayable = self
            self._ErpPayableLineItems.append(obj)

    def removeErpPayableLineItems(self, *ErpPayableLineItems):
        for obj in ErpPayableLineItems:
            obj._ErpPayable = None
            self._ErpPayableLineItems.remove(obj)

