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

class FaultIndicatorAsset(ElectricalAsset):
    """Physical asset performing FaultIndicator function.
    """

    def __init__(self, FaultIndicator=None, FaultIndicatorAssetModel=None, *args, **kw_args):
        """Initializes a new 'FaultIndicatorAsset' instance.

        @param FaultIndicator:
        @param FaultIndicatorAssetModel:
        """
        self._FaultIndicator = None
        self.FaultIndicator = FaultIndicator

        self._FaultIndicatorAssetModel = None
        self.FaultIndicatorAssetModel = FaultIndicatorAssetModel

        super(FaultIndicatorAsset, self).__init__(*args, **kw_args)

    def getFaultIndicator(self):
        
        return self._FaultIndicator

    def setFaultIndicator(self, value):
        if self._FaultIndicator is not None:
            filtered = [x for x in self.FaultIndicator.FaultIndicatorAssets if x != self]
            self._FaultIndicator._FaultIndicatorAssets = filtered

        self._FaultIndicator = value
        if self._FaultIndicator is not None:
            self._FaultIndicator._FaultIndicatorAssets.append(self)

    FaultIndicator = property(getFaultIndicator, setFaultIndicator)

    def getFaultIndicatorAssetModel(self):
        
        return self._FaultIndicatorAssetModel

    def setFaultIndicatorAssetModel(self, value):
        if self._FaultIndicatorAssetModel is not None:
            filtered = [x for x in self.FaultIndicatorAssetModel.FaultIndicatorAssets if x != self]
            self._FaultIndicatorAssetModel._FaultIndicatorAssets = filtered

        self._FaultIndicatorAssetModel = value
        if self._FaultIndicatorAssetModel is not None:
            self._FaultIndicatorAssetModel._FaultIndicatorAssets.append(self)

    FaultIndicatorAssetModel = property(getFaultIndicatorAssetModel, setFaultIndicatorAssetModel)

