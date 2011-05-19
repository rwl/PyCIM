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

class Cheque(Element):
    """The actual tender when it is a type of cheque.The actual tender when it is a type of cheque.
    """

    def __init__(self, micrNumber='', chequeNumber='', date='', kind="other", Tender=None, bankAccountDetail=None, *args, **kw_args):
        """Initialises a new 'Cheque' instance.

        @param micrNumber: The magnetic ink character recognition number printed on the cheque. 
        @param chequeNumber: Cheque reference number as printed on the cheque. 
        @param date: Date when cheque becomes valid. 
        @param kind: Kind of cheque. Values are: "other", "postalOrder", "bankOrder"
        @param Tender: Payment tender the cheque is being used for.
        @param bankAccountDetail: Details of the account holder and bank.
        """
        #: The magnetic ink character recognition number printed on the cheque.
        self.micrNumber = micrNumber

        #: Cheque reference number as printed on the cheque.
        self.chequeNumber = chequeNumber

        #: Date when cheque becomes valid.
        self.date = date

        #: Kind of cheque. Values are: "other", "postalOrder", "bankOrder"
        self.kind = kind

        self._Tender = None
        self.Tender = Tender

        self.bankAccountDetail = bankAccountDetail

        super(Cheque, self).__init__(*args, **kw_args)

    _attrs = ["micrNumber", "chequeNumber", "date", "kind"]
    _attr_types = {"micrNumber": str, "chequeNumber": str, "date": str, "kind": str}
    _defaults = {"micrNumber": '', "chequeNumber": '', "date": '', "kind": "other"}
    _enums = {"kind": "ChequeKind"}
    _refs = ["Tender", "bankAccountDetail"]
    _many_refs = []

    def getTender(self):
        """Payment tender the cheque is being used for.
        """
        return self._Tender

    def setTender(self, value):
        if self._Tender is not None:
            self._Tender._Cheque = None

        self._Tender = value
        if self._Tender is not None:
            self._Tender.Cheque = None
            self._Tender._Cheque = self

    Tender = property(getTender, setTender)

    # Details of the account holder and bank.
    bankAccountDetail = None

