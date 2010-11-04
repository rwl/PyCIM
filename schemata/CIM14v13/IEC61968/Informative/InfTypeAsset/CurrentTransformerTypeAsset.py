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

class CurrentTransformerTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic Current Transformer (CT) that may be used for various purposes such as work planning.
    """

    def __init__(self, usage='', accuracyClass='', accuracyLimit=0.0, kneePointCurrent=0.0, coreBurden=0.0, ctClass='', coreCount=0, kneePointVoltage=0.0, CurrentTransformerInfo=None, CurrentTransformerAssetModels=None, CurrentTransformers=None, nominalRatio=None, maxRatio=None, *args, **kw_args):
        """Initializes a new 'CurrentTransformerTypeAsset' instance.

        @param usage: eg. metering, protection, etc 
        @param accuracyClass: CT accuracy classification 
        @param accuracyLimit: 
        @param kneePointCurrent: Maximum primary current where the CT still displays linear characteristicts. 
        @param coreBurden: Power burden of the CT core 
        @param ctClass: 
        @param coreCount: Number of cores. 
        @param kneePointVoltage: Maximum voltage across the secondary terminals where the CT still displays linear characteristicts. 
        @param CurrentTransformerInfo:
        @param CurrentTransformerAssetModels:
        @param CurrentTransformers:
        @param nominalRatio: Nominal ratio between the primary and secondary current; i.e. 100:5
        @param maxRatio: Maximum ratio between the primary and secondary current.
        """
        #: eg. metering, protection, etc
        self.usage = usage

        #: CT accuracy classification
        self.accuracyClass = accuracyClass


        self.accuracyLimit = accuracyLimit

        #: Maximum primary current where the CT still displays linear characteristicts.
        self.kneePointCurrent = kneePointCurrent

        #: Power burden of the CT core
        self.coreBurden = coreBurden


        self.ctClass = ctClass

        #: Number of cores.
        self.coreCount = coreCount

        #: Maximum voltage across the secondary terminals where the CT still displays linear characteristicts.
        self.kneePointVoltage = kneePointVoltage

        self._CurrentTransformerInfo = None
        self.CurrentTransformerInfo = CurrentTransformerInfo

        self._CurrentTransformerAssetModels = []
        self.CurrentTransformerAssetModels = [] if CurrentTransformerAssetModels is None else CurrentTransformerAssetModels

        self._CurrentTransformers = []
        self.CurrentTransformers = [] if CurrentTransformers is None else CurrentTransformers

        self.nominalRatio = nominalRatio

        self.maxRatio = maxRatio

        super(CurrentTransformerTypeAsset, self).__init__(*args, **kw_args)

    def getCurrentTransformerInfo(self):
        
        return self._CurrentTransformerInfo

    def setCurrentTransformerInfo(self, value):
        if self._CurrentTransformerInfo is not None:
            self._CurrentTransformerInfo._CurrentTransformerTypeAsset = None

        self._CurrentTransformerInfo = value
        if self._CurrentTransformerInfo is not None:
            self._CurrentTransformerInfo._CurrentTransformerTypeAsset = self

    CurrentTransformerInfo = property(getCurrentTransformerInfo, setCurrentTransformerInfo)

    def getCurrentTransformerAssetModels(self):
        
        return self._CurrentTransformerAssetModels

    def setCurrentTransformerAssetModels(self, value):
        for x in self._CurrentTransformerAssetModels:
            x._CurrentTransformerTypeAsset = None
        for y in value:
            y._CurrentTransformerTypeAsset = self
        self._CurrentTransformerAssetModels = value

    CurrentTransformerAssetModels = property(getCurrentTransformerAssetModels, setCurrentTransformerAssetModels)

    def addCurrentTransformerAssetModels(self, *CurrentTransformerAssetModels):
        for obj in CurrentTransformerAssetModels:
            obj._CurrentTransformerTypeAsset = self
            self._CurrentTransformerAssetModels.append(obj)

    def removeCurrentTransformerAssetModels(self, *CurrentTransformerAssetModels):
        for obj in CurrentTransformerAssetModels:
            obj._CurrentTransformerTypeAsset = None
            self._CurrentTransformerAssetModels.remove(obj)

    def getCurrentTransformers(self):
        
        return self._CurrentTransformers

    def setCurrentTransformers(self, value):
        for x in self._CurrentTransformers:
            x._CurrentTransformerTypeAsset = None
        for y in value:
            y._CurrentTransformerTypeAsset = self
        self._CurrentTransformers = value

    CurrentTransformers = property(getCurrentTransformers, setCurrentTransformers)

    def addCurrentTransformers(self, *CurrentTransformers):
        for obj in CurrentTransformers:
            obj._CurrentTransformerTypeAsset = self
            self._CurrentTransformers.append(obj)

    def removeCurrentTransformers(self, *CurrentTransformers):
        for obj in CurrentTransformers:
            obj._CurrentTransformerTypeAsset = None
            self._CurrentTransformers.remove(obj)

    # Nominal ratio between the primary and secondary current; i.e. 100:5
    nominalRatio = None

    # Maximum ratio between the primary and secondary current.
    maxRatio = None

