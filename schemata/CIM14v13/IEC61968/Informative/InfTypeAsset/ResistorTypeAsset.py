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

from CIM14v13.IEC61968.Informative.InfTypeAsset.ElectricalTypeAsset import ElectricalTypeAsset

class ResistorTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic resistor that may be used for design purposes.
    """

    def __init__(self, ResistorAssetModels=None, Resistors=None, **kw_args):
        """Initializes a new 'ResistorTypeAsset' instance.

        @param ResistorAssetModels:
        @param Resistors:
        """
        self._ResistorAssetModels = []
        self.ResistorAssetModels = [] if ResistorAssetModels is None else ResistorAssetModels

        self._Resistors = []
        self.Resistors = [] if Resistors is None else Resistors

        super(ResistorTypeAsset, self).__init__(**kw_args)

    def getResistorAssetModels(self):
        
        return self._ResistorAssetModels

    def setResistorAssetModels(self, value):
        for x in self._ResistorAssetModels:
            x._ResistorTypeAsset = None
        for y in value:
            y._ResistorTypeAsset = self
        self._ResistorAssetModels = value

    ResistorAssetModels = property(getResistorAssetModels, setResistorAssetModels)

    def addResistorAssetModels(self, *ResistorAssetModels):
        for obj in ResistorAssetModels:
            obj._ResistorTypeAsset = self
            self._ResistorAssetModels.append(obj)

    def removeResistorAssetModels(self, *ResistorAssetModels):
        for obj in ResistorAssetModels:
            obj._ResistorTypeAsset = None
            self._ResistorAssetModels.remove(obj)

    def getResistors(self):
        
        return self._Resistors

    def setResistors(self, value):
        for x in self._Resistors:
            x._ResistorTypeAsset = None
        for y in value:
            y._ResistorTypeAsset = self
        self._Resistors = value

    Resistors = property(getResistors, setResistors)

    def addResistors(self, *Resistors):
        for obj in Resistors:
            obj._ResistorTypeAsset = self
            self._Resistors.append(obj)

    def removeResistors(self, *Resistors):
        for obj in Resistors:
            obj._ResistorTypeAsset = None
            self._Resistors.remove(obj)

