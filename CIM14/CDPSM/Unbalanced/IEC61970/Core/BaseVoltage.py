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

from CIM14.CDPSM.Unbalanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BaseVoltage(IdentifiedObject):
    """Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.
    """

    def __init__(self, nominalVoltage=0.0, ConductingEquipment=None, VoltageLevel=None, *args, **kw_args):
        """Initialises a new 'BaseVoltage' instance.

        @param nominalVoltage: The PowerSystemResource's base voltage. 
        @param ConductingEquipment: Use association to ConductingEquipment only when there is no VoltageLevel container used.
        @param VoltageLevel: The VoltageLevels having this BaseVoltage.
        """
        #: The PowerSystemResource's base voltage.
        self.nominalVoltage = nominalVoltage

        self._ConductingEquipment = []
        self.ConductingEquipment = [] if ConductingEquipment is None else ConductingEquipment

        self._VoltageLevel = []
        self.VoltageLevel = [] if VoltageLevel is None else VoltageLevel

        super(BaseVoltage, self).__init__(*args, **kw_args)

    _attrs = ["nominalVoltage"]
    _attr_types = {"nominalVoltage": float}
    _defaults = {"nominalVoltage": 0.0}
    _enums = {}
    _refs = ["ConductingEquipment", "VoltageLevel"]
    _many_refs = ["ConductingEquipment", "VoltageLevel"]

    def getConductingEquipment(self):
        """Use association to ConductingEquipment only when there is no VoltageLevel container used.
        """
        return self._ConductingEquipment

    def setConductingEquipment(self, value):
        for x in self._ConductingEquipment:
            x.BaseVoltage = None
        for y in value:
            y._BaseVoltage = self
        self._ConductingEquipment = value

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

    def addConductingEquipment(self, *ConductingEquipment):
        for obj in ConductingEquipment:
            obj.BaseVoltage = self

    def removeConductingEquipment(self, *ConductingEquipment):
        for obj in ConductingEquipment:
            obj.BaseVoltage = None

    def getVoltageLevel(self):
        """The VoltageLevels having this BaseVoltage.
        """
        return self._VoltageLevel

    def setVoltageLevel(self, value):
        for x in self._VoltageLevel:
            x.BaseVoltage = None
        for y in value:
            y._BaseVoltage = self
        self._VoltageLevel = value

    VoltageLevel = property(getVoltageLevel, setVoltageLevel)

    def addVoltageLevel(self, *VoltageLevel):
        for obj in VoltageLevel:
            obj.BaseVoltage = self

    def removeVoltageLevel(self, *VoltageLevel):
        for obj in VoltageLevel:
            obj.BaseVoltage = None

