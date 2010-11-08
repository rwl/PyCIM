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

from CIM14.Dynamics.VoltageCompensator.VoltageCompensator import VoltageCompensator

class VcompCross(VoltageCompensator):
    """Voltage Compensation Model for Cross-Compound Generating Unit
    """

    def __init__(self, xcomp2=0.0, rcomp2=0.0, *args, **kw_args):
        """Initialises a new 'VcompCross' instance.

        @param xcomp2: Cross-Compensating (compounding) reactance 
        @param rcomp2: Cross-Compensating (compounding) resistance 
        """
        #: Cross-Compensating (compounding) reactance
        self.xcomp2 = xcomp2

        #: Cross-Compensating (compounding) resistance
        self.rcomp2 = rcomp2

        super(VcompCross, self).__init__(*args, **kw_args)

    _attrs = ["xcomp2", "rcomp2"]
    _attr_types = {"xcomp2": float, "rcomp2": float}
    _defaults = {"xcomp2": 0.0, "rcomp2": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

