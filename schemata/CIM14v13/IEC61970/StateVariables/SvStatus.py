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

from CIM14v13.IEC61970.StateVariables.StateVariable import StateVariable

class SvStatus(StateVariable):
    """State variable for status.
    """

    def __init__(self, inService=False, ConductingEquipment=None, *args, **kw_args):
        """Initializes a new 'SvStatus' instance.

        @param inService: The in service status as a result of topology processing. 
        @param ConductingEquipment: The conducting equipment associated with the status state.
        """
        #: The in service status as a result of topology processing. 
        self.inService = inService

        self._ConductingEquipment = None
        self.ConductingEquipment = ConductingEquipment

        super(SvStatus, self).__init__(*args, **kw_args)

    def getConductingEquipment(self):
        """The conducting equipment associated with the status state.
        """
        return self._ConductingEquipment

    def setConductingEquipment(self, value):
        if self._ConductingEquipment is not None:
            self._ConductingEquipment._SvStatus = None

        self._ConductingEquipment = value
        if self._ConductingEquipment is not None:
            self._ConductingEquipment._SvStatus = self

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

