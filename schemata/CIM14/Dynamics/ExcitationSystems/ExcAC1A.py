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

class ExcAC1A(ExcitationSystem):
    """IEEE (1992/2005) AC1A Model The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.
    """

    def __init__(self, vrmin=0.0, tr=0.0, vrmax=0.0, ta=0.0, kf=0.0, te=0.0, ka=0.0, vamax=0.0, tb=0.0, e1=0.0, kd=0.0, se1=0.0, vamin=0.0, ke=0.0, kc=0.0, tf=0.0, tc=0.0, e2=0.0, se2=0.0, **kw_args):
        """Initializes a new 'ExcAC1A' instance.

        @param vrmin: Minimum exciter control signal  (&lt; 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param vrmax: Maximum exciter control signal (&gt; 0.) 
        @param ta: AVR time constant (&gt; 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param te: Exciter time constant (&gt; 0.) 
        @param ka: AVR gain (&gt; 0.) 
        @param vamax: Maximum AVR output (&gt; 0.) 
        @param tb: TGR lag time constant (&gt;= 0.) 
        @param e1: Field voltage value 1    (&gt; 0.) 
        @param kd: Exciter internal reactance  (&gt;= 0.) 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param vamin: Minimum AVR output (&lt; 0.) 
        @param ke: Exciter field resistance constant 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param tf: Rate feedback time constant (&gt; 0.) 
        @param tc: TGR lead time constant 
        @param e2: Field voltage value 2.   (&gt; 0.) 
        @param se2: Saturation factor at e2   (&gt;= 0.) 
        """
        #: Minimum exciter control signal  (&lt; 0.)
        self.vrmin = vrmin

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Maximum exciter control signal (&gt; 0.)
        self.vrmax = vrmax

        #: AVR time constant (&gt; 0.)
        self.ta = ta

        #: Rate feedback gain (&gt;= 0.)
        self.kf = kf

        #: Exciter time constant (&gt; 0.)
        self.te = te

        #: AVR gain (&gt; 0.)
        self.ka = ka

        #: Maximum AVR output (&gt; 0.)
        self.vamax = vamax

        #: TGR lag time constant (&gt;= 0.)
        self.tb = tb

        #: Field voltage value 1    (&gt; 0.)
        self.e1 = e1

        #: Exciter internal reactance  (&gt;= 0.)
        self.kd = kd

        #: Saturation factor at e1  (&gt;= 0.)
        self.se1 = se1

        #: Minimum AVR output (&lt; 0.)
        self.vamin = vamin

        #: Exciter field resistance constant
        self.ke = ke

        #: Rectifier regulation factor (&gt;= 0.)
        self.kc = kc

        #: Rate feedback time constant (&gt; 0.)
        self.tf = tf

        #: TGR lead time constant
        self.tc = tc

        #: Field voltage value 2.   (&gt; 0.)
        self.e2 = e2

        #: Saturation factor at e2   (&gt;= 0.)
        self.se2 = se2

        super(ExcAC1A, self).__init__(**kw_args)

