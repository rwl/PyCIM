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

class ACLineSegment(IdentifiedObject):
    """A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system. For symmetrical, transposed 3ph lines, it is sufficient to use ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment. If per lenght impedance data is available from a library of standard types, impedances and admittances can be calculated in one of the following ways: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model.
    """

    def __init__(self, x0=0.0, bch=0.0, b0ch=0.0, r=0.0, r0=0.0, x=0.0, *args, **kw_args):
        """Initialises a new 'ACLineSegment' instance.

        @param x0: Zero sequence series reactance of the entire line section. 
        @param bch: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line. 
        @param b0ch: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        @param r: Positive sequence series resistance of the entire line section. 
        @param r0: Zero sequence series resistance of the entire line section. 
        @param x: Positive sequence series reactance of the entire line section. 
        """
        #: Zero sequence series reactance of the entire line section.
        self.x0 = x0

        #: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.
        self.bch = bch

        #: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
        self.b0ch = b0ch

        #: Positive sequence series resistance of the entire line section.
        self.r = r

        #: Zero sequence series resistance of the entire line section.
        self.r0 = r0

        #: Positive sequence series reactance of the entire line section.
        self.x = x

        super(ACLineSegment, self).__init__(*args, **kw_args)

    _attrs = ["x0", "bch", "b0ch", "r", "r0", "x"]
    _attr_types = {"x0": float, "bch": float, "b0ch": float, "r": float, "r0": float, "x": float}
    _defaults = {"x0": 0.0, "bch": 0.0, "b0ch": 0.0, "r": 0.0, "r0": 0.0, "x": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

