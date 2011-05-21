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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class MechanicalLoad(PowerSystemResource):
    """A mechanical load represents the variation in a motor's shaft torque or power as a function of shaft speed.
    """

    def __init__(self, rotatingMachine0=None, *args, **kw_args):
        """Initialises a new 'MechanicalLoad' instance.

        @param rotatingMachine0:
        """
        self._rotatingMachine0 = []
        self.rotatingMachine0 = [] if rotatingMachine0 is None else rotatingMachine0

        super(MechanicalLoad, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["rotatingMachine0"]
    _many_refs = ["rotatingMachine0"]

    def getrotatingMachine0(self):
        
        return self._rotatingMachine0

    def setrotatingMachine0(self, value):
        for p in self._rotatingMachine0:
            filtered = [q for q in p.mechanicalLoad0 if q != self]
            self._rotatingMachine0._mechanicalLoad0 = filtered
        for r in value:
            if self not in r._mechanicalLoad0:
                r._mechanicalLoad0.append(self)
        self._rotatingMachine0 = value

    rotatingMachine0 = property(getrotatingMachine0, setrotatingMachine0)

    def addrotatingMachine0(self, *rotatingMachine0):
        for obj in rotatingMachine0:
            if self not in obj._mechanicalLoad0:
                obj._mechanicalLoad0.append(self)
            self._rotatingMachine0.append(obj)

    def removerotatingMachine0(self, *rotatingMachine0):
        for obj in rotatingMachine0:
            if self in obj._mechanicalLoad0:
                obj._mechanicalLoad0.remove(self)
            self._rotatingMachine0.remove(obj)

