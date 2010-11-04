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

class ElectricalInfo(IdentifiedObject):
    """Electrical properties of an asset or of an asset model (product by a manufacturer). Can also be used to define electrical properties for each phase individually. Not every attribute will be required for each type of asset or asset model. For example, a transformer may only have requirements for 'ratedVoltage', 'ratedApparentPower' and 'phaseCount' attributes, while a conductor will have 'r', 'x', 'b' and 'g' requirements per unit length on top of a 'ratedCurrent' and 'ratedVoltage'.
    """

    def __init__(self, b=0.0, wireCount=0, r0=0.0, frequency=0.0, g=0.0, ratedVoltage=0.0, x=0.0, phaseCount=0, ratedCurrent=0.0, b0=0.0, r=0.0, g0=0.0, ratedApparentPower=0.0, x0=0.0, bil=0.0, EndDeviceAssets=None, ElectricalTypeAssets=None, ElectricalAssets=None, ElectricalAssetModels=None, **kw_args):
        """Initializes a new 'ElectricalInfo' instance.

        @param b: Positive sequence susceptance. 
        @param wireCount: For an installed asset, this is the total number of electrical wires that are physically connected to it. For an AssetModel, this is the total number of wires that can potentially be connected to this asset type. This is particularly useful to understand overall electrical configurations for distribution secondary where the number of wires can not be derived from phase information alone. For example, 120v 2 Wires; 240v 2 Wires; 480v 1Ph 2 Wires; 120/240v 1Ph; 120/208v 3Ph Y; 120/208v 1Ph Y; 120/240v 3Ph D; 240/480v 1Ph 3 Wires; 480v 3Ph D; 240/480v 3Ph D; 277/480v 3Ph Y. 
        @param r0: Zero sequence series resistance. 
        @param frequency: Frequency at which stated device ratings apply, typically 50 Hz or 60 Hz. 
        @param g: Positive sequence conductance. 
        @param ratedVoltage: Rated voltage. 
        @param x: Positive sequence series reactance. 
        @param phaseCount: Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute. 
        @param ratedCurrent: Rated current. 
        @param b0: Zero sequence susceptance. 
        @param r: Positive sequence series resistance. 
        @param g0: Zero sequence conductance. 
        @param ratedApparentPower: Rated apparent power. 
        @param x0: Zero sequence series reactance. 
        @param bil: Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1,2 x 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges. 
        @param EndDeviceAssets: All end device assets having this set of electrical properties.
        @param ElectricalTypeAssets:
        @param ElectricalAssets:
        @param ElectricalAssetModels:
        """
        #: Positive sequence susceptance.
        self.b = b

        #: For an installed asset, this is the total number of electrical wires that are physically connected to it. For an AssetModel, this is the total number of wires that can potentially be connected to this asset type. This is particularly useful to understand overall electrical configurations for distribution secondary where the number of wires can not be derived from phase information alone. For example, 120v 2 Wires; 240v 2 Wires; 480v 1Ph 2 Wires; 120/240v 1Ph; 120/208v 3Ph Y; 120/208v 1Ph Y; 120/240v 3Ph D; 240/480v 1Ph 3 Wires; 480v 3Ph D; 240/480v 3Ph D; 277/480v 3Ph Y.
        self.wireCount = wireCount

        #: Zero sequence series resistance.
        self.r0 = r0

        #: Frequency at which stated device ratings apply, typically 50 Hz or 60 Hz.
        self.frequency = frequency

        #: Positive sequence conductance.
        self.g = g

        #: Rated voltage.
        self.ratedVoltage = ratedVoltage

        #: Positive sequence series reactance.
        self.x = x

        #: Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute.
        self.phaseCount = phaseCount

        #: Rated current.
        self.ratedCurrent = ratedCurrent

        #: Zero sequence susceptance.
        self.b0 = b0

        #: Positive sequence series resistance.
        self.r = r

        #: Zero sequence conductance.
        self.g0 = g0

        #: Rated apparent power.
        self.ratedApparentPower = ratedApparentPower

        #: Zero sequence series reactance.
        self.x0 = x0

        #: Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1,2 x 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges.
        self.bil = bil

        self._EndDeviceAssets = []
        self.EndDeviceAssets = [] if EndDeviceAssets is None else EndDeviceAssets

        self._ElectricalTypeAssets = []
        self.ElectricalTypeAssets = [] if ElectricalTypeAssets is None else ElectricalTypeAssets

        self._ElectricalAssets = []
        self.ElectricalAssets = [] if ElectricalAssets is None else ElectricalAssets

        self._ElectricalAssetModels = []
        self.ElectricalAssetModels = [] if ElectricalAssetModels is None else ElectricalAssetModels

        super(ElectricalInfo, self).__init__(**kw_args)

    def getEndDeviceAssets(self):
        """All end device assets having this set of electrical properties.
        """
        return self._EndDeviceAssets

    def setEndDeviceAssets(self, value):
        for p in self._EndDeviceAssets:
            filtered = [q for q in p.ElectricalInfos if q != self]
            self._EndDeviceAssets._ElectricalInfos = filtered
        for r in value:
            if self not in r._ElectricalInfos:
                r._ElectricalInfos.append(self)
        self._EndDeviceAssets = value

    EndDeviceAssets = property(getEndDeviceAssets, setEndDeviceAssets)

    def addEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            if self not in obj._ElectricalInfos:
                obj._ElectricalInfos.append(self)
            self._EndDeviceAssets.append(obj)

    def removeEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            if self in obj._ElectricalInfos:
                obj._ElectricalInfos.remove(self)
            self._EndDeviceAssets.remove(obj)

    def getElectricalTypeAssets(self):
        
        return self._ElectricalTypeAssets

    def setElectricalTypeAssets(self, value):
        for p in self._ElectricalTypeAssets:
            filtered = [q for q in p.ElectricalInfos if q != self]
            self._ElectricalTypeAssets._ElectricalInfos = filtered
        for r in value:
            if self not in r._ElectricalInfos:
                r._ElectricalInfos.append(self)
        self._ElectricalTypeAssets = value

    ElectricalTypeAssets = property(getElectricalTypeAssets, setElectricalTypeAssets)

    def addElectricalTypeAssets(self, *ElectricalTypeAssets):
        for obj in ElectricalTypeAssets:
            if self not in obj._ElectricalInfos:
                obj._ElectricalInfos.append(self)
            self._ElectricalTypeAssets.append(obj)

    def removeElectricalTypeAssets(self, *ElectricalTypeAssets):
        for obj in ElectricalTypeAssets:
            if self in obj._ElectricalInfos:
                obj._ElectricalInfos.remove(self)
            self._ElectricalTypeAssets.remove(obj)

    def getElectricalAssets(self):
        
        return self._ElectricalAssets

    def setElectricalAssets(self, value):
        for p in self._ElectricalAssets:
            filtered = [q for q in p.ElectricalInfos if q != self]
            self._ElectricalAssets._ElectricalInfos = filtered
        for r in value:
            if self not in r._ElectricalInfos:
                r._ElectricalInfos.append(self)
        self._ElectricalAssets = value

    ElectricalAssets = property(getElectricalAssets, setElectricalAssets)

    def addElectricalAssets(self, *ElectricalAssets):
        for obj in ElectricalAssets:
            if self not in obj._ElectricalInfos:
                obj._ElectricalInfos.append(self)
            self._ElectricalAssets.append(obj)

    def removeElectricalAssets(self, *ElectricalAssets):
        for obj in ElectricalAssets:
            if self in obj._ElectricalInfos:
                obj._ElectricalInfos.remove(self)
            self._ElectricalAssets.remove(obj)

    def getElectricalAssetModels(self):
        
        return self._ElectricalAssetModels

    def setElectricalAssetModels(self, value):
        for p in self._ElectricalAssetModels:
            filtered = [q for q in p.ElectricalInfos if q != self]
            self._ElectricalAssetModels._ElectricalInfos = filtered
        for r in value:
            if self not in r._ElectricalInfos:
                r._ElectricalInfos.append(self)
        self._ElectricalAssetModels = value

    ElectricalAssetModels = property(getElectricalAssetModels, setElectricalAssetModels)

    def addElectricalAssetModels(self, *ElectricalAssetModels):
        for obj in ElectricalAssetModels:
            if self not in obj._ElectricalInfos:
                obj._ElectricalInfos.append(self)
            self._ElectricalAssetModels.append(obj)

    def removeElectricalAssetModels(self, *ElectricalAssetModels):
        for obj in ElectricalAssetModels:
            if self in obj._ElectricalInfos:
                obj._ElectricalInfos.remove(self)
            self._ElectricalAssetModels.remove(obj)

