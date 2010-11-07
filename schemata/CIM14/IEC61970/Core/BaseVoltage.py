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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BaseVoltage(IdentifiedObject):
    """Defines a nominal base voltage which is referenced in the system.
    """

    def __init__(self, nominalVoltage=0.0, isDC=False, ConductingEquipment=None, VoltageLevel=None, TopologicalNode=None, **kw_args):
        """Initializes a new 'BaseVoltage' instance.

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

        super(BaseVoltage, self).__init__(**kw_args)

    def getConductingEquipment(self):
        """Use association to ConductingEquipment only when there is no VoltageLevel container used.
        """
        return self._ConductingEquipment

    def setConductingEquipment(self, value):
        for x in self._ConductingEquipment:
            x._BaseVoltage = None
        for y in value:
            y._BaseVoltage = self
        self._ConductingEquipment = value

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

    def addConductingEquipment(self, *ConductingEquipment):
        for obj in ConductingEquipment:
            obj._BaseVoltage = self
            self._ConductingEquipment.append(obj)

    def removeConductingEquipment(self, *ConductingEquipment):
        for obj in ConductingEquipment:
            obj._BaseVoltage = None
            self._ConductingEquipment.remove(obj)

    def getVoltageLevel(self):
        """The VoltageLevels having this BaseVoltage.
        """
        return self._VoltageLevel

    def setVoltageLevel(self, value):
        for x in self._VoltageLevel:
            x._BaseVoltage = None
        for y in value:
            y._BaseVoltage = self
        self._VoltageLevel = value

    VoltageLevel = property(getVoltageLevel, setVoltageLevel)

    def addVoltageLevel(self, *VoltageLevel):
        for obj in VoltageLevel:
            obj._BaseVoltage = self
            self._VoltageLevel.append(obj)

    def removeVoltageLevel(self, *VoltageLevel):
        for obj in VoltageLevel:
            obj._BaseVoltage = None
            self._VoltageLevel.remove(obj)

    def getTopologicalNode(self):
        """The topological nodes at the base voltage.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        for x in self._TopologicalNode:
            x._BaseVoltage = None
        for y in value:
            y._BaseVoltage = self
        self._TopologicalNode = value

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

    def addTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj._BaseVoltage = self
            self._TopologicalNode.append(obj)

    def removeTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj._BaseVoltage = None
            self._TopologicalNode.remove(obj)

