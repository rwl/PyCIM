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

from CIM14.IEC61968.Work.Work import Work

class MeterServiceWork(Work):
    """Work involving meters.
    """

    def __init__(self, OldMeterAsset=None, MeterAsset=None, *args, **kw_args):
        """Initialises a new 'MeterServiceWork' instance.

        @param OldMeterAsset: Old meter asset replaced by this work.
        @param MeterAsset: Meter asset on which this non-replacement work is performed.
        """
        self._OldMeterAsset = None
        self.OldMeterAsset = OldMeterAsset

        self._MeterAsset = None
        self.MeterAsset = MeterAsset

        super(MeterServiceWork, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["OldMeterAsset", "MeterAsset"]
    _many_refs = []

    def getOldMeterAsset(self):
        """Old meter asset replaced by this work.
        """
        return self._OldMeterAsset

    def setOldMeterAsset(self, value):
        if self._OldMeterAsset is not None:
            filtered = [x for x in self.OldMeterAsset.MeterReplacementWorks if x != self]
            self._OldMeterAsset._MeterReplacementWorks = filtered

        self._OldMeterAsset = value
        if self._OldMeterAsset is not None:
            if self not in self._OldMeterAsset._MeterReplacementWorks:
                self._OldMeterAsset._MeterReplacementWorks.append(self)

    OldMeterAsset = property(getOldMeterAsset, setOldMeterAsset)

    def getMeterAsset(self):
        """Meter asset on which this non-replacement work is performed.
        """
        return self._MeterAsset

    def setMeterAsset(self, value):
        if self._MeterAsset is not None:
            filtered = [x for x in self.MeterAsset.MeterServiceWorks if x != self]
            self._MeterAsset._MeterServiceWorks = filtered

        self._MeterAsset = value
        if self._MeterAsset is not None:
            if self not in self._MeterAsset._MeterServiceWorks:
                self._MeterAsset._MeterServiceWorks.append(self)

    MeterAsset = property(getMeterAsset, setMeterAsset)

