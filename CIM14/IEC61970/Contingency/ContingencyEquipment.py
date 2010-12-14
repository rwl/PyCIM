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

from CIM14.IEC61970.Contingency.ContingencyElement import ContingencyElement

class ContingencyEquipment(ContingencyElement):
    """A equipment to which the in service status is to change such as a power transformer or AC line segment.
    """

    def __init__(self, contingentStatus="outOfService", Equipment=None, *args, **kw_args):
        """Initialises a new 'ContingencyEquipment' instance.

        @param contingentStatus: The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied. Values are: "outOfService", "inService"
        @param Equipment: The single piece of equipment to which to apply the contingency.
        """
        #: The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied. Values are: "outOfService", "inService"
        self.contingentStatus = contingentStatus

        self._Equipment = None
        self.Equipment = Equipment

        super(ContingencyEquipment, self).__init__(*args, **kw_args)

    _attrs = ["contingentStatus"]
    _attr_types = {"contingentStatus": str}
    _defaults = {"contingentStatus": "outOfService"}
    _enums = {"contingentStatus": "ContingencyEquipmentStatusKind"}
    _refs = ["Equipment"]
    _many_refs = []

    def getEquipment(self):
        """The single piece of equipment to which to apply the contingency.
        """
        return self._Equipment

    def setEquipment(self, value):
        if self._Equipment is not None:
            filtered = [x for x in self.Equipment.ContingencyEquipment if x != self]
            self._Equipment._ContingencyEquipment = filtered

        self._Equipment = value
        if self._Equipment is not None:
            if self not in self._Equipment._ContingencyEquipment:
                self._Equipment._ContingencyEquipment.append(self)

    Equipment = property(getEquipment, setEquipment)

