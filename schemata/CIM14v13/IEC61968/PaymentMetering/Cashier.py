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

class Cashier(IdentifiedObject):
    """The operator of the point of sale for the duration of CashierShift. Cashier is under the exclusive management control of Vendor.
    """

    def __init__(self, ElectronicAddresses=None, CashierShifts=None, Vendor=None, **kw_args):
        """Initializes a new 'Cashier' instance.

        @param ElectronicAddresses:
        @param CashierShifts: All shifts operated by this cashier.
        @param Vendor: Vendor that manages this Cachier.
        """
        self._ElectronicAddresses = []
        self.ElectronicAddresses = [] if ElectronicAddresses is None else ElectronicAddresses

        self._CashierShifts = []
        self.CashierShifts = [] if CashierShifts is None else CashierShifts

        self._Vendor = None
        self.Vendor = Vendor

        super(Cashier, self).__init__(**kw_args)

    def getElectronicAddresses(self):
        
        return self._ElectronicAddresses

    def setElectronicAddresses(self, value):
        for x in self._ElectronicAddresses:
            x._Cashier = None
        for y in value:
            y._Cashier = self
        self._ElectronicAddresses = value

    ElectronicAddresses = property(getElectronicAddresses, setElectronicAddresses)

    def addElectronicAddresses(self, *ElectronicAddresses):
        for obj in ElectronicAddresses:
            obj._Cashier = self
            self._ElectronicAddresses.append(obj)

    def removeElectronicAddresses(self, *ElectronicAddresses):
        for obj in ElectronicAddresses:
            obj._Cashier = None
            self._ElectronicAddresses.remove(obj)

    def getCashierShifts(self):
        """All shifts operated by this cashier.
        """
        return self._CashierShifts

    def setCashierShifts(self, value):
        for x in self._CashierShifts:
            x._Cashier = None
        for y in value:
            y._Cashier = self
        self._CashierShifts = value

    CashierShifts = property(getCashierShifts, setCashierShifts)

    def addCashierShifts(self, *CashierShifts):
        for obj in CashierShifts:
            obj._Cashier = self
            self._CashierShifts.append(obj)

    def removeCashierShifts(self, *CashierShifts):
        for obj in CashierShifts:
            obj._Cashier = None
            self._CashierShifts.remove(obj)

    def getVendor(self):
        """Vendor that manages this Cachier.
        """
        return self._Vendor

    def setVendor(self, value):
        if self._Vendor is not None:
            filtered = [x for x in self.Vendor.Cashiers if x != self]
            self._Vendor._Cashiers = filtered

        self._Vendor = value
        if self._Vendor is not None:
            self._Vendor._Cashiers.append(self)

    Vendor = property(getVendor, setVendor)

