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

from CIM14.IEC61970.Wires.RegulatingCondEq import RegulatingCondEq

class GenLoad(RegulatingCondEq):
    """Representation of a small generator as a negative load rather than a dynamic generator model. This practice is also referred to as 'netting' the generation with the load, i.e. taking the net value of load minus generation as the new load value.  For dynamic modeling purposes, each generator that does not have a dynamic load model must have a genLoad record.
    """

    def __init__(self, synchronousMachine0=None, *args, **kw_args):
        """Initialises a new 'GenLoad' instance.

        @param synchronousMachine0:
        """
        self._synchronousMachine0 = []
        self.synchronousMachine0 = [] if synchronousMachine0 is None else synchronousMachine0

        super(GenLoad, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["synchronousMachine0"]
    _many_refs = ["synchronousMachine0"]

    def getsynchronousMachine0(self):
        
        return self._synchronousMachine0

    def setsynchronousMachine0(self, value):
        for p in self._synchronousMachine0:
            filtered = [q for q in p.genLoad0 if q != self]
            self._synchronousMachine0._genLoad0 = filtered
        for r in value:
            if self not in r._genLoad0:
                r._genLoad0.append(self)
        self._synchronousMachine0 = value

    synchronousMachine0 = property(getsynchronousMachine0, setsynchronousMachine0)

    def addsynchronousMachine0(self, *synchronousMachine0):
        for obj in synchronousMachine0:
            if self not in obj._genLoad0:
                obj._genLoad0.append(self)
            self._synchronousMachine0.append(obj)

    def removesynchronousMachine0(self, *synchronousMachine0):
        for obj in synchronousMachine0:
            if self in obj._genLoad0:
                obj._genLoad0.remove(self)
            self._synchronousMachine0.remove(obj)

