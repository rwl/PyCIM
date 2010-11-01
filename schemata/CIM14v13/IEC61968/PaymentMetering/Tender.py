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

class Tender(IdentifiedObject):
    """Tender is what is 'offered' by the customer towards making a payment and is often more than the required payment (hence the need for 'change'). The payment is thus that part of the Tender that goes towards settlement of a particular transaction. Tender is modelled as an aggregation of Cheque and Card. Both these tender types can exist in a single tender bid thus 'accountHolderName' must exist separately in each of Cheque and Card as each could have a different account holder name.
    """

    def __init__(self, kind='cheque', amount=0.0, change=0.0, Cheque=None, Card=None, Receipt=None, *args, **kw_args):
        """Initializes a new 'Tender' instance.

        @param kind: Kind of tender from customer. Values are: "cheque", "card", "other", "unspecified", "cash"
        @param amount: Amount tendered by customer. 
        @param change: Difference between amount tendered by customer and the amount charged by point of sale. 
        @param Cheque: Cheque used to tender payment.
        @param Card: Card used to tender payment.
        @param Receipt: Receipt that recorded this receiving of a payment in the form of tenders.
        """
        #: Kind of tender from customer. Values are: "cheque", "card", "other", "unspecified", "cash"
        self.kind = kind

        #: Amount tendered by customer. 
        self.amount = amount

        #: Difference between amount tendered by customer and the amount charged by point of sale. 
        self.change = change

        self._Cheque = None
        self.Cheque = Cheque

        self._Card = None
        self.Card = Card

        self._Receipt = None
        self.Receipt = Receipt

        super(Tender, self).__init__(*args, **kw_args)

    def getCheque(self):
        """Cheque used to tender payment.
        """
        return self._Cheque

    def setCheque(self, value):
        if self._Cheque is not None:
            self._Cheque._Tender = None

        self._Cheque = value
        if self._Cheque is not None:
            self._Cheque._Tender = self

    Cheque = property(getCheque, setCheque)

    def getCard(self):
        """Card used to tender payment.
        """
        return self._Card

    def setCard(self, value):
        if self._Card is not None:
            self._Card._Tender = None

        self._Card = value
        if self._Card is not None:
            self._Card._Tender = self

    Card = property(getCard, setCard)

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
            self._Receipt._Tenders.append(self)

    Receipt = property(getReceipt, setReceipt)

