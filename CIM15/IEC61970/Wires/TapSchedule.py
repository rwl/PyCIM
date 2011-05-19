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

from CIM15.IEC61970.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule

class TapSchedule(SeasonDayTypeSchedule):
    """A pre-established pattern over time for a tap step.A pre-established pattern over time for a tap step.
    """

    def __init__(self, TapChanger=None, *args, **kw_args):
        """Initialises a new 'TapSchedule' instance.

        @param TapChanger: A TapSchedule is associated with a TapChanger.
        """
        self._TapChanger = None
        self.TapChanger = TapChanger

        super(TapSchedule, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TapChanger"]
    _many_refs = []

    def getTapChanger(self):
        """A TapSchedule is associated with a TapChanger.
        """
        return self._TapChanger

    def setTapChanger(self, value):
        if self._TapChanger is not None:
            filtered = [x for x in self.TapChanger.TapSchedules if x != self]
            self._TapChanger._TapSchedules = filtered

        self._TapChanger = value
        if self._TapChanger is not None:
            if self not in self._TapChanger._TapSchedules:
                self._TapChanger._TapSchedules.append(self)

    TapChanger = property(getTapChanger, setTapChanger)

