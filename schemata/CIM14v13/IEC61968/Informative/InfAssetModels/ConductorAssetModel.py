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

from CIM14v13.IEC61968.AssetModels.AssetModel import AssetModel

class ConductorAssetModel(AssetModel):
    """A type of conductor made by a particular manufacturer (Organisation). Its ElectricalProperties are defined as being per unit length (which is defined by the unitLength attribute)
    """

    def __init__(self, ConductorAssets=None, ConductorInfo=None, *args, **kw_args):
        """Initializes a new 'ConductorAssetModel' instance.

        @param ConductorAssets:
        @param ConductorInfo:
        """
        self._ConductorAssets = []
        self.ConductorAssets = [] if ConductorAssets is None else ConductorAssets

        self._ConductorInfo = None
        self.ConductorInfo = ConductorInfo

        super(ConductorAssetModel, self).__init__(*args, **kw_args)

    def getConductorAssets(self):
        
        return self._ConductorAssets

    def setConductorAssets(self, value):
        for x in self._ConductorAssets:
            x._ConductorAssetModel = None
        for y in value:
            y._ConductorAssetModel = self
        self._ConductorAssets = value

    ConductorAssets = property(getConductorAssets, setConductorAssets)

    def addConductorAssets(self, *ConductorAssets):
        for obj in ConductorAssets:
            obj._ConductorAssetModel = self
            self._ConductorAssets.append(obj)

    def removeConductorAssets(self, *ConductorAssets):
        for obj in ConductorAssets:
            obj._ConductorAssetModel = None
            self._ConductorAssets.remove(obj)

    def getConductorInfo(self):
        
        return self._ConductorInfo

    def setConductorInfo(self, value):
        if self._ConductorInfo is not None:
            self._ConductorInfo._ConductorAssetModel = None

        self._ConductorInfo = value
        if self._ConductorInfo is not None:
            self._ConductorInfo._ConductorAssetModel = self

    ConductorInfo = property(getConductorInfo, setConductorInfo)

