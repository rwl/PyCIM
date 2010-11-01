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

class CreditRegister(IdentifiedObject):
    """Accumulated credits transacted per CreditKind for a given function. There could be several of these registers, one for each CreditKind; depending on the application.
    """

    def __init__(self, creditKind='other', creditAmount=None, SDPAccountingFunction=None, *args, **kw_args):
        """Initializes a new 'CreditRegister' instance.

        @param creditKind: Several different types of credit are typically implemented in the case of a prepayment meter.  For example: credit transferred by means of a token carrier, or credit advanced automatically inside the meter under certain conditions, or credit held in reserved to be released under emergency conditions, or credit granted by local authority as a basic life support mechanism and may be dispensed automatically by the meter under certain conditions or credit available under severe climate conditions such as during winter over a weekend. Values are: "other", "reserveCredit", "lifelineCredit", "advanceCredit", "tokenCredit", "grantCredit"
        @param creditAmount: Credit amount in favour of the customer. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
        @param SDPAccountingFunction:
        """
        #: Several different types of credit are typically implemented in the case of a prepayment meter.  For example: credit transferred by means of a token carrier, or credit advanced automatically inside the meter under certain conditions, or credit held in reserved to be released under emergency conditions, or credit granted by local authority as a basic life support mechanism and may be dispensed automatically by the meter under certain conditions or credit available under severe climate conditions such as during winter over a weekend. Values are: "other", "reserveCredit", "lifelineCredit", "advanceCredit", "tokenCredit", "grantCredit"
        self.creditKind = creditKind

        self.creditAmount = creditAmount

        self._SDPAccountingFunction = None
        self.SDPAccountingFunction = SDPAccountingFunction

        super(CreditRegister, self).__init__(*args, **kw_args)

    # Credit amount in favour of the customer. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
    creditAmount = None

    def getSDPAccountingFunction(self):
        
        return self._SDPAccountingFunction

    def setSDPAccountingFunction(self, value):
        if self._SDPAccountingFunction is not None:
            filtered = [x for x in self.SDPAccountingFunction.CreditRegisters if x != self]
            self._SDPAccountingFunction._CreditRegisters = filtered

        self._SDPAccountingFunction = value
        if self._SDPAccountingFunction is not None:
            self._SDPAccountingFunction._CreditRegisters.append(self)

    SDPAccountingFunction = property(getSDPAccountingFunction, setSDPAccountingFunction)

