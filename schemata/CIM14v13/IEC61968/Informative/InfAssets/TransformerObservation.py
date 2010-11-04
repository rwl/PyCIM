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

class TransformerObservation(IdentifiedObject):
    """Common information captured during transformer inspections and/or diagnostics. Note that some properties may be measured through other means and therefore have measurement values in addition to the observed values recorded here.
    """

    def __init__(self, oilNeutralizationNumber='', topOilTemp=0.0, dga='', pumpVibration='', oilColor='', oilIFT='', oilDielectricStrength=0.0, hotSpotTemp=0.0, oilLevel='', waterContent='', bushingTemp=0.0, furfuralDP='', freqResp='', status=None, WindingInsulationPFs=None, TransformerAsset=None, Transformer=None, BushingInsultationPFs=None, ProcedureDataSets=None, *args, **kw_args):
        """Initializes a new 'TransformerObservation' instance.

        @param oilNeutralizationNumber: Oil Quality Analysis-Neutralization Number - Number - Mg KOH. 
        @param topOilTemp: Top oil temperature. 
        @param dga: Dissolved Gas Analysis. Typical values are: Acceptable, Overheating, Corona, Sparking, Arcing. 
        @param pumpVibration: Pump vibration, with typical values being: nominal, high. 
        @param oilColor: Oil Quality Analysis-Color. 
        @param oilIFT: Oil Quality Analysis- inter facial tension (IFT) - number-Dynes/CM. 
        @param oilDielectricStrength: Oil Quality Analysis-Dielectric Strength. 
        @param hotSpotTemp: Hotspot oil temperature. 
        @param oilLevel: The level of oil in the transformer. 
        @param waterContent: Water Content expressed in parts per million. 
        @param bushingTemp: Bushing temperature. 
        @param furfuralDP: Overall measure of furfural in oil and mechanical strength of paper. DP, the degree of polymerization, is the strength of the paper. Furfural is a measure of furfural compounds, often expressed in parts per million. 
        @param freqResp: Frequency Response Analysis. Typical values are: acceptable, slight movement, significant movement, failed, near failure. A graphic of the response diagram, which is a type of document, may be associated with this analysis through the recursive document relationship of the ProcedureDataSet. 
        @param status:
        @param WindingInsulationPFs:
        @param TransformerAsset:
        @param Transformer:
        @param BushingInsultationPFs:
        @param ProcedureDataSets:
        """
        #: Oil Quality Analysis-Neutralization Number - Number - Mg KOH.
        self.oilNeutralizationNumber = oilNeutralizationNumber

        #: Top oil temperature.
        self.topOilTemp = topOilTemp

        #: Dissolved Gas Analysis. Typical values are: Acceptable, Overheating, Corona, Sparking, Arcing.
        self.dga = dga

        #: Pump vibration, with typical values being: nominal, high.
        self.pumpVibration = pumpVibration

        #: Oil Quality Analysis-Color.
        self.oilColor = oilColor

        #: Oil Quality Analysis- inter facial tension (IFT) - number-Dynes/CM.
        self.oilIFT = oilIFT

        #: Oil Quality Analysis-Dielectric Strength.
        self.oilDielectricStrength = oilDielectricStrength

        #: Hotspot oil temperature.
        self.hotSpotTemp = hotSpotTemp

        #: The level of oil in the transformer.
        self.oilLevel = oilLevel

        #: Water Content expressed in parts per million.
        self.waterContent = waterContent

        #: Bushing temperature.
        self.bushingTemp = bushingTemp

        #: Overall measure of furfural in oil and mechanical strength of paper. DP, the degree of polymerization, is the strength of the paper. Furfural is a measure of furfural compounds, often expressed in parts per million.
        self.furfuralDP = furfuralDP

        #: Frequency Response Analysis. Typical values are: acceptable, slight movement, significant movement, failed, near failure. A graphic of the response diagram, which is a type of document, may be associated with this analysis through the recursive document relationship of the ProcedureDataSet.
        self.freqResp = freqResp

        self.status = status

        self._WindingInsulationPFs = []
        self.WindingInsulationPFs = [] if WindingInsulationPFs is None else WindingInsulationPFs

        self._TransformerAsset = None
        self.TransformerAsset = TransformerAsset

        self._Transformer = None
        self.Transformer = Transformer

        self._BushingInsultationPFs = []
        self.BushingInsultationPFs = [] if BushingInsultationPFs is None else BushingInsultationPFs

        self._ProcedureDataSets = []
        self.ProcedureDataSets = [] if ProcedureDataSets is None else ProcedureDataSets

        super(TransformerObservation, self).__init__(*args, **kw_args)

    status = None

    def getWindingInsulationPFs(self):
        
        return self._WindingInsulationPFs

    def setWindingInsulationPFs(self, value):
        for x in self._WindingInsulationPFs:
            x._TransformerObservation = None
        for y in value:
            y._TransformerObservation = self
        self._WindingInsulationPFs = value

    WindingInsulationPFs = property(getWindingInsulationPFs, setWindingInsulationPFs)

    def addWindingInsulationPFs(self, *WindingInsulationPFs):
        for obj in WindingInsulationPFs:
            obj._TransformerObservation = self
            self._WindingInsulationPFs.append(obj)

    def removeWindingInsulationPFs(self, *WindingInsulationPFs):
        for obj in WindingInsulationPFs:
            obj._TransformerObservation = None
            self._WindingInsulationPFs.remove(obj)

    def getTransformerAsset(self):
        
        return self._TransformerAsset

    def setTransformerAsset(self, value):
        if self._TransformerAsset is not None:
            filtered = [x for x in self.TransformerAsset.TransformerObservations if x != self]
            self._TransformerAsset._TransformerObservations = filtered

        self._TransformerAsset = value
        if self._TransformerAsset is not None:
            self._TransformerAsset._TransformerObservations.append(self)

    TransformerAsset = property(getTransformerAsset, setTransformerAsset)

    def getTransformer(self):
        
        return self._Transformer

    def setTransformer(self, value):
        if self._Transformer is not None:
            filtered = [x for x in self.Transformer.TransformerObservations if x != self]
            self._Transformer._TransformerObservations = filtered

        self._Transformer = value
        if self._Transformer is not None:
            self._Transformer._TransformerObservations.append(self)

    Transformer = property(getTransformer, setTransformer)

    def getBushingInsultationPFs(self):
        
        return self._BushingInsultationPFs

    def setBushingInsultationPFs(self, value):
        for x in self._BushingInsultationPFs:
            x._TransformerObservation = None
        for y in value:
            y._TransformerObservation = self
        self._BushingInsultationPFs = value

    BushingInsultationPFs = property(getBushingInsultationPFs, setBushingInsultationPFs)

    def addBushingInsultationPFs(self, *BushingInsultationPFs):
        for obj in BushingInsultationPFs:
            obj._TransformerObservation = self
            self._BushingInsultationPFs.append(obj)

    def removeBushingInsultationPFs(self, *BushingInsultationPFs):
        for obj in BushingInsultationPFs:
            obj._TransformerObservation = None
            self._BushingInsultationPFs.remove(obj)

    def getProcedureDataSets(self):
        
        return self._ProcedureDataSets

    def setProcedureDataSets(self, value):
        for p in self._ProcedureDataSets:
            filtered = [q for q in p.TransformerObservations if q != self]
            self._ProcedureDataSets._TransformerObservations = filtered
        for r in value:
            if self not in r._TransformerObservations:
                r._TransformerObservations.append(self)
        self._ProcedureDataSets = value

    ProcedureDataSets = property(getProcedureDataSets, setProcedureDataSets)

    def addProcedureDataSets(self, *ProcedureDataSets):
        for obj in ProcedureDataSets:
            if self not in obj._TransformerObservations:
                obj._TransformerObservations.append(self)
            self._ProcedureDataSets.append(obj)

    def removeProcedureDataSets(self, *ProcedureDataSets):
        for obj in ProcedureDataSets:
            if self in obj._TransformerObservations:
                obj._TransformerObservations.remove(self)
            self._ProcedureDataSets.remove(obj)

