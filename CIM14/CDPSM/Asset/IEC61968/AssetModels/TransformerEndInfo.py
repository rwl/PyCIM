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

from CIM15.CDPSM.Asset.IEC61968.Assets.AssetInfo import AssetInfo

class TransformerEndInfo(AssetInfo):
    """Transformer end data.
    """

    def __init__(self, ratedU=0.0, endNumber=0, phaseAngleClock=0, emergencyS=0.0, ratedS=0.0, shortTermS=0.0, r=0.0, insulationU=0.0, connectionKind="Z", TransformerTankInfo=None, TransformerEnd=None, *args, **kw_args):
        """Initialises a new 'TransformerEndInfo' instance.

        @param ratedU: Rated voltage: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings. 
        @param endNumber: Number for this transformer end, corresponding to the end's order in the PowerTransformer.vectorGroup attribute. Highest voltage winding should be 1. 
        @param phaseAngleClock: Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngleClock' = 11. 
        @param emergencyS: Apparent power that the winding can carry under emergency conditions (also called long-term emergency power). 
        @param ratedS: Normal apparent power rating. 
        @param shortTermS: Apparent power that this winding can carry for a short period of time (in emergency). 
        @param r: DC resistance. 
        @param insulationU: Basic insulation level voltage rating. 
        @param connectionKind: Kind of connection. Values are: "Z", "A", "Yn", "Y", "Zn", "D", "I"
        @param TransformerTankInfo: Transformer tank data that this end description is part of.
        @param TransformerEnd: All transformer ends described by this end data.
        """
        #: Rated voltage: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.
        self.ratedU = ratedU

        #: Number for this transformer end, corresponding to the end's order in the PowerTransformer.vectorGroup attribute. Highest voltage winding should be 1.
        self.endNumber = endNumber

        #: Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngleClock' = 11.
        self.phaseAngleClock = phaseAngleClock

        #: Apparent power that the winding can carry under emergency conditions (also called long-term emergency power).
        self.emergencyS = emergencyS

        #: Normal apparent power rating.
        self.ratedS = ratedS

        #: Apparent power that this winding can carry for a short period of time (in emergency).
        self.shortTermS = shortTermS

        #: DC resistance.
        self.r = r

        #: Basic insulation level voltage rating.
        self.insulationU = insulationU

        #: Kind of connection. Values are: "Z", "A", "Yn", "Y", "Zn", "D", "I"
        self.connectionKind = connectionKind

        self._TransformerTankInfo = None
        self.TransformerTankInfo = TransformerTankInfo

        self._TransformerEnd = []
        self.TransformerEnd = [] if TransformerEnd is None else TransformerEnd

        super(TransformerEndInfo, self).__init__(*args, **kw_args)

    _attrs = ["ratedU", "endNumber", "phaseAngleClock", "emergencyS", "ratedS", "shortTermS", "r", "insulationU", "connectionKind"]
    _attr_types = {"ratedU": float, "endNumber": int, "phaseAngleClock": int, "emergencyS": float, "ratedS": float, "shortTermS": float, "r": float, "insulationU": float, "connectionKind": str}
    _defaults = {"ratedU": 0.0, "endNumber": 0, "phaseAngleClock": 0, "emergencyS": 0.0, "ratedS": 0.0, "shortTermS": 0.0, "r": 0.0, "insulationU": 0.0, "connectionKind": "Z"}
    _enums = {"connectionKind": "WindingConnection"}
    _refs = ["TransformerTankInfo", "TransformerEnd"]
    _many_refs = ["TransformerEnd"]

    def getTransformerTankInfo(self):
        """Transformer tank data that this end description is part of.
        """
        return self._TransformerTankInfo

    def setTransformerTankInfo(self, value):
        if self._TransformerTankInfo is not None:
            filtered = [x for x in self.TransformerTankInfo.TransformerEndInfos if x != self]
            self._TransformerTankInfo._TransformerEndInfos = filtered

        self._TransformerTankInfo = value
        if self._TransformerTankInfo is not None:
            if self not in self._TransformerTankInfo._TransformerEndInfos:
                self._TransformerTankInfo._TransformerEndInfos.append(self)

    TransformerTankInfo = property(getTransformerTankInfo, setTransformerTankInfo)

    def getTransformerEnd(self):
        """All transformer ends described by this end data.
        """
        return self._TransformerEnd

    def setTransformerEnd(self, value):
        for x in self._TransformerEnd:
            x.TransformerEndInfo = None
        for y in value:
            y._TransformerEndInfo = self
        self._TransformerEnd = value

    TransformerEnd = property(getTransformerEnd, setTransformerEnd)

    def addTransformerEnd(self, *TransformerEnd):
        for obj in TransformerEnd:
            obj.TransformerEndInfo = self

    def removeTransformerEnd(self, *TransformerEnd):
        for obj in TransformerEnd:
            obj.TransformerEndInfo = None

