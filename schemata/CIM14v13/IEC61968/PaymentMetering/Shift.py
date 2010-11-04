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

class Shift(IdentifiedObject):
    """Generally referring to a period of operation or work performed. Whether shift is open/closed can be derived from attributes 'activiryInterval.start' and 'activityInterval.end'. The grand total for receipts (i.e., cumulative total of all actual receipted amounts during this shift; bankable + non-bankable; excludes rounding error totals) can be derived from Receipt attributes: =sum(Receipt.receiptAmount) ; includes bankable and non-bankable receipts. Must also reconcile against: =sum(receiptsGrandTotalBankable + receiptsGrandTotalNonBankable). Must also reconcile against ReceiptSummary: =sum(ReceiptSummary.receiptsTotal). The attributes with 'GrandTotal' defined in this class may need to be used when the source data is periodically flushed from the system and then these cannot be derived.
    """

    def __init__(self, transactionsGrandTotalRounding=0.0, transactionsGrandTotal=0.0, receiptsGrandTotalBankable=0.0, receiptsGrandTotalRounding=0.0, receiptsGrandTotalNonBankable=0.0, ReceiptSummaries=None, activityInterval=None, TransactionSummaries=None, *args, **kw_args):
        """Initializes a new 'Shift' instance.

        @param transactionsGrandTotalRounding: Cumulative amount in error due to process rounding not reflected in transactionsGandTotal. Values are obtained from Transaction attributes: =sum(Transaction.transactionRounding). 
        @param transactionsGrandTotal: Cumulative total of transacted amounts during this shift. Values are obtained from Transaction attributes: =sum(Transaction.transactionAmount). It must also reconcile against TransactionSummary: =sum(TransactionSummary.transactionsTotal). 
        @param receiptsGrandTotalBankable: Total of amounts receipted during this shift that can be manually banked (cash and cheques for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = true. 
        @param receiptsGrandTotalRounding: Cumulative amount in error due to process rounding not reflected in receiptsGrandTotal. Values are obtained from Receipt attributes: =sum(Receipt.receiptRounding). 
        @param receiptsGrandTotalNonBankable: Total of amounts receipted during this shift that cannot be manually banked (card payments for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = false. 
        @param ReceiptSummaries: All receipt summaries for this shift.
        @param activityInterval: Interval for activity of this shift.
        @param TransactionSummaries: All transaction summaries recorded for this shift.
        """
        #: Cumulative amount in error due to process rounding not reflected in transactionsGandTotal. Values are obtained from Transaction attributes: =sum(Transaction.transactionRounding).
        self.transactionsGrandTotalRounding = transactionsGrandTotalRounding

        #: Cumulative total of transacted amounts during this shift. Values are obtained from Transaction attributes: =sum(Transaction.transactionAmount). It must also reconcile against TransactionSummary: =sum(TransactionSummary.transactionsTotal).
        self.transactionsGrandTotal = transactionsGrandTotal

        #: Total of amounts receipted during this shift that can be manually banked (cash and cheques for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = true.
        self.receiptsGrandTotalBankable = receiptsGrandTotalBankable

        #: Cumulative amount in error due to process rounding not reflected in receiptsGrandTotal. Values are obtained from Receipt attributes: =sum(Receipt.receiptRounding).
        self.receiptsGrandTotalRounding = receiptsGrandTotalRounding

        #: Total of amounts receipted during this shift that cannot be manually banked (card payments for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = false.
        self.receiptsGrandTotalNonBankable = receiptsGrandTotalNonBankable

        self._ReceiptSummaries = []
        self.ReceiptSummaries = [] if ReceiptSummaries is None else ReceiptSummaries

        self.activityInterval = activityInterval

        self._TransactionSummaries = []
        self.TransactionSummaries = [] if TransactionSummaries is None else TransactionSummaries

        super(Shift, self).__init__(*args, **kw_args)

    def getReceiptSummaries(self):
        """All receipt summaries for this shift.
        """
        return self._ReceiptSummaries

    def setReceiptSummaries(self, value):
        for x in self._ReceiptSummaries:
            x._Shift = None
        for y in value:
            y._Shift = self
        self._ReceiptSummaries = value

    ReceiptSummaries = property(getReceiptSummaries, setReceiptSummaries)

    def addReceiptSummaries(self, *ReceiptSummaries):
        for obj in ReceiptSummaries:
            obj._Shift = self
            self._ReceiptSummaries.append(obj)

    def removeReceiptSummaries(self, *ReceiptSummaries):
        for obj in ReceiptSummaries:
            obj._Shift = None
            self._ReceiptSummaries.remove(obj)

    # Interval for activity of this shift.
    activityInterval = None

    def getTransactionSummaries(self):
        """All transaction summaries recorded for this shift.
        """
        return self._TransactionSummaries

    def setTransactionSummaries(self, value):
        for x in self._TransactionSummaries:
            x._Shift = None
        for y in value:
            y._Shift = self
        self._TransactionSummaries = value

    TransactionSummaries = property(getTransactionSummaries, setTransactionSummaries)

    def addTransactionSummaries(self, *TransactionSummaries):
        for obj in TransactionSummaries:
            obj._Shift = self
            self._TransactionSummaries.append(obj)

    def removeTransactionSummaries(self, *TransactionSummaries):
        for obj in TransactionSummaries:
            obj._Shift = None
            self._TransactionSummaries.remove(obj)

