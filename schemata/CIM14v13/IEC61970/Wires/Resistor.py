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

from CIM14v13.IEC61970.Core.ConductingEquipment import ConductingEquipment

class Resistor(ConductingEquipment):
    """Resistor, typically used in filter configurations or as earthing resistor for transformers.  Used for electrical model of distribution networks.
    """

    def __init__(self, ResistorTypeAsset=None, ResistorAsset=None, *args, **kw_args):
        """Initializes a new 'Resistor' instance.

        @param ResistorTypeAsset:
        @param ResistorAsset:
        """
        self._ResistorTypeAsset = None
        self.ResistorTypeAsset = ResistorTypeAsset

        self._ResistorAsset = None
        self.ResistorAsset = ResistorAsset

        super(Resistor, self).__init__(*args, **kw_args)

    def getResistorTypeAsset(self):
        
        return self._ResistorTypeAsset

    def setResistorTypeAsset(self, value):
        if self._ResistorTypeAsset is not None:
            filtered = [x for x in self.ResistorTypeAsset.Resistors if x != self]
            self._ResistorTypeAsset._Resistors = filtered

        self._ResistorTypeAsset = value
        if self._ResistorTypeAsset is not None:
            self._ResistorTypeAsset._Resistors.append(self)

    ResistorTypeAsset = property(getResistorTypeAsset, setResistorTypeAsset)

    def getResistorAsset(self):
        
        return self._ResistorAsset

    def setResistorAsset(self, value):
        if self._ResistorAsset is not None:
            self._ResistorAsset._Resistor = None

        self._ResistorAsset = value
        if self._ResistorAsset is not None:
            self._ResistorAsset._Resistor = self

    ResistorAsset = property(getResistorAsset, setResistorAsset)

