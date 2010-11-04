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

class FinancialInfo(IdentifiedObject):
    """Various current financial properties associated with a particular asset. Historical properties may be determined by ActivityRecords associated with the asset.
    """

    def __init__(self, costType='', plantTransferDateTime='', actualPurchaseCost=0.0, purchaseDateTime='', purchaseOrderNumber='', warrantyEndDateTime='', valueDateTime='', account='', financialValue=0.0, quantity=0, costDescription='', Asset=None, *args, **kw_args):
        """Initializes a new 'FinancialInfo' instance.

        @param costType: Category of cost to which this Material Item belongs. 
        @param plantTransferDateTime: Date and time asset's financial value was put in plant for regulatory accounting purposes (e.g., for rate base calculations). This is sometime referred to as the 'in-service date.' 
        @param actualPurchaseCost: The actual purchase cost of this particular asset. 
        @param purchaseDateTime: Date and time asset was purchased. 
        @param purchaseOrderNumber: Purchase order identifier. 
        @param warrantyEndDateTime: Date and time warranty on asset expires. 
        @param valueDateTime: Date and time at which the financial value was last established. 
        @param account: The account to which this actual material item is charged. 
        @param financialValue: Value of asset as of 'valueDateTime'. 
        @param quantity: The quantity of the asset if per unit length, for example conductor. 
        @param costDescription: Description of the cost. 
        @param Asset:
        """
        #: Category of cost to which this Material Item belongs.
        self.costType = costType

        #: Date and time asset's financial value was put in plant for regulatory accounting purposes (e.g., for rate base calculations). This is sometime referred to as the 'in-service date.'
        self.plantTransferDateTime = plantTransferDateTime

        #: The actual purchase cost of this particular asset.
        self.actualPurchaseCost = actualPurchaseCost

        #: Date and time asset was purchased.
        self.purchaseDateTime = purchaseDateTime

        #: Purchase order identifier.
        self.purchaseOrderNumber = purchaseOrderNumber

        #: Date and time warranty on asset expires.
        self.warrantyEndDateTime = warrantyEndDateTime

        #: Date and time at which the financial value was last established.
        self.valueDateTime = valueDateTime

        #: The account to which this actual material item is charged.
        self.account = account

        #: Value of asset as of 'valueDateTime'.
        self.financialValue = financialValue

        #: The quantity of the asset if per unit length, for example conductor.
        self.quantity = quantity

        #: Description of the cost.
        self.costDescription = costDescription

        self._Asset = None
        self.Asset = Asset

        super(FinancialInfo, self).__init__(*args, **kw_args)

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            self._Asset._FinancialInfo = None

        self._Asset = value
        if self._Asset is not None:
            self._Asset._FinancialInfo = self

    Asset = property(getAsset, setAsset)

