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

from CIM14.IEC61970.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule

class ConformLoadSchedule(SeasonDayTypeSchedule):
    """A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """

    def __init__(self, ConformLoadGroup=None, *args, **kw_args):
        """Initialises a new 'ConformLoadSchedule' instance.

        @param ConformLoadGroup: The ConformLoadGroup where the ConformLoadSchedule belongs.
        """
        self._ConformLoadGroup = None
        self.ConformLoadGroup = ConformLoadGroup

        super(ConformLoadSchedule, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ConformLoadGroup"]
    _many_refs = []

    def getConformLoadGroup(self):
        """The ConformLoadGroup where the ConformLoadSchedule belongs.
        """
        return self._ConformLoadGroup

    def setConformLoadGroup(self, value):
        if self._ConformLoadGroup is not None:
            filtered = [x for x in self.ConformLoadGroup.ConformLoadSchedules if x != self]
            self._ConformLoadGroup._ConformLoadSchedules = filtered

        self._ConformLoadGroup = value
        if self._ConformLoadGroup is not None:
            if self not in self._ConformLoadGroup._ConformLoadSchedules:
                self._ConformLoadGroup._ConformLoadSchedules.append(self)

    ConformLoadGroup = property(getConformLoadGroup, setConformLoadGroup)

