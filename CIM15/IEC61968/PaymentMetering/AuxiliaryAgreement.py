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

from CIM15.IEC61968.Common.Agreement import Agreement

class AuxiliaryAgreement(Agreement):
    """An ad-hoc auxiliary account agreement associated with a customer agreement, not part of the customer's account, but typically subject to formal agreement between customer and supplier (utility). Typically this is used to collect revenue owing by the customer for other services or arrears accrued with the utility for other services. It is typically linked to a prepaid token purchase transaction, thus forcing the customer to make a payment towards settlement of the auxiliary account balance whenever he needs to purchase a prepaid token for electricity. The present status of auxiliary agreement can be defined in the context of the utility's business rules, for example: enabled, disabled, pending, over recovered, under recovered, written off, etc.An ad-hoc auxiliary account agreement associated with a customer agreement, not part of the customer's account, but typically subject to formal agreement between customer and supplier (utility). Typically this is used to collect revenue owing by the customer for other services or arrears accrued with the utility for other services. It is typically linked to a prepaid token purchase transaction, thus forcing the customer to make a payment towards settlement of the auxiliary account balance whenever he needs to purchase a prepaid token for electricity. The present status of auxiliary agreement can be defined in the context of the utility's business rules, for example: enabled, disabled, pending, over recovered, under recovered, written off, etc.
    """

    def __init__(self, vendPortionArrear=0.0, auxRef='', payCycle='', arrearsInterest=0.0, fixedAmount=0.0, vendPortion=0.0, subCategory='', auxCycle='', auxPriorityCode='', minAmount=0.0, CustomerAgreement=None, AuxiliaryAccounts=None, *args, **kw_args):
        """Initialises a new 'AuxiliaryAgreement' instance.

        @param vendPortionArrear: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this auxiliary agreement when payments are in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant. 
        @param auxRef: A local reference to this auxiliary agreement defined in the context of the implementation and not related to IdentifiedObject.mRID. 
        @param payCycle: The contractually expected payment frequency (by the customer). Examples are: ad-hoc; on specified date; hourly, daily, weekly, monthly. etc. 
        @param arrearsInterest: The interest per annum to be charged prorata on 'AuxiliaryAccount.dueArrears' at the end of each 'payCycle'. 
        @param fixedAmount: The fixed amount that must be collected from each vending transaction towards settlement of this auxiliary agreement. Note that there may be multiple tokens vended per vending transaction, but this is not relevant. 
        @param vendPortion: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this auxiliary agreement when payments are not in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant. 
        @param subCategory: Sub-category of this AuxiliaryAgreement as sub-classification of the inherited 'category'. 
        @param auxCycle: The frequency for automatically recurring auxiliary charges, where 'AuxiliaryAccount.initialCharge' is recursively added to 'AuxiliaryAccount.dueCurrent' at the start of each 'auxCycle'. For example: on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc. 
        @param auxPriorityCode: The coded priority indicating the priority that this auxiliary agreement has above other auxiliary agreements (associated with the same customer agreement) when it comes to competing for settlement from a payment transaction or token purchase. 
        @param minAmount: The minimum amount that must be paid at any transaction towards settling this auxiliry agreement or reducing the balance. 
        @param CustomerAgreement: Customer agreement this (non-service related) auxiliary agreement refers to.
        @param AuxiliaryAccounts: All auxiliary accounts regulated by this agreement.
        """
        #: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this auxiliary agreement when payments are in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
        self.vendPortionArrear = vendPortionArrear

        #: A local reference to this auxiliary agreement defined in the context of the implementation and not related to IdentifiedObject.mRID.
        self.auxRef = auxRef

        #: The contractually expected payment frequency (by the customer). Examples are: ad-hoc; on specified date; hourly, daily, weekly, monthly. etc.
        self.payCycle = payCycle

        #: The interest per annum to be charged prorata on 'AuxiliaryAccount.dueArrears' at the end of each 'payCycle'.
        self.arrearsInterest = arrearsInterest

        #: The fixed amount that must be collected from each vending transaction towards settlement of this auxiliary agreement. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
        self.fixedAmount = fixedAmount

        #: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this auxiliary agreement when payments are not in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
        self.vendPortion = vendPortion

        #: Sub-category of this AuxiliaryAgreement as sub-classification of the inherited 'category'.
        self.subCategory = subCategory

        #: The frequency for automatically recurring auxiliary charges, where 'AuxiliaryAccount.initialCharge' is recursively added to 'AuxiliaryAccount.dueCurrent' at the start of each 'auxCycle'. For example: on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc.
        self.auxCycle = auxCycle

        #: The coded priority indicating the priority that this auxiliary agreement has above other auxiliary agreements (associated with the same customer agreement) when it comes to competing for settlement from a payment transaction or token purchase.
        self.auxPriorityCode = auxPriorityCode

        #: The minimum amount that must be paid at any transaction towards settling this auxiliry agreement or reducing the balance.
        self.minAmount = minAmount

        self._CustomerAgreement = None
        self.CustomerAgreement = CustomerAgreement

        self._AuxiliaryAccounts = []
        self.AuxiliaryAccounts = [] if AuxiliaryAccounts is None else AuxiliaryAccounts

        super(AuxiliaryAgreement, self).__init__(*args, **kw_args)

    _attrs = ["vendPortionArrear", "auxRef", "payCycle", "arrearsInterest", "fixedAmount", "vendPortion", "subCategory", "auxCycle", "auxPriorityCode", "minAmount"]
    _attr_types = {"vendPortionArrear": float, "auxRef": str, "payCycle": str, "arrearsInterest": float, "fixedAmount": float, "vendPortion": float, "subCategory": str, "auxCycle": str, "auxPriorityCode": str, "minAmount": float}
    _defaults = {"vendPortionArrear": 0.0, "auxRef": '', "payCycle": '', "arrearsInterest": 0.0, "fixedAmount": 0.0, "vendPortion": 0.0, "subCategory": '', "auxCycle": '', "auxPriorityCode": '', "minAmount": 0.0}
    _enums = {}
    _refs = ["CustomerAgreement", "AuxiliaryAccounts"]
    _many_refs = ["AuxiliaryAccounts"]

    def getCustomerAgreement(self):
        """Customer agreement this (non-service related) auxiliary agreement refers to.
        """
        return self._CustomerAgreement

    def setCustomerAgreement(self, value):
        if self._CustomerAgreement is not None:
            filtered = [x for x in self.CustomerAgreement.AuxiliaryAgreements if x != self]
            self._CustomerAgreement._AuxiliaryAgreements = filtered

        self._CustomerAgreement = value
        if self._CustomerAgreement is not None:
            if self not in self._CustomerAgreement._AuxiliaryAgreements:
                self._CustomerAgreement._AuxiliaryAgreements.append(self)

    CustomerAgreement = property(getCustomerAgreement, setCustomerAgreement)

    def getAuxiliaryAccounts(self):
        """All auxiliary accounts regulated by this agreement.
        """
        return self._AuxiliaryAccounts

    def setAuxiliaryAccounts(self, value):
        for x in self._AuxiliaryAccounts:
            x.AuxiliaryAgreement = None
        for y in value:
            y._AuxiliaryAgreement = self
        self._AuxiliaryAccounts = value

    AuxiliaryAccounts = property(getAuxiliaryAccounts, setAuxiliaryAccounts)

    def addAuxiliaryAccounts(self, *AuxiliaryAccounts):
        for obj in AuxiliaryAccounts:
            obj.AuxiliaryAgreement = self

    def removeAuxiliaryAccounts(self, *AuxiliaryAccounts):
        for obj in AuxiliaryAccounts:
            obj.AuxiliaryAgreement = None

