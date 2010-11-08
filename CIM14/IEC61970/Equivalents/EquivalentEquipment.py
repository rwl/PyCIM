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

from CIM14.IEC61970.Core.ConductingEquipment import ConductingEquipment

class EquivalentEquipment(ConductingEquipment):
    """The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.
    """

    def __init__(self, EquivalentNetwork=None, *args, **kw_args):
        """Initialises a new 'EquivalentEquipment' instance.

        @param EquivalentNetwork: The equivalent where the reduced model belongs.
        """
        self._EquivalentNetwork = None
        self.EquivalentNetwork = EquivalentNetwork

        super(EquivalentEquipment, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["EquivalentNetwork"]
    _many_refs = []

    def getEquivalentNetwork(self):
        """The equivalent where the reduced model belongs.
        """
        return self._EquivalentNetwork

    def setEquivalentNetwork(self, value):
        if self._EquivalentNetwork is not None:
            filtered = [x for x in self.EquivalentNetwork.EquivalentEquipments if x != self]
            self._EquivalentNetwork._EquivalentEquipments = filtered

        self._EquivalentNetwork = value
        if self._EquivalentNetwork is not None:
            self._EquivalentNetwork._EquivalentEquipments.append(self)

    EquivalentNetwork = property(getEquivalentNetwork, setEquivalentNetwork)

