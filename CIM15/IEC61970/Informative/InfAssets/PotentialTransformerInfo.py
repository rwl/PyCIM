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

class PotentialTransformerInfo(AssetInfo):
    """Properties of potential transformer asset.Properties of potential transformer asset.
    """

    def __init__(self, ptClass='', accuracyClass='', nominalRatio=None, primaryRatio=None, tertiaryRatio=None, PTs=None, secondaryRatio=None, *args, **kw_args):
        """Initialises a new 'PotentialTransformerInfo' instance.

        @param ptClass: 
        @param accuracyClass: 
        @param nominalRatio:
        @param primaryRatio: Ratio for the primary winding tap changer.
        @param tertiaryRatio: Ratio for the tertiary winding tap changer.
        @param PTs: All potential (voltage) transformers described by this data.
        @param secondaryRatio: Ratio for the secondary winding tap changer.
        """

        self.ptClass = ptClass


        self.accuracyClass = accuracyClass

        self.nominalRatio = nominalRatio

        self.primaryRatio = primaryRatio

        self.tertiaryRatio = tertiaryRatio

        self._PTs = []
        self.PTs = [] if PTs is None else PTs

        self.secondaryRatio = secondaryRatio

        super(PotentialTransformerInfo, self).__init__(*args, **kw_args)

    _attrs = ["ptClass", "accuracyClass"]
    _attr_types = {"ptClass": str, "accuracyClass": str}
    _defaults = {"ptClass": '', "accuracyClass": ''}
    _enums = {}
    _refs = ["nominalRatio", "primaryRatio", "tertiaryRatio", "PTs", "secondaryRatio"]
    _many_refs = ["PTs"]

    nominalRatio = None

    # Ratio for the primary winding tap changer.
    primaryRatio = None

    # Ratio for the tertiary winding tap changer.
    tertiaryRatio = None

    def getPTs(self):
        """All potential (voltage) transformers described by this data.
        """
        return self._PTs

    def setPTs(self, value):
        for x in self._PTs:
            x.PTInfo = None
        for y in value:
            y._PTInfo = self
        self._PTs = value

    PTs = property(getPTs, setPTs)

    def addPTs(self, *PTs):
        for obj in PTs:
            obj.PTInfo = self

    def removePTs(self, *PTs):
        for obj in PTs:
            obj.PTInfo = None

    # Ratio for the secondary winding tap changer.
    secondaryRatio = None

