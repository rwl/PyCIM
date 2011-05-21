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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BaseVoltage(IdentifiedObject):
    """Defines a nominal base voltage which is referenced in the system.
    """

    def __init__(self, nominalVoltage=0.0, isDC=False, ConductingEquipment=None, VoltageLevel=None, TopologicalNode=None, *args, **kw_args):
        """Initialises a new 'BaseVoltage' instance.

        @param nominalVoltage: The PowerSystemResource's base voltage. 
        @param isDC: If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current. 
        @param ConductingEquipment: Use association to ConductingEquipment only when there is no VoltageLevel container used.
        @param VoltageLevel: The VoltageLevels having this BaseVoltage.
        @param TopologicalNode: The topological nodes at the base voltage.
        """
        #: The PowerSystemResource's base voltage.
        self.nominalVoltage = nominalVoltage

        #: If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.
        self.isDC = isDC

        self._ConductingEquipment = []
        self.ConductingEquipment = [] if ConductingEquipment is None else ConductingEquipment

        self._VoltageLevel = []
        self.VoltageLevel = [] if VoltageLevel is None else VoltageLevel

        self._TopologicalNode = []
        self.TopologicalNode = [] if TopologicalNode is None else TopologicalNode

        super(BaseVoltage, self).__init__(*args, **kw_args)

    _attrs = ["nominalVoltage", "isDC"]
    _attr_types = {"nominalVoltage": float, "isDC": bool}
    _defaults = {"nominalVoltage": 0.0, "isDC": False}
    _enums = {}
    _refs = ["ConductingEquipment", "VoltageLevel", "TopologicalNode"]
    _many_refs = ["ConductingEquipment", "VoltageLevel", "TopologicalNode"]

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

    def getTopologicalNode(self):
        """The topological nodes at the base voltage.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        for x in self._TopologicalNode:
            x.BaseVoltage = None
        for y in value:
            y._BaseVoltage = self
        self._TopologicalNode = value

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

    def addTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj.BaseVoltage = self

    def removeTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj.BaseVoltage = None

