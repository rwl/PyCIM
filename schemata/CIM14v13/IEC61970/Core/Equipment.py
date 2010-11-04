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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class Equipment(PowerSystemResource):
    """The parts of a power system that are physical devices, electronic or mechanical
    """

    def __init__(self, normaIlyInService=False, ContingencyEquipment=None, CustomerAgreements=None, OperationalLimitSet=None, EquipmentContainer=None, **kw_args):
        """Initializes a new 'Equipment' instance.

        @param normaIlyInService: The equipment is normally in service. 
        @param ContingencyEquipment: The contingency element associated with the equipment.
        @param CustomerAgreements:
        @param OperationalLimitSet: The equipment limit sets associated with the equipment.
        @param EquipmentContainer: The association is used in the naming hierarchy.
        """
        #: The equipment is normally in service.
        self.normaIlyInService = normaIlyInService

        self._ContingencyEquipment = []
        self.ContingencyEquipment = [] if ContingencyEquipment is None else ContingencyEquipment

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._OperationalLimitSet = []
        self.OperationalLimitSet = [] if OperationalLimitSet is None else OperationalLimitSet

        self._EquipmentContainer = None
        self.EquipmentContainer = EquipmentContainer

        super(Equipment, self).__init__(**kw_args)

    def getContingencyEquipment(self):
        """The contingency element associated with the equipment.
        """
        return self._ContingencyEquipment

    def setContingencyEquipment(self, value):
        for x in self._ContingencyEquipment:
            x._Equipment = None
        for y in value:
            y._Equipment = self
        self._ContingencyEquipment = value

    ContingencyEquipment = property(getContingencyEquipment, setContingencyEquipment)

    def addContingencyEquipment(self, *ContingencyEquipment):
        for obj in ContingencyEquipment:
            obj._Equipment = self
            self._ContingencyEquipment.append(obj)

    def removeContingencyEquipment(self, *ContingencyEquipment):
        for obj in ContingencyEquipment:
            obj._Equipment = None
            self._ContingencyEquipment.remove(obj)

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

    def getOperationalLimitSet(self):
        """The equipment limit sets associated with the equipment.
        """
        return self._OperationalLimitSet

    def setOperationalLimitSet(self, value):
        for x in self._OperationalLimitSet:
            x._Equipment = None
        for y in value:
            y._Equipment = self
        self._OperationalLimitSet = value

    OperationalLimitSet = property(getOperationalLimitSet, setOperationalLimitSet)

    def addOperationalLimitSet(self, *OperationalLimitSet):
        for obj in OperationalLimitSet:
            obj._Equipment = self
            self._OperationalLimitSet.append(obj)

    def removeOperationalLimitSet(self, *OperationalLimitSet):
        for obj in OperationalLimitSet:
            obj._Equipment = None
            self._OperationalLimitSet.remove(obj)

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
            self._EquipmentContainer._Equipments.append(self)

    EquipmentContainer = property(getEquipmentContainer, setEquipmentContainer)

