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

class GeneratorTypeAsset(ElectricalTypeAsset):
    """Documentation for generic generation equipment that may be used for various purposes such as work planning. It defines both the Real and Reactive power properties (modelled at the PSR level as a GeneratingUnit + SynchronousMachine)
    """

    def __init__(self, rDirectSubtrans=0.0, xDirectSubtrans=0.0, rQuadTrans=0.0, xQuadTrans=0.0, xQuadSync=0.0, xDirectSync=0.0, rQuadSync=0.0, maxQ=0.0, rDirectSync=0.0, rDirectTrans=0.0, rQuadSubtrans=0.0, minQ=0.0, minP=0.0, maxP=0.0, xDirectTrans=0.0, xQuadSubtrans=0.0, GeneratorAssetModels=None, **kw_args):
        """Initializes a new 'GeneratorTypeAsset' instance.

        @param rDirectSubtrans: Direct-axis subtransient resistance 
        @param xDirectSubtrans: Direct-axis subtransient reactance 
        @param rQuadTrans: Quadrature-axis Transient resistance 
        @param xQuadTrans: Quadrature-axis transient reactance. 
        @param xQuadSync: Quadrature-axis synchronous reactance 
        @param xDirectSync: Direct-axis synchronous reactance 
        @param rQuadSync: Quadrature-axis synchronous resistance 
        @param maxQ: Maximum reactive power limit. 
        @param rDirectSync: Direct-axis synchronous resistance 
        @param rDirectTrans: Direct-axis Transient resistance 
        @param rQuadSubtrans: Quadrature-axis subtransient resistance 
        @param minQ: Minimum reactive power generated. 
        @param minP: Minimum real power generated. 
        @param maxP: Maximum real power limit. 
        @param xDirectTrans: Direct-axis Transient reactance 
        @param xQuadSubtrans: Quadrature-axis subtransient reactance 
        @param GeneratorAssetModels:
        """
        #: Direct-axis subtransient resistance
        self.rDirectSubtrans = rDirectSubtrans

        #: Direct-axis subtransient reactance
        self.xDirectSubtrans = xDirectSubtrans

        #: Quadrature-axis Transient resistance
        self.rQuadTrans = rQuadTrans

        #: Quadrature-axis transient reactance.
        self.xQuadTrans = xQuadTrans

        #: Quadrature-axis synchronous reactance
        self.xQuadSync = xQuadSync

        #: Direct-axis synchronous reactance
        self.xDirectSync = xDirectSync

        #: Quadrature-axis synchronous resistance
        self.rQuadSync = rQuadSync

        #: Maximum reactive power limit.
        self.maxQ = maxQ

        #: Direct-axis synchronous resistance
        self.rDirectSync = rDirectSync

        #: Direct-axis Transient resistance
        self.rDirectTrans = rDirectTrans

        #: Quadrature-axis subtransient resistance
        self.rQuadSubtrans = rQuadSubtrans

        #: Minimum reactive power generated.
        self.minQ = minQ

        #: Minimum real power generated.
        self.minP = minP

        #: Maximum real power limit.
        self.maxP = maxP

        #: Direct-axis Transient reactance
        self.xDirectTrans = xDirectTrans

        #: Quadrature-axis subtransient reactance
        self.xQuadSubtrans = xQuadSubtrans

        self._GeneratorAssetModels = []
        self.GeneratorAssetModels = [] if GeneratorAssetModels is None else GeneratorAssetModels

        super(GeneratorTypeAsset, self).__init__(**kw_args)

    def getGeneratorAssetModels(self):
        
        return self._GeneratorAssetModels

    def setGeneratorAssetModels(self, value):
        for x in self._GeneratorAssetModels:
            x._GeneratorTypeAsset = None
        for y in value:
            y._GeneratorTypeAsset = self
        self._GeneratorAssetModels = value

    GeneratorAssetModels = property(getGeneratorAssetModels, setGeneratorAssetModels)

    def addGeneratorAssetModels(self, *GeneratorAssetModels):
        for obj in GeneratorAssetModels:
            obj._GeneratorTypeAsset = self
            self._GeneratorAssetModels.append(obj)

    def removeGeneratorAssetModels(self, *GeneratorAssetModels):
        for obj in GeneratorAssetModels:
            obj._GeneratorTypeAsset = None
            self._GeneratorAssetModels.remove(obj)

