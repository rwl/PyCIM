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

from CIM16.IEC61970.Core.PowerSystemResource import PowerSystemResource

class Equipment(PowerSystemResource):
    """The parts of a power system that are physical devices, electronic or mechanicalThe parts of a power system that are physical devices, electronic or mechanical
    """

    def __init__(self, normallyInService=False, aggregate=False, ContingencyEquipment=None, CustomerAgreements=None, EquipmentContainer=None, *args, **kw_args):
        """Initialises a new 'Equipment' instance.

        @param normallyInService: The equipment is normally in service. 
        @param aggregate: The single instance of equipment represents multiple pieces of equipment that have been modeled together as an aggregate.  Examples would be PowerTransformers or SychronousMachines operating in parallel modeled as a single aggregate PowerTransformer or aggregate SynchronousMachine.  This is not to be used to indicate equipment that is part of a group of interdependent equipment produced by a network production program. 
        @param ContingencyEquipment: The contingency element associated with the equipment.
        @param CustomerAgreements:
        @param EquipmentContainer: The association is used in the naming hierarchy.
        """
        #: The equipment is normally in service.
        self.normallyInService = normallyInService

        #: The single instance of equipment represents multiple pieces of equipment that have been modeled together as an aggregate.  Examples would be PowerTransformers or SychronousMachines operating in parallel modeled as a single aggregate PowerTransformer or aggregate SynchronousMachine.  This is not to be used to indicate equipment that is part of a group of interdependent equipment produced by a network production program.
        self.aggregate = aggregate

        self._ContingencyEquipment = []
        self.ContingencyEquipment = [] if ContingencyEquipment is None else ContingencyEquipment

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._EquipmentContainer = None
        self.EquipmentContainer = EquipmentContainer

        super(Equipment, self).__init__(*args, **kw_args)

    _attrs = ["normallyInService", "aggregate"]
    _attr_types = {"normallyInService": bool, "aggregate": bool}
    _defaults = {"normallyInService": False, "aggregate": False}
    _enums = {}
    _refs = ["ContingencyEquipment", "CustomerAgreements", "EquipmentContainer"]
    _many_refs = ["ContingencyEquipment", "CustomerAgreements"]

    def getContingencyEquipment(self):
        """The contingency element associated with the equipment.
        """
        return self._ContingencyEquipment

    def setContingencyEquipment(self, value):
        for x in self._ContingencyEquipment:
            x.Equipment = None
        for y in value:
            y._Equipment = self
        self._ContingencyEquipment = value

    ContingencyEquipment = property(getContingencyEquipment, setContingencyEquipment)

    def addContingencyEquipment(self, *ContingencyEquipment):
        for obj in ContingencyEquipment:
            obj.Equipment = self

    def removeContingencyEquipment(self, *ContingencyEquipment):
        for obj in ContingencyEquipment:
            obj.Equipment = None

    def getCustomerAgreements(self):
        
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for p in self._CustomerAgreements:
            filtered = [q for q in p.Equipments if q != self]
            self._CustomerAgreements._Equipments = filtered
        for r in value:
            if self not in r._Equipments:
                r._Equipments.append(self)
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            if self not in obj._Equipments:
                obj._Equipments.append(self)
            self._CustomerAgreements.append(obj)

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            if self in obj._Equipments:
                obj._Equipments.remove(self)
            self._CustomerAgreements.remove(obj)

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

