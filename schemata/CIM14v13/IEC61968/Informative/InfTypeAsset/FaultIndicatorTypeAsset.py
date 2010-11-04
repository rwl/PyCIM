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

class FaultIndicatorTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic fault indicator that may be used for design purposes.
    """

    def __init__(self, resetKind='other', FaultIndicatorAssetModels=None, FaultIndicators=None, *args, **kw_args):
        """Initializes a new 'FaultIndicatorTypeAsset' instance.

        @param resetKind: Kind of reset mechanisim of this fault indicator. Values are: "other", "remote", "manual", "automatic"
        @param FaultIndicatorAssetModels:
        @param FaultIndicators:
        """
        #: Kind of reset mechanisim of this fault indicator.Values are: "other", "remote", "manual", "automatic"
        self.resetKind = resetKind

        self._FaultIndicatorAssetModels = []
        self.FaultIndicatorAssetModels = [] if FaultIndicatorAssetModels is None else FaultIndicatorAssetModels

        self._FaultIndicators = []
        self.FaultIndicators = [] if FaultIndicators is None else FaultIndicators

        super(FaultIndicatorTypeAsset, self).__init__(*args, **kw_args)

    def getFaultIndicatorAssetModels(self):
        
        return self._FaultIndicatorAssetModels

    def setFaultIndicatorAssetModels(self, value):
        for x in self._FaultIndicatorAssetModels:
            x._FaultIndicatorTypeAsset = None
        for y in value:
            y._FaultIndicatorTypeAsset = self
        self._FaultIndicatorAssetModels = value

    FaultIndicatorAssetModels = property(getFaultIndicatorAssetModels, setFaultIndicatorAssetModels)

    def addFaultIndicatorAssetModels(self, *FaultIndicatorAssetModels):
        for obj in FaultIndicatorAssetModels:
            obj._FaultIndicatorTypeAsset = self
            self._FaultIndicatorAssetModels.append(obj)

    def removeFaultIndicatorAssetModels(self, *FaultIndicatorAssetModels):
        for obj in FaultIndicatorAssetModels:
            obj._FaultIndicatorTypeAsset = None
            self._FaultIndicatorAssetModels.remove(obj)

    def getFaultIndicators(self):
        
        return self._FaultIndicators

    def setFaultIndicators(self, value):
        for x in self._FaultIndicators:
            x._FaultIndicatorTypeAsset = None
        for y in value:
            y._FaultIndicatorTypeAsset = self
        self._FaultIndicators = value

    FaultIndicators = property(getFaultIndicators, setFaultIndicators)

    def addFaultIndicators(self, *FaultIndicators):
        for obj in FaultIndicators:
            obj._FaultIndicatorTypeAsset = self
            self._FaultIndicators.append(obj)

    def removeFaultIndicators(self, *FaultIndicators):
        for obj in FaultIndicators:
            obj._FaultIndicatorTypeAsset = None
            self._FaultIndicators.remove(obj)

