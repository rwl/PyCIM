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

class CircuitSection(IdentifiedObject):
    """Section of circuit located between two sectionalizing devices. It may contain other circuit sections, for example, a lateral tapped off a primary.
    """

    def __init__(self, connectionKind='electricallyConnected', ConductorAssets=None, NetworkDataSets=None, PowerSystemResources=None, Circuits=None, **kw_args):
        """Initializes a new 'CircuitSection' instance.

        @param connectionKind: Kind of this circuit section. Values are: "electricallyConnected", "nominallyConnected", "other", "asBuilt"
        @param ConductorAssets:
        @param NetworkDataSets:
        @param PowerSystemResources:
        @param Circuits:
        """
        #: Kind of this circuit section.Values are: "electricallyConnected", "nominallyConnected", "other", "asBuilt"
        self.connectionKind = connectionKind

        self._ConductorAssets = []
        self.ConductorAssets = [] if ConductorAssets is None else ConductorAssets

        self._NetworkDataSets = []
        self.NetworkDataSets = [] if NetworkDataSets is None else NetworkDataSets

        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        self.Circuits = [] if Circuits is None else Circuits

        super(CircuitSection, self).__init__(**kw_args)

    def getConductorAssets(self):
        
        return self._ConductorAssets

    def setConductorAssets(self, value):
        for x in self._ConductorAssets:
            x._CircuitSection = None
        for y in value:
            y._CircuitSection = self
        self._ConductorAssets = value

    ConductorAssets = property(getConductorAssets, setConductorAssets)

    def addConductorAssets(self, *ConductorAssets):
        for obj in ConductorAssets:
            obj._CircuitSection = self
            self._ConductorAssets.append(obj)

    def removeConductorAssets(self, *ConductorAssets):
        for obj in ConductorAssets:
            obj._CircuitSection = None
            self._ConductorAssets.remove(obj)

    def getNetworkDataSets(self):
        
        return self._NetworkDataSets

    def setNetworkDataSets(self, value):
        for p in self._NetworkDataSets:
            filtered = [q for q in p.CircuitSections if q != self]
            self._NetworkDataSets._CircuitSections = filtered
        for r in value:
            if self not in r._CircuitSections:
                r._CircuitSections.append(self)
        self._NetworkDataSets = value

    NetworkDataSets = property(getNetworkDataSets, setNetworkDataSets)

    def addNetworkDataSets(self, *NetworkDataSets):
        for obj in NetworkDataSets:
            if self not in obj._CircuitSections:
                obj._CircuitSections.append(self)
            self._NetworkDataSets.append(obj)

    def removeNetworkDataSets(self, *NetworkDataSets):
        for obj in NetworkDataSets:
            if self in obj._CircuitSections:
                obj._CircuitSections.remove(self)
            self._NetworkDataSets.remove(obj)

    def getPowerSystemResources(self):
        
        return self._PowerSystemResources

    def setPowerSystemResources(self, value):
        for p in self._PowerSystemResources:
            filtered = [q for q in p.CircuitSections if q != self]
            self._PowerSystemResources._CircuitSections = filtered
        for r in value:
            if self not in r._CircuitSections:
                r._CircuitSections.append(self)
        self._PowerSystemResources = value

    PowerSystemResources = property(getPowerSystemResources, setPowerSystemResources)

    def addPowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self not in obj._CircuitSections:
                obj._CircuitSections.append(self)
            self._PowerSystemResources.append(obj)

    def removePowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self in obj._CircuitSections:
                obj._CircuitSections.remove(self)
            self._PowerSystemResources.remove(obj)

    def add_Circuits(self, *Circuits):
        for obj in Circuits:
            self.Circuits.append(obj)

    def remove_Circuits(self, *Circuits):
        for obj in Circuits:
            self.Circuits.remove(obj)

