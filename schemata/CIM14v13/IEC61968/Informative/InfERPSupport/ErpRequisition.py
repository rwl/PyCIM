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

class ErpRequisition(Document):
    """General information that applies to a utility requisition that is a request for the purchase of goods or services. Typically, a requisition leads to the creation of a purchase order to a specific supplier.
    """

    def __init__(self, ErpReqLineItems=None, *args, **kw_args):
        """Initializes a new 'ErpRequisition' instance.

        @param ErpReqLineItems:
        """
        self._ErpReqLineItems = []
        self.ErpReqLineItems = [] if ErpReqLineItems is None else ErpReqLineItems

        super(ErpRequisition, self).__init__(*args, **kw_args)

    def getErpReqLineItems(self):
        
        return self._ErpReqLineItems

    def setErpReqLineItems(self, value):
        for x in self._ErpReqLineItems:
            x._ErpRequisition = None
        for y in value:
            y._ErpRequisition = self
        self._ErpReqLineItems = value

    ErpReqLineItems = property(getErpReqLineItems, setErpReqLineItems)

    def addErpReqLineItems(self, *ErpReqLineItems):
        for obj in ErpReqLineItems:
            obj._ErpRequisition = self
            self._ErpReqLineItems.append(obj)

    def removeErpReqLineItems(self, *ErpReqLineItems):
        for obj in ErpReqLineItems:
            obj._ErpRequisition = None
            self._ErpReqLineItems.remove(obj)

