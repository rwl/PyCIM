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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource

class ShuntCompensatorPhase(PowerSystemResource):
    """Single phase of a multi-phase shunt compensator when its attributes might be different per phase.Single phase of a multi-phase shunt compensator when its attributes might be different per phase.
    """

    def __init__(self, ShuntCompensator=None, *args, **kw_args):
        """Initialises a new 'ShuntCompensatorPhase' instance.

        @param ShuntCompensator:
        """
        self._ShuntCompensator = None
        self.ShuntCompensator = ShuntCompensator

        super(ShuntCompensatorPhase, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ShuntCompensator"]
    _many_refs = []

    def getShuntCompensator(self):
        
        return self._ShuntCompensator

    def setShuntCompensator(self, value):
        if self._ShuntCompensator is not None:
            filtered = [x for x in self.ShuntCompensator.ShuntCompensatorPhases if x != self]
            self._ShuntCompensator._ShuntCompensatorPhases = filtered

        self._ShuntCompensator = value
        if self._ShuntCompensator is not None:
            if self not in self._ShuntCompensator._ShuntCompensatorPhases:
                self._ShuntCompensator._ShuntCompensatorPhases.append(self)

    ShuntCompensator = property(getShuntCompensator, setShuntCompensator)

