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

class Card(Element):
    """Documentation of the tender when it is a type of card (credit, debit, etc).
    """

    def __init__(self, pan='', expiryDate='', accountHolderName='', cvNumber='', Tender=None, **kw_args):
        """Initializes a new 'Card' instance.

        @param pan: The primary account number. 
        @param expiryDate: The date when this card expires. 
        @param accountHolderName: Name of account holder. 
        @param cvNumber: The card verification number. 
        @param Tender: Payment tender this card is being used for.
        """
        #: The primary account number.
        self.pan = pan

        #: The date when this card expires.
        self.expiryDate = expiryDate

        #: Name of account holder.
        self.accountHolderName = accountHolderName

        #: The card verification number.
        self.cvNumber = cvNumber

        self._Tender = None
        self.Tender = Tender

        super(Card, self).__init__(**kw_args)

    def getTender(self):
        """Payment tender this card is being used for.
        """
        return self._Tender

    def setTender(self, value):
        if self._Tender is not None:
            self._Tender._Card = None

        self._Tender = value
        if self._Tender is not None:
            self._Tender._Card = self

    Tender = property(getTender, setTender)

