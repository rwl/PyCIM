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

"""This package contains only diagrams, drawn by hand from PaymentMetering-related XSDs that are in Part 9 document. Entry points into the schema are filled with green. Non-used associations are light grey.
"""

nsPrefix = "cimPaymentMetering"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#PaymentMetering"

from CIM14.IEC61968.PaymentMetering.ServiceSupplier import ServiceSupplier
from CIM14.IEC61968.PaymentMetering.Shift import Shift
from CIM14.IEC61968.PaymentMetering.Tender import Tender
from CIM14.IEC61968.PaymentMetering.TariffProfile import TariffProfile
from CIM14.IEC61968.PaymentMetering.ConsumptionTariffInterval import ConsumptionTariffInterval
from CIM14.IEC61968.PaymentMetering.BankAccountDetail import BankAccountDetail
from CIM14.IEC61968.PaymentMetering.Cheque import Cheque
from CIM14.IEC61968.PaymentMetering.CashierShift import CashierShift
from CIM14.IEC61968.PaymentMetering.Due import Due
from CIM14.IEC61968.PaymentMetering.AccountingUnit import AccountingUnit
from CIM14.IEC61968.PaymentMetering.Card import Card
from CIM14.IEC61968.PaymentMetering.AuxiliaryAccount import AuxiliaryAccount
from CIM14.IEC61968.PaymentMetering.MerchantAgreement import MerchantAgreement
from CIM14.IEC61968.PaymentMetering.LineDetail import LineDetail
from CIM14.IEC61968.PaymentMetering.Transactor import Transactor
from CIM14.IEC61968.PaymentMetering.MerchantAccount import MerchantAccount
from CIM14.IEC61968.PaymentMetering.Vendor import Vendor
from CIM14.IEC61968.PaymentMetering.Transaction import Transaction
from CIM14.IEC61968.PaymentMetering.Charge import Charge
from CIM14.IEC61968.PaymentMetering.VendorShift import VendorShift
from CIM14.IEC61968.PaymentMetering.TimeTariffInterval import TimeTariffInterval
from CIM14.IEC61968.PaymentMetering.Cashier import Cashier
from CIM14.IEC61968.PaymentMetering.PointOfSale import PointOfSale
from CIM14.IEC61968.PaymentMetering.Receipt import Receipt
from CIM14.IEC61968.PaymentMetering.AuxiliaryAgreement import AuxiliaryAgreement
from CIM14.IEC61968.PaymentMetering.AccountMovement import AccountMovement

class ChequeKind(str):
    """Kind of cheque.
    Values are: other, postalOrder, bankOrder
    """
    pass

class TransactionKind(str):
    """Kind of transaction.
    Values are: diversePayment, tokenSalePayment, serviceChargePayment, other, transactionReversal, taxChargePayment, meterConfigurationToken, accountPayment, tokenFreeIssue, tokenExchange, tokenCancellation, tokenGrant, auxiliaryChargePayment
    """
    pass

class ChargeKind(str):
    """Kind of charge.
    Values are: demandCharge, other, auxiliaryCharge, taxCharge, consumptionCharge
    """
    pass

class CreditKind(str):
    """Kind of credit.
    Values are: grantCredit, tokenCredit, reserveCredit, other, advanceCredit, lifelineCredit
    """
    pass

class SupplierKind(str):
    """Kind of supplier.
    Values are: retailer, utility, other
    """
    pass

class TenderKind(str):
    """Kind of tender.
    Values are: cash, unspecified, card, other, cheque
    """
    pass
