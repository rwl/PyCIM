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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class PowerRating(IdentifiedObject):
    """There are often stages of power which are associated with stages of cooling. For instance, a transformer may be rated 121kV on the primary, 15kV on the secondary and 4kV on the tertiary winding. These are voltage ratings and the power ratings are generally the same for all three windings and independent of the voltage ratings, there are instances where the tertiary may have a lower power rating. For example, for three stages, the power rating may be 15/20/25 MVA and the cooling is OA/FA/FOA. The 15 MVA rating goes with the OA cooling (Oil and Air cooling). This is called the self cooled rating as there are no external cooling enhancements. The 20 MVA rating goes with the FA cooling (Forced Air cooling), this means that when the fans are running and thus enhancing the cooling characteristics, the transformer can operate at a power level of 20 MVA. The 25 MVA rating goes with the FOA cooling (Forced Oil and Air cooling), this means that when the fans and pumps are running and thus enhancing the cooling characteristics even more than before, the transformer can operate at a power level of 25 MVA. This 15/20/25 MVA does not state how the power is split between the various windings. It may be 25 MVA input on the primary, 25 MVA output on the secondary and 0 MVA output on the tertiary. It may also operate at 25 MVA input on the primary, 17 MVA output on the secondary and 8 MVA output on the tertiary.There are often stages of power which are associated with stages of cooling. For instance, a transformer may be rated 121kV on the primary, 15kV on the secondary and 4kV on the tertiary winding. These are voltage ratings and the power ratings are generally the same for all three windings and independent of the voltage ratings, there are instances where the tertiary may have a lower power rating. For example, for three stages, the power rating may be 15/20/25 MVA and the cooling is OA/FA/FOA. The 15 MVA rating goes with the OA cooling (Oil and Air cooling). This is called the self cooled rating as there are no external cooling enhancements. The 20 MVA rating goes with the FA cooling (Forced Air cooling), this means that when the fans are running and thus enhancing the cooling characteristics, the transformer can operate at a power level of 20 MVA. The 25 MVA rating goes with the FOA cooling (Forced Oil and Air cooling), this means that when the fans and pumps are running and thus enhancing the cooling characteristics even more than before, the transformer can operate at a power level of 25 MVA. This 15/20/25 MVA does not state how the power is split between the various windings. It may be 25 MVA input on the primary, 25 MVA output on the secondary and 0 MVA output on the tertiary. It may also operate at 25 MVA input on the primary, 17 MVA output on the secondary and 8 MVA output on the tertiary.
    """

    def __init__(self, stage=0, powerRating=0.0, coolingKind="forcedAir", TransformerAssets=None, *args, **kw_args):
        """Initialises a new 'PowerRating' instance.

        @param stage: Stage of cooling and associated power rating. 
        @param powerRating: The power rating associated with type of cooling specified for this stage. 
        @param coolingKind: Kind of cooling system. Values are: "forcedAir", "selfCooling", "forcedOilAndAir", "other"
        @param TransformerAssets:
        """
        #: Stage of cooling and associated power rating.
        self.stage = stage

        #: The power rating associated with type of cooling specified for this stage.
        self.powerRating = powerRating

        #: Kind of cooling system. Values are: "forcedAir", "selfCooling", "forcedOilAndAir", "other"
        self.coolingKind = coolingKind

        self._TransformerAssets = []
        self.TransformerAssets = [] if TransformerAssets is None else TransformerAssets

        super(PowerRating, self).__init__(*args, **kw_args)

    _attrs = ["stage", "powerRating", "coolingKind"]
    _attr_types = {"stage": int, "powerRating": float, "coolingKind": str}
    _defaults = {"stage": 0, "powerRating": 0.0, "coolingKind": "forcedAir"}
    _enums = {"coolingKind": "CoolingKind"}
    _refs = ["TransformerAssets"]
    _many_refs = ["TransformerAssets"]

    def getTransformerAssets(self):
        
        return self._TransformerAssets

    def setTransformerAssets(self, value):
        for p in self._TransformerAssets:
            filtered = [q for q in p.PowerRatings if q != self]
            self._TransformerAssets._PowerRatings = filtered
        for r in value:
            if self not in r._PowerRatings:
                r._PowerRatings.append(self)
        self._TransformerAssets = value

    TransformerAssets = property(getTransformerAssets, setTransformerAssets)

    def addTransformerAssets(self, *TransformerAssets):
        for obj in TransformerAssets:
            if self not in obj._PowerRatings:
                obj._PowerRatings.append(self)
            self._TransformerAssets.append(obj)

    def removeTransformerAssets(self, *TransformerAssets):
        for obj in TransformerAssets:
            if self in obj._PowerRatings:
                obj._PowerRatings.remove(self)
            self._TransformerAssets.remove(obj)

