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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class PerLengthSequenceImpedance(IdentifiedObject):
    """Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.
    """

    def __init__(self, r0=0.0, r=0.0, b0ch=0.0, x0=0.0, gch=0.0, g0ch=0.0, bch=0.0, x=0.0, ConductorSegments=None, *args, **kw_args):
        """Initialises a new 'PerLengthSequenceImpedance' instance.

        @param r0: Zero sequence series resistance, per unit of length. 
        @param r: Positive sequence series resistance, per unit of length. 
        @param b0ch: Zero sequence shunt (charging) susceptance, per unit of length. 
        @param x0: Zero sequence series reactance, per unit of length. 
        @param gch: Positive sequence shunt (charging) conductance, per unit of length. 
        @param g0ch: Zero sequence shunt (charging) conductance, per unit of length. 
        @param bch: Positive sequence shunt (charging) susceptance, per unit of length. 
        @param x: Positive sequence series reactance, per unit of length. 
        @param ConductorSegments: All conductor segments described by this sequence impedance.
        """
        #: Zero sequence series resistance, per unit of length.
        self.r0 = r0

        #: Positive sequence series resistance, per unit of length.
        self.r = r

        #: Zero sequence shunt (charging) susceptance, per unit of length.
        self.b0ch = b0ch

        #: Zero sequence series reactance, per unit of length.
        self.x0 = x0

        #: Positive sequence shunt (charging) conductance, per unit of length.
        self.gch = gch

        #: Zero sequence shunt (charging) conductance, per unit of length.
        self.g0ch = g0ch

        #: Positive sequence shunt (charging) susceptance, per unit of length.
        self.bch = bch

        #: Positive sequence series reactance, per unit of length.
        self.x = x

        self._ConductorSegments = []
        self.ConductorSegments = [] if ConductorSegments is None else ConductorSegments

        super(PerLengthSequenceImpedance, self).__init__(*args, **kw_args)

    _attrs = ["r0", "r", "b0ch", "x0", "gch", "g0ch", "bch", "x"]
    _attr_types = {"r0": float, "r": float, "b0ch": float, "x0": float, "gch": float, "g0ch": float, "bch": float, "x": float}
    _defaults = {"r0": 0.0, "r": 0.0, "b0ch": 0.0, "x0": 0.0, "gch": 0.0, "g0ch": 0.0, "bch": 0.0, "x": 0.0}
    _enums = {}
    _refs = ["ConductorSegments"]
    _many_refs = ["ConductorSegments"]

    def getConductorSegments(self):
        """All conductor segments described by this sequence impedance.
        """
        return self._ConductorSegments

    def setConductorSegments(self, value):
        for x in self._ConductorSegments:
            x._SequenceImpedance = None
        for y in value:
            y._SequenceImpedance = self
        self._ConductorSegments = value

    ConductorSegments = property(getConductorSegments, setConductorSegments)

    def addConductorSegments(self, *ConductorSegments):
        for obj in ConductorSegments:
            obj._SequenceImpedance = self
            self._ConductorSegments.append(obj)

    def removeConductorSegments(self, *ConductorSegments):
        for obj in ConductorSegments:
            obj._SequenceImpedance = None
            self._ConductorSegments.remove(obj)

