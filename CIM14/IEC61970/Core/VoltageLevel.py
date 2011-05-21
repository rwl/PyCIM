# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.IEC61970.Core.EquipmentContainer import EquipmentContainer

class VoltageLevel(EquipmentContainer):
    """A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """

    def __init__(self, highVoltageLimit=0.0, lowVoltageLimit=0.0, Substation=None, Bays=None, BaseVoltage=None, *args, **kw_args):
        """Initialises a new 'VoltageLevel' instance.

        @param highVoltageLimit: The bus bar's high voltage limit 
        @param lowVoltageLimit: The bus bar's low voltage limit 
        @param Substation: The association is used in the naming hierarchy.
        @param Bays: The association is used in the naming hierarchy.
        @param BaseVoltage: The base voltage used for all equipment within the VoltageLevel.
        """
        #: The bus bar's high voltage limit
        self.highVoltageLimit = highVoltageLimit

        #: The bus bar's low voltage limit
        self.lowVoltageLimit = lowVoltageLimit

        self._Substation = None
        self.Substation = Substation

        self._Bays = []
        self.Bays = [] if Bays is None else Bays

        self._BaseVoltage = None
        self.BaseVoltage = BaseVoltage

        super(VoltageLevel, self).__init__(*args, **kw_args)

    _attrs = ["highVoltageLimit", "lowVoltageLimit"]
    _attr_types = {"highVoltageLimit": float, "lowVoltageLimit": float}
    _defaults = {"highVoltageLimit": 0.0, "lowVoltageLimit": 0.0}
    _enums = {}
    _refs = ["Substation", "Bays", "BaseVoltage"]
    _many_refs = ["Bays"]

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
            if self not in self._Substation._VoltageLevels:
                self._Substation._VoltageLevels.append(self)

    Substation = property(getSubstation, setSubstation)

    def getBays(self):
        """The association is used in the naming hierarchy.
        """
        return self._Bays

    def setBays(self, value):
        for x in self._Bays:
            x.VoltageLevel = None
        for y in value:
            y._VoltageLevel = self
        self._Bays = value

    Bays = property(getBays, setBays)

    def addBays(self, *Bays):
        for obj in Bays:
            obj.VoltageLevel = self

    def removeBays(self, *Bays):
        for obj in Bays:
            obj.VoltageLevel = None

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
            if self not in self._BaseVoltage._VoltageLevel:
                self._BaseVoltage._VoltageLevel.append(self)

    BaseVoltage = property(getBaseVoltage, setBaseVoltage)

