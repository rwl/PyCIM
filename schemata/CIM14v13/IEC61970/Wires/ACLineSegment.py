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

from CIM14v13.IEC61970.Wires.Conductor import Conductor

class ACLineSegment(Conductor):
    """A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.
    """

    def __init__(self, bch=0.0, r=0.0, gch=0.0, r0=0.0, b0ch=0.0, x0=0.0, x=0.0, g0ch=0.0, **kw_args):
        """Initializes a new 'ACLineSegment' instance.

        @param bch: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line. 
        @param r: Positive sequence series resistance of the entire line section. 
        @param gch: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section. 
        @param r0: Zero sequence series resistance of the entire line section. 
        @param b0ch: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        @param x0: Zero sequence series reactance of the entire line section. 
        @param x: Positive sequence series reactance of the entire line section. 
        @param g0ch: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section. 
        """
        #: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.
        self.bch = bch

        #: Positive sequence series resistance of the entire line section.
        self.r = r

        #: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
        self.gch = gch

        #: Zero sequence series resistance of the entire line section.
        self.r0 = r0

        #: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
        self.b0ch = b0ch

        #: Zero sequence series reactance of the entire line section.
        self.x0 = x0

        #: Positive sequence series reactance of the entire line section.
        self.x = x

        #: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
        self.g0ch = g0ch

        super(ACLineSegment, self).__init__(**kw_args)

