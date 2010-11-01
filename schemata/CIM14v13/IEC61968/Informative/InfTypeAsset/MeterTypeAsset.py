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

class MeterTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic meter that may be used for design purposes. Rather than being associated with CustomerMeter, it is associated with EnergyConsumer as it may be used for many applications, such as tie line metering, in addition to customer metering.
    """

    def __init__(self, MeterAssetModels=None, *args, **kw_args):
        """Initializes a new 'MeterTypeAsset' instance.

        @param MeterAssetModels:
        """
        self._MeterAssetModels = []
        self.MeterAssetModels = [] if MeterAssetModels is None else MeterAssetModels

        super(MeterTypeAsset, self).__init__(*args, **kw_args)

    def getMeterAssetModels(self):
        
        return self._MeterAssetModels

    def setMeterAssetModels(self, value):
        for x in self._MeterAssetModels:
            x._MeterTypeAsset = None
        for y in value:
            y._MeterTypeAsset = self
        self._MeterAssetModels = value

    MeterAssetModels = property(getMeterAssetModels, setMeterAssetModels)

    def addMeterAssetModels(self, *MeterAssetModels):
        for obj in MeterAssetModels:
            obj._MeterTypeAsset = self
            self._MeterAssetModels.append(obj)

    def removeMeterAssetModels(self, *MeterAssetModels):
        for obj in MeterAssetModels:
            obj._MeterTypeAsset = None
            self._MeterAssetModels.remove(obj)

