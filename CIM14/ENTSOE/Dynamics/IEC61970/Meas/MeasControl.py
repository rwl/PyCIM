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

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreIdentifiedObject import CoreIdentifiedObject

class MeasControl(CoreIdentifiedObject):

    def __init__(self, RegulatingCondEq=None, *args, **kw_args):
        """Initialises a new 'MeasControl' instance.

        @param RegulatingCondEq: 
        """
        self._RegulatingCondEq = None
        self.RegulatingCondEq = RegulatingCondEq

        super(MeasControl, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["RegulatingCondEq"]
    _many_refs = []

    def getRegulatingCondEq(self):
        """
        """
        return self._RegulatingCondEq

    def setRegulatingCondEq(self, value):
        if self._RegulatingCondEq is not None:
            filtered = [x for x in self.RegulatingCondEq.Controls if x != self]
            self._RegulatingCondEq._Controls = filtered

        self._RegulatingCondEq = value
        if self._RegulatingCondEq is not None:
            if self not in self._RegulatingCondEq._Controls:
                self._RegulatingCondEq._Controls.append(self)

    RegulatingCondEq = property(getRegulatingCondEq, setRegulatingCondEq)

