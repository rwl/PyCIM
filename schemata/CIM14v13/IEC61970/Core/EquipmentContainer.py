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

from CIM14v13.IEC61970.Core.ConnectivityNodeContainer import ConnectivityNodeContainer

class EquipmentContainer(ConnectivityNodeContainer):
    """A modeling construct to provide a root class for containing equipment.
    """

    def __init__(self, Equipments=None, **kw_args):
        """Initializes a new 'EquipmentContainer' instance.

        @param Equipments: The association is used in the naming hierarchy.
        """
        self._Equipments = []
        self.Equipments = [] if Equipments is None else Equipments

        super(EquipmentContainer, self).__init__(**kw_args)

    def getEquipments(self):
        """The association is used in the naming hierarchy.
        """
        return self._Equipments

    def setEquipments(self, value):
        for x in self._Equipments:
            x._EquipmentContainer = None
        for y in value:
            y._EquipmentContainer = self
        self._Equipments = value

    Equipments = property(getEquipments, setEquipments)

    def addEquipments(self, *Equipments):
        for obj in Equipments:
            obj._EquipmentContainer = self
            self._Equipments.append(obj)

    def removeEquipments(self, *Equipments):
        for obj in Equipments:
            obj._EquipmentContainer = None
            self._Equipments.remove(obj)

