# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class FinancialInfo(IdentifiedObject):
    """Various current financial properties associated with a particular asset. Historical properties may be determined by ActivityRecords associated with the asset.Various current financial properties associated with a particular asset. Historical properties may be determined by ActivityRecords associated with the asset.
    """

    def __init__(self, warrantyEndDateTime='', costDescription='', purchaseDateTime='', account='', financialValue=0.0, purchaseOrderNumber='', plantTransferDateTime='', quantity="", valueDateTime='', costType='', actualPurchaseCost=0.0, Asset=None, *args, **kw_args):
        """Initialises a new 'FinancialInfo' instance.

        @param warrantyEndDateTime: Date and time warranty on asset expires. 
        @param costDescription: Description of the cost. 
        @param purchaseDateTime: Date and time asset was purchased. 
        @param account: The account to which this actual material item is charged. 
        @param financialValue: Value of asset as of 'valueDateTime'. 
        @param purchaseOrderNumber: Purchase order identifier. 
        @param plantTransferDateTime: Date and time asset's financial value was put in plant for regulatory accounting purposes (e.g., for rate base calculations). This is sometime referred to as the 'in-service date.' 
        @param quantity: The quantity of the asset if per unit length, for example conductor. 
        @param valueDateTime: Date and time at which the financial value was last established. 
        @param costType: Category of cost to which this Material Item belongs. 
        @param actualPurchaseCost: The actual purchase cost of this particular asset. 
        @param Asset:
        """
        #: Date and time warranty on asset expires.
        self.warrantyEndDateTime = warrantyEndDateTime

        #: Description of the cost.
        self.costDescription = costDescription

        #: Date and time asset was purchased.
        self.purchaseDateTime = purchaseDateTime

        #: The account to which this actual material item is charged.
        self.account = account

        #: Value of asset as of 'valueDateTime'.
        self.financialValue = financialValue

        #: Purchase order identifier.
        self.purchaseOrderNumber = purchaseOrderNumber

        #: Date and time asset's financial value was put in plant for regulatory accounting purposes (e.g., for rate base calculations). This is sometime referred to as the 'in-service date.'
        self.plantTransferDateTime = plantTransferDateTime

        #: The quantity of the asset if per unit length, for example conductor.
        self.quantity = quantity

        #: Date and time at which the financial value was last established.
        self.valueDateTime = valueDateTime

        #: Category of cost to which this Material Item belongs.
        self.costType = costType

        #: The actual purchase cost of this particular asset.
        self.actualPurchaseCost = actualPurchaseCost

        self._Asset = None
        self.Asset = Asset

        super(FinancialInfo, self).__init__(*args, **kw_args)

    _attrs = ["warrantyEndDateTime", "costDescription", "purchaseDateTime", "account", "financialValue", "purchaseOrderNumber", "plantTransferDateTime", "quantity", "valueDateTime", "costType", "actualPurchaseCost"]
    _attr_types = {"warrantyEndDateTime": str, "costDescription": str, "purchaseDateTime": str, "account": str, "financialValue": float, "purchaseOrderNumber": str, "plantTransferDateTime": str, "quantity": str, "valueDateTime": str, "costType": str, "actualPurchaseCost": float}
    _defaults = {"warrantyEndDateTime": '', "costDescription": '', "purchaseDateTime": '', "account": '', "financialValue": 0.0, "purchaseOrderNumber": '', "plantTransferDateTime": '', "quantity": "", "valueDateTime": '', "costType": '', "actualPurchaseCost": 0.0}
    _enums = {}
    _refs = ["Asset"]
    _many_refs = []

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            self._Asset._FinancialInfo = None

        self._Asset = value
        if self._Asset is not None:
            self._Asset.FinancialInfo = None
            self._Asset._FinancialInfo = self

    Asset = property(getAsset, setAsset)

