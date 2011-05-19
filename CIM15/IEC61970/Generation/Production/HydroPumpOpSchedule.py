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

from CIM15.IEC61970.Core.RegularIntervalSchedule import RegularIntervalSchedule

class HydroPumpOpSchedule(RegularIntervalSchedule):
    """The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)
    """

    def __init__(self, HydroPump=None, *args, **kw_args):
        """Initialises a new 'HydroPumpOpSchedule' instance.

        @param HydroPump: The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        """
        self._HydroPump = None
        self.HydroPump = HydroPump

        super(HydroPumpOpSchedule, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["HydroPump"]
    _many_refs = []

    def getHydroPump(self):
        """The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        """
        return self._HydroPump

    def setHydroPump(self, value):
        if self._HydroPump is not None:
            self._HydroPump._HydroPumpOpSchedule = None

        self._HydroPump = value
        if self._HydroPump is not None:
            self._HydroPump.HydroPumpOpSchedule = None
            self._HydroPump._HydroPumpOpSchedule = self

    HydroPump = property(getHydroPump, setHydroPump)

