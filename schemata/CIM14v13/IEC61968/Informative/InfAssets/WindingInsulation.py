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

class WindingInsulation(IdentifiedObject):
    """Winding insulation condition as a result of a test.
    """

    def __init__(self, insulationPFStatus='', leakageReactance=0.0, insulationResistance='', FromWinding=None, Ground=None, TransformerObservation=None, status=None, ToWinding=None, *args, **kw_args):
        """Initializes a new 'WindingInsulation' instance.

        @param insulationPFStatus: Status of Winding Insulation Power Factor as of statusDate: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed. 
        @param leakageReactance: As of statusDate, the leakage reactance measured at the 'from' winding with the 'to' winding short-circuited and all other windings open-circuited. 
        @param insulationResistance: For testType, status of Winding Insulation Resistance as of statusDate. Typical values are: Acceptable, Questionable, Failed. 
        @param FromWinding:
        @param Ground:
        @param TransformerObservation:
        @param status:
        @param ToWinding:
        """
        #: Status of Winding Insulation Power Factor as of statusDate: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed. 
        self.insulationPFStatus = insulationPFStatus

        #: As of statusDate, the leakage reactance measured at the 'from' winding with the 'to' winding short-circuited and all other windings open-circuited. 
        self.leakageReactance = leakageReactance

        #: For testType, status of Winding Insulation Resistance as of statusDate. Typical values are: Acceptable, Questionable, Failed. 
        self.insulationResistance = insulationResistance

        self._FromWinding = None
        self.FromWinding = FromWinding

        self._Ground = None
        self.Ground = Ground

        self._TransformerObservation = None
        self.TransformerObservation = TransformerObservation

        self.status = status

        self._ToWinding = None
        self.ToWinding = ToWinding

        super(WindingInsulation, self).__init__(*args, **kw_args)

    def getFromWinding(self):
        
        return self._FromWinding

    def setFromWinding(self, value):
        if self._FromWinding is not None:
            filtered = [x for x in self.FromWinding.FromWindingInsulations if x != self]
            self._FromWinding._FromWindingInsulations = filtered

        self._FromWinding = value
        if self._FromWinding is not None:
            self._FromWinding._FromWindingInsulations.append(self)

    FromWinding = property(getFromWinding, setFromWinding)

    def getGround(self):
        
        return self._Ground

    def setGround(self, value):
        if self._Ground is not None:
            filtered = [x for x in self.Ground.WindingInsulations if x != self]
            self._Ground._WindingInsulations = filtered

        self._Ground = value
        if self._Ground is not None:
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
            self._TransformerObservation._WindingInsulationPFs.append(self)

    TransformerObservation = property(getTransformerObservation, setTransformerObservation)

    status = None

    def getToWinding(self):
        
        return self._ToWinding

    def setToWinding(self, value):
        if self._ToWinding is not None:
            filtered = [x for x in self.ToWinding.ToWindingInsulations if x != self]
            self._ToWinding._ToWindingInsulations = filtered

        self._ToWinding = value
        if self._ToWinding is not None:
            self._ToWinding._ToWindingInsulations.append(self)

    ToWinding = property(getToWinding, setToWinding)

