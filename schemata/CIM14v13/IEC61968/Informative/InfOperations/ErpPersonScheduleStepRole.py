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

class ErpPersonScheduleStepRole(Role):
    """Roles played between Persons and Schedule Steps.
    """

    def __init__(self, SwitchingStep=None, ErpPerson=None, *args, **kw_args):
        """Initializes a new 'ErpPersonScheduleStepRole' instance.

        @param SwitchingStep:
        @param ErpPerson:
        """
        self._SwitchingStep = None
        self.SwitchingStep = SwitchingStep

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        super(ErpPersonScheduleStepRole, self).__init__(*args, **kw_args)

    def getSwitchingStep(self):
        
        return self._SwitchingStep

    def setSwitchingStep(self, value):
        if self._SwitchingStep is not None:
            self._SwitchingStep._ErpPersonRole = None

        self._SwitchingStep = value
        if self._SwitchingStep is not None:
            self._SwitchingStep._ErpPersonRole = self

    SwitchingStep = property(getSwitchingStep, setSwitchingStep)

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.SwitchingStepRoles if x != self]
            self._ErpPerson._SwitchingStepRoles = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            self._ErpPerson._SwitchingStepRoles.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

