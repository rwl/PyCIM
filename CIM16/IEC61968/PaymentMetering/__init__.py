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

"""This package is an extension of the Metering package and contains the information classes that support specialised applications such as prepayment metering. These classes are generally associated with the collection and control of revenue from the customer for a delivered service.
"""

from CIM16.IEC61968.PaymentMetering.VendorShift import VendorShift
from CIM16.IEC61968.PaymentMetering.Transactor import Transactor
from CIM16.IEC61968.PaymentMetering.CashierShift import CashierShift
from CIM16.IEC61968.PaymentMetering.TariffProfile import TariffProfile
from CIM16.IEC61968.PaymentMetering.AccountingUnit import AccountingUnit
from CIM16.IEC61968.PaymentMetering.Transaction import Transaction
from CIM16.IEC61968.PaymentMetering.TimeTariffInterval import TimeTariffInterval
from CIM16.IEC61968.PaymentMetering.Charge import Charge
from CIM16.IEC61968.PaymentMetering.AuxiliaryAgreement import AuxiliaryAgreement
from CIM16.IEC61968.PaymentMetering.Tender import Tender
from CIM16.IEC61968.PaymentMetering.ServiceSupplier import ServiceSupplier
from CIM16.IEC61968.PaymentMetering.MerchantAgreement import MerchantAgreement
from CIM16.IEC61968.PaymentMetering.LineDetail import LineDetail
from CIM16.IEC61968.PaymentMetering.ConsumptionTariffInterval import ConsumptionTariffInterval
from CIM16.IEC61968.PaymentMetering.Vendor import Vendor
from CIM16.IEC61968.PaymentMetering.Cheque import Cheque
from CIM16.IEC61968.PaymentMetering.AccountMovement import AccountMovement
from CIM16.IEC61968.PaymentMetering.Shift import Shift
from CIM16.IEC61968.PaymentMetering.Receipt import Receipt
from CIM16.IEC61968.PaymentMetering.Due import Due
from CIM16.IEC61968.PaymentMetering.BankAccountDetail import BankAccountDetail
from CIM16.IEC61968.PaymentMetering.AuxiliaryAccount import AuxiliaryAccount
from CIM16.IEC61968.PaymentMetering.Cashier import Cashier
from CIM16.IEC61968.PaymentMetering.Card import Card
from CIM16.IEC61968.PaymentMetering.MerchantAccount import MerchantAccount
from CIM16.IEC61968.PaymentMetering.PointOfSale import PointOfSale

nsURI = "http://iec.ch/TC57/2013/CIM-schema-cim16#PaymentMetering"
nsPrefix = "cimPaymentMetering"


class TenderKind(str):
    """Values are: unspecified, cheque, other, cash, card
    """
    pass

class ChequeKind(str):
    """Values are: other, postalOrder, bankOrder
    """
    pass

class ChargeKind(str):
    """Values are: other, demandCharge, consumptionCharge, auxiliaryCharge, taxCharge
    """
    pass

class TransactionKind(str):
    """Values are: other, serviceChargePayment, accountPayment, tokenSalePayment, tokenCancellation, taxChargePayment, tokenExchange, tokenGrant, diversePayment, auxiliaryChargePayment, meterConfigurationToken, tokenFreeIssue, transactionReversal
    """
    pass

class SupplierKind(str):
    """Values are: other, retailer, utility
    """
    pass
