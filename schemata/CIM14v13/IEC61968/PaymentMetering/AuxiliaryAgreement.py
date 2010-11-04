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

from CIM14v13.IEC61968.Common.Agreement import Agreement

class AuxiliaryAgreement(Agreement):
    """An ad-hoc auxiliary account agreement associated with a customer agreement, not part of the customer's account, but typically subject to formal agreement between customer and supplier (utility). Typically this is used to collect revenue owing by the customer for other services or arrears accrued with the utility for other services. It is typically linked to a prepaid token purchase transaction, thus forcing the customer to make a payment towards settlement of the auxiliary account balance whenever he needs to purchase a prepaid token for electricity. The present status of AuxiliaryAgreement can be defined in the context of the utility's business rules, for example: enabled, disabled, pending, over recovered, under recovered, written off, etc.
    """

    def __init__(self, auxPriorityCode='', fixedAmount=0.0, payCycle='', vendPortion=0.0, vendPortionArrear=0.0, minAmount=0.0, auxCycle='', auxRef='', subCategory='', arrearsInterest=0.0, CustomerAgreement=None, AuxiliaryAccounts=None, **kw_args):
        """Initializes a new 'AuxiliaryAgreement' instance.

        @param auxPriorityCode: The coded priority indicating the priority that this AuxiliaryAgreement has above other AuxiliaryAgreements (associated with the same customer agreement) when it comes to competing for settlement from a payment transaction or token purchase. 
        @param fixedAmount: The fixed amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement. Note that there may be multiple tokens vended per vending transaction, but this is not relevant. 
        @param payCycle: The contractually expected payment frequency (by the customer). Examples are: ad-hoc; on specified date; hourly, daily, weekly, monthly. etc. 
        @param vendPortion: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are not in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant. 
        @param vendPortionArrear: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant. 
        @param minAmount: The minimum amount that must be paid at any transaction towards settling this AuxiliryAgreement or reducing the balance. 
        @param auxCycle: The frequency for automatically recurring auxiliary charges, where AuxiliaryAccount.initialCharge is recursively added to AuxiliaryAccount.dueCurrent at the start of each auxCycle. For example: on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc. 
        @param auxRef: A local reference to this AuxiliaryAgreement defined in the context of the implementation and not related to IdentifiedObject.mRID. 
        @param subCategory: Sub-category of this AuxiliaryAgreement as sub-classification of the inherited 'category'. 
        @param arrearsInterest: The interest per annum to be charged prorata on AuxiliaryAccount.dueArrears at the end of each payCycle. 
        @param CustomerAgreement: Customer agreement this (non-service related) auxiliary agreement refers to.
        @param AuxiliaryAccounts: All auxiliary accounts regulated by this agreement.
        """
        #: The coded priority indicating the priority that this AuxiliaryAgreement has above other AuxiliaryAgreements (associated with the same customer agreement) when it comes to competing for settlement from a payment transaction or token purchase.
        self.auxPriorityCode = auxPriorityCode

        #: The fixed amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
        self.fixedAmount = fixedAmount

        #: The contractually expected payment frequency (by the customer). Examples are: ad-hoc; on specified date; hourly, daily, weekly, monthly. etc.
        self.payCycle = payCycle

        #: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are not in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
        self.vendPortion = vendPortion

        #: The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
        self.vendPortionArrear = vendPortionArrear

        #: The minimum amount that must be paid at any transaction towards settling this AuxiliryAgreement or reducing the balance.
        self.minAmount = minAmount

        #: The frequency for automatically recurring auxiliary charges, where AuxiliaryAccount.initialCharge is recursively added to AuxiliaryAccount.dueCurrent at the start of each auxCycle. For example: on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc.
        self.auxCycle = auxCycle

        #: A local reference to this AuxiliaryAgreement defined in the context of the implementation and not related to IdentifiedObject.mRID.
        self.auxRef = auxRef

        #: Sub-category of this AuxiliaryAgreement as sub-classification of the inherited 'category'.
        self.subCategory = subCategory

        #: The interest per annum to be charged prorata on AuxiliaryAccount.dueArrears at the end of each payCycle.
        self.arrearsInterest = arrearsInterest

        self._CustomerAgreement = None
        self.CustomerAgreement = CustomerAgreement

        self._AuxiliaryAccounts = []
        self.AuxiliaryAccounts = [] if AuxiliaryAccounts is None else AuxiliaryAccounts

        super(AuxiliaryAgreement, self).__init__(**kw_args)

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
            self._CustomerAgreement._AuxiliaryAgreements.append(self)

    CustomerAgreement = property(getCustomerAgreement, setCustomerAgreement)

    def getAuxiliaryAccounts(self):
        """All auxiliary accounts regulated by this agreement.
        """
        return self._AuxiliaryAccounts

    def setAuxiliaryAccounts(self, value):
        for x in self._AuxiliaryAccounts:
            x._AuxiliaryAgreement = None
        for y in value:
            y._AuxiliaryAgreement = self
        self._AuxiliaryAccounts = value

    AuxiliaryAccounts = property(getAuxiliaryAccounts, setAuxiliaryAccounts)

    def addAuxiliaryAccounts(self, *AuxiliaryAccounts):
        for obj in AuxiliaryAccounts:
            obj._AuxiliaryAgreement = self
            self._AuxiliaryAccounts.append(obj)

    def removeAuxiliaryAccounts(self, *AuxiliaryAccounts):
        for obj in AuxiliaryAccounts:
            obj._AuxiliaryAgreement = None
            self._AuxiliaryAccounts.remove(obj)

