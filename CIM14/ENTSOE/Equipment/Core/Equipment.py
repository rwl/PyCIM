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

from CIM14.ENTSOE.Equipment.Core.PowerSystemResource import PowerSystemResource

class Equipment(PowerSystemResource):
    """The parts of a power system that are physical devices, electronic or mechanical
    """

    def __init__(self, aggregate=False, OperationalLimitSet=None, EquipmentContainer=None, *args, **kw_args):
        """Initialises a new 'Equipment' instance.

        @param aggregate: The single instance of equipment represents multiple pieces of equipment that have been modeled together as an aggregate.  Examples would be PowerTransformers or SychronousMachines operating in parallel modeled as a single aggregate PowerTransformer or aggregate SynchronousMachine.  This is not to be used to indicate equipment that is part of a group of interdependent equipment produced by a network production program.For ENTSO-E, the TSOs will use this flag for equivalent equipment. This Boolean flag indicates that this equipment (element) of the power system model is obtained by a network reduction procedure.  If the flag is set to 'true', the equipment is treated as an equivalent.  This flag provides an alternative way of representing an aggregated (equivalent) element by allowing usage of all available attributes for a given class instead of usage of dedicated classes for equivalent equipment that have a limited number of attributes.  Do not use this attribute for TransformerWinding, BusBarSection, EquivalentBranch, EquivalentShunt and EquivalentInjection. 
        @param OperationalLimitSet: The equipment limit sets associated with the equipment.
        @param EquipmentContainer: The association is used in the naming hierarchy.
        """
        #: The single instance of equipment represents multiple pieces of equipment that have been modeled together as an aggregate.  Examples would be PowerTransformers or SychronousMachines operating in parallel modeled as a single aggregate PowerTransformer or aggregate SynchronousMachine.  This is not to be used to indicate equipment that is part of a group of interdependent equipment produced by a network production program.For ENTSO-E, the TSOs will use this flag for equivalent equipment. This Boolean flag indicates that this equipment (element) of the power system model is obtained by a network reduction procedure.  If the flag is set to 'true', the equipment is treated as an equivalent.  This flag provides an alternative way of representing an aggregated (equivalent) element by allowing usage of all available attributes for a given class instead of usage of dedicated classes for equivalent equipment that have a limited number of attributes.  Do not use this attribute for TransformerWinding, BusBarSection, EquivalentBranch, EquivalentShunt and EquivalentInjection.
        self.aggregate = aggregate

        self._OperationalLimitSet = []
        self.OperationalLimitSet = [] if OperationalLimitSet is None else OperationalLimitSet

        self._EquipmentContainer = None
        self.EquipmentContainer = EquipmentContainer

        super(Equipment, self).__init__(*args, **kw_args)

    _attrs = ["aggregate"]
    _attr_types = {"aggregate": bool}
    _defaults = {"aggregate": False}
    _enums = {}
    _refs = ["OperationalLimitSet", "EquipmentContainer"]
    _many_refs = ["OperationalLimitSet"]

    def getOperationalLimitSet(self):
        """The equipment limit sets associated with the equipment.
        """
        return self._OperationalLimitSet

    def setOperationalLimitSet(self, value):
        for x in self._OperationalLimitSet:
            x.Equipment = None
        for y in value:
            y._Equipment = self
        self._OperationalLimitSet = value

    OperationalLimitSet = property(getOperationalLimitSet, setOperationalLimitSet)

    def addOperationalLimitSet(self, *OperationalLimitSet):
        for obj in OperationalLimitSet:
            obj.Equipment = self

    def removeOperationalLimitSet(self, *OperationalLimitSet):
        for obj in OperationalLimitSet:
            obj.Equipment = None

    def getEquipmentContainer(self):
        """The association is used in the naming hierarchy.
        """
        return self._EquipmentContainer

    def setEquipmentContainer(self, value):
        if self._EquipmentContainer is not None:
            filtered = [x for x in self.EquipmentContainer.Equipments if x != self]
            self._EquipmentContainer._Equipments = filtered

        self._EquipmentContainer = value
        if self._EquipmentContainer is not None:
            if self not in self._EquipmentContainer._Equipments:
                self._EquipmentContainer._Equipments.append(self)

    EquipmentContainer = property(getEquipmentContainer, setEquipmentContainer)

