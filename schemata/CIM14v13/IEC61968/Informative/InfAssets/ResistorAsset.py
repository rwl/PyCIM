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

from CIM14v13.IEC61968.Informative.InfAssets.ElectricalAsset import ElectricalAsset

class ResistorAsset(ElectricalAsset):
    """Physical asset performing Resistor function.
    """

    def __init__(self, Resistor=None, ResistorAssetModel=None, *args, **kw_args):
        """Initializes a new 'ResistorAsset' instance.

        @param Resistor:
        @param ResistorAssetModel:
        """
        self._Resistor = None
        self.Resistor = Resistor

        self._ResistorAssetModel = None
        self.ResistorAssetModel = ResistorAssetModel

        super(ResistorAsset, self).__init__(*args, **kw_args)

    def getResistor(self):
        
        return self._Resistor

    def setResistor(self, value):
        if self._Resistor is not None:
            self._Resistor._ResistorAsset = None

        self._Resistor = value
        if self._Resistor is not None:
            self._Resistor._ResistorAsset = self

    Resistor = property(getResistor, setResistor)

    def getResistorAssetModel(self):
        
        return self._ResistorAssetModel

    def setResistorAssetModel(self, value):
        if self._ResistorAssetModel is not None:
            filtered = [x for x in self.ResistorAssetModel.ResistorAssets if x != self]
            self._ResistorAssetModel._ResistorAssets = filtered

        self._ResistorAssetModel = value
        if self._ResistorAssetModel is not None:
            self._ResistorAssetModel._ResistorAssets.append(self)

    ResistorAssetModel = property(getResistorAssetModel, setResistorAssetModel)

