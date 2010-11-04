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

from CIM14v13.IEC61968.Metering.DeviceFunction import DeviceFunction

class SDPAccountingFunction(DeviceFunction):
    """Service delivery point accounting function, particularly for payment meter.
    """

    def __init__(self, ChargeRegisters=None, availableCredit=None, creditExpiryLevel=None, CreditRegisters=None, ServiceKind=None, lowCreditWarningLevel=None, **kw_args):
        """Initializes a new 'SDPAccountingFunction' instance.

        @param ChargeRegisters:
        @param availableCredit: The value is the balance of the sum of credits minus the sum of charges from the CreditRegisters and the ChargeRegisters. The sum might be complex function. The units are either in currency units or service units, depending on the value of accountingMode.
        @param creditExpiryLevel: The value is a predefined set point for the level of the availableCredit to reach when the service will be interrupted. In the case of a prepayment meter the interruption is typically implemented by means of an electro-mechanical switch and the value is typically set = 0. The units are either in currency units or service units, depending on the value of accountingMode.
        @param CreditRegisters:
        @param ServiceKind:
        @param lowCreditWarningLevel: The value is a predefined set point for the level of the availableCredit to reach when a warning will be indicated to the customer. It serves to warn the customer that it is time to purchase more credit in the case of a prepayment meter implementation. The units are either in currency units or service units, depending on the value of accountingMode.
        """
        self._ChargeRegisters = []
        self.ChargeRegisters = [] if ChargeRegisters is None else ChargeRegisters

        self.availableCredit = availableCredit

        self.creditExpiryLevel = creditExpiryLevel

        self._CreditRegisters = []
        self.CreditRegisters = [] if CreditRegisters is None else CreditRegisters

        self._ServiceKind = None
        self.ServiceKind = ServiceKind

        self.lowCreditWarningLevel = lowCreditWarningLevel

        super(SDPAccountingFunction, self).__init__(**kw_args)

    def getChargeRegisters(self):
        
        return self._ChargeRegisters

    def setChargeRegisters(self, value):
        for x in self._ChargeRegisters:
            x._SPAccountingFunction = None
        for y in value:
            y._SPAccountingFunction = self
        self._ChargeRegisters = value

    ChargeRegisters = property(getChargeRegisters, setChargeRegisters)

    def addChargeRegisters(self, *ChargeRegisters):
        for obj in ChargeRegisters:
            obj._SPAccountingFunction = self
            self._ChargeRegisters.append(obj)

    def removeChargeRegisters(self, *ChargeRegisters):
        for obj in ChargeRegisters:
            obj._SPAccountingFunction = None
            self._ChargeRegisters.remove(obj)

    # The value is the balance of the sum of credits minus the sum of charges from the CreditRegisters and the ChargeRegisters. The sum might be complex function. The units are either in currency units or service units, depending on the value of accountingMode.
    availableCredit = None

    # The value is a predefined set point for the level of the availableCredit to reach when the service will be interrupted. In the case of a prepayment meter the interruption is typically implemented by means of an electro-mechanical switch and the value is typically set = 0. The units are either in currency units or service units, depending on the value of accountingMode.
    creditExpiryLevel = None

    def getCreditRegisters(self):
        
        return self._CreditRegisters

    def setCreditRegisters(self, value):
        for x in self._CreditRegisters:
            x._SDPAccountingFunction = None
        for y in value:
            y._SDPAccountingFunction = self
        self._CreditRegisters = value

    CreditRegisters = property(getCreditRegisters, setCreditRegisters)

    def addCreditRegisters(self, *CreditRegisters):
        for obj in CreditRegisters:
            obj._SDPAccountingFunction = self
            self._CreditRegisters.append(obj)

    def removeCreditRegisters(self, *CreditRegisters):
        for obj in CreditRegisters:
            obj._SDPAccountingFunction = None
            self._CreditRegisters.remove(obj)

    def getServiceKind(self):
        
        return self._ServiceKind

    def setServiceKind(self, value):
        if self._ServiceKind is not None:
            filtered = [x for x in self.ServiceKind.SPAccountingFunctions if x != self]
            self._ServiceKind._SPAccountingFunctions = filtered

        self._ServiceKind = value
        if self._ServiceKind is not None:
            self._ServiceKind._SPAccountingFunctions.append(self)

    ServiceKind = property(getServiceKind, setServiceKind)

    # The value is a predefined set point for the level of the availableCredit to reach when a warning will be indicated to the customer. It serves to warn the customer that it is time to purchase more credit in the case of a prepayment meter implementation. The units are either in currency units or service units, depending on the value of accountingMode.
    lowCreditWarningLevel = None

