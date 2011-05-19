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

from CIM15.IEC61968.Assets.AssetInfo import AssetInfo

class FaultIndicatorInfo(AssetInfo):
    """Parameters of fault indicator asset.Parameters of fault indicator asset.
    """

    def __init__(self, resetKind="automatic", FaultIndicators=None, *args, **kw_args):
        """Initialises a new 'FaultIndicatorInfo' instance.

        @param resetKind: Kind of reset mechanisim of this fault indicator. Values are: "automatic", "other", "remote", "manual"
        @param FaultIndicators: All fault indicators described by this data.
        """
        #: Kind of reset mechanisim of this fault indicator. Values are: "automatic", "other", "remote", "manual"
        self.resetKind = resetKind

        self._FaultIndicators = []
        self.FaultIndicators = [] if FaultIndicators is None else FaultIndicators

        super(FaultIndicatorInfo, self).__init__(*args, **kw_args)

    _attrs = ["resetKind"]
    _attr_types = {"resetKind": str}
    _defaults = {"resetKind": "automatic"}
    _enums = {"resetKind": "FaultIndicatorResetKind"}
    _refs = ["FaultIndicators"]
    _many_refs = ["FaultIndicators"]

    def getFaultIndicators(self):
        """All fault indicators described by this data.
        """
        return self._FaultIndicators

    def setFaultIndicators(self, value):
        for x in self._FaultIndicators:
            x.FaultIndicatorInfo = None
        for y in value:
            y._FaultIndicatorInfo = self
        self._FaultIndicators = value

    FaultIndicators = property(getFaultIndicators, setFaultIndicators)

    def addFaultIndicators(self, *FaultIndicators):
        for obj in FaultIndicators:
            obj.FaultIndicatorInfo = self

    def removeFaultIndicators(self, *FaultIndicators):
        for obj in FaultIndicators:
            obj.FaultIndicatorInfo = None

