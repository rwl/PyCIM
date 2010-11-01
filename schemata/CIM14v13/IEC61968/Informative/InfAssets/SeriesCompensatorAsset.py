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

class SeriesCompensatorAsset(ElectricalAsset):
    """For a a series capacitor or reactor, this is the physical asset performing the SeriesCompensator role (PSR).
    """

    def __init__(self, SeriesCompensatorAssetModel=None, *args, **kw_args):
        """Initializes a new 'SeriesCompensatorAsset' instance.

        @param SeriesCompensatorAssetModel:
        """
        self._SeriesCompensatorAssetModel = None
        self.SeriesCompensatorAssetModel = SeriesCompensatorAssetModel

        super(SeriesCompensatorAsset, self).__init__(*args, **kw_args)

    def getSeriesCompensatorAssetModel(self):
        
        return self._SeriesCompensatorAssetModel

    def setSeriesCompensatorAssetModel(self, value):
        if self._SeriesCompensatorAssetModel is not None:
            self._SeriesCompensatorAssetModel._SeriesCompensatorAsset = None

        self._SeriesCompensatorAssetModel = value
        if self._SeriesCompensatorAssetModel is not None:
            self._SeriesCompensatorAssetModel._SeriesCompensatorAsset = self

    SeriesCompensatorAssetModel = property(getSeriesCompensatorAssetModel, setSeriesCompensatorAssetModel)

