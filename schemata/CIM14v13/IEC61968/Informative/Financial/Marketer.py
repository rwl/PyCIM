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

from CIM14v13.IEC61968.Informative.InfERPSupport.ErpOrganisation import ErpOrganisation

class Marketer(ErpOrganisation):
    """Matches buyers and sellers, and secures transmission (and other ancillary services) needed to complete the energy transaction.
    """

    def __init__(self, HeldBy=None, ResoldBy=None, Resells_EnergyProduct=None, HoldsTitleTo_EnergyProducts=None, *args, **kw_args):
        """Initializes a new 'Marketer' instance.

        @param HeldBy: A Marketer holds title to a ServiceReservation.
        @param ResoldBy: A ServiceReservation may be resold by a Marketer.
        @param Resells_EnergyProduct: A Marketer may resell an EnergyProduct.
        @param HoldsTitleTo_EnergyProducts: A Marketer holds title to an EnergyProduct.
        """
        self._HeldBy = []
        self.HeldBy = [] if HeldBy is None else HeldBy

        self._ResoldBy = None
        self.ResoldBy = ResoldBy

        self._Resells_EnergyProduct = []
        self.Resells_EnergyProduct = [] if Resells_EnergyProduct is None else Resells_EnergyProduct

        self._HoldsTitleTo_EnergyProducts = []
        self.HoldsTitleTo_EnergyProducts = [] if HoldsTitleTo_EnergyProducts is None else HoldsTitleTo_EnergyProducts

        super(Marketer, self).__init__(*args, **kw_args)

    def getHeldBy(self):
        """A Marketer holds title to a ServiceReservation.
        """
        return self._HeldBy

    def setHeldBy(self, value):
        for x in self._HeldBy:
            x._Holds = None
        for y in value:
            y._Holds = self
        self._HeldBy = value

    HeldBy = property(getHeldBy, setHeldBy)

    def addHeldBy(self, *HeldBy):
        for obj in HeldBy:
            obj._Holds = self
            self._HeldBy.append(obj)

    def removeHeldBy(self, *HeldBy):
        for obj in HeldBy:
            obj._Holds = None
            self._HeldBy.remove(obj)

    def getResoldBy(self):
        """A ServiceReservation may be resold by a Marketer.
        """
        return self._ResoldBy

    def setResoldBy(self, value):
        if self._ResoldBy is not None:
            self._ResoldBy._Resells = None

        self._ResoldBy = value
        if self._ResoldBy is not None:
            self._ResoldBy._Resells = self

    ResoldBy = property(getResoldBy, setResoldBy)

    def getResells_EnergyProduct(self):
        """A Marketer may resell an EnergyProduct.
        """
        return self._Resells_EnergyProduct

    def setResells_EnergyProduct(self, value):
        for p in self._Resells_EnergyProduct:
            filtered = [q for q in p.ResoldBy_Marketers if q != self]
            self._Resells_EnergyProduct._ResoldBy_Marketers = filtered
        for r in value:
            if self not in r._ResoldBy_Marketers:
                r._ResoldBy_Marketers.append(self)
        self._Resells_EnergyProduct = value

    Resells_EnergyProduct = property(getResells_EnergyProduct, setResells_EnergyProduct)

    def addResells_EnergyProduct(self, *Resells_EnergyProduct):
        for obj in Resells_EnergyProduct:
            if self not in obj._ResoldBy_Marketers:
                obj._ResoldBy_Marketers.append(self)
            self._Resells_EnergyProduct.append(obj)

    def removeResells_EnergyProduct(self, *Resells_EnergyProduct):
        for obj in Resells_EnergyProduct:
            if self in obj._ResoldBy_Marketers:
                obj._ResoldBy_Marketers.remove(self)
            self._Resells_EnergyProduct.remove(obj)

    def getHoldsTitleTo_EnergyProducts(self):
        """A Marketer holds title to an EnergyProduct.
        """
        return self._HoldsTitleTo_EnergyProducts

    def setHoldsTitleTo_EnergyProducts(self, value):
        for x in self._HoldsTitleTo_EnergyProducts:
            x._TitleHeldBy_Marketer = None
        for y in value:
            y._TitleHeldBy_Marketer = self
        self._HoldsTitleTo_EnergyProducts = value

    HoldsTitleTo_EnergyProducts = property(getHoldsTitleTo_EnergyProducts, setHoldsTitleTo_EnergyProducts)

    def addHoldsTitleTo_EnergyProducts(self, *HoldsTitleTo_EnergyProducts):
        for obj in HoldsTitleTo_EnergyProducts:
            obj._TitleHeldBy_Marketer = self
            self._HoldsTitleTo_EnergyProducts.append(obj)

    def removeHoldsTitleTo_EnergyProducts(self, *HoldsTitleTo_EnergyProducts):
        for obj in HoldsTitleTo_EnergyProducts:
            obj._TitleHeldBy_Marketer = None
            self._HoldsTitleTo_EnergyProducts.remove(obj)

