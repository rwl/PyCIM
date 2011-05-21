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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Transaction(IdentifiedObject):
    """The record of details of payment for service or token sale.
    """

    def __init__(self, kind="diversePayment", serviceUnitsEnergy=0.0, diverseReference='', receiverReference='', donorReference='', serviceUnitsError=0.0, reversedId='', PricingStructure=None, UserAttributes=None, CustomerAccount=None, CashierShift=None, VendorShift=None, MeterAsset=None, AuxiliaryAccount=None, line=None, Receipt=None, *args, **kw_args):
        """Initialises a new 'Transaction' instance.

        @param kind: Kind of transaction. Values are: "diversePayment", "tokenSalePayment", "serviceChargePayment", "other", "transactionReversal", "taxChargePayment", "meterConfigurationToken", "accountPayment", "tokenFreeIssue", "tokenExchange", "tokenCancellation", "tokenGrant", "auxiliaryChargePayment"
        @param serviceUnitsEnergy: Actual amount of service units that is being paid for. 
        @param diverseReference: Formal reference for use with diverse payment (traffic fine for example). 
        @param receiverReference: Reference to the entity that is the recipient of 'amount' (for example, supplier for service charge payment; or tax receiver for VAT). 
        @param donorReference: Reference to the entity that is the source of 'amount' (for example: customer for token purchase; or supplier for free issue token). 
        @param serviceUnitsError: Number of service units not reflected in 'serviceUnitsEnergy' due to process rounding or truncating errors. 
        @param reversedId: (if 'kind' is transactionReversal) Reference to the original transaction that is being reversed by this transaction. 
        @param PricingStructure: Pricing structure applicable for this transaction.
        @param UserAttributes: All snapshots of meter parameters recorded at the time of this transaction. Use 'name' and 'value.value' attributes to specify name and value of a parameter from meter.
        @param CustomerAccount: Customer account for this payment transaction.
        @param CashierShift: Cashier shift during which this transaction was recorded.
        @param VendorShift: Vendor shift during which this transaction was recorded.
        @param MeterAsset: Meter asset for this vending transaction.
        @param AuxiliaryAccount: Auxiliary account for this payment transaction.
        @param line: Transaction amount, rounding, date and note for this transaction line.
        @param Receipt: The receipted payment for which this transaction has been recorded.
        """
        #: Kind of transaction. Values are: "diversePayment", "tokenSalePayment", "serviceChargePayment", "other", "transactionReversal", "taxChargePayment", "meterConfigurationToken", "accountPayment", "tokenFreeIssue", "tokenExchange", "tokenCancellation", "tokenGrant", "auxiliaryChargePayment"
        self.kind = kind

        #: Actual amount of service units that is being paid for.
        self.serviceUnitsEnergy = serviceUnitsEnergy

        #: Formal reference for use with diverse payment (traffic fine for example).
        self.diverseReference = diverseReference

        #: Reference to the entity that is the recipient of 'amount' (for example, supplier for service charge payment; or tax receiver for VAT).
        self.receiverReference = receiverReference

        #: Reference to the entity that is the source of 'amount' (for example: customer for token purchase; or supplier for free issue token).
        self.donorReference = donorReference

        #: Number of service units not reflected in 'serviceUnitsEnergy' due to process rounding or truncating errors.
        self.serviceUnitsError = serviceUnitsError

        #: (if 'kind' is transactionReversal) Reference to the original transaction that is being reversed by this transaction.
        self.reversedId = reversedId

        self._PricingStructure = None
        self.PricingStructure = PricingStructure

        self._UserAttributes = []
        self.UserAttributes = [] if UserAttributes is None else UserAttributes

        self._CustomerAccount = None
        self.CustomerAccount = CustomerAccount

        self._CashierShift = None
        self.CashierShift = CashierShift

        self._VendorShift = None
        self.VendorShift = VendorShift

        self._MeterAsset = None
        self.MeterAsset = MeterAsset

        self._AuxiliaryAccount = None
        self.AuxiliaryAccount = AuxiliaryAccount

        self.line = line

        self._Receipt = None
        self.Receipt = Receipt

        super(Transaction, self).__init__(*args, **kw_args)

    _attrs = ["kind", "serviceUnitsEnergy", "diverseReference", "receiverReference", "donorReference", "serviceUnitsError", "reversedId"]
    _attr_types = {"kind": str, "serviceUnitsEnergy": float, "diverseReference": str, "receiverReference": str, "donorReference": str, "serviceUnitsError": float, "reversedId": str}
    _defaults = {"kind": "diversePayment", "serviceUnitsEnergy": 0.0, "diverseReference": '', "receiverReference": '', "donorReference": '', "serviceUnitsError": 0.0, "reversedId": ''}
    _enums = {"kind": "TransactionKind"}
    _refs = ["PricingStructure", "UserAttributes", "CustomerAccount", "CashierShift", "VendorShift", "MeterAsset", "AuxiliaryAccount", "line", "Receipt"]
    _many_refs = ["UserAttributes"]

    def getPricingStructure(self):
        """Pricing structure applicable for this transaction.
        """
        return self._PricingStructure

    def setPricingStructure(self, value):
        if self._PricingStructure is not None:
            filtered = [x for x in self.PricingStructure.Transactions if x != self]
            self._PricingStructure._Transactions = filtered

        self._PricingStructure = value
        if self._PricingStructure is not None:
            if self not in self._PricingStructure._Transactions:
                self._PricingStructure._Transactions.append(self)

    PricingStructure = property(getPricingStructure, setPricingStructure)

    def getUserAttributes(self):
        """All snapshots of meter parameters recorded at the time of this transaction. Use 'name' and 'value.value' attributes to specify name and value of a parameter from meter.
        """
        return self._UserAttributes

    def setUserAttributes(self, value):
        for x in self._UserAttributes:
            x.Transaction = None
        for y in value:
            y._Transaction = self
        self._UserAttributes = value

    UserAttributes = property(getUserAttributes, setUserAttributes)

    def addUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            obj.Transaction = self

    def removeUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            obj.Transaction = None

    def getCustomerAccount(self):
        """Customer account for this payment transaction.
        """
        return self._CustomerAccount

    def setCustomerAccount(self, value):
        if self._CustomerAccount is not None:
            filtered = [x for x in self.CustomerAccount.PaymentTransactions if x != self]
            self._CustomerAccount._PaymentTransactions = filtered

        self._CustomerAccount = value
        if self._CustomerAccount is not None:
            if self not in self._CustomerAccount._PaymentTransactions:
                self._CustomerAccount._PaymentTransactions.append(self)

    CustomerAccount = property(getCustomerAccount, setCustomerAccount)

    def getCashierShift(self):
        """Cashier shift during which this transaction was recorded.
        """
        return self._CashierShift

    def setCashierShift(self, value):
        if self._CashierShift is not None:
            filtered = [x for x in self.CashierShift.Transactions if x != self]
            self._CashierShift._Transactions = filtered

        self._CashierShift = value
        if self._CashierShift is not None:
            if self not in self._CashierShift._Transactions:
                self._CashierShift._Transactions.append(self)

    CashierShift = property(getCashierShift, setCashierShift)

    def getVendorShift(self):
        """Vendor shift during which this transaction was recorded.
        """
        return self._VendorShift

    def setVendorShift(self, value):
        if self._VendorShift is not None:
            filtered = [x for x in self.VendorShift.Transactions if x != self]
            self._VendorShift._Transactions = filtered

        self._VendorShift = value
        if self._VendorShift is not None:
            if self not in self._VendorShift._Transactions:
                self._VendorShift._Transactions.append(self)

    VendorShift = property(getVendorShift, setVendorShift)

    def getMeterAsset(self):
        """Meter asset for this vending transaction.
        """
        return self._MeterAsset

    def setMeterAsset(self, value):
        if self._MeterAsset is not None:
            filtered = [x for x in self.MeterAsset.VendingTransactions if x != self]
            self._MeterAsset._VendingTransactions = filtered

        self._MeterAsset = value
        if self._MeterAsset is not None:
            if self not in self._MeterAsset._VendingTransactions:
                self._MeterAsset._VendingTransactions.append(self)

    MeterAsset = property(getMeterAsset, setMeterAsset)

    def getAuxiliaryAccount(self):
        """Auxiliary account for this payment transaction.
        """
        return self._AuxiliaryAccount

    def setAuxiliaryAccount(self, value):
        if self._AuxiliaryAccount is not None:
            filtered = [x for x in self.AuxiliaryAccount.PaymentTransactions if x != self]
            self._AuxiliaryAccount._PaymentTransactions = filtered

        self._AuxiliaryAccount = value
        if self._AuxiliaryAccount is not None:
            if self not in self._AuxiliaryAccount._PaymentTransactions:
                self._AuxiliaryAccount._PaymentTransactions.append(self)

    AuxiliaryAccount = property(getAuxiliaryAccount, setAuxiliaryAccount)

    # Transaction amount, rounding, date and note for this transaction line.
    line = None

    def getReceipt(self):
        """The receipted payment for which this transaction has been recorded.
        """
        return self._Receipt

    def setReceipt(self, value):
        if self._Receipt is not None:
            filtered = [x for x in self.Receipt.Transactions if x != self]
            self._Receipt._Transactions = filtered

        self._Receipt = value
        if self._Receipt is not None:
            if self not in self._Receipt._Transactions:
                self._Receipt._Transactions.append(self)

    Receipt = property(getReceipt, setReceipt)

