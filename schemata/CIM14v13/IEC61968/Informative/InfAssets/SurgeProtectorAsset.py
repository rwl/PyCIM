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

class SurgeProtectorAsset(ElectricalAsset):
    """Physical asset performing SurgeProtector function.
    """

    def __init__(self, SurgeProtector=None, SurgeProtectorAssetModel=None, *args, **kw_args):
        """Initializes a new 'SurgeProtectorAsset' instance.

        @param SurgeProtector:
        @param SurgeProtectorAssetModel:
        """
        self._SurgeProtector = None
        self.SurgeProtector = SurgeProtector

        self._SurgeProtectorAssetModel = None
        self.SurgeProtectorAssetModel = SurgeProtectorAssetModel

        super(SurgeProtectorAsset, self).__init__(*args, **kw_args)

    def getSurgeProtector(self):
        
        return self._SurgeProtector

    def setSurgeProtector(self, value):
        if self._SurgeProtector is not None:
            self._SurgeProtector._SurgeProtectorAsset = None

        self._SurgeProtector = value
        if self._SurgeProtector is not None:
            self._SurgeProtector._SurgeProtectorAsset = self

    SurgeProtector = property(getSurgeProtector, setSurgeProtector)

    def getSurgeProtectorAssetModel(self):
        
        return self._SurgeProtectorAssetModel

    def setSurgeProtectorAssetModel(self, value):
        if self._SurgeProtectorAssetModel is not None:
            filtered = [x for x in self.SurgeProtectorAssetModel.SurgeProtectorAssets if x != self]
            self._SurgeProtectorAssetModel._SurgeProtectorAssets = filtered

        self._SurgeProtectorAssetModel = value
        if self._SurgeProtectorAssetModel is not None:
            self._SurgeProtectorAssetModel._SurgeProtectorAssets.append(self)

    SurgeProtectorAssetModel = property(getSurgeProtectorAssetModel, setSurgeProtectorAssetModel)

