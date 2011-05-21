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

"""This package contains only diagrams, drawn by hand from PaymentMetering-related XSDs that are in Part 9 document. Entry points into the schema are filled with green. Non-used associations are light grey.
"""

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

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#PaymentMetering"
nsPrefix = "cimPaymentMetering"


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
