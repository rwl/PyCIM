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

class TieToMeasurement(IdentifiedObject):
    """Ties a block input to a specific state variable measurment.  Thus giving a unit type, a location in the network (typically a terminal).   A specific value is not given, just enough information to obtain the value from the model during a solution. This has nothing to do with SCADA.
    """

    def __init__(self, measurement0=None, block0=None, metaBlockInput0=None, *args, **kw_args):
        """Initialises a new 'TieToMeasurement' instance.

        @param measurement0:
        @param block0:
        @param metaBlockInput0: The identified block input to which this measurement applies.   Note this applies only to the external interface of blocks.
        """
        self._measurement0 = None
        self.measurement0 = measurement0

        self._block0 = None
        self.block0 = block0

        self._metaBlockInput0 = None
        self.metaBlockInput0 = metaBlockInput0

        super(TieToMeasurement, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["measurement0", "block0", "metaBlockInput0"]
    _many_refs = []

    def getmeasurement0(self):
        
        return self._measurement0

    def setmeasurement0(self, value):
        if self._measurement0 is not None:
            filtered = [x for x in self.measurement0.tieToMeasurement0 if x != self]
            self._measurement0._tieToMeasurement0 = filtered

        self._measurement0 = value
        if self._measurement0 is not None:
            if self not in self._measurement0._tieToMeasurement0:
                self._measurement0._tieToMeasurement0.append(self)

    measurement0 = property(getmeasurement0, setmeasurement0)

    def getblock0(self):
        
        return self._block0

    def setblock0(self, value):
        if self._block0 is not None:
            filtered = [x for x in self.block0.tieToMeasurement0 if x != self]
            self._block0._tieToMeasurement0 = filtered

        self._block0 = value
        if self._block0 is not None:
            if self not in self._block0._tieToMeasurement0:
                self._block0._tieToMeasurement0.append(self)

    block0 = property(getblock0, setblock0)

    def getmetaBlockInput0(self):
        """The identified block input to which this measurement applies.   Note this applies only to the external interface of blocks.
        """
        return self._metaBlockInput0

    def setmetaBlockInput0(self, value):
        if self._metaBlockInput0 is not None:
            filtered = [x for x in self.metaBlockInput0.tieToMeasurement0 if x != self]
            self._metaBlockInput0._tieToMeasurement0 = filtered

        self._metaBlockInput0 = value
        if self._metaBlockInput0 is not None:
            if self not in self._metaBlockInput0._tieToMeasurement0:
                self._metaBlockInput0._tieToMeasurement0.append(self)

    metaBlockInput0 = property(getmetaBlockInput0, setmetaBlockInput0)

