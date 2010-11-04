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

from CIM14v13.IEC61970.Core.EquipmentContainer import EquipmentContainer

class VoltageLevel(EquipmentContainer):
    """A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """

    def __init__(self, lowVoltageLimit=0.0, highVoltageLimit=0.0, Bays=None, Substation=None, BaseVoltage=None, *args, **kw_args):
        """Initializes a new 'VoltageLevel' instance.

        @param lowVoltageLimit: The bus bar's low voltage limit 
        @param highVoltageLimit: The bus bar's high voltage limit 
        @param Bays: The association is used in the naming hierarchy.
        @param Substation: The association is used in the naming hierarchy.
        @param BaseVoltage: The base voltage used for all equipment within the VoltageLevel.
        """
        #: The bus bar's low voltage limit
        self.lowVoltageLimit = lowVoltageLimit

        #: The bus bar's high voltage limit
        self.highVoltageLimit = highVoltageLimit

        self._Bays = []
        self.Bays = [] if Bays is None else Bays

        self._Substation = None
        self.Substation = Substation

        self._BaseVoltage = None
        self.BaseVoltage = BaseVoltage

        super(VoltageLevel, self).__init__(*args, **kw_args)

    def getBays(self):
        """The association is used in the naming hierarchy.
        """
        return self._Bays

    def setBays(self, value):
        for x in self._Bays:
            x._VoltageLevel = None
        for y in value:
            y._VoltageLevel = self
        self._Bays = value

    Bays = property(getBays, setBays)

    def addBays(self, *Bays):
        for obj in Bays:
            obj._VoltageLevel = self
            self._Bays.append(obj)

    def removeBays(self, *Bays):
        for obj in Bays:
            obj._VoltageLevel = None
            self._Bays.remove(obj)

    def getSubstation(self):
        """The association is used in the naming hierarchy.
        """
        return self._Substation

    def setSubstation(self, value):
        if self._Substation is not None:
            filtered = [x for x in self.Substation.VoltageLevels if x != self]
            self._Substation._VoltageLevels = filtered

        self._Substation = value
        if self._Substation is not None:
            self._Substation._VoltageLevels.append(self)

    Substation = property(getSubstation, setSubstation)

    def getBaseVoltage(self):
        """The base voltage used for all equipment within the VoltageLevel.
        """
        return self._BaseVoltage

    def setBaseVoltage(self, value):
        if self._BaseVoltage is not None:
            filtered = [x for x in self.BaseVoltage.VoltageLevel if x != self]
            self._BaseVoltage._VoltageLevel = filtered

        self._BaseVoltage = value
        if self._BaseVoltage is not None:
            self._BaseVoltage._VoltageLevel.append(self)

    BaseVoltage = property(getBaseVoltage, setBaseVoltage)

