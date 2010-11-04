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

class EquivalentNetwork(ConnectivityNodeContainer):
    """A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.
    """

    def __init__(self, EquivalentEquipments=None, **kw_args):
        """Initializes a new 'EquivalentNetwork' instance.

        @param EquivalentEquipments: The associated reduced equivalents.
        """
        self._EquivalentEquipments = []
        self.EquivalentEquipments = [] if EquivalentEquipments is None else EquivalentEquipments

        super(EquivalentNetwork, self).__init__(**kw_args)

    def getEquivalentEquipments(self):
        """The associated reduced equivalents.
        """
        return self._EquivalentEquipments

    def setEquivalentEquipments(self, value):
        for x in self._EquivalentEquipments:
            x._EquivalentNetwork = None
        for y in value:
            y._EquivalentNetwork = self
        self._EquivalentEquipments = value

    EquivalentEquipments = property(getEquivalentEquipments, setEquivalentEquipments)

    def addEquivalentEquipments(self, *EquivalentEquipments):
        for obj in EquivalentEquipments:
            obj._EquivalentNetwork = self
            self._EquivalentEquipments.append(obj)

    def removeEquivalentEquipments(self, *EquivalentEquipments):
        for obj in EquivalentEquipments:
            obj._EquivalentNetwork = None
            self._EquivalentEquipments.remove(obj)

