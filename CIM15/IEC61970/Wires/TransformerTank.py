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

from CIM15.IEC61970.Core.Equipment import Equipment

class TransformerTank(Equipment):
    """An assembly of two or more coupled windings that transform electrical power between voltage levels. These windings are bound on a common core and place in the same tank. Transformer tank can be used to model both single-phase and 3-phase transformers.An assembly of two or more coupled windings that transform electrical power between voltage levels. These windings are bound on a common core and place in the same tank. Transformer tank can be used to model both single-phase and 3-phase transformers.
    """

    def __init__(self, ServiceDeliveryPoints=None, TransformerTankEnds=None, PowerTransformer=None, TransformerTankInfo=None, TransformerObservations=None, *args, **kw_args):
        """Initialises a new 'TransformerTank' instance.

        @param ServiceDeliveryPoints: All service delivery points supplied by this transformer.
        @param TransformerTankEnds: All windings of this transformer.
        @param PowerTransformer: Bank this transformer belongs to.
        @param TransformerTankInfo: Transformer tank data.
        @param TransformerObservations:
        """
        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._TransformerTankEnds = []
        self.TransformerTankEnds = [] if TransformerTankEnds is None else TransformerTankEnds

        self._PowerTransformer = None
        self.PowerTransformer = PowerTransformer

        self._TransformerTankInfo = None
        self.TransformerTankInfo = TransformerTankInfo

        self._TransformerObservations = []
        self.TransformerObservations = [] if TransformerObservations is None else TransformerObservations

        super(TransformerTank, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ServiceDeliveryPoints", "TransformerTankEnds", "PowerTransformer", "TransformerTankInfo", "TransformerObservations"]
    _many_refs = ["ServiceDeliveryPoints", "TransformerTankEnds", "TransformerObservations"]

    def getServiceDeliveryPoints(self):
        """All service delivery points supplied by this transformer.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x.TransformerTanks = None
        for y in value:
            y._TransformerTanks = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.TransformerTanks = self

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.TransformerTanks = None

    def getTransformerTankEnds(self):
        """All windings of this transformer.
        """
        return self._TransformerTankEnds

    def setTransformerTankEnds(self, value):
        for x in self._TransformerTankEnds:
            x.TransformerTank = None
        for y in value:
            y._TransformerTank = self
        self._TransformerTankEnds = value

    TransformerTankEnds = property(getTransformerTankEnds, setTransformerTankEnds)

    def addTransformerTankEnds(self, *TransformerTankEnds):
        for obj in TransformerTankEnds:
            obj.TransformerTank = self

    def removeTransformerTankEnds(self, *TransformerTankEnds):
        for obj in TransformerTankEnds:
            obj.TransformerTank = None

    def getPowerTransformer(self):
        """Bank this transformer belongs to.
        """
        return self._PowerTransformer

    def setPowerTransformer(self, value):
        if self._PowerTransformer is not None:
            filtered = [x for x in self.PowerTransformer.TransformerTanks if x != self]
            self._PowerTransformer._TransformerTanks = filtered

        self._PowerTransformer = value
        if self._PowerTransformer is not None:
            if self not in self._PowerTransformer._TransformerTanks:
                self._PowerTransformer._TransformerTanks.append(self)

    PowerTransformer = property(getPowerTransformer, setPowerTransformer)

    def getTransformerTankInfo(self):
        """Transformer tank data.
        """
        return self._TransformerTankInfo

    def setTransformerTankInfo(self, value):
        if self._TransformerTankInfo is not None:
            filtered = [x for x in self.TransformerTankInfo.TransformerTanks if x != self]
            self._TransformerTankInfo._TransformerTanks = filtered

        self._TransformerTankInfo = value
        if self._TransformerTankInfo is not None:
            if self not in self._TransformerTankInfo._TransformerTanks:
                self._TransformerTankInfo._TransformerTanks.append(self)

    TransformerTankInfo = property(getTransformerTankInfo, setTransformerTankInfo)

    def getTransformerObservations(self):
        
        return self._TransformerObservations

    def setTransformerObservations(self, value):
        for x in self._TransformerObservations:
            x.Transformer = None
        for y in value:
            y._Transformer = self
        self._TransformerObservations = value

    TransformerObservations = property(getTransformerObservations, setTransformerObservations)

    def addTransformerObservations(self, *TransformerObservations):
        for obj in TransformerObservations:
            obj.Transformer = self

    def removeTransformerObservations(self, *TransformerObservations):
        for obj in TransformerObservations:
            obj.Transformer = None

