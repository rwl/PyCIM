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

class ErpReqLineItem(IdentifiedObject):
    """Information that describes a requested item and its attributes.
    """

    def __init__(self, deliveryDate='', code='', quantity=0, cost=0.0, ErpRequisition=None, TypeMaterial=None, ErpPOLineItem=None, status=None, ErpQuoteLineItem=None, TypeAsset=None, **kw_args):
        """Initializes a new 'ErpReqLineItem' instance.

        @param deliveryDate: 
        @param code: 
        @param quantity: Quantity of item requisitioned. 
        @param cost: Cost of material 
        @param ErpRequisition:
        @param TypeMaterial:
        @param ErpPOLineItem:
        @param status:
        @param ErpQuoteLineItem:
        @param TypeAsset:
        """

        self.deliveryDate = deliveryDate


        self.code = code

        #: Quantity of item requisitioned.
        self.quantity = quantity

        #: Cost of material
        self.cost = cost

        self._ErpRequisition = None
        self.ErpRequisition = ErpRequisition

        self._TypeMaterial = None
        self.TypeMaterial = TypeMaterial

        self._ErpPOLineItem = None
        self.ErpPOLineItem = ErpPOLineItem

        self.status = status

        self._ErpQuoteLineItem = None
        self.ErpQuoteLineItem = ErpQuoteLineItem

        self._TypeAsset = None
        self.TypeAsset = TypeAsset

        super(ErpReqLineItem, self).__init__(**kw_args)

    def getErpRequisition(self):
        
        return self._ErpRequisition

    def setErpRequisition(self, value):
        if self._ErpRequisition is not None:
            filtered = [x for x in self.ErpRequisition.ErpReqLineItems if x != self]
            self._ErpRequisition._ErpReqLineItems = filtered

        self._ErpRequisition = value
        if self._ErpRequisition is not None:
            self._ErpRequisition._ErpReqLineItems.append(self)

    ErpRequisition = property(getErpRequisition, setErpRequisition)

    def getTypeMaterial(self):
        
        return self._TypeMaterial

    def setTypeMaterial(self, value):
        if self._TypeMaterial is not None:
            filtered = [x for x in self.TypeMaterial.ErpReqLineItems if x != self]
            self._TypeMaterial._ErpReqLineItems = filtered

        self._TypeMaterial = value
        if self._TypeMaterial is not None:
            self._TypeMaterial._ErpReqLineItems.append(self)

    TypeMaterial = property(getTypeMaterial, setTypeMaterial)

    def getErpPOLineItem(self):
        
        return self._ErpPOLineItem

    def setErpPOLineItem(self, value):
        if self._ErpPOLineItem is not None:
            self._ErpPOLineItem._ErpReqLineItem = None

        self._ErpPOLineItem = value
        if self._ErpPOLineItem is not None:
            self._ErpPOLineItem._ErpReqLineItem = self

    ErpPOLineItem = property(getErpPOLineItem, setErpPOLineItem)

    status = None

    def getErpQuoteLineItem(self):
        
        return self._ErpQuoteLineItem

    def setErpQuoteLineItem(self, value):
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem._ErpReqLineItem = None

        self._ErpQuoteLineItem = value
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem._ErpReqLineItem = self

    ErpQuoteLineItem = property(getErpQuoteLineItem, setErpQuoteLineItem)

    def getTypeAsset(self):
        
        return self._TypeAsset

    def setTypeAsset(self, value):
        if self._TypeAsset is not None:
            filtered = [x for x in self.TypeAsset.ErpReqLineItems if x != self]
            self._TypeAsset._ErpReqLineItems = filtered

        self._TypeAsset = value
        if self._TypeAsset is not None:
            self._TypeAsset._ErpReqLineItems.append(self)

    TypeAsset = property(getTypeAsset, setTypeAsset)

