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

from CIM15.IEC61968.Assets.Asset import Asset

class Streetlight(Asset):
    """Streetlight asset.Streetlight asset.
    """

    def __init__(self, armLength=0.0, lampKind="metalHalide", lightRating=0.0, Pole=None, *args, **kw_args):
        """Initialises a new 'Streetlight' instance.

        @param armLength: Length of arm. Note that a new light may be placed on an existing arm. 
        @param lampKind: Lamp kind. Values are: "metalHalide", "highPressureSodium", "other", "mercuryVapor"
        @param lightRating: Power rating of light. 
        @param Pole: Streetlight(s) may be attached to a pole.
        """
        #: Length of arm. Note that a new light may be placed on an existing arm.
        self.armLength = armLength

        #: Lamp kind. Values are: "metalHalide", "highPressureSodium", "other", "mercuryVapor"
        self.lampKind = lampKind

        #: Power rating of light.
        self.lightRating = lightRating

        self._Pole = None
        self.Pole = Pole

        super(Streetlight, self).__init__(*args, **kw_args)

    _attrs = ["armLength", "lampKind", "lightRating"]
    _attr_types = {"armLength": float, "lampKind": str, "lightRating": float}
    _defaults = {"armLength": 0.0, "lampKind": "metalHalide", "lightRating": 0.0}
    _enums = {"lampKind": "StreetlightLampKind"}
    _refs = ["Pole"]
    _many_refs = []

    def getPole(self):
        """Streetlight(s) may be attached to a pole.
        """
        return self._Pole

    def setPole(self, value):
        if self._Pole is not None:
            filtered = [x for x in self.Pole.Streetlights if x != self]
            self._Pole._Streetlights = filtered

        self._Pole = value
        if self._Pole is not None:
            if self not in self._Pole._Streetlights:
                self._Pole._Streetlights.append(self)

    Pole = property(getPole, setPole)

