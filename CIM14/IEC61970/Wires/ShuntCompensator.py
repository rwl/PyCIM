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

from CIM14.IEC61970.Wires.RegulatingCondEq import RegulatingCondEq

class ShuntCompensator(RegulatingCondEq):
    """A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.
    """

    def __init__(self, maxU=0.0, reactivePerSection=0.0, aVRDelay=0.0, voltageSensitivity=0.0, normalSections=0, g0PerSection=0.0, maximumSections=0, bPerSection=0.0, nomQ=0.0, switchOnCount=0, minU=0.0, b0PerSection=0.0, switchOnDate='', nomU=0.0, gPerSection=0.0, SvShuntCompensatorSections=None, *args, **kw_args):
        """Initialises a new 'ShuntCompensator' instance.

        @param maxU: The maximum voltage at which the capacitor bank should operate. 
        @param reactivePerSection: For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage. 
        @param aVRDelay: Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR). 
        @param voltageSensitivity: Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power. 
        @param normalSections: For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ). 
        @param g0PerSection: Zero sequence shunt (charging) conductance per section 
        @param maximumSections: For a capacitor bank, the maximum number of sections that may be switched in. 
        @param bPerSection: Positive sequence shunt (charging) susceptance per section 
        @param nomQ: Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive. 
        @param switchOnCount: The switch on count since the capacitor count was last reset or initialized. 
        @param minU: The minimum voltage at which the capacitor bank should operate. 
        @param b0PerSection: Zero sequence shunt (charging) susceptance per section 
        @param switchOnDate: The date and time when the capacitor bank was last switched on. 
        @param nomU: The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network. 
        @param gPerSection: Positive sequence shunt (charging) conductance per section 
        @param SvShuntCompensatorSections: The state for the number of shunt compensator sections in service.
        """
        #: The maximum voltage at which the capacitor bank should operate.
        self.maxU = maxU

        #: For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
        self.reactivePerSection = reactivePerSection

        #: Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR).
        self.aVRDelay = aVRDelay

        #: Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power.
        self.voltageSensitivity = voltageSensitivity

        #: For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
        self.normalSections = normalSections

        #: Zero sequence shunt (charging) conductance per section
        self.g0PerSection = g0PerSection

        #: For a capacitor bank, the maximum number of sections that may be switched in.
        self.maximumSections = maximumSections

        #: Positive sequence shunt (charging) susceptance per section
        self.bPerSection = bPerSection

        #: Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.
        self.nomQ = nomQ

        #: The switch on count since the capacitor count was last reset or initialized.
        self.switchOnCount = switchOnCount

        #: The minimum voltage at which the capacitor bank should operate.
        self.minU = minU

        #: Zero sequence shunt (charging) susceptance per section
        self.b0PerSection = b0PerSection

        #: The date and time when the capacitor bank was last switched on.
        self.switchOnDate = switchOnDate

        #: The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
        self.nomU = nomU

        #: Positive sequence shunt (charging) conductance per section
        self.gPerSection = gPerSection

        self._SvShuntCompensatorSections = None
        self.SvShuntCompensatorSections = SvShuntCompensatorSections

        super(ShuntCompensator, self).__init__(*args, **kw_args)

    _attrs = ["maxU", "reactivePerSection", "aVRDelay", "voltageSensitivity", "normalSections", "g0PerSection", "maximumSections", "bPerSection", "nomQ", "switchOnCount", "minU", "b0PerSection", "switchOnDate", "nomU", "gPerSection"]
    _attr_types = {"maxU": float, "reactivePerSection": float, "aVRDelay": float, "voltageSensitivity": float, "normalSections": int, "g0PerSection": float, "maximumSections": int, "bPerSection": float, "nomQ": float, "switchOnCount": int, "minU": float, "b0PerSection": float, "switchOnDate": str, "nomU": float, "gPerSection": float}
    _defaults = {"maxU": 0.0, "reactivePerSection": 0.0, "aVRDelay": 0.0, "voltageSensitivity": 0.0, "normalSections": 0, "g0PerSection": 0.0, "maximumSections": 0, "bPerSection": 0.0, "nomQ": 0.0, "switchOnCount": 0, "minU": 0.0, "b0PerSection": 0.0, "switchOnDate": '', "nomU": 0.0, "gPerSection": 0.0}
    _enums = {}
    _refs = ["SvShuntCompensatorSections"]
    _many_refs = []

    def getSvShuntCompensatorSections(self):
        """The state for the number of shunt compensator sections in service.
        """
        return self._SvShuntCompensatorSections

    def setSvShuntCompensatorSections(self, value):
        if self._SvShuntCompensatorSections is not None:
            self._SvShuntCompensatorSections._ShuntCompensator = None

        self._SvShuntCompensatorSections = value
        if self._SvShuntCompensatorSections is not None:
            self._SvShuntCompensatorSections.ShuntCompensator = None
            self._SvShuntCompensatorSections._ShuntCompensator = self

    SvShuntCompensatorSections = property(getSvShuntCompensatorSections, setSvShuntCompensatorSections)

