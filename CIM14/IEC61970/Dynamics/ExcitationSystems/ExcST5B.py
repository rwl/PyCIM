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

from CIM14.IEC61970.Dynamics.ExcitationSystems.ExcitationSystem import ExcitationSystem

class ExcST5B(ExcitationSystem):
    """IEEE (2005) ST5B Model  The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits. The corresponding stabilizer models that can be used with these models are the Type PSS2B, PSS3B, or PSS4B.
    """

    def __init__(self, tb2=0.0, tb1=0.0, tub2=0.0, tuc1=0.0, kr=0.0, tob2=0.0, tob1=0.0, tc1=0.0, toc1=0.0, tub1=0.0, tc2=0.0, kc=0.0, vrmax=0.0, tuc2=0.0, toc2=0.0, t1=0.0, tr=0.0, vrmin=0.0, *args, **kw_args):
        """Initialises a new 'ExcST5B' instance.

        @param tb2: Regulator lag time constant (&gt;= 0.) 
        @param tb1: Regulator lag time constant (&gt;= 0.) 
        @param tub2: UEL lag time constant (&gt;= 0.) 
        @param tuc1: UEL lead time constant. 
        @param kr: Regulator gain (&gt; 0.) 
        @param tob2: OEL lag time constant (&gt;= 0.) 
        @param tob1: OEL lag time constant (&gt;= 0.) 
        @param tc1: Regulator lead time constant 
        @param toc1: OEL lead time constant 
        @param tub1: UEL lag time constant (&gt;= 0.) 
        @param tc2: Regulator lead time constant. 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param vrmax: Maximum regulator output (&gt; 0.) 
        @param tuc2: UEL lead time constant 
        @param toc2: OEL lead time constant 
        @param t1: Firing circuit time constant (&gt;= 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param vrmin: Minimum regulator output (&lt; 0.) 
        """
        #: Regulator lag time constant (&gt;= 0.)
        self.tb2 = tb2

        #: Regulator lag time constant (&gt;= 0.)
        self.tb1 = tb1

        #: UEL lag time constant (&gt;= 0.)
        self.tub2 = tub2

        #: UEL lead time constant.
        self.tuc1 = tuc1

        #: Regulator gain (&gt; 0.)
        self.kr = kr

        #: OEL lag time constant (&gt;= 0.)
        self.tob2 = tob2

        #: OEL lag time constant (&gt;= 0.)
        self.tob1 = tob1

        #: Regulator lead time constant
        self.tc1 = tc1

        #: OEL lead time constant
        self.toc1 = toc1

        #: UEL lag time constant (&gt;= 0.)
        self.tub1 = tub1

        #: Regulator lead time constant.
        self.tc2 = tc2

        #: Rectifier regulation factor (&gt;= 0.)
        self.kc = kc

        #: Maximum regulator output (&gt; 0.)
        self.vrmax = vrmax

        #: UEL lead time constant
        self.tuc2 = tuc2

        #: OEL lead time constant
        self.toc2 = toc2

        #: Firing circuit time constant (&gt;= 0.)
        self.t1 = t1

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Minimum regulator output (&lt; 0.)
        self.vrmin = vrmin

        super(ExcST5B, self).__init__(*args, **kw_args)

    _attrs = ["tb2", "tb1", "tub2", "tuc1", "kr", "tob2", "tob1", "tc1", "toc1", "tub1", "tc2", "kc", "vrmax", "tuc2", "toc2", "t1", "tr", "vrmin"]
    _attr_types = {"tb2": float, "tb1": float, "tub2": float, "tuc1": float, "kr": float, "tob2": float, "tob1": float, "tc1": float, "toc1": float, "tub1": float, "tc2": float, "kc": float, "vrmax": float, "tuc2": float, "toc2": float, "t1": float, "tr": float, "vrmin": float}
    _defaults = {"tb2": 0.0, "tb1": 0.0, "tub2": 0.0, "tuc1": 0.0, "kr": 0.0, "tob2": 0.0, "tob1": 0.0, "tc1": 0.0, "toc1": 0.0, "tub1": 0.0, "tc2": 0.0, "kc": 0.0, "vrmax": 0.0, "tuc2": 0.0, "toc2": 0.0, "t1": 0.0, "tr": 0.0, "vrmin": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

