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

from CIM14.CDPSM.Balanced.IEC61970.Core.ConductingEquipment import ConductingEquipment

class ShuntCompensator(ConductingEquipment):
    """A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.
    """

    def __init__(self, nomQ=0.0, nomU=0.0, normalSections=0, maximumSections=0, reactivePerSection=0.0, *args, **kw_args):
        """Initialises a new 'ShuntCompensator' instance.

        @param nomQ: Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive. 
        @param nomU: The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network. 
        @param normalSections: For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ). 
        @param maximumSections: For a capacitor bank, the maximum number of sections that may be switched in. 
        @param reactivePerSection: For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage. 
        """
        #: Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.
        self.nomQ = nomQ

        #: The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
        self.nomU = nomU

        #: For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
        self.normalSections = normalSections

        #: For a capacitor bank, the maximum number of sections that may be switched in.
        self.maximumSections = maximumSections

        #: For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
        self.reactivePerSection = reactivePerSection

        super(ShuntCompensator, self).__init__(*args, **kw_args)

    _attrs = ["nomQ", "nomU", "normalSections", "maximumSections", "reactivePerSection"]
    _attr_types = {"nomQ": float, "nomU": float, "normalSections": int, "maximumSections": int, "reactivePerSection": float}
    _defaults = {"nomQ": 0.0, "nomU": 0.0, "normalSections": 0, "maximumSections": 0, "reactivePerSection": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

