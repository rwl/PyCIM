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

from CIM14v13.IEC61968.AssetModels.AssetModel import AssetModel

class TapChangerAssetModel(AssetModel):
    """Documentation for a type of a tap changer of a particular product model made by a manufacturer.
    """

    def __init__(self, switchingKind='vacuum', neutralStep=0, lowStep=0, frequency=0.0, stepVoltageIncrement=0.0, ratedCurrent=0.0, initialDelay=0.0, tapCount=0, ratedVoltage=0.0, stepPhaseIncrement=0.0, subsequentDelay=0.0, highStep=0, ratedApparentPower=0.0, phaseCount=0, bil=0.0, TapChangerAssets=None, *args, **kw_args):
        """Initializes a new 'TapChangerAssetModel' instance.

        @param switchingKind: Switching kind of tap changer. Values are: "vacuum", "reactive", "other", "resistive"
        @param neutralStep: The neutral tap step position for this type of winding. 
        @param lowStep: Lowest possible tap step position, retard from neutral 
        @param frequency: Frequency at which stated device ratings apply, typically 50Hz or 60Hz. 
        @param stepVoltageIncrement: Tap step increment, in per cent of nominal voltage, per step position. 
        @param ratedCurrent: Rated current. 
        @param initialDelay: Maximum allowed delay for initial tap changer operation (first step change) 
        @param tapCount: Number of taps. 
        @param ratedVoltage: Rated voltage. 
        @param stepPhaseIncrement: Phase shift, in degrees, per step position 
        @param subsequentDelay: Maximum allowed delay for isubsequent tap changer operations 
        @param highStep: Highest possible tap step position, advance from neutral 
        @param ratedApparentPower: Rated apparent power. 
        @param phaseCount: Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute. 
        @param bil: Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1.2 X 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges. 
        @param TapChangerAssets:
        """
        #: Switching kind of tap changer.Values are: "vacuum", "reactive", "other", "resistive"
        self.switchingKind = switchingKind

        #: The neutral tap step position for this type of winding.
        self.neutralStep = neutralStep

        #: Lowest possible tap step position, retard from neutral
        self.lowStep = lowStep

        #: Frequency at which stated device ratings apply, typically 50Hz or 60Hz.
        self.frequency = frequency

        #: Tap step increment, in per cent of nominal voltage, per step position.
        self.stepVoltageIncrement = stepVoltageIncrement

        #: Rated current.
        self.ratedCurrent = ratedCurrent

        #: Maximum allowed delay for initial tap changer operation (first step change)
        self.initialDelay = initialDelay

        #: Number of taps.
        self.tapCount = tapCount

        #: Rated voltage.
        self.ratedVoltage = ratedVoltage

        #: Phase shift, in degrees, per step position
        self.stepPhaseIncrement = stepPhaseIncrement

        #: Maximum allowed delay for isubsequent tap changer operations
        self.subsequentDelay = subsequentDelay

        #: Highest possible tap step position, advance from neutral
        self.highStep = highStep

        #: Rated apparent power.
        self.ratedApparentPower = ratedApparentPower

        #: Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute.
        self.phaseCount = phaseCount

        #: Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1.2 X 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges.
        self.bil = bil

        self._TapChangerAssets = []
        self.TapChangerAssets = [] if TapChangerAssets is None else TapChangerAssets

        super(TapChangerAssetModel, self).__init__(*args, **kw_args)

    def getTapChangerAssets(self):
        
        return self._TapChangerAssets

    def setTapChangerAssets(self, value):
        for x in self._TapChangerAssets:
            x._TapChangerAssetModel = None
        for y in value:
            y._TapChangerAssetModel = self
        self._TapChangerAssets = value

    TapChangerAssets = property(getTapChangerAssets, setTapChangerAssets)

    def addTapChangerAssets(self, *TapChangerAssets):
        for obj in TapChangerAssets:
            obj._TapChangerAssetModel = self
            self._TapChangerAssets.append(obj)

    def removeTapChangerAssets(self, *TapChangerAssets):
        for obj in TapChangerAssets:
            obj._TapChangerAssetModel = None
            self._TapChangerAssets.remove(obj)

