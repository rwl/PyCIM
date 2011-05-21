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

from CIM14.ENTSOE.Equipment.Core.PowerSystemResource import PowerSystemResource

class HydroPump(PowerSystemResource):
    """A synchronous motor-driven pump, typically associated with a pumped storage plant
    """

    def __init__(self, SynchronousMachine=None, *args, **kw_args):
        """Initialises a new 'HydroPump' instance.

        @param SynchronousMachine: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        """
        self._SynchronousMachine = None
        self.SynchronousMachine = SynchronousMachine

        super(HydroPump, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SynchronousMachine"]
    _many_refs = []

    def getSynchronousMachine(self):
        """The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        """
        return self._SynchronousMachine

    def setSynchronousMachine(self, value):
        if self._SynchronousMachine is not None:
            self._SynchronousMachine._HydroPump = None

        self._SynchronousMachine = value
        if self._SynchronousMachine is not None:
            self._SynchronousMachine.HydroPump = None
            self._SynchronousMachine._HydroPump = self

    SynchronousMachine = property(getSynchronousMachine, setSynchronousMachine)

