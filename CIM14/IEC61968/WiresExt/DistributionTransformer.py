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

from CIM14.IEC61970.Core.Equipment import Equipment

class DistributionTransformer(Equipment):
    """An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes.
    """

    def __init__(self, Windings=None, ServiceDeliveryPoints=None, TransformerBank=None, TransformerInfo=None, *args, **kw_args):
        """Initialises a new 'DistributionTransformer' instance.

        @param Windings: All windings of this transformer.
        @param ServiceDeliveryPoints: All service delivery points supplied by this transformer.
        @param TransformerBank: Bank this transformer belongs to.
        @param TransformerInfo: Transformer data.
        """
        self._Windings = []
        self.Windings = [] if Windings is None else Windings

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._TransformerBank = None
        self.TransformerBank = TransformerBank

        self._TransformerInfo = None
        self.TransformerInfo = TransformerInfo

        super(DistributionTransformer, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Windings", "ServiceDeliveryPoints", "TransformerBank", "TransformerInfo"]
    _many_refs = ["Windings", "ServiceDeliveryPoints"]

    def getWindings(self):
        """All windings of this transformer.
        """
        return self._Windings

    def setWindings(self, value):
        for x in self._Windings:
            x.Transformer = None
        for y in value:
            y._Transformer = self
        self._Windings = value

    Windings = property(getWindings, setWindings)

    def addWindings(self, *Windings):
        for obj in Windings:
            obj.Transformer = self

    def removeWindings(self, *Windings):
        for obj in Windings:
            obj.Transformer = None

    def getServiceDeliveryPoints(self):
        """All service delivery points supplied by this transformer.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x.Transformer = None
        for y in value:
            y._Transformer = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.Transformer = self

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.Transformer = None

    def getTransformerBank(self):
        """Bank this transformer belongs to.
        """
        return self._TransformerBank

    def setTransformerBank(self, value):
        if self._TransformerBank is not None:
            filtered = [x for x in self.TransformerBank.Transformers if x != self]
            self._TransformerBank._Transformers = filtered

        self._TransformerBank = value
        if self._TransformerBank is not None:
            if self not in self._TransformerBank._Transformers:
                self._TransformerBank._Transformers.append(self)

    TransformerBank = property(getTransformerBank, setTransformerBank)

    def getTransformerInfo(self):
        """Transformer data.
        """
        return self._TransformerInfo

    def setTransformerInfo(self, value):
        if self._TransformerInfo is not None:
            filtered = [x for x in self.TransformerInfo.Transformers if x != self]
            self._TransformerInfo._Transformers = filtered

        self._TransformerInfo = value
        if self._TransformerInfo is not None:
            if self not in self._TransformerInfo._Transformers:
                self._TransformerInfo._Transformers.append(self)

    TransformerInfo = property(getTransformerInfo, setTransformerInfo)

