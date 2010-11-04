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

from CIM14v13.IEC61968.Informative.InfAssets.SwitchInfo import SwitchInfo

class RecloserInfo(SwitchInfo):
    """Properties of reclosers.
    """

    def __init__(self, groundTripNormalEnabled=False, groundTripCapable=False, groundTripRating=0.0, phaseTripRating=0.0, recloseLockoutCount=0, RecloserAssetModels=None, RecloserTypeAsset=None, RecloserAssets=None, *args, **kw_args):
        """Initializes a new 'RecloserInfo' instance.

        @param groundTripNormalEnabled: True if normal status of ground trip is enabled. 
        @param groundTripCapable: True if device has ground trip capability. 
        @param groundTripRating: Ground trip rating. 
        @param phaseTripRating: Phase trip rating. 
        @param recloseLockoutCount: Total number of phase reclose operations. 
        @param RecloserAssetModels:
        @param RecloserTypeAsset:
        @param RecloserAssets:
        """
        #: True if normal status of ground trip is enabled.
        self.groundTripNormalEnabled = groundTripNormalEnabled

        #: True if device has ground trip capability.
        self.groundTripCapable = groundTripCapable

        #: Ground trip rating.
        self.groundTripRating = groundTripRating

        #: Phase trip rating.
        self.phaseTripRating = phaseTripRating

        #: Total number of phase reclose operations.
        self.recloseLockoutCount = recloseLockoutCount

        self._RecloserAssetModels = []
        self.RecloserAssetModels = [] if RecloserAssetModels is None else RecloserAssetModels

        self._RecloserTypeAsset = None
        self.RecloserTypeAsset = RecloserTypeAsset

        self._RecloserAssets = []
        self.RecloserAssets = [] if RecloserAssets is None else RecloserAssets

        super(RecloserInfo, self).__init__(*args, **kw_args)

    def getRecloserAssetModels(self):
        
        return self._RecloserAssetModels

    def setRecloserAssetModels(self, value):
        for x in self._RecloserAssetModels:
            x._RecloserInfo = None
        for y in value:
            y._RecloserInfo = self
        self._RecloserAssetModels = value

    RecloserAssetModels = property(getRecloserAssetModels, setRecloserAssetModels)

    def addRecloserAssetModels(self, *RecloserAssetModels):
        for obj in RecloserAssetModels:
            obj._RecloserInfo = self
            self._RecloserAssetModels.append(obj)

    def removeRecloserAssetModels(self, *RecloserAssetModels):
        for obj in RecloserAssetModels:
            obj._RecloserInfo = None
            self._RecloserAssetModels.remove(obj)

    def getRecloserTypeAsset(self):
        
        return self._RecloserTypeAsset

    def setRecloserTypeAsset(self, value):
        if self._RecloserTypeAsset is not None:
            self._RecloserTypeAsset._RecloserInfo = None

        self._RecloserTypeAsset = value
        if self._RecloserTypeAsset is not None:
            self._RecloserTypeAsset._RecloserInfo = self

    RecloserTypeAsset = property(getRecloserTypeAsset, setRecloserTypeAsset)

    def getRecloserAssets(self):
        
        return self._RecloserAssets

    def setRecloserAssets(self, value):
        for x in self._RecloserAssets:
            x._RecloserInfo = None
        for y in value:
            y._RecloserInfo = self
        self._RecloserAssets = value

    RecloserAssets = property(getRecloserAssets, setRecloserAssets)

    def addRecloserAssets(self, *RecloserAssets):
        for obj in RecloserAssets:
            obj._RecloserInfo = self
            self._RecloserAssets.append(obj)

    def removeRecloserAssets(self, *RecloserAssets):
        for obj in RecloserAssets:
            obj._RecloserInfo = None
            self._RecloserAssets.remove(obj)

