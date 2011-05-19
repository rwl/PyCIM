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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class RecloseSequence(IdentifiedObject):
    """A reclose sequence (open and close) is defined for each possible reclosure of a breaker.A reclose sequence (open and close) is defined for each possible reclosure of a breaker.
    """

    def __init__(self, recloseStep=0, recloseDelay=0.0, ProtectedSwitch=None, *args, **kw_args):
        """Initialises a new 'RecloseSequence' instance.

        @param recloseStep: Indicates the ordinal position of the reclose step relative to other steps in the sequence. 
        @param recloseDelay: Indicates the time lapse before the reclose step will execute a reclose. 
        @param ProtectedSwitch: A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        #: Indicates the ordinal position of the reclose step relative to other steps in the sequence.
        self.recloseStep = recloseStep

        #: Indicates the time lapse before the reclose step will execute a reclose.
        self.recloseDelay = recloseDelay

        self._ProtectedSwitch = None
        self.ProtectedSwitch = ProtectedSwitch

        super(RecloseSequence, self).__init__(*args, **kw_args)

    _attrs = ["recloseStep", "recloseDelay"]
    _attr_types = {"recloseStep": int, "recloseDelay": float}
    _defaults = {"recloseStep": 0, "recloseDelay": 0.0}
    _enums = {}
    _refs = ["ProtectedSwitch"]
    _many_refs = []

    def getProtectedSwitch(self):
        """A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        return self._ProtectedSwitch

    def setProtectedSwitch(self, value):
        if self._ProtectedSwitch is not None:
            filtered = [x for x in self.ProtectedSwitch.RecloseSequences if x != self]
            self._ProtectedSwitch._RecloseSequences = filtered

        self._ProtectedSwitch = value
        if self._ProtectedSwitch is not None:
            if self not in self._ProtectedSwitch._RecloseSequences:
                self._ProtectedSwitch._RecloseSequences.append(self)

    ProtectedSwitch = property(getProtectedSwitch, setProtectedSwitch)

