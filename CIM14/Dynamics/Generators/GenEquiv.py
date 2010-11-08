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

from CIM14.Dynamics.RotatingMachine import RotatingMachine

class GenEquiv(RotatingMachine):
    """An equivalent representation of a synchronous generator as a constant internal voltage behind an impedance Ra plus Xp.
    """

    def __init__(self, xp=0.0, synchronousMachine0=None, *args, **kw_args):
        """Initialises a new 'GenEquiv' instance.

        @param xp: Equivalent reactance, also known as Xp. 
        @param synchronousMachine0:
        """
        #: Equivalent reactance, also known as Xp.
        self.xp = xp

        self._synchronousMachine0 = []
        self.synchronousMachine0 = [] if synchronousMachine0 is None else synchronousMachine0

        super(GenEquiv, self).__init__(*args, **kw_args)

    _attrs = ["xp"]
    _attr_types = {"xp": float}
    _defaults = {"xp": 0.0}
    _enums = {}
    _refs = ["synchronousMachine0"]
    _many_refs = ["synchronousMachine0"]

    def getsynchronousMachine0(self):
        
        return self._synchronousMachine0

    def setsynchronousMachine0(self, value):
        for p in self._synchronousMachine0:
            filtered = [q for q in p.genEquiv0 if q != self]
            self._synchronousMachine0._genEquiv0 = filtered
        for r in value:
            if self not in r._genEquiv0:
                r._genEquiv0.append(self)
        self._synchronousMachine0 = value

    synchronousMachine0 = property(getsynchronousMachine0, setsynchronousMachine0)

    def addsynchronousMachine0(self, *synchronousMachine0):
        for obj in synchronousMachine0:
            if self not in obj._genEquiv0:
                obj._genEquiv0.append(self)
            self._synchronousMachine0.append(obj)

    def removesynchronousMachine0(self, *synchronousMachine0):
        for obj in synchronousMachine0:
            if self in obj._genEquiv0:
                obj._genEquiv0.remove(self)
            self._synchronousMachine0.remove(obj)

