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

class EnergySource(IdentifiedObject):
    """A generic equivalent for an energy supplier on a transmission or distribution voltage level.
    """

    def __init__(self, voltageMagnitude=0.0, x=0.0, r=0.0, nominalVoltage=0.0, voltageAngle=0.0, *args, **kw_args):
        """Initialises a new 'EnergySource' instance.

        @param voltageMagnitude: Phase-to-phase open circuit voltage magnitude. 
        @param x: Positive sequence Thevenin reactance. 
        @param r: Positive sequence Thevenin resistance. 
        @param nominalVoltage: Phase-to-phase nominal voltage. 
        @param voltageAngle: Phase angle of a-phase open circuit. 
        """
        #: Phase-to-phase open circuit voltage magnitude.
        self.voltageMagnitude = voltageMagnitude

        #: Positive sequence Thevenin reactance.
        self.x = x

        #: Positive sequence Thevenin resistance.
        self.r = r

        #: Phase-to-phase nominal voltage.
        self.nominalVoltage = nominalVoltage

        #: Phase angle of a-phase open circuit.
        self.voltageAngle = voltageAngle

        super(EnergySource, self).__init__(*args, **kw_args)

    _attrs = ["voltageMagnitude", "x", "r", "nominalVoltage", "voltageAngle"]
    _attr_types = {"voltageMagnitude": float, "x": float, "r": float, "nominalVoltage": float, "voltageAngle": float}
    _defaults = {"voltageMagnitude": 0.0, "x": 0.0, "r": 0.0, "nominalVoltage": 0.0, "voltageAngle": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

