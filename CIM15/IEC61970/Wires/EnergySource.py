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

from CIM15.IEC61970.Core.ConductingEquipment import ConductingEquipment

class EnergySource(ConductingEquipment):
    """A generic equivalent for an energy supplier on a transmission or distribution voltage level.A generic equivalent for an energy supplier on a transmission or distribution voltage level.
    """

    def __init__(self, r0=0.0, voltageMagnitude=0.0, xn=0.0, nominalVoltage=0.0, x=0.0, r=0.0, voltageAngle=0.0, rn=0.0, x0=0.0, activePower=0.0, *args, **kw_args):
        """Initialises a new 'EnergySource' instance.

        @param r0: Zero sequence Thevenin resistance. 
        @param voltageMagnitude: Phase-to-phase open circuit voltage magnitude. 
        @param xn: Negative sequence Thevenin reactance. 
        @param nominalVoltage: Phase-to-phase nominal voltage. 
        @param x: Positive sequence Thevenin reactance. 
        @param r: Positive sequence Thevenin resistance. 
        @param voltageAngle: Phase angle of a-phase open circuit. 
        @param rn: Negative sequence Thevenin resistance. 
        @param x0: Zero sequence Thevenin reactance. 
        @param activePower: High voltage source load 
        """
        #: Zero sequence Thevenin resistance.
        self.r0 = r0

        #: Phase-to-phase open circuit voltage magnitude.
        self.voltageMagnitude = voltageMagnitude

        #: Negative sequence Thevenin reactance.
        self.xn = xn

        #: Phase-to-phase nominal voltage.
        self.nominalVoltage = nominalVoltage

        #: Positive sequence Thevenin reactance.
        self.x = x

        #: Positive sequence Thevenin resistance.
        self.r = r

        #: Phase angle of a-phase open circuit.
        self.voltageAngle = voltageAngle

        #: Negative sequence Thevenin resistance.
        self.rn = rn

        #: Zero sequence Thevenin reactance.
        self.x0 = x0

        #: High voltage source load
        self.activePower = activePower

        super(EnergySource, self).__init__(*args, **kw_args)

    _attrs = ["r0", "voltageMagnitude", "xn", "nominalVoltage", "x", "r", "voltageAngle", "rn", "x0", "activePower"]
    _attr_types = {"r0": float, "voltageMagnitude": float, "xn": float, "nominalVoltage": float, "x": float, "r": float, "voltageAngle": float, "rn": float, "x0": float, "activePower": float}
    _defaults = {"r0": 0.0, "voltageMagnitude": 0.0, "xn": 0.0, "nominalVoltage": 0.0, "x": 0.0, "r": 0.0, "voltageAngle": 0.0, "rn": 0.0, "x0": 0.0, "activePower": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

