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

from CIM14v13.IEC61968.Informative.InfAssetModels.ElectricalAssetModel import ElectricalAssetModel

class SeriesCompensatorAssetModel(ElectricalAssetModel):
    """For application as a series capacitor or reactor, this is documentation for a type of a capacitor or reactor of a particular product model made by a manufacturer.
    """

    def __init__(self, SeriesCompensatorAsset=None, ShuntCompensatorTypeAsset=None, *args, **kw_args):
        """Initializes a new 'SeriesCompensatorAssetModel' instance.

        @param SeriesCompensatorAsset:
        @param ShuntCompensatorTypeAsset:
        """
        self._SeriesCompensatorAsset = None
        self.SeriesCompensatorAsset = SeriesCompensatorAsset

        self._ShuntCompensatorTypeAsset = None
        self.ShuntCompensatorTypeAsset = ShuntCompensatorTypeAsset

        super(SeriesCompensatorAssetModel, self).__init__(*args, **kw_args)

    def getSeriesCompensatorAsset(self):
        
        return self._SeriesCompensatorAsset

    def setSeriesCompensatorAsset(self, value):
        if self._SeriesCompensatorAsset is not None:
            self._SeriesCompensatorAsset._SeriesCompensatorAssetModel = None

        self._SeriesCompensatorAsset = value
        if self._SeriesCompensatorAsset is not None:
            self._SeriesCompensatorAsset._SeriesCompensatorAssetModel = self

    SeriesCompensatorAsset = property(getSeriesCompensatorAsset, setSeriesCompensatorAsset)

    def getShuntCompensatorTypeAsset(self):
        
        return self._ShuntCompensatorTypeAsset

    def setShuntCompensatorTypeAsset(self, value):
        if self._ShuntCompensatorTypeAsset is not None:
            filtered = [x for x in self.ShuntCompensatorTypeAsset.ShuntCompensatorAssetModels if x != self]
            self._ShuntCompensatorTypeAsset._ShuntCompensatorAssetModels = filtered

        self._ShuntCompensatorTypeAsset = value
        if self._ShuntCompensatorTypeAsset is not None:
            self._ShuntCompensatorTypeAsset._ShuntCompensatorAssetModels.append(self)

    ShuntCompensatorTypeAsset = property(getShuntCompensatorTypeAsset, setShuntCompensatorTypeAsset)

