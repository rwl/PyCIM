# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class PowerRating(IdentifiedObject):
    """There are often stages of power which are associated with stages of cooling. For instance, a transformer may be rated 121kV on the primary, 15kV on the secondary and 4kV on the tertiary winding. These are voltage ratings and the power ratings are generally the same for all three windings and independent of the voltage ratings, there are instances where the tertiary may have a lower power rating. For example, for three stages, the power rating may be 15/20/25 MVA and the cooling is OA/FA/FOA. The 15 MVA rating goes with the OA cooling (Oil and Air cooling). This is called the self cooled rating as there are no external cooling enhancements. The 20 MVA rating goes with the FA cooling (Forced Air cooling), this means that when the fans are running and thus enhancing the cooling characteristics, the transformer can operate at a power level of 20 MVA. The 25 MVA rating goes with the FOA cooling (Forced Oil and Air cooling), this means that when the fans and pumps are running and thus enhancing the cooling characteristics even more than before, the transformer can operate at a power level of 25 MVA. This 15/20/25 MVA does not state how the power is split between the various windings. It may be 25 MVA input on the primary, 25 MVA output on the secondary and 0 MVA output on the tertiary. It may also operate at 25 MVA input on the primary, 17 MVA output on the secondary and 8 MVA output on the tertiary.
    """

    def __init__(self, coolingKind='other', powerRating=0.0, stage=0, TransformerAssets=None, **kw_args):
        """Initializes a new 'PowerRating' instance.

        @param coolingKind: Kind of cooling system. Values are: "other", "forcedAir", "forcedOilAndAir", "selfCooling"
        @param powerRating: The power rating associated with type of cooling specified for this stage. 
        @param stage: Stage of cooling and associated power rating. 
        @param TransformerAssets:
        """
        #: Kind of cooling system.Values are: "other", "forcedAir", "forcedOilAndAir", "selfCooling"
        self.coolingKind = coolingKind

        #: The power rating associated with type of cooling specified for this stage.
        self.powerRating = powerRating

        #: Stage of cooling and associated power rating.
        self.stage = stage

        self._TransformerAssets = []
        self.TransformerAssets = [] if TransformerAssets is None else TransformerAssets

        super(PowerRating, self).__init__(**kw_args)

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

