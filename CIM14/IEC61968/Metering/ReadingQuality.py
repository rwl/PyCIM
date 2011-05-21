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

from CIM14.Element import Element

class ReadingQuality(Element):
    """Quality of a specific reading value or interval reading value. Note that more than one Quality may be applicable to a given Reading. Typically not used unless problems or unusual conditions occur (i.e., quality for each Reading is assumed to be 'Good' unless stated otherwise in associated ReadingQuality).
    """

    def __init__(self, quality='', IntervalReading=None, Reading=None, *args, **kw_args):
        """Initialises a new 'ReadingQuality' instance.

        @param quality: Quality, to be specified if different than 'Good'. 
        @param IntervalReading: Interval reading value to which this quality applies.
        @param Reading: Reading value to which this quality applies.
        """
        #: Quality, to be specified if different than 'Good'.
        self.quality = quality

        self._IntervalReading = None
        self.IntervalReading = IntervalReading

        self._Reading = None
        self.Reading = Reading

        super(ReadingQuality, self).__init__(*args, **kw_args)

    _attrs = ["quality"]
    _attr_types = {"quality": str}
    _defaults = {"quality": ''}
    _enums = {}
    _refs = ["IntervalReading", "Reading"]
    _many_refs = []

    def getIntervalReading(self):
        """Interval reading value to which this quality applies.
        """
        return self._IntervalReading

    def setIntervalReading(self, value):
        if self._IntervalReading is not None:
            filtered = [x for x in self.IntervalReading.ReadingQualities if x != self]
            self._IntervalReading._ReadingQualities = filtered

        self._IntervalReading = value
        if self._IntervalReading is not None:
            if self not in self._IntervalReading._ReadingQualities:
                self._IntervalReading._ReadingQualities.append(self)

    IntervalReading = property(getIntervalReading, setIntervalReading)

    def getReading(self):
        """Reading value to which this quality applies.
        """
        return self._Reading

    def setReading(self, value):
        if self._Reading is not None:
            filtered = [x for x in self.Reading.ReadingQualities if x != self]
            self._Reading._ReadingQualities = filtered

        self._Reading = value
        if self._Reading is not None:
            if self not in self._Reading._ReadingQualities:
                self._Reading._ReadingQualities.append(self)

    Reading = property(getReading, setReading)

