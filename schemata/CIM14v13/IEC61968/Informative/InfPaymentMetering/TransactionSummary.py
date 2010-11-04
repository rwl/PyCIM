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

from CIM14v13.Element import Element

class TransactionSummary(Element):
    """The record of detail of payment transactions pertaining to one shift of operation (one record per 'transactionKind').
    """

    def __init__(self, transactionKind='auxiliaryChargePayment', Shift=None, line=None, **kw_args):
        """Initializes a new 'TransactionSummary' instance.

        @param transactionKind: 'Transaction.kind' for which 'transactionsTotal' is given. Values are: "auxiliaryChargePayment", "tokenExchange", "tokenCancellation", "transactionReversal", "diversePayment", "tokenFreeIssue", "other", "meterConfigurationToken", "tokenSalePayment", "accountPayment", "taxChargePayment", "serviceChargePayment", "tokenGrant"
        @param Shift: Shift to which this summary applies.
        @param line: Totalised amount transacted during the shift for this specific 'transactionKind', i.e., sum of 'Transaction.line.amount' per 'Transaction.kind'. Cumulative amount of rounding errors due to process rounding not reflected in 'LineDetail.amount' for 'transactionKind', i.e., sum of 'Transaction.line.rounding' per 'Transaction.kind'.
        """
        #: 'Transaction.kind' for which 'transactionsTotal' is given.Values are: "auxiliaryChargePayment", "tokenExchange", "tokenCancellation", "transactionReversal", "diversePayment", "tokenFreeIssue", "other", "meterConfigurationToken", "tokenSalePayment", "accountPayment", "taxChargePayment", "serviceChargePayment", "tokenGrant"
        self.transactionKind = transactionKind

        self._Shift = None
        self.Shift = Shift

        self.line = line

        super(TransactionSummary, self).__init__(**kw_args)

    def getShift(self):
        """Shift to which this summary applies.
        """
        return self._Shift

    def setShift(self, value):
        if self._Shift is not None:
            filtered = [x for x in self.Shift.TransactionSummaries if x != self]
            self._Shift._TransactionSummaries = filtered

        self._Shift = value
        if self._Shift is not None:
            self._Shift._TransactionSummaries.append(self)

    Shift = property(getShift, setShift)

    # Totalised amount transacted during the shift for this specific 'transactionKind', i.e., sum of 'Transaction.line.amount' per 'Transaction.kind'. Cumulative amount of rounding errors due to process rounding not reflected in 'LineDetail.amount' for 'transactionKind', i.e., sum of 'Transaction.line.rounding' per 'Transaction.kind'.
    line = None

