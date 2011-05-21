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

from CIM15.CDPSM.Balanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ShuntCompensator(IdentifiedObject):
    """A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.
    """

    def __init__(self, nomQ=0.0, maxU=0.0, g0PerSection=0.0, gPerSection=0.0, minU=0.0, bPerSection=0.0, reactivePerSection=0.0, voltageSensitivity=0.0, nomU=0.0, normalSections=0, b0PerSection=0.0, maximumSections=0, *args, **kw_args):
        """Initialises a new 'ShuntCompensator' instance.

        @param nomQ: Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive. 
        @param maxU: The maximum voltage at which the capacitor bank should operate. 
        @param g0PerSection: Zero sequence shunt (charging) conductance per section 
        @param gPerSection: Positive sequence shunt (charging) conductance per section 
        @param minU: The minimum voltage at which the capacitor bank should operate. 
        @param bPerSection: Positive sequence shunt (charging) susceptance per section 
        @param reactivePerSection: For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage. 
        @param voltageSensitivity: Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power. 
        @param nomU: The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network. 
        @param normalSections: For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ). 
        @param b0PerSection: Zero sequence shunt (charging) susceptance per section 
        @param maximumSections: For a capacitor bank, the maximum number of sections that may be switched in. 
        """
        #: Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.
        self.nomQ = nomQ

        #: The maximum voltage at which the capacitor bank should operate.
        self.maxU = maxU

        #: Zero sequence shunt (charging) conductance per section
        self.g0PerSection = g0PerSection

        #: Positive sequence shunt (charging) conductance per section
        self.gPerSection = gPerSection

        #: The minimum voltage at which the capacitor bank should operate.
        self.minU = minU

        #: Positive sequence shunt (charging) susceptance per section
        self.bPerSection = bPerSection

        #: For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
        self.reactivePerSection = reactivePerSection

        #: Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power.
        self.voltageSensitivity = voltageSensitivity

        #: The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
        self.nomU = nomU

        #: For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
        self.normalSections = normalSections

        #: Zero sequence shunt (charging) susceptance per section
        self.b0PerSection = b0PerSection

        #: For a capacitor bank, the maximum number of sections that may be switched in.
        self.maximumSections = maximumSections

        super(ShuntCompensator, self).__init__(*args, **kw_args)

    _attrs = ["nomQ", "maxU", "g0PerSection", "gPerSection", "minU", "bPerSection", "reactivePerSection", "voltageSensitivity", "nomU", "normalSections", "b0PerSection", "maximumSections"]
    _attr_types = {"nomQ": float, "maxU": float, "g0PerSection": float, "gPerSection": float, "minU": float, "bPerSection": float, "reactivePerSection": float, "voltageSensitivity": float, "nomU": float, "normalSections": int, "b0PerSection": float, "maximumSections": int}
    _defaults = {"nomQ": 0.0, "maxU": 0.0, "g0PerSection": 0.0, "gPerSection": 0.0, "minU": 0.0, "bPerSection": 0.0, "reactivePerSection": 0.0, "voltageSensitivity": 0.0, "nomU": 0.0, "normalSections": 0, "b0PerSection": 0.0, "maximumSections": 0}
    _enums = {}
    _refs = []
    _many_refs = []

