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

class TransformerObservation(IdentifiedObject):
    """Common information captured during transformer inspections and/or diagnostics. Note that some properties may be measured through other means and therefore have measurement values in addition to the observed values recorded here.Common information captured during transformer inspections and/or diagnostics. Note that some properties may be measured through other means and therefore have measurement values in addition to the observed values recorded here.
    """

    def __init__(self, oilNeutralizationNumber='', waterContent='', oilLevel='', freqResp='', oilDielectricStrength=0.0, oilColor='', hotSpotTemp=0.0, dga='', furfuralDP='', oilIFT='', bushingTemp=0.0, topOilTemp=0.0, pumpVibration='', BushingInsultationPFs=None, ProcedureDataSets=None, Transformer=None, status=None, WindingInsulationPFs=None, TransformerAsset=None, *args, **kw_args):
        """Initialises a new 'TransformerObservation' instance.

        @param oilNeutralizationNumber: Oil Quality Analysis-Neutralization Number - Number - Mg KOH. 
        @param waterContent: Water Content expressed in parts per million. 
        @param oilLevel: The level of oil in the transformer. 
        @param freqResp: Frequency Response Analysis. Typical values are: acceptable, slight movement, significant movement, failed, near failure. A graphic of the response diagram, which is a type of document, may be associated with this analysis through the recursive document relationship of the ProcedureDataSet. 
        @param oilDielectricStrength: Oil Quality Analysis-Dielectric Strength. 
        @param oilColor: Oil Quality Analysis-Color. 
        @param hotSpotTemp: Hotspot oil temperature. 
        @param dga: Dissolved Gas Analysis. Typical values are: Acceptable, Overheating, Corona, Sparking, Arcing. 
        @param furfuralDP: Overall measure of furfural in oil and mechanical strength of paper. DP, the degree of polymerization, is the strength of the paper. Furfural is a measure of furfural compounds, often expressed in parts per million. 
        @param oilIFT: Oil Quality Analysis- inter facial tension (IFT) - number-Dynes/CM. 
        @param bushingTemp: Bushing temperature. 
        @param topOilTemp: Top oil temperature. 
        @param pumpVibration: Pump vibration, with typical values being: nominal, high. 
        @param BushingInsultationPFs:
        @param ProcedureDataSets:
        @param Transformer:
        @param status:
        @param WindingInsulationPFs:
        @param TransformerAsset:
        """
        #: Oil Quality Analysis-Neutralization Number - Number - Mg KOH.
        self.oilNeutralizationNumber = oilNeutralizationNumber

        #: Water Content expressed in parts per million.
        self.waterContent = waterContent

        #: The level of oil in the transformer.
        self.oilLevel = oilLevel

        #: Frequency Response Analysis. Typical values are: acceptable, slight movement, significant movement, failed, near failure. A graphic of the response diagram, which is a type of document, may be associated with this analysis through the recursive document relationship of the ProcedureDataSet.
        self.freqResp = freqResp

        #: Oil Quality Analysis-Dielectric Strength.
        self.oilDielectricStrength = oilDielectricStrength

        #: Oil Quality Analysis-Color.
        self.oilColor = oilColor

        #: Hotspot oil temperature.
        self.hotSpotTemp = hotSpotTemp

        #: Dissolved Gas Analysis. Typical values are: Acceptable, Overheating, Corona, Sparking, Arcing.
        self.dga = dga

        #: Overall measure of furfural in oil and mechanical strength of paper. DP, the degree of polymerization, is the strength of the paper. Furfural is a measure of furfural compounds, often expressed in parts per million.
        self.furfuralDP = furfuralDP

        #: Oil Quality Analysis- inter facial tension (IFT) - number-Dynes/CM.
        self.oilIFT = oilIFT

        #: Bushing temperature.
        self.bushingTemp = bushingTemp

        #: Top oil temperature.
        self.topOilTemp = topOilTemp

        #: Pump vibration, with typical values being: nominal, high.
        self.pumpVibration = pumpVibration

        self._BushingInsultationPFs = []
        self.BushingInsultationPFs = [] if BushingInsultationPFs is None else BushingInsultationPFs

        self._ProcedureDataSets = []
        self.ProcedureDataSets = [] if ProcedureDataSets is None else ProcedureDataSets

        self._Transformer = None
        self.Transformer = Transformer

        self.status = status

        self._WindingInsulationPFs = []
        self.WindingInsulationPFs = [] if WindingInsulationPFs is None else WindingInsulationPFs

        self._TransformerAsset = None
        self.TransformerAsset = TransformerAsset

        super(TransformerObservation, self).__init__(*args, **kw_args)

    _attrs = ["oilNeutralizationNumber", "waterContent", "oilLevel", "freqResp", "oilDielectricStrength", "oilColor", "hotSpotTemp", "dga", "furfuralDP", "oilIFT", "bushingTemp", "topOilTemp", "pumpVibration"]
    _attr_types = {"oilNeutralizationNumber": str, "waterContent": str, "oilLevel": str, "freqResp": str, "oilDielectricStrength": float, "oilColor": str, "hotSpotTemp": float, "dga": str, "furfuralDP": str, "oilIFT": str, "bushingTemp": float, "topOilTemp": float, "pumpVibration": str}
    _defaults = {"oilNeutralizationNumber": '', "waterContent": '', "oilLevel": '', "freqResp": '', "oilDielectricStrength": 0.0, "oilColor": '', "hotSpotTemp": 0.0, "dga": '', "furfuralDP": '', "oilIFT": '', "bushingTemp": 0.0, "topOilTemp": 0.0, "pumpVibration": ''}
    _enums = {}
    _refs = ["BushingInsultationPFs", "ProcedureDataSets", "Transformer", "status", "WindingInsulationPFs", "TransformerAsset"]
    _many_refs = ["BushingInsultationPFs", "ProcedureDataSets", "WindingInsulationPFs"]

    def getBushingInsultationPFs(self):
        
        return self._BushingInsultationPFs

    def setBushingInsultationPFs(self, value):
        for x in self._BushingInsultationPFs:
            x.TransformerObservation = None
        for y in value:
            y._TransformerObservation = self
        self._BushingInsultationPFs = value

    BushingInsultationPFs = property(getBushingInsultationPFs, setBushingInsultationPFs)

    def addBushingInsultationPFs(self, *BushingInsultationPFs):
        for obj in BushingInsultationPFs:
            obj.TransformerObservation = self

    def removeBushingInsultationPFs(self, *BushingInsultationPFs):
        for obj in BushingInsultationPFs:
            obj.TransformerObservation = None

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

    def getTransformer(self):
        
        return self._Transformer

    def setTransformer(self, value):
        if self._Transformer is not None:
            filtered = [x for x in self.Transformer.TransformerObservations if x != self]
            self._Transformer._TransformerObservations = filtered

        self._Transformer = value
        if self._Transformer is not None:
            if self not in self._Transformer._TransformerObservations:
                self._Transformer._TransformerObservations.append(self)

    Transformer = property(getTransformer, setTransformer)

    status = None

    def getWindingInsulationPFs(self):
        
        return self._WindingInsulationPFs

    def setWindingInsulationPFs(self, value):
        for x in self._WindingInsulationPFs:
            x.TransformerObservation = None
        for y in value:
            y._TransformerObservation = self
        self._WindingInsulationPFs = value

    WindingInsulationPFs = property(getWindingInsulationPFs, setWindingInsulationPFs)

    def addWindingInsulationPFs(self, *WindingInsulationPFs):
        for obj in WindingInsulationPFs:
            obj.TransformerObservation = self

    def removeWindingInsulationPFs(self, *WindingInsulationPFs):
        for obj in WindingInsulationPFs:
            obj.TransformerObservation = None

    def getTransformerAsset(self):
        
        return self._TransformerAsset

    def setTransformerAsset(self, value):
        if self._TransformerAsset is not None:
            filtered = [x for x in self.TransformerAsset.TransformerObservations if x != self]
            self._TransformerAsset._TransformerObservations = filtered

        self._TransformerAsset = value
        if self._TransformerAsset is not None:
            if self not in self._TransformerAsset._TransformerObservations:
                self._TransformerAsset._TransformerObservations.append(self)

    TransformerAsset = property(getTransformerAsset, setTransformerAsset)

