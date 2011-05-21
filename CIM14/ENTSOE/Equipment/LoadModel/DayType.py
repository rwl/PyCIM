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

from CIM14.ENTSOE.Equipment.Core.IdentifiedObject import IdentifiedObject

class DayType(IdentifiedObject):
    """Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """

    def __init__(self, SeasonDayTypeSchedules=None, *args, **kw_args):
        """Initialises a new 'DayType' instance.

        @param SeasonDayTypeSchedules: Schedules that use this DayType.
        """
        self._SeasonDayTypeSchedules = []
        self.SeasonDayTypeSchedules = [] if SeasonDayTypeSchedules is None else SeasonDayTypeSchedules

        super(DayType, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SeasonDayTypeSchedules"]
    _many_refs = ["SeasonDayTypeSchedules"]

    def getSeasonDayTypeSchedules(self):
        """Schedules that use this DayType.
        """
        return self._SeasonDayTypeSchedules

    def setSeasonDayTypeSchedules(self, value):
        for x in self._SeasonDayTypeSchedules:
            x.DayType = None
        for y in value:
            y._DayType = self
        self._SeasonDayTypeSchedules = value

    SeasonDayTypeSchedules = property(getSeasonDayTypeSchedules, setSeasonDayTypeSchedules)

    def addSeasonDayTypeSchedules(self, *SeasonDayTypeSchedules):
        for obj in SeasonDayTypeSchedules:
            obj.DayType = self

    def removeSeasonDayTypeSchedules(self, *SeasonDayTypeSchedules):
        for obj in SeasonDayTypeSchedules:
            obj.DayType = None

