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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class MutualCoupling(IdentifiedObject):
    """This class represents the zero sequence line mutual coupling.
    """

    def __init__(self, distance12=0.0, b0ch=0.0, r0=0.0, g0ch=0.0, distance22=0.0, distance21=0.0, distance11=0.0, x0=0.0, Second_Terminal=None, First_Terminal=None, *args, **kw_args):
        """Initializes a new 'MutualCoupling' instance.

        @param distance12: Distance from the first line's from specified terminal to end of coupled region 
        @param b0ch: Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        @param r0: Zero sequence branch-to-branch mutual impedance coupling, resistance 
        @param g0ch: Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. 
        @param distance22: Distance from the second line's specified terminal to end of coupled region 
        @param distance21: Distance from the second line's specified terminal to start of coupled region 
        @param distance11: Distance from the first line's specified terminal to start of coupled region 
        @param x0: Zero sequence branch-to-branch mutual impedance coupling, reactance 
        @param Second_Terminal: The starting terminal for the calculation of distances along the second branch of the mutual coupling.
        @param First_Terminal: The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.
        """
        #: Distance from the first line's from specified terminal to end of coupled region 
        self.distance12 = distance12

        #: Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        self.b0ch = b0ch

        #: Zero sequence branch-to-branch mutual impedance coupling, resistance 
        self.r0 = r0

        #: Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. 
        self.g0ch = g0ch

        #: Distance from the second line's specified terminal to end of coupled region 
        self.distance22 = distance22

        #: Distance from the second line's specified terminal to start of coupled region 
        self.distance21 = distance21

        #: Distance from the first line's specified terminal to start of coupled region 
        self.distance11 = distance11

        #: Zero sequence branch-to-branch mutual impedance coupling, reactance 
        self.x0 = x0

        self._Second_Terminal = None
        self.Second_Terminal = Second_Terminal

        self._First_Terminal = None
        self.First_Terminal = First_Terminal

        super(MutualCoupling, self).__init__(*args, **kw_args)

    def getSecond_Terminal(self):
        """The starting terminal for the calculation of distances along the second branch of the mutual coupling.
        """
        return self._Second_Terminal

    def setSecond_Terminal(self, value):
        if self._Second_Terminal is not None:
            filtered = [x for x in self.Second_Terminal.HasSecond_MutualCoupling if x != self]
            self._Second_Terminal._HasSecond_MutualCoupling = filtered

        self._Second_Terminal = value
        if self._Second_Terminal is not None:
            self._Second_Terminal._HasSecond_MutualCoupling.append(self)

    Second_Terminal = property(getSecond_Terminal, setSecond_Terminal)

    def getFirst_Terminal(self):
        """The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.
        """
        return self._First_Terminal

    def setFirst_Terminal(self, value):
        if self._First_Terminal is not None:
            filtered = [x for x in self.First_Terminal.HasFirst_MutualCoupling if x != self]
            self._First_Terminal._HasFirst_MutualCoupling = filtered

        self._First_Terminal = value
        if self._First_Terminal is not None:
            self._First_Terminal._HasFirst_MutualCoupling.append(self)

    First_Terminal = property(getFirst_Terminal, setFirst_Terminal)

