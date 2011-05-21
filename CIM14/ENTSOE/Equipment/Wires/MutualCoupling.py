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

from CIM14.ENTSOE.Equipment.Core.IdentifiedObject import IdentifiedObject

class MutualCoupling(IdentifiedObject):
    """This class represents the zero sequence line mutual coupling.
    """

    def __init__(self, g0ch=0.0, r0=0.0, x0=0.0, distance11=0.0, distance12=0.0, distance22=0.0, distance21=0.0, b0ch=0.0, Second_Terminal=None, First_Terminal=None, *args, **kw_args):
        """Initialises a new 'MutualCoupling' instance.

        @param g0ch: Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. 
        @param r0: Zero sequence branch-to-branch mutual impedance coupling, resistance 
        @param x0: Zero sequence branch-to-branch mutual impedance coupling, reactance 
        @param distance11: Distance from the first line's specified terminal to start of coupled region 
        @param distance12: Distance from the first line's from specified terminal to end of coupled region 
        @param distance22: Distance from the second line's specified terminal to end of coupled region 
        @param distance21: Distance from the second line's specified terminal to start of coupled region 
        @param b0ch: Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        @param Second_Terminal: The starting terminal for the calculation of distances along the second branch of the mutual coupling.
        @param First_Terminal: The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.
        """
        #: Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.
        self.g0ch = g0ch

        #: Zero sequence branch-to-branch mutual impedance coupling, resistance
        self.r0 = r0

        #: Zero sequence branch-to-branch mutual impedance coupling, reactance
        self.x0 = x0

        #: Distance from the first line's specified terminal to start of coupled region
        self.distance11 = distance11

        #: Distance from the first line's from specified terminal to end of coupled region
        self.distance12 = distance12

        #: Distance from the second line's specified terminal to end of coupled region
        self.distance22 = distance22

        #: Distance from the second line's specified terminal to start of coupled region
        self.distance21 = distance21

        #: Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.
        self.b0ch = b0ch

        self._Second_Terminal = None
        self.Second_Terminal = Second_Terminal

        self._First_Terminal = None
        self.First_Terminal = First_Terminal

        super(MutualCoupling, self).__init__(*args, **kw_args)

    _attrs = ["g0ch", "r0", "x0", "distance11", "distance12", "distance22", "distance21", "b0ch"]
    _attr_types = {"g0ch": float, "r0": float, "x0": float, "distance11": float, "distance12": float, "distance22": float, "distance21": float, "b0ch": float}
    _defaults = {"g0ch": 0.0, "r0": 0.0, "x0": 0.0, "distance11": 0.0, "distance12": 0.0, "distance22": 0.0, "distance21": 0.0, "b0ch": 0.0}
    _enums = {}
    _refs = ["Second_Terminal", "First_Terminal"]
    _many_refs = []

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
            if self not in self._Second_Terminal._HasSecond_MutualCoupling:
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
            if self not in self._First_Terminal._HasFirst_MutualCoupling:
                self._First_Terminal._HasFirst_MutualCoupling.append(self)

    First_Terminal = property(getFirst_Terminal, setFirst_Terminal)

