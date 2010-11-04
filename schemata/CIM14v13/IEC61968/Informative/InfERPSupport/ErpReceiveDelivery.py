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

class ErpReceiveDelivery(Document):
    """Transaction for an Organisation receiving goods or services that may be used to indicate receipt of goods in conjunction with a purchase order. A receivable is an open (unpaid) item in the Accounts Receivable ledger.
    """

    def __init__(self, ErpRecDelvLineItems=None, **kw_args):
        """Initializes a new 'ErpReceiveDelivery' instance.

        @param ErpRecDelvLineItems:
        """
        self._ErpRecDelvLineItems = []
        self.ErpRecDelvLineItems = [] if ErpRecDelvLineItems is None else ErpRecDelvLineItems

        super(ErpReceiveDelivery, self).__init__(**kw_args)

    def getErpRecDelvLineItems(self):
        
        return self._ErpRecDelvLineItems

    def setErpRecDelvLineItems(self, value):
        for x in self._ErpRecDelvLineItems:
            x._ErpReceiveDelivery = None
        for y in value:
            y._ErpReceiveDelivery = self
        self._ErpRecDelvLineItems = value

    ErpRecDelvLineItems = property(getErpRecDelvLineItems, setErpRecDelvLineItems)

    def addErpRecDelvLineItems(self, *ErpRecDelvLineItems):
        for obj in ErpRecDelvLineItems:
            obj._ErpReceiveDelivery = self
            self._ErpRecDelvLineItems.append(obj)

    def removeErpRecDelvLineItems(self, *ErpRecDelvLineItems):
        for obj in ErpRecDelvLineItems:
            obj._ErpReceiveDelivery = None
            self._ErpRecDelvLineItems.remove(obj)

