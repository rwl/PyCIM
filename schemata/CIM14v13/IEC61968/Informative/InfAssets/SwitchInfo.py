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

from CIM14v13.IEC61968.Assets.ElectricalInfo import ElectricalInfo

class SwitchInfo(ElectricalInfo):
    """Properties of a switch.
    """

    def __init__(self, makingCapacity=0.0, poleCount=0, interruptingRating=0.0, withstandCurrent=0.0, minimumCurrent=0.0, loadBreak=False, gang=False, dielectricStrength=0.0, remote=False, SwitchAssets=None, SwitchAssetModel=None, SwitchTypeAsset=None, *args, **kw_args):
        """Initializes a new 'SwitchInfo' instance.

        @param makingCapacity: The highest value of current the switch can make at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        @param poleCount: Number of poles (i.e. of current carrying conductors that are switched). 
        @param interruptingRating: Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage. 
        @param withstandCurrent: The highest value of current the switch can carry in the closed position at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        @param minimumCurrent: The lowest value of current that the switch can make, carry and break in uninterrupted duty at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        @param loadBreak: True if switch has load breaking capabiity. Unless specified false, this is always assumed to be true for breakers and reclosers. 
        @param gang: True if multi-phase switch controls all phases concurrently. 
        @param dielectricStrength: The maximum rms voltage that may be applied across an open contact without breaking down the dielectric properties of the switch in the open position. 
        @param remote: True if device is capable of being operated by remote control. 
        @param SwitchAssets:
        @param SwitchAssetModel:
        @param SwitchTypeAsset:
        """
        #: The highest value of current the switch can make at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        self.makingCapacity = makingCapacity

        #: Number of poles (i.e. of current carrying conductors that are switched). 
        self.poleCount = poleCount

        #: Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage. 
        self.interruptingRating = interruptingRating

        #: The highest value of current the switch can carry in the closed position at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        self.withstandCurrent = withstandCurrent

        #: The lowest value of current that the switch can make, carry and break in uninterrupted duty at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        self.minimumCurrent = minimumCurrent

        #: True if switch has load breaking capabiity. Unless specified false, this is always assumed to be true for breakers and reclosers. 
        self.loadBreak = loadBreak

        #: True if multi-phase switch controls all phases concurrently. 
        self.gang = gang

        #: The maximum rms voltage that may be applied across an open contact without breaking down the dielectric properties of the switch in the open position. 
        self.dielectricStrength = dielectricStrength

        #: True if device is capable of being operated by remote control. 
        self.remote = remote

        self._SwitchAssets = []
        self.SwitchAssets = [] if SwitchAssets is None else SwitchAssets

        self._SwitchAssetModel = None
        self.SwitchAssetModel = SwitchAssetModel

        self._SwitchTypeAsset = None
        self.SwitchTypeAsset = SwitchTypeAsset

        super(SwitchInfo, self).__init__(*args, **kw_args)

    def getSwitchAssets(self):
        
        return self._SwitchAssets

    def setSwitchAssets(self, value):
        for x in self._SwitchAssets:
            x._SwitchInfo = None
        for y in value:
            y._SwitchInfo = self
        self._SwitchAssets = value

    SwitchAssets = property(getSwitchAssets, setSwitchAssets)

    def addSwitchAssets(self, *SwitchAssets):
        for obj in SwitchAssets:
            obj._SwitchInfo = self
            self._SwitchAssets.append(obj)

    def removeSwitchAssets(self, *SwitchAssets):
        for obj in SwitchAssets:
            obj._SwitchInfo = None
            self._SwitchAssets.remove(obj)

    def getSwitchAssetModel(self):
        
        return self._SwitchAssetModel

    def setSwitchAssetModel(self, value):
        if self._SwitchAssetModel is not None:
            self._SwitchAssetModel._SwitchInfo = None

        self._SwitchAssetModel = value
        if self._SwitchAssetModel is not None:
            self._SwitchAssetModel._SwitchInfo = self

    SwitchAssetModel = property(getSwitchAssetModel, setSwitchAssetModel)

    def getSwitchTypeAsset(self):
        
        return self._SwitchTypeAsset

    def setSwitchTypeAsset(self, value):
        if self._SwitchTypeAsset is not None:
            self._SwitchTypeAsset._SwitchInfo = None

        self._SwitchTypeAsset = value
        if self._SwitchTypeAsset is not None:
            self._SwitchTypeAsset._SwitchInfo = self

    SwitchTypeAsset = property(getSwitchTypeAsset, setSwitchTypeAsset)

