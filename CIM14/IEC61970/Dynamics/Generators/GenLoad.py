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

