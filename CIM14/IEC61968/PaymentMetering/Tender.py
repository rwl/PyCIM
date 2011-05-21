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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Tender(IdentifiedObject):
    """Tender is what is 'offered' by the customer towards making a payment and is often more than the required payment (hence the need for 'change'). The payment is thus that part of the Tender that goes towards settlement of a particular transaction. Tender is modelled as an aggregation of Cheque and Card. Both these tender types can exist in a single tender bid thus 'accountHolderName' must exist separately in each of Cheque and Card as each could have a different account holder name.
    """

    def __init__(self, kind="cash", amount=0.0, change=0.0, Cheque=None, Receipt=None, Card=None, *args, **kw_args):
        """Initialises a new 'Tender' instance.

        @param kind: Kind of tender from customer. Values are: "cash", "unspecified", "card", "other", "cheque"
        @param amount: Amount tendered by customer. 
        @param change: Difference between amount tendered by customer and the amount charged by point of sale. 
        @param Cheque: Cheque used to tender payment.
        @param Receipt: Receipt that recorded this receiving of a payment in the form of tenders.
        @param Card: Card used to tender payment.
        """
        #: Kind of tender from customer. Values are: "cash", "unspecified", "card", "other", "cheque"
        self.kind = kind

        #: Amount tendered by customer.
        self.amount = amount

        #: Difference between amount tendered by customer and the amount charged by point of sale.
        self.change = change

        self._Cheque = None
        self.Cheque = Cheque

        self._Receipt = None
        self.Receipt = Receipt

        self._Card = None
        self.Card = Card

        super(Tender, self).__init__(*args, **kw_args)

    _attrs = ["kind", "amount", "change"]
    _attr_types = {"kind": str, "amount": float, "change": float}
    _defaults = {"kind": "cash", "amount": 0.0, "change": 0.0}
    _enums = {"kind": "TenderKind"}
    _refs = ["Cheque", "Receipt", "Card"]
    _many_refs = []

    def getCheque(self):
        """Cheque used to tender payment.
        """
        return self._Cheque

    def setCheque(self, value):
        if self._Cheque is not None:
            self._Cheque._Tender = None

        self._Cheque = value
        if self._Cheque is not None:
            self._Cheque.Tender = None
            self._Cheque._Tender = self

    Cheque = property(getCheque, setCheque)

    def getReceipt(self):
        """Receipt that recorded this receiving of a payment in the form of tenders.
        """
        return self._Receipt

    def setReceipt(self, value):
        if self._Receipt is not None:
            filtered = [x for x in self.Receipt.Tenders if x != self]
            self._Receipt._Tenders = filtered

        self._Receipt = value
        if self._Receipt is not None:
            if self not in self._Receipt._Tenders:
                self._Receipt._Tenders.append(self)

    Receipt = property(getReceipt, setReceipt)

    def getCard(self):
        """Card used to tender payment.
        """
        return self._Card

    def setCard(self, value):
        if self._Card is not None:
            self._Card._Tender = None

        self._Card = value
        if self._Card is not None:
            self._Card.Tender = None
            self._Card._Tender = self

    Card = property(getCard, setCard)

