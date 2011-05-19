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

from CIM15.IEC61968.Assets.AssetContainer import AssetContainer

class DuctBank(AssetContainer):
    """A duct bank may contain many ducts. Each duct contains individual lines that are expressed as conductor assets (thereby describing each line's physical asset characteristics), which are each associated with ACLineSegments and other classes describing their electrical characteristics.A duct bank may contain many ducts. Each duct contains individual lines that are expressed as conductor assets (thereby describing each line's physical asset characteristics), which are each associated with ACLineSegments and other classes describing their electrical characteristics.
    """

    def __init__(self, circuitCount=0, DuctInfos=None, *args, **kw_args):
        """Initialises a new 'DuctBank' instance.

        @param circuitCount: Number of circuits in duct bank. Refer to associations between a duct (ConductorAsset) and an ACLineSegment to understand which circuits are in which ducts. 
        @param DuctInfos:
        """
        #: Number of circuits in duct bank. Refer to associations between a duct (ConductorAsset) and an ACLineSegment to understand which circuits are in which ducts.
        self.circuitCount = circuitCount

        self._DuctInfos = []
        self.DuctInfos = [] if DuctInfos is None else DuctInfos

        super(DuctBank, self).__init__(*args, **kw_args)

    _attrs = ["circuitCount"]
    _attr_types = {"circuitCount": int}
    _defaults = {"circuitCount": 0}
    _enums = {}
    _refs = ["DuctInfos"]
    _many_refs = ["DuctInfos"]

    def getDuctInfos(self):
        
        return self._DuctInfos

    def setDuctInfos(self, value):
        for x in self._DuctInfos:
            x.DuctBankInfo = None
        for y in value:
            y._DuctBankInfo = self
        self._DuctInfos = value

    DuctInfos = property(getDuctInfos, setDuctInfos)

    def addDuctInfos(self, *DuctInfos):
        for obj in DuctInfos:
            obj.DuctBankInfo = self

    def removeDuctInfos(self, *DuctInfos):
        for obj in DuctInfos:
            obj.DuctBankInfo = None

