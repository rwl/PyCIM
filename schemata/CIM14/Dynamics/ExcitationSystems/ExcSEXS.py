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

from CIM14.Dynamics.ExcitationSystems.ExcitationSystem import ExcitationSystem

class ExcSEXS(ExcitationSystem):
    """Simplified Excitation System Model
    """

    def __init__(self, tb=0.0, kc=0.0, emax=0.0, tatb=0.0, tc=0.0, efdmin=0.0, efdmax=0.0, emin=0.0, k=0.0, te=0.0, **kw_args):
        """Initializes a new 'ExcSEXS' instance.

        @param tb: Denominator time constant of lag-lead block 
        @param kc: PI controller gain (&gt; 0. if Tc &gt; 0.) 
        @param emax: Maximum field voltage output 
        @param tatb: Ta/Tb - gain reduction ratio of lag-lead element 
        @param tc: PI controller phase lead time constant 
        @param efdmin: Field voltage clipping minimum limit 
        @param efdmax: Field voltage clipping maximum limit 
        @param emin: Minimum field voltage output 
        @param k: Gain (&gt; 0.) 
        @param te: Time constant of gain block (&gt; 0.) 
        """
        #: Denominator time constant of lag-lead block
        self.tb = tb

        #: PI controller gain (&gt; 0. if Tc &gt; 0.)
        self.kc = kc

        #: Maximum field voltage output
        self.emax = emax

        #: Ta/Tb - gain reduction ratio of lag-lead element
        self.tatb = tatb

        #: PI controller phase lead time constant
        self.tc = tc

        #: Field voltage clipping minimum limit
        self.efdmin = efdmin

        #: Field voltage clipping maximum limit
        self.efdmax = efdmax

        #: Minimum field voltage output
        self.emin = emin

        #: Gain (&gt; 0.)
        self.k = k

        #: Time constant of gain block (&gt; 0.)
        self.te = te

        super(ExcSEXS, self).__init__(**kw_args)

