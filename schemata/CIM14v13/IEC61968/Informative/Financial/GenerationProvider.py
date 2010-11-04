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

class GenerationProvider(ErpOrganisation):
    """The energy seller in the energy marketplace.
    """

    def __init__(self, GeneratingUnits=None, EnergyProducts=None, ServicePoint=None, **kw_args):
        """Initializes a new 'GenerationProvider' instance.

        @param GeneratingUnits: A GenerationProvider operates one or more GeneratingUnits.
        @param EnergyProducts:
        @param ServicePoint: A GenerationProvider has one or more ServicePoints where energy is injected into the network.
        """
        self._GeneratingUnits = []
        self.GeneratingUnits = [] if GeneratingUnits is None else GeneratingUnits

        self._EnergyProducts = []
        self.EnergyProducts = [] if EnergyProducts is None else EnergyProducts

        self._ServicePoint = []
        self.ServicePoint = [] if ServicePoint is None else ServicePoint

        super(GenerationProvider, self).__init__(**kw_args)

    def getGeneratingUnits(self):
        """A GenerationProvider operates one or more GeneratingUnits.
        """
        return self._GeneratingUnits

    def setGeneratingUnits(self, value):
        for x in self._GeneratingUnits:
            x._OperatedBy_GenerationProvider = None
        for y in value:
            y._OperatedBy_GenerationProvider = self
        self._GeneratingUnits = value

    GeneratingUnits = property(getGeneratingUnits, setGeneratingUnits)

    def addGeneratingUnits(self, *GeneratingUnits):
        for obj in GeneratingUnits:
            obj._OperatedBy_GenerationProvider = self
            self._GeneratingUnits.append(obj)

    def removeGeneratingUnits(self, *GeneratingUnits):
        for obj in GeneratingUnits:
            obj._OperatedBy_GenerationProvider = None
            self._GeneratingUnits.remove(obj)

    def getEnergyProducts(self):
        
        return self._EnergyProducts

    def setEnergyProducts(self, value):
        for x in self._EnergyProducts:
            x._GenerationProvider = None
        for y in value:
            y._GenerationProvider = self
        self._EnergyProducts = value

    EnergyProducts = property(getEnergyProducts, setEnergyProducts)

    def addEnergyProducts(self, *EnergyProducts):
        for obj in EnergyProducts:
            obj._GenerationProvider = self
            self._EnergyProducts.append(obj)

    def removeEnergyProducts(self, *EnergyProducts):
        for obj in EnergyProducts:
            obj._GenerationProvider = None
            self._EnergyProducts.remove(obj)

    def getServicePoint(self):
        """A GenerationProvider has one or more ServicePoints where energy is injected into the network.
        """
        return self._ServicePoint

    def setServicePoint(self, value):
        for x in self._ServicePoint:
            x._GenerationProvider = None
        for y in value:
            y._GenerationProvider = self
        self._ServicePoint = value

    ServicePoint = property(getServicePoint, setServicePoint)

    def addServicePoint(self, *ServicePoint):
        for obj in ServicePoint:
            obj._GenerationProvider = self
            self._ServicePoint.append(obj)

    def removeServicePoint(self, *ServicePoint):
        for obj in ServicePoint:
            obj._GenerationProvider = None
            self._ServicePoint.remove(obj)

