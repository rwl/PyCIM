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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Shift(IdentifiedObject):
    """Generally referring to a period of operation or work performed. Whether shift is open/closed can be derived from attributes 'activiryInterval.start' and 'activityInterval.end'. The grand total for receipts (i.e., cumulative total of all actual receipted amounts during this shift; bankable + non-bankable; excludes rounding error totals) can be derived from receipt: =sum(Receipt.receiptAmount) ; includes bankable and non-bankable receipts. Must also reconcile against: =sum(receiptsGrandTotalBankable + receiptsGrandTotalNonBankable). Must also reconcile against ReceiptSummary: =sum(ReceiptSummary.receiptsTotal). The attributes with 'GrandTotal' defined in this class may need to be used when the source data is periodically flushed from the system and then these cannot be derived.Generally referring to a period of operation or work performed. Whether shift is open/closed can be derived from attributes 'activiryInterval.start' and 'activityInterval.end'. The grand total for receipts (i.e., cumulative total of all actual receipted amounts during this shift; bankable + non-bankable; excludes rounding error totals) can be derived from receipt: =sum(Receipt.receiptAmount) ; includes bankable and non-bankable receipts. Must also reconcile against: =sum(receiptsGrandTotalBankable + receiptsGrandTotalNonBankable). Must also reconcile against ReceiptSummary: =sum(ReceiptSummary.receiptsTotal). The attributes with 'GrandTotal' defined in this class may need to be used when the source data is periodically flushed from the system and then these cannot be derived.
    """

    def __init__(self, transactionsGrandTotal=0.0, receiptsGrandTotalBankable=0.0, receiptsGrandTotalRounding=0.0, transactionsGrandTotalRounding=0.0, receiptsGrandTotalNonBankable=0.0, activityInterval=None, *args, **kw_args):
        """Initialises a new 'Shift' instance.

        @param transactionsGrandTotal: Cumulative total of transacted amounts during this shift. Values are obtained from Transaction attributes: =sum(Transaction.transactionAmount). It must also reconcile against TransactionSummary: =sum(TransactionSummary.transactionsTotal). 
        @param receiptsGrandTotalBankable: Total of amounts receipted during this shift that can be manually banked (cash and cheques for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = true. 
        @param receiptsGrandTotalRounding: Cumulative amount in error due to process rounding not reflected in receiptsGrandTotal. Values are obtained from Receipt attributes: =sum(Receipt.receiptRounding). 
        @param transactionsGrandTotalRounding: Cumulative amount in error due to process rounding not reflected in transactionsGandTotal. Values are obtained from Transaction attributes: =sum(Transaction.transactionRounding). 
        @param receiptsGrandTotalNonBankable: Total of amounts receipted during this shift that cannot be manually banked (card payments for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = false. 
        @param activityInterval: Interval for activity of this shift.
        """
        #: Cumulative total of transacted amounts during this shift. Values are obtained from Transaction attributes: =sum(Transaction.transactionAmount). It must also reconcile against TransactionSummary: =sum(TransactionSummary.transactionsTotal).
        self.transactionsGrandTotal = transactionsGrandTotal

        #: Total of amounts receipted during this shift that can be manually banked (cash and cheques for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = true.
        self.receiptsGrandTotalBankable = receiptsGrandTotalBankable

        #: Cumulative amount in error due to process rounding not reflected in receiptsGrandTotal. Values are obtained from Receipt attributes: =sum(Receipt.receiptRounding).
        self.receiptsGrandTotalRounding = receiptsGrandTotalRounding

        #: Cumulative amount in error due to process rounding not reflected in transactionsGandTotal. Values are obtained from Transaction attributes: =sum(Transaction.transactionRounding).
        self.transactionsGrandTotalRounding = transactionsGrandTotalRounding

        #: Total of amounts receipted during this shift that cannot be manually banked (card payments for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = false.
        self.receiptsGrandTotalNonBankable = receiptsGrandTotalNonBankable

        self.activityInterval = activityInterval

        super(Shift, self).__init__(*args, **kw_args)

    _attrs = ["transactionsGrandTotal", "receiptsGrandTotalBankable", "receiptsGrandTotalRounding", "transactionsGrandTotalRounding", "receiptsGrandTotalNonBankable"]
    _attr_types = {"transactionsGrandTotal": float, "receiptsGrandTotalBankable": float, "receiptsGrandTotalRounding": float, "transactionsGrandTotalRounding": float, "receiptsGrandTotalNonBankable": float}
    _defaults = {"transactionsGrandTotal": 0.0, "receiptsGrandTotalBankable": 0.0, "receiptsGrandTotalRounding": 0.0, "transactionsGrandTotalRounding": 0.0, "receiptsGrandTotalNonBankable": 0.0}
    _enums = {}
    _refs = ["activityInterval"]
    _many_refs = []

    # Interval for activity of this shift.
    activityInterval = None

