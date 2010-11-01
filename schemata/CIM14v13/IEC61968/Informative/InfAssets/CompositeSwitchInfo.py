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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class CompositeSwitchInfo(IdentifiedObject):
    """Properties of a composite switch.
    """

    def __init__(self, phaseCode='BC', ratedVoltage=0.0, phaseCount=0, remote=False, initOpMode='', gang=False, switchStateCount=0, interruptingRating=0.0, CompositeSwitchAssetModel=None, CompositeSwitchAssets=None, CompositeSwitchTypeAsset=None, *args, **kw_args):
        """Initializes a new 'CompositeSwitchInfo' instance.

        @param phaseCode: Phases carried, if applicable. Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        @param ratedVoltage: Rated voltage. 
        @param phaseCount: Supported number of phases, typically 0, 1 or 3. 
        @param remote: True if device is capable of being operated by remote control. 
        @param initOpMode: Initial operating mode, with the following values: Automatic, Manual. 
        @param gang: True if multi-phase switch controls all phases concurrently. 
        @param switchStateCount: Number of switch states represented by the composite switch. 
        @param interruptingRating: Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage. 
        @param CompositeSwitchAssetModel:
        @param CompositeSwitchAssets:
        @param CompositeSwitchTypeAsset:
        """
        #: Phases carried, if applicable. Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        self.phaseCode = phaseCode

        #: Rated voltage. 
        self.ratedVoltage = ratedVoltage

        #: Supported number of phases, typically 0, 1 or 3. 
        self.phaseCount = phaseCount

        #: True if device is capable of being operated by remote control. 
        self.remote = remote

        #: Initial operating mode, with the following values: Automatic, Manual. 
        self.initOpMode = initOpMode

        #: True if multi-phase switch controls all phases concurrently. 
        self.gang = gang

        #: Number of switch states represented by the composite switch. 
        self.switchStateCount = switchStateCount

        #: Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage. 
        self.interruptingRating = interruptingRating

        self._CompositeSwitchAssetModel = None
        self.CompositeSwitchAssetModel = CompositeSwitchAssetModel

        self._CompositeSwitchAssets = []
        self.CompositeSwitchAssets = [] if CompositeSwitchAssets is None else CompositeSwitchAssets

        self._CompositeSwitchTypeAsset = None
        self.CompositeSwitchTypeAsset = CompositeSwitchTypeAsset

        super(CompositeSwitchInfo, self).__init__(*args, **kw_args)

    def getCompositeSwitchAssetModel(self):
        
        return self._CompositeSwitchAssetModel

    def setCompositeSwitchAssetModel(self, value):
        if self._CompositeSwitchAssetModel is not None:
            self._CompositeSwitchAssetModel._CompositeSwitchInfo = None

        self._CompositeSwitchAssetModel = value
        if self._CompositeSwitchAssetModel is not None:
            self._CompositeSwitchAssetModel._CompositeSwitchInfo = self

    CompositeSwitchAssetModel = property(getCompositeSwitchAssetModel, setCompositeSwitchAssetModel)

    def getCompositeSwitchAssets(self):
        
        return self._CompositeSwitchAssets

    def setCompositeSwitchAssets(self, value):
        for x in self._CompositeSwitchAssets:
            x._CompositeSwitchInfo = None
        for y in value:
            y._CompositeSwitchInfo = self
        self._CompositeSwitchAssets = value

    CompositeSwitchAssets = property(getCompositeSwitchAssets, setCompositeSwitchAssets)

    def addCompositeSwitchAssets(self, *CompositeSwitchAssets):
        for obj in CompositeSwitchAssets:
            obj._CompositeSwitchInfo = self
            self._CompositeSwitchAssets.append(obj)

    def removeCompositeSwitchAssets(self, *CompositeSwitchAssets):
        for obj in CompositeSwitchAssets:
            obj._CompositeSwitchInfo = None
            self._CompositeSwitchAssets.remove(obj)

    def getCompositeSwitchTypeAsset(self):
        
        return self._CompositeSwitchTypeAsset

    def setCompositeSwitchTypeAsset(self, value):
        if self._CompositeSwitchTypeAsset is not None:
            self._CompositeSwitchTypeAsset._CompositeSwitchInfo = None

        self._CompositeSwitchTypeAsset = value
        if self._CompositeSwitchTypeAsset is not None:
            self._CompositeSwitchTypeAsset._CompositeSwitchInfo = self

    CompositeSwitchTypeAsset = property(getCompositeSwitchTypeAsset, setCompositeSwitchTypeAsset)

