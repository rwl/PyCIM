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

class SeriesCompensatorTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic series compensator that may be used for design purposes.
    """

    def __init__(self, ShuntCompensatorAssetModels=None, *args, **kw_args):
        """Initializes a new 'SeriesCompensatorTypeAsset' instance.

        @param ShuntCompensatorAssetModels:
        """
        self._ShuntCompensatorAssetModels = []
        self.ShuntCompensatorAssetModels = [] if ShuntCompensatorAssetModels is None else ShuntCompensatorAssetModels

        super(SeriesCompensatorTypeAsset, self).__init__(*args, **kw_args)

    def getShuntCompensatorAssetModels(self):
        
        return self._ShuntCompensatorAssetModels

    def setShuntCompensatorAssetModels(self, value):
        for x in self._ShuntCompensatorAssetModels:
            x._ShuntCompensatorTypeAsset = None
        for y in value:
            y._ShuntCompensatorTypeAsset = self
        self._ShuntCompensatorAssetModels = value

    ShuntCompensatorAssetModels = property(getShuntCompensatorAssetModels, setShuntCompensatorAssetModels)

    def addShuntCompensatorAssetModels(self, *ShuntCompensatorAssetModels):
        for obj in ShuntCompensatorAssetModels:
            obj._ShuntCompensatorTypeAsset = self
            self._ShuntCompensatorAssetModels.append(obj)

    def removeShuntCompensatorAssetModels(self, *ShuntCompensatorAssetModels):
        for obj in ShuntCompensatorAssetModels:
            obj._ShuntCompensatorTypeAsset = None
            self._ShuntCompensatorAssetModels.remove(obj)

