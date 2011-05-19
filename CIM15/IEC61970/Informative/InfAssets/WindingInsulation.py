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

class WindingInsulation(IdentifiedObject):
    """Winding insulation condition as a result of a test.Winding insulation condition as a result of a test.
    """

    def __init__(self, insulationPFStatus='', insulationResistance='', leakageReactance=0.0, Ground=None, TransformerObservation=None, ToWinding=None, FromWinding=None, status=None, *args, **kw_args):
        """Initialises a new 'WindingInsulation' instance.

        @param insulationPFStatus: Status of Winding Insulation Power Factor as of statusDate: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed. 
        @param insulationResistance: For testType, status of Winding Insulation Resistance as of statusDate. Typical values are: Acceptable, Questionable, Failed. 
        @param leakageReactance: As of statusDate, the leakage reactance measured at the 'from' winding with the 'to' winding short-circuited and all other windings open-circuited. 
        @param Ground:
        @param TransformerObservation:
        @param ToWinding:
        @param FromWinding:
        @param status:
        """
        #: Status of Winding Insulation Power Factor as of statusDate: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed.
        self.insulationPFStatus = insulationPFStatus

        #: For testType, status of Winding Insulation Resistance as of statusDate. Typical values are: Acceptable, Questionable, Failed.
        self.insulationResistance = insulationResistance

        #: As of statusDate, the leakage reactance measured at the 'from' winding with the 'to' winding short-circuited and all other windings open-circuited.
        self.leakageReactance = leakageReactance

        self._Ground = None
        self.Ground = Ground

        self._TransformerObservation = None
        self.TransformerObservation = TransformerObservation

        self._ToWinding = None
        self.ToWinding = ToWinding

        self._FromWinding = None
        self.FromWinding = FromWinding

        self.status = status

        super(WindingInsulation, self).__init__(*args, **kw_args)

    _attrs = ["insulationPFStatus", "insulationResistance", "leakageReactance"]
    _attr_types = {"insulationPFStatus": str, "insulationResistance": str, "leakageReactance": float}
    _defaults = {"insulationPFStatus": '', "insulationResistance": '', "leakageReactance": 0.0}
    _enums = {}
    _refs = ["Ground", "TransformerObservation", "ToWinding", "FromWinding", "status"]
    _many_refs = []

    def getGround(self):
        
        return self._Ground

    def setGround(self, value):
        if self._Ground is not None:
            filtered = [x for x in self.Ground.WindingInsulations if x != self]
            self._Ground._WindingInsulations = filtered

        self._Ground = value
        if self._Ground is not None:
            if self not in self._Ground._WindingInsulations:
                self._Ground._WindingInsulations.append(self)

    Ground = property(getGround, setGround)

    def getTransformerObservation(self):
        
        return self._TransformerObservation

    def setTransformerObservation(self, value):
        if self._TransformerObservation is not None:
            filtered = [x for x in self.TransformerObservation.WindingInsulationPFs if x != self]
            self._TransformerObservation._WindingInsulationPFs = filtered

        self._TransformerObservation = value
        if self._TransformerObservation is not None:
            if self not in self._TransformerObservation._WindingInsulationPFs:
                self._TransformerObservation._WindingInsulationPFs.append(self)

    TransformerObservation = property(getTransformerObservation, setTransformerObservation)

    def getToWinding(self):
        
        return self._ToWinding

    def setToWinding(self, value):
        if self._ToWinding is not None:
            filtered = [x for x in self.ToWinding.ToWindingInsulations if x != self]
            self._ToWinding._ToWindingInsulations = filtered

        self._ToWinding = value
        if self._ToWinding is not None:
            if self not in self._ToWinding._ToWindingInsulations:
                self._ToWinding._ToWindingInsulations.append(self)

    ToWinding = property(getToWinding, setToWinding)

    def getFromWinding(self):
        
        return self._FromWinding

    def setFromWinding(self, value):
        if self._FromWinding is not None:
            filtered = [x for x in self.FromWinding.FromWindingInsulations if x != self]
            self._FromWinding._FromWindingInsulations = filtered

        self._FromWinding = value
        if self._FromWinding is not None:
            if self not in self._FromWinding._FromWindingInsulations:
                self._FromWinding._FromWindingInsulations.append(self)

    FromWinding = property(getFromWinding, setFromWinding)

    status = None

