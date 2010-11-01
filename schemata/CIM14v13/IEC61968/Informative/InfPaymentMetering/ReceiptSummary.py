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

class ReceiptSummary(Element):
    """Record of detail of receipts pertaining to one shift of operation (one record per 'tenderKind').
    """

    def __init__(self, tenderKind='cheque', Shift=None, line=None, *args, **kw_args):
        """Initializes a new 'ReceiptSummary' instance.

        @param tenderKind: 'Tender.kind' for which 'receiptsTotal' is given. Values are: "cheque", "card", "other", "unspecified", "cash"
        @param Shift: Shift for which this summary is given.
        @param line: Totalised amount receipted during the shift for 'tenderKind', i.e., sum of ('Tender.amount' - 'Tender.change') per 'Tender.kind'.
        """
        #: 'Tender.kind' for which 'receiptsTotal' is given. Values are: "cheque", "card", "other", "unspecified", "cash"
        self.tenderKind = tenderKind

        self._Shift = None
        self.Shift = Shift

        self.line = line

        super(ReceiptSummary, self).__init__(*args, **kw_args)

    def getShift(self):
        """Shift for which this summary is given.
        """
        return self._Shift

    def setShift(self, value):
        if self._Shift is not None:
            filtered = [x for x in self.Shift.ReceiptSummaries if x != self]
            self._Shift._ReceiptSummaries = filtered

        self._Shift = value
        if self._Shift is not None:
            self._Shift._ReceiptSummaries.append(self)

    Shift = property(getShift, setShift)

    # Totalised amount receipted during the shift for 'tenderKind', i.e., sum of ('Tender.amount' - 'Tender.change') per 'Tender.kind'.
    line = None

