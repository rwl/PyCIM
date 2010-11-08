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

from CIM14.IEC61970.Wires.Conductor import Conductor

class ACLineSegment(Conductor):
    """A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.
    """

    def __init__(self, gch=0.0, r=0.0, x0=0.0, bch=0.0, x=0.0, r0=0.0, g0ch=0.0, b0ch=0.0, *args, **kw_args):
        """Initialises a new 'ACLineSegment' instance.

        @param gch: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section. 
        @param r: Positive sequence series resistance of the entire line section. 
        @param x0: Zero sequence series reactance of the entire line section. 
        @param bch: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line. 
        @param x: Positive sequence series reactance of the entire line section. 
        @param r0: Zero sequence series resistance of the entire line section. 
        @param g0ch: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section. 
        @param b0ch: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        """
        #: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
        self.gch = gch

        #: Positive sequence series resistance of the entire line section.
        self.r = r

        #: Zero sequence series reactance of the entire line section.
        self.x0 = x0

        #: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.
        self.bch = bch

        #: Positive sequence series reactance of the entire line section.
        self.x = x

        #: Zero sequence series resistance of the entire line section.
        self.r0 = r0

        #: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
        self.g0ch = g0ch

        #: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
        self.b0ch = b0ch

        super(ACLineSegment, self).__init__(*args, **kw_args)

    _attrs = ["gch", "r", "x0", "bch", "x", "r0", "g0ch", "b0ch"]
    _attr_types = {"gch": float, "r": float, "x0": float, "bch": float, "x": float, "r0": float, "g0ch": float, "b0ch": float}
    _defaults = {"gch": 0.0, "r": 0.0, "x0": 0.0, "bch": 0.0, "x": 0.0, "r0": 0.0, "g0ch": 0.0, "b0ch": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

