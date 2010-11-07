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

class ExcSCRX(ExcitationSystem):
    """Simple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problem
    """

    def __init__(self, tb=0.0, cswitch=False, emin=0.0, k=0.0, te=0.0, emax=0.0, tatb=0.0, rcrfd=0.0, **kw_args):
        """Initializes a new 'ExcSCRX' instance.

        @param tb: Denominator time constant of lag-lead block 
        @param cswitch: Power source switch:     1 ? fixed voltage     0 ? generator terminal voltage 
        @param emin: Minimum field voltage output 
        @param k: Gain (&gt; 0.) 
        @param te: Time constant of gain block (&gt; 0.) 
        @param emax: Maximum field voltage output 
        @param tatb: Ta/Tb - gain reduction ratio of lag-lead element 
        @param rcrfd: Rc/Rfd - ratio of field discharge resistance to field winding resistance 
        """
        #: Denominator time constant of lag-lead block
        self.tb = tb

        #: Power source switch:     1 ? fixed voltage     0 ? generator terminal voltage
        self.cswitch = cswitch

        #: Minimum field voltage output
        self.emin = emin

        #: Gain (&gt; 0.)
        self.k = k

        #: Time constant of gain block (&gt; 0.)
        self.te = te

        #: Maximum field voltage output
        self.emax = emax

        #: Ta/Tb - gain reduction ratio of lag-lead element
        self.tatb = tatb

        #: Rc/Rfd - ratio of field discharge resistance to field winding resistance
        self.rcrfd = rcrfd

        super(ExcSCRX, self).__init__(**kw_args)

