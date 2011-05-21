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

from CIM14.IEC61968.Common.Agreement import Agreement

class AuxiliaryAgreement(Agreement):
    """An ad-hoc auxiliary account agreement associated with a customer agreement, not part of the customer's account, but typically subject to formal agreement between customer and supplier (utility). Typically this is used to collect revenue owing by the customer for other services or arrears accrued with the utility for other services. It is typically linked to a prepaid token purchase transaction, thus forcing the customer to make a payment towards settlement of the auxiliary account balance whenever he needs to purchase a prepaid token for electricity. The present status of AuxiliaryAgreement can be defined in the context of the utility's business rules, for example: enabled, disabled, pending, over recovered, under recovered, written off, etc.
    """

    def __init__(self, arrearsInterest=0.0, vendPortion=0.0, minAmount=0.0, auxPriorityCode='', subCategory='', auxRef='', auxCycle='', vendPortionArrear=0.0, payCycle='', fixedAmount=0.0, AuxiliaryAccounts=None, CustomerAgreement=None, *args, **kw_args):
        """Initialises a new 'AuxiliaryAgreement' instance.

        @param arrearsInterest: The interest per annum to be charged prorata on AuxiliaryAccount.dueArrears at the end of each payCycle. 
        @param vendPortion: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are not in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant. 
        @param minAmount: The minimum amount that must be paid at any transaction towards settling this AuxiliryAgreement or reducing the balance. 
        @param auxPriorityCode: The coded priority indicating the priority that this AuxiliaryAgreement has above other AuxiliaryAgreements (associated with the same customer agreement) when it comes to competing for settlement from a payment transaction or token purchase. 
        @param subCategory: Sub-category of this AuxiliaryAgreement as sub-classification of the inherited 'category'. 
        @param auxRef: A local reference to this AuxiliaryAgreement defined in the context of the implementation and not related to IdentifiedObject.mRID. 
        @param auxCycle: The frequency for automatically recurring auxiliary charges, where AuxiliaryAccount.initialCharge is recursively added to AuxiliaryAccount.dueCurrent at the start of each auxCycle. For example: on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc. 
        @param vendPortionArrear: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant. 
        @param payCycle: The contractually expected payment frequency (by the customer). Examples are: ad-hoc; on specified date; hourly, daily, weekly, monthly. etc. 
        @param fixedAmount: The fixed amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement. Note that there may be multiple tokens vended per vending transaction, but this is not relevant. 
        @param AuxiliaryAccounts: All auxiliary accounts regulated by this agreement.
        @param CustomerAgreement: Customer agreement this (non-service related) auxiliary agreement refers to.
        """
        #: The interest per annum to be charged prorata on AuxiliaryAccount.dueArrears at the end of each payCycle.
        self.arrearsInterest = arrearsInterest

        #: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are not in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
        self.vendPortion = vendPortion

        #: The minimum amount that must be paid at any transaction towards settling this AuxiliryAgreement or reducing the balance.
        self.minAmount = minAmount

        #: The coded priority indicating the priority that this AuxiliaryAgreement has above other AuxiliaryAgreements (associated with the same customer agreement) when it comes to competing for settlement from a payment transaction or token purchase.
        self.auxPriorityCode = auxPriorityCode

        #: Sub-category of this AuxiliaryAgreement as sub-classification of the inherited 'category'.
        self.subCategory = subCategory

        #: A local reference to this AuxiliaryAgreement defined in the context of the implementation and not related to IdentifiedObject.mRID.
        self.auxRef = auxRef

        #: The frequency for automatically recurring auxiliary charges, where AuxiliaryAccount.initialCharge is recursively added to AuxiliaryAccount.dueCurrent at the start of each auxCycle. For example: on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc.
        self.auxCycle = auxCycle

        #: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
        self.vendPortionArrear = vendPortionArrear

        #: The contractually expected payment frequency (by the customer). Examples are: ad-hoc; on specified date; hourly, daily, weekly, monthly. etc.
        self.payCycle = payCycle

        #: The fixed amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
        self.fixedAmount = fixedAmount

        self._AuxiliaryAccounts = []
        self.AuxiliaryAccounts = [] if AuxiliaryAccounts is None else AuxiliaryAccounts

        self._CustomerAgreement = None
        self.CustomerAgreement = CustomerAgreement

        super(AuxiliaryAgreement, self).__init__(*args, **kw_args)

    _attrs = ["arrearsInterest", "vendPortion", "minAmount", "auxPriorityCode", "subCategory", "auxRef", "auxCycle", "vendPortionArrear", "payCycle", "fixedAmount"]
    _attr_types = {"arrearsInterest": float, "vendPortion": float, "minAmount": float, "auxPriorityCode": str, "subCategory": str, "auxRef": str, "auxCycle": str, "vendPortionArrear": float, "payCycle": str, "fixedAmount": float}
    _defaults = {"arrearsInterest": 0.0, "vendPortion": 0.0, "minAmount": 0.0, "auxPriorityCode": '', "subCategory": '', "auxRef": '', "auxCycle": '', "vendPortionArrear": 0.0, "payCycle": '', "fixedAmount": 0.0}
    _enums = {}
    _refs = ["AuxiliaryAccounts", "CustomerAgreement"]
    _many_refs = ["AuxiliaryAccounts"]

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

