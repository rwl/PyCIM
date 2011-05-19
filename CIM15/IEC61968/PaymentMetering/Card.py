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

from CIM15.Element import Element

class Card(Element):
    """Documentation of the tender when it is a type of card (credit, debit, etc).Documentation of the tender when it is a type of card (credit, debit, etc).
    """

    def __init__(self, cvNumber='', expiryDate='', pan='', accountHolderName='', Tender=None, *args, **kw_args):
        """Initialises a new 'Card' instance.

        @param cvNumber: The card verification number. 
        @param expiryDate: The date when this card expires. 
        @param pan: The primary account number. 
        @param accountHolderName: Name of account holder. 
        @param Tender: Payment tender this card is being used for.
        """
        #: The card verification number.
        self.cvNumber = cvNumber

        #: The date when this card expires.
        self.expiryDate = expiryDate

        #: The primary account number.
        self.pan = pan

        #: Name of account holder.
        self.accountHolderName = accountHolderName

        self._Tender = None
        self.Tender = Tender

        super(Card, self).__init__(*args, **kw_args)

    _attrs = ["cvNumber", "expiryDate", "pan", "accountHolderName"]
    _attr_types = {"cvNumber": str, "expiryDate": str, "pan": str, "accountHolderName": str}
    _defaults = {"cvNumber": '', "expiryDate": '', "pan": '', "accountHolderName": ''}
    _enums = {}
    _refs = ["Tender"]
    _many_refs = []

    def getTender(self):
        """Payment tender this card is being used for.
        """
        return self._Tender

    def setTender(self, value):
        if self._Tender is not None:
            self._Tender._Card = None

        self._Tender = value
        if self._Tender is not None:
            self._Tender.Card = None
            self._Tender._Card = self

    Tender = property(getTender, setTender)

