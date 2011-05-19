# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Informative.InfAssets.GenericAssetModelOrMaterial import GenericAssetModelOrMaterial

class GeneratorTypeAsset(GenericAssetModelOrMaterial):
    """Documentation for generic generation equipment that may be used for various purposes such as work planning. It defines both the Real and Reactive power properties (modelled at the PSR level as a GeneratingUnit + SynchronousMachine)Documentation for generic generation equipment that may be used for various purposes such as work planning. It defines both the Real and Reactive power properties (modelled at the PSR level as a GeneratingUnit + SynchronousMachine)
    """

    def __init__(self, xDirectSync=0.0, rQuadSubtrans=0.0, rDirectSync=0.0, rDirectSubtrans=0.0, maxQ=0.0, xQuadSync=0.0, minQ=0.0, minP=0.0, maxP=0.0, rQuadSync=0.0, xQuadSubtrans=0.0, rDirectTrans=0.0, rQuadTrans=0.0, xDirectSubtrans=0.0, xDirectTrans=0.0, xQuadTrans=0.0, *args, **kw_args):
        """Initialises a new 'GeneratorTypeAsset' instance.

        @param xDirectSync: Direct-axis synchronous reactance 
        @param rQuadSubtrans: Quadrature-axis subtransient resistance 
        @param rDirectSync: Direct-axis synchronous resistance 
        @param rDirectSubtrans: Direct-axis subtransient resistance 
        @param maxQ: Maximum reactive power limit. 
        @param xQuadSync: Quadrature-axis synchronous reactance 
        @param minQ: Minimum reactive power generated. 
        @param minP: Minimum real power generated. 
        @param maxP: Maximum real power limit. 
        @param rQuadSync: Quadrature-axis synchronous resistance 
        @param xQuadSubtrans: Quadrature-axis subtransient reactance 
        @param rDirectTrans: Direct-axis Transient resistance 
        @param rQuadTrans: Quadrature-axis Transient resistance 
        @param xDirectSubtrans: Direct-axis subtransient reactance 
        @param xDirectTrans: Direct-axis Transient reactance 
        @param xQuadTrans: Quadrature-axis transient reactance. 
        """
        #: Direct-axis synchronous reactance
        self.xDirectSync = xDirectSync

        #: Quadrature-axis subtransient resistance
        self.rQuadSubtrans = rQuadSubtrans

        #: Direct-axis synchronous resistance
        self.rDirectSync = rDirectSync

        #: Direct-axis subtransient resistance
        self.rDirectSubtrans = rDirectSubtrans

        #: Maximum reactive power limit.
        self.maxQ = maxQ

        #: Quadrature-axis synchronous reactance
        self.xQuadSync = xQuadSync

        #: Minimum reactive power generated.
        self.minQ = minQ

        #: Minimum real power generated.
        self.minP = minP

        #: Maximum real power limit.
        self.maxP = maxP

        #: Quadrature-axis synchronous resistance
        self.rQuadSync = rQuadSync

        #: Quadrature-axis subtransient reactance
        self.xQuadSubtrans = xQuadSubtrans

        #: Direct-axis Transient resistance
        self.rDirectTrans = rDirectTrans

        #: Quadrature-axis Transient resistance
        self.rQuadTrans = rQuadTrans

        #: Direct-axis subtransient reactance
        self.xDirectSubtrans = xDirectSubtrans

        #: Direct-axis Transient reactance
        self.xDirectTrans = xDirectTrans

        #: Quadrature-axis transient reactance.
        self.xQuadTrans = xQuadTrans

        super(GeneratorTypeAsset, self).__init__(*args, **kw_args)

    _attrs = ["xDirectSync", "rQuadSubtrans", "rDirectSync", "rDirectSubtrans", "maxQ", "xQuadSync", "minQ", "minP", "maxP", "rQuadSync", "xQuadSubtrans", "rDirectTrans", "rQuadTrans", "xDirectSubtrans", "xDirectTrans", "xQuadTrans"]
    _attr_types = {"xDirectSync": float, "rQuadSubtrans": float, "rDirectSync": float, "rDirectSubtrans": float, "maxQ": float, "xQuadSync": float, "minQ": float, "minP": float, "maxP": float, "rQuadSync": float, "xQuadSubtrans": float, "rDirectTrans": float, "rQuadTrans": float, "xDirectSubtrans": float, "xDirectTrans": float, "xQuadTrans": float}
    _defaults = {"xDirectSync": 0.0, "rQuadSubtrans": 0.0, "rDirectSync": 0.0, "rDirectSubtrans": 0.0, "maxQ": 0.0, "xQuadSync": 0.0, "minQ": 0.0, "minP": 0.0, "maxP": 0.0, "rQuadSync": 0.0, "xQuadSubtrans": 0.0, "rDirectTrans": 0.0, "rQuadTrans": 0.0, "xDirectSubtrans": 0.0, "xDirectTrans": 0.0, "xQuadTrans": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

