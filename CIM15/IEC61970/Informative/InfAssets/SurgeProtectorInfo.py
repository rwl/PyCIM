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

class SurgeProtectorInfo(AssetInfo):
    """Properties of surge protector asset.Properties of surge protector asset.
    """

    def __init__(self, maxCurrentRating=0.0, maxContinousOperatingVoltage=0.0, nominalDesignVoltage=0.0, maxEnergyAbsorption=0.0, SurgeProtectors=None, *args, **kw_args):
        """Initialises a new 'SurgeProtectorInfo' instance.

        @param maxCurrentRating: 
        @param maxContinousOperatingVoltage: 
        @param nominalDesignVoltage: 
        @param maxEnergyAbsorption: 
        @param SurgeProtectors: All surge protectors described by this data.
        """

        self.maxCurrentRating = maxCurrentRating


        self.maxContinousOperatingVoltage = maxContinousOperatingVoltage


        self.nominalDesignVoltage = nominalDesignVoltage


        self.maxEnergyAbsorption = maxEnergyAbsorption

        self._SurgeProtectors = []
        self.SurgeProtectors = [] if SurgeProtectors is None else SurgeProtectors

        super(SurgeProtectorInfo, self).__init__(*args, **kw_args)

    _attrs = ["maxCurrentRating", "maxContinousOperatingVoltage", "nominalDesignVoltage", "maxEnergyAbsorption"]
    _attr_types = {"maxCurrentRating": float, "maxContinousOperatingVoltage": float, "nominalDesignVoltage": float, "maxEnergyAbsorption": float}
    _defaults = {"maxCurrentRating": 0.0, "maxContinousOperatingVoltage": 0.0, "nominalDesignVoltage": 0.0, "maxEnergyAbsorption": 0.0}
    _enums = {}
    _refs = ["SurgeProtectors"]
    _many_refs = ["SurgeProtectors"]

    def getSurgeProtectors(self):
        """All surge protectors described by this data.
        """
        return self._SurgeProtectors

    def setSurgeProtectors(self, value):
        for x in self._SurgeProtectors:
            x.SurgeProtectorInfo = None
        for y in value:
            y._SurgeProtectorInfo = self
        self._SurgeProtectors = value

    SurgeProtectors = property(getSurgeProtectors, setSurgeProtectors)

    def addSurgeProtectors(self, *SurgeProtectors):
        for obj in SurgeProtectors:
            obj.SurgeProtectorInfo = self

    def removeSurgeProtectors(self, *SurgeProtectors):
        for obj in SurgeProtectors:
            obj.SurgeProtectorInfo = None

