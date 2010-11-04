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

class PotentialTransformerTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic Potential Transformer (PT) that may be used for various purposes such as work planning.
    """

    def __init__(self, ptClass='', accuracyClass='', nominalRatio=None, PotentialTransformers=None, PotentialTransformerAssetModels=None, PotentialTransformerInfo=None, *args, **kw_args):
        """Initializes a new 'PotentialTransformerTypeAsset' instance.

        @param ptClass: 
        @param accuracyClass: 
        @param nominalRatio:
        @param PotentialTransformers:
        @param PotentialTransformerAssetModels:
        @param PotentialTransformerInfo:
        """

        self.ptClass = ptClass


        self.accuracyClass = accuracyClass

        self.nominalRatio = nominalRatio

        self._PotentialTransformers = []
        self.PotentialTransformers = [] if PotentialTransformers is None else PotentialTransformers

        self._PotentialTransformerAssetModels = []
        self.PotentialTransformerAssetModels = [] if PotentialTransformerAssetModels is None else PotentialTransformerAssetModels

        self._PotentialTransformerInfo = None
        self.PotentialTransformerInfo = PotentialTransformerInfo

        super(PotentialTransformerTypeAsset, self).__init__(*args, **kw_args)

    nominalRatio = None

    def getPotentialTransformers(self):
        
        return self._PotentialTransformers

    def setPotentialTransformers(self, value):
        for x in self._PotentialTransformers:
            x._PotentialTransformerTypeAsset = None
        for y in value:
            y._PotentialTransformerTypeAsset = self
        self._PotentialTransformers = value

    PotentialTransformers = property(getPotentialTransformers, setPotentialTransformers)

    def addPotentialTransformers(self, *PotentialTransformers):
        for obj in PotentialTransformers:
            obj._PotentialTransformerTypeAsset = self
            self._PotentialTransformers.append(obj)

    def removePotentialTransformers(self, *PotentialTransformers):
        for obj in PotentialTransformers:
            obj._PotentialTransformerTypeAsset = None
            self._PotentialTransformers.remove(obj)

    def getPotentialTransformerAssetModels(self):
        
        return self._PotentialTransformerAssetModels

    def setPotentialTransformerAssetModels(self, value):
        for x in self._PotentialTransformerAssetModels:
            x._PotentialTransformerTypeAsset = None
        for y in value:
            y._PotentialTransformerTypeAsset = self
        self._PotentialTransformerAssetModels = value

    PotentialTransformerAssetModels = property(getPotentialTransformerAssetModels, setPotentialTransformerAssetModels)

    def addPotentialTransformerAssetModels(self, *PotentialTransformerAssetModels):
        for obj in PotentialTransformerAssetModels:
            obj._PotentialTransformerTypeAsset = self
            self._PotentialTransformerAssetModels.append(obj)

    def removePotentialTransformerAssetModels(self, *PotentialTransformerAssetModels):
        for obj in PotentialTransformerAssetModels:
            obj._PotentialTransformerTypeAsset = None
            self._PotentialTransformerAssetModels.remove(obj)

    def getPotentialTransformerInfo(self):
        
        return self._PotentialTransformerInfo

    def setPotentialTransformerInfo(self, value):
        if self._PotentialTransformerInfo is not None:
            self._PotentialTransformerInfo._PotentialTransformerTypeAsset = None

        self._PotentialTransformerInfo = value
        if self._PotentialTransformerInfo is not None:
            self._PotentialTransformerInfo._PotentialTransformerTypeAsset = self

    PotentialTransformerInfo = property(getPotentialTransformerInfo, setPotentialTransformerInfo)

