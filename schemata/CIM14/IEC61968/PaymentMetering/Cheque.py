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

from CIM14.Element import Element

class Cheque(Element):
    """The actual tender when it is a type of cheque.
    """

    def __init__(self, kind="other", micrNumber='', date='', chequeNumber='', Tender=None, bankAccountDetail=None, *args, **kw_args):
        """Initialises a new 'Cheque' instance.

        @param kind: Kind of cheque. Values are: "other", "postalOrder", "bankOrder"
        @param micrNumber: The magnetic ink character recognition number printed on the cheque. 
        @param date: Date when cheque becomes valid. 
        @param chequeNumber: Cheque reference number as printed on the cheque. 
        @param Tender: Payment tender the cheque is being used for.
        @param bankAccountDetail: Details of the account holder and bank.
        """
        #: Kind of cheque. Values are: "other", "postalOrder", "bankOrder"
        self.kind = kind

        #: The magnetic ink character recognition number printed on the cheque.
        self.micrNumber = micrNumber

        #: Date when cheque becomes valid.
        self.date = date

        #: Cheque reference number as printed on the cheque.
        self.chequeNumber = chequeNumber

        self._Tender = None
        self.Tender = Tender

        self.bankAccountDetail = bankAccountDetail

        super(Cheque, self).__init__(*args, **kw_args)

    _attrs = ["kind", "micrNumber", "date", "chequeNumber"]
    _attr_types = {"kind": str, "micrNumber": str, "date": str, "chequeNumber": str}
    _defaults = {"kind": "other", "micrNumber": '', "date": '', "chequeNumber": ''}
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
            self._Tender._Cheque = self

    Tender = property(getTender, setTender)

    # Details of the account holder and bank.
    bankAccountDetail = None

