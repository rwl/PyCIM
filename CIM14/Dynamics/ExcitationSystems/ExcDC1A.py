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

class ExcDC1A(ExcitationSystem):
    """IEEE (1992/2005) DC1A Model  This model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types). Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required.
    """

    def __init__(self, ta=0.0, ka=0.0, e1=0.0, tb=0.0, se2=0.0, te=0.0, exclim=0.0, e2=0.0, tr=0.0, uelin=0.0, tf=0.0, vrmax=0.0, kf=0.0, ke=0.0, se1=0.0, vrmin=0.0, tc=0.0, *args, **kw_args):
        """Initialises a new 'ExcDC1A' instance.

        @param ta: Time constant (&gt; 0.) 
        @param ka: Gain (&gt; 0.) 
        @param e1: Field voltage value 1    (&gt; 0.) 
        @param tb: Lag time constant (&gt;= 0.) 
        @param se2: Saturation factor at e2  (&gt;= 0.) 
        @param te: Exciter time constant (&gt; 0.) 
        @param exclim: If not 0, apply lower limit of 0. to exciter output 
        @param e2: Field voltage value 2.   (&gt; 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param uelin: UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        @param tf: Rate feedback time constant, sec. (&gt; 0.) 
        @param vrmax: Maximum controller output 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param ke: Exciter field resistance line slope 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param vrmin: Minimum controller output (&lt; 0.) 
        @param tc: Lead time constant 
        """
        #: Time constant (&gt; 0.)
        self.ta = ta

        #: Gain (&gt; 0.)
        self.ka = ka

        #: Field voltage value 1    (&gt; 0.)
        self.e1 = e1

        #: Lag time constant (&gt;= 0.)
        self.tb = tb

        #: Saturation factor at e2  (&gt;= 0.)
        self.se2 = se2

        #: Exciter time constant (&gt; 0.)
        self.te = te

        #: If not 0, apply lower limit of 0. to exciter output
        self.exclim = exclim

        #: Field voltage value 2.   (&gt; 0.)
        self.e2 = e2

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: UEL input: if &lt; 2, HV gate; if = 2, add to error signal
        self.uelin = uelin

        #: Rate feedback time constant, sec. (&gt; 0.)
        self.tf = tf

        #: Maximum controller output
        self.vrmax = vrmax

        #: Rate feedback gain (&gt;= 0.)
        self.kf = kf

        #: Exciter field resistance line slope
        self.ke = ke

        #: Saturation factor at e1  (&gt;= 0.)
        self.se1 = se1

        #: Minimum controller output (&lt; 0.)
        self.vrmin = vrmin

        #: Lead time constant
        self.tc = tc

        super(ExcDC1A, self).__init__(*args, **kw_args)

    _attrs = ["ta", "ka", "e1", "tb", "se2", "te", "exclim", "e2", "tr", "uelin", "tf", "vrmax", "kf", "ke", "se1", "vrmin", "tc"]
    _attr_types = {"ta": float, "ka": float, "e1": float, "tb": float, "se2": float, "te": float, "exclim": float, "e2": float, "tr": float, "uelin": float, "tf": float, "vrmax": float, "kf": float, "ke": float, "se1": float, "vrmin": float, "tc": float}
    _defaults = {"ta": 0.0, "ka": 0.0, "e1": 0.0, "tb": 0.0, "se2": 0.0, "te": 0.0, "exclim": 0.0, "e2": 0.0, "tr": 0.0, "uelin": 0.0, "tf": 0.0, "vrmax": 0.0, "kf": 0.0, "ke": 0.0, "se1": 0.0, "vrmin": 0.0, "tc": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

