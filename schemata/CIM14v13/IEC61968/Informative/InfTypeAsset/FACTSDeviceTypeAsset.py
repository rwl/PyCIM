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

class FACTSDeviceTypeAsset(ElectricalTypeAsset):
    """Documentation for generic Flexible alternating current transmission systems (FACTS) devices that may be used for various purposes such as work planning.
    """

    def __init__(self, FACTSDeviceAssetModels=None, *args, **kw_args):
        """Initializes a new 'FACTSDeviceTypeAsset' instance.

        @param FACTSDeviceAssetModels:
        """
        self._FACTSDeviceAssetModels = []
        self.FACTSDeviceAssetModels = [] if FACTSDeviceAssetModels is None else FACTSDeviceAssetModels

        super(FACTSDeviceTypeAsset, self).__init__(*args, **kw_args)

    def getFACTSDeviceAssetModels(self):
        
        return self._FACTSDeviceAssetModels

    def setFACTSDeviceAssetModels(self, value):
        for x in self._FACTSDeviceAssetModels:
            x._FACTSDeviceTypeAsset = None
        for y in value:
            y._FACTSDeviceTypeAsset = self
        self._FACTSDeviceAssetModels = value

    FACTSDeviceAssetModels = property(getFACTSDeviceAssetModels, setFACTSDeviceAssetModels)

    def addFACTSDeviceAssetModels(self, *FACTSDeviceAssetModels):
        for obj in FACTSDeviceAssetModels:
            obj._FACTSDeviceTypeAsset = self
            self._FACTSDeviceAssetModels.append(obj)

    def removeFACTSDeviceAssetModels(self, *FACTSDeviceAssetModels):
        for obj in FACTSDeviceAssetModels:
            obj._FACTSDeviceTypeAsset = None
            self._FACTSDeviceAssetModels.remove(obj)

