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

class SurgeProtectorTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic surge arrestor that may be used for design purposes.
    """

    def __init__(self, maximumEnergyAbsorption=0.0, maximumContinousOperatingVoltage=0.0, maximumCurrentRating=0.0, nominalDesignVoltage=0.0, SurgeProtectors=None, SurgeProtectorAssetModels=None, *args, **kw_args):
        """Initializes a new 'SurgeProtectorTypeAsset' instance.

        @param maximumEnergyAbsorption: 
        @param maximumContinousOperatingVoltage: 
        @param maximumCurrentRating: 
        @param nominalDesignVoltage: 
        @param SurgeProtectors:
        @param SurgeProtectorAssetModels:
        """
 
        self.maximumEnergyAbsorption = maximumEnergyAbsorption

 
        self.maximumContinousOperatingVoltage = maximumContinousOperatingVoltage

 
        self.maximumCurrentRating = maximumCurrentRating

 
        self.nominalDesignVoltage = nominalDesignVoltage

        self._SurgeProtectors = []
        self.SurgeProtectors = [] if SurgeProtectors is None else SurgeProtectors

        self._SurgeProtectorAssetModels = []
        self.SurgeProtectorAssetModels = [] if SurgeProtectorAssetModels is None else SurgeProtectorAssetModels

        super(SurgeProtectorTypeAsset, self).__init__(*args, **kw_args)

    def getSurgeProtectors(self):
        
        return self._SurgeProtectors

    def setSurgeProtectors(self, value):
        for x in self._SurgeProtectors:
            x._SurgeProtectorTypeAsset = None
        for y in value:
            y._SurgeProtectorTypeAsset = self
        self._SurgeProtectors = value

    SurgeProtectors = property(getSurgeProtectors, setSurgeProtectors)

    def addSurgeProtectors(self, *SurgeProtectors):
        for obj in SurgeProtectors:
            obj._SurgeProtectorTypeAsset = self
            self._SurgeProtectors.append(obj)

    def removeSurgeProtectors(self, *SurgeProtectors):
        for obj in SurgeProtectors:
            obj._SurgeProtectorTypeAsset = None
            self._SurgeProtectors.remove(obj)

    def getSurgeProtectorAssetModels(self):
        
        return self._SurgeProtectorAssetModels

    def setSurgeProtectorAssetModels(self, value):
        for x in self._SurgeProtectorAssetModels:
            x._SurgeProtectorTypeAsset = None
        for y in value:
            y._SurgeProtectorTypeAsset = self
        self._SurgeProtectorAssetModels = value

    SurgeProtectorAssetModels = property(getSurgeProtectorAssetModels, setSurgeProtectorAssetModels)

    def addSurgeProtectorAssetModels(self, *SurgeProtectorAssetModels):
        for obj in SurgeProtectorAssetModels:
            obj._SurgeProtectorTypeAsset = self
            self._SurgeProtectorAssetModels.append(obj)

    def removeSurgeProtectorAssetModels(self, *SurgeProtectorAssetModels):
        for obj in SurgeProtectorAssetModels:
            obj._SurgeProtectorTypeAsset = None
            self._SurgeProtectorAssetModels.remove(obj)

