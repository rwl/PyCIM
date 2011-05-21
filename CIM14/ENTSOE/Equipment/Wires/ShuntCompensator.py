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

from CIM14.ENTSOE.Equipment.Wires.RegulatingCondEq import RegulatingCondEq

class ShuntCompensator(RegulatingCondEq):
    """A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.-  [R9.3] is satisfied by navigation to ConnectivityNode and Substation -  If the reactivePerSection attribute is positive, the Compensator is a capacitor.  If the value is negative, the Compensator is a reactor. -  Attributes b0PerSection and g0PerSection are not required.
    """

    def __init__(self, g0PerSection=0.0, bPerSection=0.0, nomU=0.0, gPerSection=0.0, normalSections=0, b0PerSection=0.0, maximumSections=0, *args, **kw_args):
        """Initialises a new 'ShuntCompensator' instance.

        @param g0PerSection: Zero sequence shunt (charging) conductance per section 
        @param bPerSection: Positive sequence shunt (charging) susceptance per section 
        @param nomU: The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network. 
        @param gPerSection: Positive sequence shunt (charging) conductance per section 
        @param normalSections: For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ). 
        @param b0PerSection: Zero sequence shunt (charging) susceptance per section 
        @param maximumSections: For a capacitor bank, the maximum number of sections that may be switched in. 
        """
        #: Zero sequence shunt (charging) conductance per section
        self.g0PerSection = g0PerSection

        #: Positive sequence shunt (charging) susceptance per section
        self.bPerSection = bPerSection

        #: The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
        self.nomU = nomU

        #: Positive sequence shunt (charging) conductance per section
        self.gPerSection = gPerSection

        #: For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
        self.normalSections = normalSections

        #: Zero sequence shunt (charging) susceptance per section
        self.b0PerSection = b0PerSection

        #: For a capacitor bank, the maximum number of sections that may be switched in.
        self.maximumSections = maximumSections

        super(ShuntCompensator, self).__init__(*args, **kw_args)

    _attrs = ["g0PerSection", "bPerSection", "nomU", "gPerSection", "normalSections", "b0PerSection", "maximumSections"]
    _attr_types = {"g0PerSection": float, "bPerSection": float, "nomU": float, "gPerSection": float, "normalSections": int, "b0PerSection": float, "maximumSections": int}
    _defaults = {"g0PerSection": 0.0, "bPerSection": 0.0, "nomU": 0.0, "gPerSection": 0.0, "normalSections": 0, "b0PerSection": 0.0, "maximumSections": 0}
    _enums = {}
    _refs = []
    _many_refs = []

