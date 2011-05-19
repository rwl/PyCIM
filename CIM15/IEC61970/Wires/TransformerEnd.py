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

class TransformerEnd(IdentifiedObject):
    """TransformerEnd is a conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In earlier CIM versions, the TransformerWinding class served a similar purpose. This successor TransformerEnd class is more flexible and has important differences with TransformerWinding.TransformerEnd is a conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In earlier CIM versions, the TransformerWinding class served a similar purpose. This successor TransformerEnd class is more flexible and has important differences with TransformerWinding.
    """

    def __init__(self, endNumber=0, rground=0.0, grounded=False, magBaseU=0.0, magSatFlux=0.0, bmagSat=0.0, xground=0.0, Terminal=None, FromWindingInsulations=None, CoreAdmittance=None, TransformerEndInfo=None, PhaseTapChanger=None, RatioTapChanger=None, FromMeshImpedance=None, ToWindingInsulations=None, ToMeshImpedance=None, StarImpedance=None, *args, **kw_args):
        """Initialises a new 'TransformerEnd' instance.

        @param endNumber: Number for this transformer end, corresponding to the end's order in the PowerTransformer.vectorGroup attribute. Highest voltage winding should be 1. 
        @param rground: (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true. 
        @param grounded: (for Yn and Zn connections) True if the neutral is solidly grounded. 
        @param magBaseU: The reference voltage at which the magnetizing saturation measurements were made 
        @param magSatFlux: Core magnetizing saturation curve knee flux level. 
        @param bmagSat: Core shunt magnetizing susceptance in the saturation region. 
        @param xground: (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true. 
        @param Terminal: External terminal of the power transformer to which this end belongs.
        @param FromWindingInsulations:
        @param CoreAdmittance: Core admittance of this transformer end, representing magnetising current and core losses. The full values of the transformer should be supplied for one transformer end only.
        @param TransformerEndInfo: Data for this transformer end.
        @param PhaseTapChanger: Phase tap changer associated with this transformer end.
        @param RatioTapChanger: Ratio tap changer associated with this transformer end.
        @param FromMeshImpedance: All mesh impedances between this 'to' and other 'from' transformer ends.
        @param ToWindingInsulations:
        @param ToMeshImpedance: All mesh impedances between this 'from' and other 'to' transformer ends.
        @param StarImpedance: (accurate for 2- or 3-winding transformers only) Pi-model impedances of this transformer end. By convention, for a two winding transformer, the full values of the transformer should be entered on the high voltage end (endNumber=1).
        """
        #: Number for this transformer end, corresponding to the end's order in the PowerTransformer.vectorGroup attribute. Highest voltage winding should be 1.
        self.endNumber = endNumber

        #: (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true.
        self.rground = rground

        #: (for Yn and Zn connections) True if the neutral is solidly grounded.
        self.grounded = grounded

        #: The reference voltage at which the magnetizing saturation measurements were made
        self.magBaseU = magBaseU

        #: Core magnetizing saturation curve knee flux level.
        self.magSatFlux = magSatFlux

        #: Core shunt magnetizing susceptance in the saturation region.
        self.bmagSat = bmagSat

        #: (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true.
        self.xground = xground

        self._Terminal = None
        self.Terminal = Terminal

        self._FromWindingInsulations = []
        self.FromWindingInsulations = [] if FromWindingInsulations is None else FromWindingInsulations

        self._CoreAdmittance = None
        self.CoreAdmittance = CoreAdmittance

        self._TransformerEndInfo = None
        self.TransformerEndInfo = TransformerEndInfo

        self._PhaseTapChanger = None
        self.PhaseTapChanger = PhaseTapChanger

        self._RatioTapChanger = None
        self.RatioTapChanger = RatioTapChanger

        self._FromMeshImpedance = []
        self.FromMeshImpedance = [] if FromMeshImpedance is None else FromMeshImpedance

        self._ToWindingInsulations = []
        self.ToWindingInsulations = [] if ToWindingInsulations is None else ToWindingInsulations

        self._ToMeshImpedance = []
        self.ToMeshImpedance = [] if ToMeshImpedance is None else ToMeshImpedance

        self._StarImpedance = None
        self.StarImpedance = StarImpedance

        super(TransformerEnd, self).__init__(*args, **kw_args)

    _attrs = ["endNumber", "rground", "grounded", "magBaseU", "magSatFlux", "bmagSat", "xground"]
    _attr_types = {"endNumber": int, "rground": float, "grounded": bool, "magBaseU": float, "magSatFlux": float, "bmagSat": float, "xground": float}
    _defaults = {"endNumber": 0, "rground": 0.0, "grounded": False, "magBaseU": 0.0, "magSatFlux": 0.0, "bmagSat": 0.0, "xground": 0.0}
    _enums = {}
    _refs = ["Terminal", "FromWindingInsulations", "CoreAdmittance", "TransformerEndInfo", "PhaseTapChanger", "RatioTapChanger", "FromMeshImpedance", "ToWindingInsulations", "ToMeshImpedance", "StarImpedance"]
    _many_refs = ["FromWindingInsulations", "FromMeshImpedance", "ToWindingInsulations", "ToMeshImpedance"]

    def getTerminal(self):
        """External terminal of the power transformer to which this end belongs.
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            filtered = [x for x in self.Terminal.TransformerEnd if x != self]
            self._Terminal._TransformerEnd = filtered

        self._Terminal = value
        if self._Terminal is not None:
            if self not in self._Terminal._TransformerEnd:
                self._Terminal._TransformerEnd.append(self)

    Terminal = property(getTerminal, setTerminal)

    def getFromWindingInsulations(self):
        
        return self._FromWindingInsulations

    def setFromWindingInsulations(self, value):
        for x in self._FromWindingInsulations:
            x.FromWinding = None
        for y in value:
            y._FromWinding = self
        self._FromWindingInsulations = value

    FromWindingInsulations = property(getFromWindingInsulations, setFromWindingInsulations)

    def addFromWindingInsulations(self, *FromWindingInsulations):
        for obj in FromWindingInsulations:
            obj.FromWinding = self

    def removeFromWindingInsulations(self, *FromWindingInsulations):
        for obj in FromWindingInsulations:
            obj.FromWinding = None

    def getCoreAdmittance(self):
        """Core admittance of this transformer end, representing magnetising current and core losses. The full values of the transformer should be supplied for one transformer end only.
        """
        return self._CoreAdmittance

    def setCoreAdmittance(self, value):
        if self._CoreAdmittance is not None:
            filtered = [x for x in self.CoreAdmittance.TransformerEnd if x != self]
            self._CoreAdmittance._TransformerEnd = filtered

        self._CoreAdmittance = value
        if self._CoreAdmittance is not None:
            if self not in self._CoreAdmittance._TransformerEnd:
                self._CoreAdmittance._TransformerEnd.append(self)

    CoreAdmittance = property(getCoreAdmittance, setCoreAdmittance)

    def getTransformerEndInfo(self):
        """Data for this transformer end.
        """
        return self._TransformerEndInfo

    def setTransformerEndInfo(self, value):
        if self._TransformerEndInfo is not None:
            filtered = [x for x in self.TransformerEndInfo.TransformerEnd if x != self]
            self._TransformerEndInfo._TransformerEnd = filtered

        self._TransformerEndInfo = value
        if self._TransformerEndInfo is not None:
            if self not in self._TransformerEndInfo._TransformerEnd:
                self._TransformerEndInfo._TransformerEnd.append(self)

    TransformerEndInfo = property(getTransformerEndInfo, setTransformerEndInfo)

    def getPhaseTapChanger(self):
        """Phase tap changer associated with this transformer end.
        """
        return self._PhaseTapChanger

    def setPhaseTapChanger(self, value):
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger._TransformerEnd = None

        self._PhaseTapChanger = value
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger.TransformerEnd = None
            self._PhaseTapChanger._TransformerEnd = self

    PhaseTapChanger = property(getPhaseTapChanger, setPhaseTapChanger)

    def getRatioTapChanger(self):
        """Ratio tap changer associated with this transformer end.
        """
        return self._RatioTapChanger

    def setRatioTapChanger(self, value):
        if self._RatioTapChanger is not None:
            self._RatioTapChanger._TransformerEnd = None

        self._RatioTapChanger = value
        if self._RatioTapChanger is not None:
            self._RatioTapChanger.TransformerEnd = None
            self._RatioTapChanger._TransformerEnd = self

    RatioTapChanger = property(getRatioTapChanger, setRatioTapChanger)

    def getFromMeshImpedance(self):
        """All mesh impedances between this 'to' and other 'from' transformer ends.
        """
        return self._FromMeshImpedance

    def setFromMeshImpedance(self, value):
        for x in self._FromMeshImpedance:
            x.FromTransformerEnd = None
        for y in value:
            y._FromTransformerEnd = self
        self._FromMeshImpedance = value

    FromMeshImpedance = property(getFromMeshImpedance, setFromMeshImpedance)

    def addFromMeshImpedance(self, *FromMeshImpedance):
        for obj in FromMeshImpedance:
            obj.FromTransformerEnd = self

    def removeFromMeshImpedance(self, *FromMeshImpedance):
        for obj in FromMeshImpedance:
            obj.FromTransformerEnd = None

    def getToWindingInsulations(self):
        
        return self._ToWindingInsulations

    def setToWindingInsulations(self, value):
        for x in self._ToWindingInsulations:
            x.ToWinding = None
        for y in value:
            y._ToWinding = self
        self._ToWindingInsulations = value

    ToWindingInsulations = property(getToWindingInsulations, setToWindingInsulations)

    def addToWindingInsulations(self, *ToWindingInsulations):
        for obj in ToWindingInsulations:
            obj.ToWinding = self

    def removeToWindingInsulations(self, *ToWindingInsulations):
        for obj in ToWindingInsulations:
            obj.ToWinding = None

    def getToMeshImpedance(self):
        """All mesh impedances between this 'from' and other 'to' transformer ends.
        """
        return self._ToMeshImpedance

    def setToMeshImpedance(self, value):
        for p in self._ToMeshImpedance:
            filtered = [q for q in p.ToTransformerEnd if q != self]
            self._ToMeshImpedance._ToTransformerEnd = filtered
        for r in value:
            if self not in r._ToTransformerEnd:
                r._ToTransformerEnd.append(self)
        self._ToMeshImpedance = value

    ToMeshImpedance = property(getToMeshImpedance, setToMeshImpedance)

    def addToMeshImpedance(self, *ToMeshImpedance):
        for obj in ToMeshImpedance:
            if self not in obj._ToTransformerEnd:
                obj._ToTransformerEnd.append(self)
            self._ToMeshImpedance.append(obj)

    def removeToMeshImpedance(self, *ToMeshImpedance):
        for obj in ToMeshImpedance:
            if self in obj._ToTransformerEnd:
                obj._ToTransformerEnd.remove(self)
            self._ToMeshImpedance.remove(obj)

    def getStarImpedance(self):
        """(accurate for 2- or 3-winding transformers only) Pi-model impedances of this transformer end. By convention, for a two winding transformer, the full values of the transformer should be entered on the high voltage end (endNumber=1).
        """
        return self._StarImpedance

    def setStarImpedance(self, value):
        if self._StarImpedance is not None:
            filtered = [x for x in self.StarImpedance.TransformerEnd if x != self]
            self._StarImpedance._TransformerEnd = filtered

        self._StarImpedance = value
        if self._StarImpedance is not None:
            if self not in self._StarImpedance._TransformerEnd:
                self._StarImpedance._TransformerEnd.append(self)

    StarImpedance = property(getStarImpedance, setStarImpedance)

