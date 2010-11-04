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

class ErpReceivable(Document):
    """Transaction representing an invoice, credit memo or debit memo to a customer. It is an open (unpaid) item in the Accounts Receivable ledger.
    """

    def __init__(self, ErpRecLineItems=None, **kw_args):
        """Initializes a new 'ErpReceivable' instance.

        @param ErpRecLineItems:
        """
        self._ErpRecLineItems = []
        self.ErpRecLineItems = [] if ErpRecLineItems is None else ErpRecLineItems

        super(ErpReceivable, self).__init__(**kw_args)

    def getErpRecLineItems(self):
        
        return self._ErpRecLineItems

    def setErpRecLineItems(self, value):
        for x in self._ErpRecLineItems:
            x._ErpReceivable = None
        for y in value:
            y._ErpReceivable = self
        self._ErpRecLineItems = value

    ErpRecLineItems = property(getErpRecLineItems, setErpRecLineItems)

    def addErpRecLineItems(self, *ErpRecLineItems):
        for obj in ErpRecLineItems:
            obj._ErpReceivable = self
            self._ErpRecLineItems.append(obj)

    def removeErpRecLineItems(self, *ErpRecLineItems):
        for obj in ErpRecLineItems:
            obj._ErpReceivable = None
            self._ErpRecLineItems.remove(obj)

