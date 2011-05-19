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

class CurrentTransformerInfo(AssetInfo):
    """Properties of current transformer asset.Properties of current transformer asset.
    """

    def __init__(self, tertiaryFlsRating=0.0, coreCount=0, secondaryFlsRating=0.0, usage='', accuracyClass='', ctClass='', kneePointVoltage=0.0, coreBurden=0.0, accuracyLimit=0.0, kneePointCurrent=0.0, primaryFlsRating=0.0, nominalRatio=None, secondaryRatio=None, CTs=None, tertiaryRatio=None, maxRatio=None, primaryRatio=None, *args, **kw_args):
        """Initialises a new 'CurrentTransformerInfo' instance.

        @param tertiaryFlsRating: Full load secondary (FLS) rating for tertiary winding. 
        @param coreCount: Number of cores. 
        @param secondaryFlsRating: Full load secondary (FLS) rating for secondary winding. 
        @param usage: eg. metering, protection, etc 
        @param accuracyClass: CT accuracy classification 
        @param ctClass: 
        @param kneePointVoltage: Maximum voltage across the secondary terminals where the CT still displays linear characteristicts. 
        @param coreBurden: Power burden of the CT core 
        @param accuracyLimit: 
        @param kneePointCurrent: Maximum primary current where the CT still displays linear characteristicts. 
        @param primaryFlsRating: Full load secondary (FLS) rating for primary winding. 
        @param nominalRatio: Nominal ratio between the primary and secondary current; i.e. 100:5
        @param secondaryRatio: Ratio for the secondary winding tap changer.
        @param CTs: All current transformers described by this data.
        @param tertiaryRatio: Ratio for the tertiary winding tap changer.
        @param maxRatio: Maximum ratio between the primary and secondary current.
        @param primaryRatio: Ratio for the primary winding tap changer.
        """
        #: Full load secondary (FLS) rating for tertiary winding.
        self.tertiaryFlsRating = tertiaryFlsRating

        #: Number of cores.
        self.coreCount = coreCount

        #: Full load secondary (FLS) rating for secondary winding.
        self.secondaryFlsRating = secondaryFlsRating

        #: eg. metering, protection, etc
        self.usage = usage

        #: CT accuracy classification
        self.accuracyClass = accuracyClass


        self.ctClass = ctClass

        #: Maximum voltage across the secondary terminals where the CT still displays linear characteristicts.
        self.kneePointVoltage = kneePointVoltage

        #: Power burden of the CT core
        self.coreBurden = coreBurden


        self.accuracyLimit = accuracyLimit

        #: Maximum primary current where the CT still displays linear characteristicts.
        self.kneePointCurrent = kneePointCurrent

        #: Full load secondary (FLS) rating for primary winding.
        self.primaryFlsRating = primaryFlsRating

        self.nominalRatio = nominalRatio

        self.secondaryRatio = secondaryRatio

        self._CTs = []
        self.CTs = [] if CTs is None else CTs

        self.tertiaryRatio = tertiaryRatio

        self.maxRatio = maxRatio

        self.primaryRatio = primaryRatio

        super(CurrentTransformerInfo, self).__init__(*args, **kw_args)

    _attrs = ["tertiaryFlsRating", "coreCount", "secondaryFlsRating", "usage", "accuracyClass", "ctClass", "kneePointVoltage", "coreBurden", "accuracyLimit", "kneePointCurrent", "primaryFlsRating"]
    _attr_types = {"tertiaryFlsRating": float, "coreCount": int, "secondaryFlsRating": float, "usage": str, "accuracyClass": str, "ctClass": str, "kneePointVoltage": float, "coreBurden": float, "accuracyLimit": float, "kneePointCurrent": float, "primaryFlsRating": float}
    _defaults = {"tertiaryFlsRating": 0.0, "coreCount": 0, "secondaryFlsRating": 0.0, "usage": '', "accuracyClass": '', "ctClass": '', "kneePointVoltage": 0.0, "coreBurden": 0.0, "accuracyLimit": 0.0, "kneePointCurrent": 0.0, "primaryFlsRating": 0.0}
    _enums = {}
    _refs = ["nominalRatio", "secondaryRatio", "CTs", "tertiaryRatio", "maxRatio", "primaryRatio"]
    _many_refs = ["CTs"]

    # Nominal ratio between the primary and secondary current; i.e. 100:5
    nominalRatio = None

    # Ratio for the secondary winding tap changer.
    secondaryRatio = None

    def getCTs(self):
        """All current transformers described by this data.
        """
        return self._CTs

    def setCTs(self, value):
        for x in self._CTs:
            x.CTInfo = None
        for y in value:
            y._CTInfo = self
        self._CTs = value

    CTs = property(getCTs, setCTs)

    def addCTs(self, *CTs):
        for obj in CTs:
            obj.CTInfo = self

    def removeCTs(self, *CTs):
        for obj in CTs:
            obj.CTInfo = None

    # Ratio for the tertiary winding tap changer.
    tertiaryRatio = None

    # Maximum ratio between the primary and secondary current.
    maxRatio = None

    # Ratio for the primary winding tap changer.
    primaryRatio = None

