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

class ChargeRegister(IdentifiedObject):
    """Accumulated charges transacted per ChargeKind for a given function. There could be several of these registers, one for each ChargeKind; depending on the application.
    """

    def __init__(self, chargeKind='other', chargeAmount=None, SPAccountingFunction=None, *args, **kw_args):
        """Initializes a new 'ChargeRegister' instance.

        @param chargeKind: Several different types of charges are typically implemented in the case of a prepayment meter. For example: a charge according to a tariff for consumption and possibly a demand component, or a charge for a debt that is loaded in the meter to be recovered on a time basis, or a standing charge to be levied at the end of each billing period, or a tax charge loaded in the meter to be recovered on a consumption basis or a time basis. Values are: "other", "auxiliaryCharge", "demandCharge", "taxCharge", "consumptionCharge"
        @param chargeAmount: Charge amount in favour of the supplier. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
        @param SPAccountingFunction:
        """
        #: Several different types of charges are typically implemented in the case of a prepayment meter. For example: a charge according to a tariff for consumption and possibly a demand component, or a charge for a debt that is loaded in the meter to be recovered on a time basis, or a standing charge to be levied at the end of each billing period, or a tax charge loaded in the meter to be recovered on a consumption basis or a time basis. Values are: "other", "auxiliaryCharge", "demandCharge", "taxCharge", "consumptionCharge"
        self.chargeKind = chargeKind

        self.chargeAmount = chargeAmount

        self._SPAccountingFunction = None
        self.SPAccountingFunction = SPAccountingFunction

        super(ChargeRegister, self).__init__(*args, **kw_args)

    # Charge amount in favour of the supplier. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
    chargeAmount = None

    def getSPAccountingFunction(self):
        
        return self._SPAccountingFunction

    def setSPAccountingFunction(self, value):
        if self._SPAccountingFunction is not None:
            filtered = [x for x in self.SPAccountingFunction.ChargeRegisters if x != self]
            self._SPAccountingFunction._ChargeRegisters = filtered

        self._SPAccountingFunction = value
        if self._SPAccountingFunction is not None:
            self._SPAccountingFunction._ChargeRegisters.append(self)

    SPAccountingFunction = property(getSPAccountingFunction, setSPAccountingFunction)

