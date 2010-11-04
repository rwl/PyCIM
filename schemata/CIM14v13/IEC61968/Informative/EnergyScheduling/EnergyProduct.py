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

from CIM14v13.IEC61968.Common.Agreement import Agreement

class EnergyProduct(Agreement):
    """An EnergyProduct is offered commercially as a ContractOrTariff.
    """

    def __init__(self, ServicePoint=None, GenerationProvider=None, EnergyTransactions=None, ResoldBy_Marketers=None, TitleHeldBy_Marketer=None, **kw_args):
        """Initializes a new 'EnergyProduct' instance.

        @param ServicePoint: An EnergyProduct injects energy into a service point.
        @param GenerationProvider:
        @param EnergyTransactions: The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.
        @param ResoldBy_Marketers: A Marketer may resell an EnergyProduct.
        @param TitleHeldBy_Marketer: A Marketer holds title to an EnergyProduct.
        """
        self._ServicePoint = []
        self.ServicePoint = [] if ServicePoint is None else ServicePoint

        self._GenerationProvider = None
        self.GenerationProvider = GenerationProvider

        self._EnergyTransactions = []
        self.EnergyTransactions = [] if EnergyTransactions is None else EnergyTransactions

        self._ResoldBy_Marketers = []
        self.ResoldBy_Marketers = [] if ResoldBy_Marketers is None else ResoldBy_Marketers

        self._TitleHeldBy_Marketer = None
        self.TitleHeldBy_Marketer = TitleHeldBy_Marketer

        super(EnergyProduct, self).__init__(**kw_args)

    def getServicePoint(self):
        """An EnergyProduct injects energy into a service point.
        """
        return self._ServicePoint

    def setServicePoint(self, value):
        for p in self._ServicePoint:
            filtered = [q for q in p.EnergyProducts if q != self]
            self._ServicePoint._EnergyProducts = filtered
        for r in value:
            if self not in r._EnergyProducts:
                r._EnergyProducts.append(self)
        self._ServicePoint = value

    ServicePoint = property(getServicePoint, setServicePoint)

    def addServicePoint(self, *ServicePoint):
        for obj in ServicePoint:
            if self not in obj._EnergyProducts:
                obj._EnergyProducts.append(self)
            self._ServicePoint.append(obj)

    def removeServicePoint(self, *ServicePoint):
        for obj in ServicePoint:
            if self in obj._EnergyProducts:
                obj._EnergyProducts.remove(self)
            self._ServicePoint.remove(obj)

    def getGenerationProvider(self):
        
        return self._GenerationProvider

    def setGenerationProvider(self, value):
        if self._GenerationProvider is not None:
            filtered = [x for x in self.GenerationProvider.EnergyProducts if x != self]
            self._GenerationProvider._EnergyProducts = filtered

        self._GenerationProvider = value
        if self._GenerationProvider is not None:
            self._GenerationProvider._EnergyProducts.append(self)

    GenerationProvider = property(getGenerationProvider, setGenerationProvider)

    def getEnergyTransactions(self):
        """The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.
        """
        return self._EnergyTransactions

    def setEnergyTransactions(self, value):
        for x in self._EnergyTransactions:
            x._EnergyProduct = None
        for y in value:
            y._EnergyProduct = self
        self._EnergyTransactions = value

    EnergyTransactions = property(getEnergyTransactions, setEnergyTransactions)

    def addEnergyTransactions(self, *EnergyTransactions):
        for obj in EnergyTransactions:
            obj._EnergyProduct = self
            self._EnergyTransactions.append(obj)

    def removeEnergyTransactions(self, *EnergyTransactions):
        for obj in EnergyTransactions:
            obj._EnergyProduct = None
            self._EnergyTransactions.remove(obj)

    def getResoldBy_Marketers(self):
        """A Marketer may resell an EnergyProduct.
        """
        return self._ResoldBy_Marketers

    def setResoldBy_Marketers(self, value):
        for p in self._ResoldBy_Marketers:
            filtered = [q for q in p.Resells_EnergyProduct if q != self]
            self._ResoldBy_Marketers._Resells_EnergyProduct = filtered
        for r in value:
            if self not in r._Resells_EnergyProduct:
                r._Resells_EnergyProduct.append(self)
        self._ResoldBy_Marketers = value

    ResoldBy_Marketers = property(getResoldBy_Marketers, setResoldBy_Marketers)

    def addResoldBy_Marketers(self, *ResoldBy_Marketers):
        for obj in ResoldBy_Marketers:
            if self not in obj._Resells_EnergyProduct:
                obj._Resells_EnergyProduct.append(self)
            self._ResoldBy_Marketers.append(obj)

    def removeResoldBy_Marketers(self, *ResoldBy_Marketers):
        for obj in ResoldBy_Marketers:
            if self in obj._Resells_EnergyProduct:
                obj._Resells_EnergyProduct.remove(self)
            self._ResoldBy_Marketers.remove(obj)

    def getTitleHeldBy_Marketer(self):
        """A Marketer holds title to an EnergyProduct.
        """
        return self._TitleHeldBy_Marketer

    def setTitleHeldBy_Marketer(self, value):
        if self._TitleHeldBy_Marketer is not None:
            filtered = [x for x in self.TitleHeldBy_Marketer.HoldsTitleTo_EnergyProducts if x != self]
            self._TitleHeldBy_Marketer._HoldsTitleTo_EnergyProducts = filtered

        self._TitleHeldBy_Marketer = value
        if self._TitleHeldBy_Marketer is not None:
            self._TitleHeldBy_Marketer._HoldsTitleTo_EnergyProducts.append(self)

    TitleHeldBy_Marketer = property(getTitleHeldBy_Marketer, setTitleHeldBy_Marketer)

