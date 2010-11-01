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

from CIM14v13.IEC61968.Informative.InfCommon.Role import Role

class OutageStepPsrRole(Role):
    """Roles played between Power System Resources and Outage Steps. Examples roles include: normal supply, actual supply, interrupting device, restoration device.
    """

    def __init__(self, ConductingEquipment=None, OutageStep=None, *args, **kw_args):
        """Initializes a new 'OutageStepPsrRole' instance.

        @param ConductingEquipment:
        @param OutageStep:
        """
        self._ConductingEquipment = None
        self.ConductingEquipment = ConductingEquipment

        self._OutageStep = None
        self.OutageStep = OutageStep

        super(OutageStepPsrRole, self).__init__(*args, **kw_args)

    def getConductingEquipment(self):
        
        return self._ConductingEquipment

    def setConductingEquipment(self, value):
        if self._ConductingEquipment is not None:
            filtered = [x for x in self.ConductingEquipment.OutageStepRoles if x != self]
            self._ConductingEquipment._OutageStepRoles = filtered

        self._ConductingEquipment = value
        if self._ConductingEquipment is not None:
            self._ConductingEquipment._OutageStepRoles.append(self)

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

    def getOutageStep(self):
        
        return self._OutageStep

    def setOutageStep(self, value):
        if self._OutageStep is not None:
            filtered = [x for x in self.OutageStep.ConductingEquipmentRoles if x != self]
            self._OutageStep._ConductingEquipmentRoles = filtered

        self._OutageStep = value
        if self._OutageStep is not None:
            self._OutageStep._ConductingEquipmentRoles.append(self)

    OutageStep = property(getOutageStep, setOutageStep)

