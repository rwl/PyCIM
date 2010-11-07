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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Shift(IdentifiedObject):
    """Generally referring to a period of operation or work performed. Whether shift is open/closed can be derived from attributes 'activiryInterval.start' and 'activityInterval.end'. The grand total for receipts (i.e., cumulative total of all actual receipted amounts during this shift; bankable + non-bankable; excludes rounding error totals) can be derived from Receipt attributes: =sum(Receipt.receiptAmount) ; includes bankable and non-bankable receipts. Must also reconcile against: =sum(receiptsGrandTotalBankable + receiptsGrandTotalNonBankable). Must also reconcile against ReceiptSummary: =sum(ReceiptSummary.receiptsTotal). The attributes with 'GrandTotal' defined in this class may need to be used when the source data is periodically flushed from the system and then these cannot be derived.
    """

    def __init__(self, receiptsGrandTotalNonBankable=0.0, receiptsGrandTotalBankable=0.0, receiptsGrandTotalRounding=0.0, transactionsGrandTotal=0.0, transactionsGrandTotalRounding=0.0, activityInterval=None, **kw_args):
        """Initializes a new 'Shift' instance.

        @param receiptsGrandTotalNonBankable: Total of amounts receipted during this shift that cannot be manually banked (card payments for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = false. 
        @param receiptsGrandTotalBankable: Total of amounts receipted during this shift that can be manually banked (cash and cheques for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = true. 
        @param receiptsGrandTotalRounding: Cumulative amount in error due to process rounding not reflected in receiptsGrandTotal. Values are obtained from Receipt attributes: =sum(Receipt.receiptRounding). 
        @param transactionsGrandTotal: Cumulative total of transacted amounts during this shift. Values are obtained from Transaction attributes: =sum(Transaction.transactionAmount). It must also reconcile against TransactionSummary: =sum(TransactionSummary.transactionsTotal). 
        @param transactionsGrandTotalRounding: Cumulative amount in error due to process rounding not reflected in transactionsGandTotal. Values are obtained from Transaction attributes: =sum(Transaction.transactionRounding). 
        @param activityInterval: Interval for activity of this shift.
        """
        #: Total of amounts receipted during this shift that cannot be manually banked (card payments for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = false.
        self.receiptsGrandTotalNonBankable = receiptsGrandTotalNonBankable

        #: Total of amounts receipted during this shift that can be manually banked (cash and cheques for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = true.
        self.receiptsGrandTotalBankable = receiptsGrandTotalBankable

        #: Cumulative amount in error due to process rounding not reflected in receiptsGrandTotal. Values are obtained from Receipt attributes: =sum(Receipt.receiptRounding).
        self.receiptsGrandTotalRounding = receiptsGrandTotalRounding

        #: Cumulative total of transacted amounts during this shift. Values are obtained from Transaction attributes: =sum(Transaction.transactionAmount). It must also reconcile against TransactionSummary: =sum(TransactionSummary.transactionsTotal).
        self.transactionsGrandTotal = transactionsGrandTotal

        #: Cumulative amount in error due to process rounding not reflected in transactionsGandTotal. Values are obtained from Transaction attributes: =sum(Transaction.transactionRounding).
        self.transactionsGrandTotalRounding = transactionsGrandTotalRounding

        self.activityInterval = activityInterval

        super(Shift, self).__init__(**kw_args)

    # Interval for activity of this shift.
    activityInterval = None

