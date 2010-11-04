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

class FACTSDeviceAsset(ElectricalAsset):
    """Physical asset used to perform the FACTSDevice's role.
    """

    def __init__(self, kind='tsbr', FACTSDeviceAssetModel=None, **kw_args):
        """Initializes a new 'FACTSDeviceAsset' instance.

        @param kind: Kind of FACTS device. Values are: "tsbr", "statcom", "tcvl", "tssc", "tcpar", "svc", "upfc", "tcsc"
        @param FACTSDeviceAssetModel:
        """
        #: Kind of FACTS device.Values are: "tsbr", "statcom", "tcvl", "tssc", "tcpar", "svc", "upfc", "tcsc"
        self.kind = kind

        self._FACTSDeviceAssetModel = None
        self.FACTSDeviceAssetModel = FACTSDeviceAssetModel

        super(FACTSDeviceAsset, self).__init__(**kw_args)

    def getFACTSDeviceAssetModel(self):
        
        return self._FACTSDeviceAssetModel

    def setFACTSDeviceAssetModel(self, value):
        if self._FACTSDeviceAssetModel is not None:
            filtered = [x for x in self.FACTSDeviceAssetModel.FACTSDeviceAssets if x != self]
            self._FACTSDeviceAssetModel._FACTSDeviceAssets = filtered

        self._FACTSDeviceAssetModel = value
        if self._FACTSDeviceAssetModel is not None:
            self._FACTSDeviceAssetModel._FACTSDeviceAssets.append(self)

    FACTSDeviceAssetModel = property(getFACTSDeviceAssetModel, setFACTSDeviceAssetModel)

