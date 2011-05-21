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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class RemotePoint(IdentifiedObject):
    """For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.
    """

    def __init__(self, RemoteUnit=None, *args, **kw_args):
        """Initialises a new 'RemotePoint' instance.

        @param RemoteUnit: Remote unit this point belongs to.
        """
        self._RemoteUnit = None
        self.RemoteUnit = RemoteUnit

        super(RemotePoint, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["RemoteUnit"]
    _many_refs = []

    def getRemoteUnit(self):
        """Remote unit this point belongs to.
        """
        return self._RemoteUnit

    def setRemoteUnit(self, value):
        if self._RemoteUnit is not None:
            filtered = [x for x in self.RemoteUnit.RemotePoints if x != self]
            self._RemoteUnit._RemotePoints = filtered

        self._RemoteUnit = value
        if self._RemoteUnit is not None:
            if self not in self._RemoteUnit._RemotePoints:
                self._RemoteUnit._RemotePoints.append(self)

    RemoteUnit = property(getRemoteUnit, setRemoteUnit)

