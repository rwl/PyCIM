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

from CIM14.IEC61970.Core.Equipment import Equipment

class DistributionTransformer(Equipment):
    """An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes.
    """

    def __init__(self, Windings=None, ServiceDeliveryPoints=None, TransformerBank=None, TransformerInfo=None, **kw_args):
        """Initializes a new 'DistributionTransformer' instance.

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

        super(DistributionTransformer, self).__init__(**kw_args)

    def getWindings(self):
        """All windings of this transformer.
        """
        return self._Windings

    def setWindings(self, value):
        for x in self._Windings:
            x._Transformer = None
        for y in value:
            y._Transformer = self
        self._Windings = value

    Windings = property(getWindings, setWindings)

    def addWindings(self, *Windings):
        for obj in Windings:
            obj._Transformer = self
            self._Windings.append(obj)

    def removeWindings(self, *Windings):
        for obj in Windings:
            obj._Transformer = None
            self._Windings.remove(obj)

    def getServiceDeliveryPoints(self):
        """All service delivery points supplied by this transformer.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x._Transformer = None
        for y in value:
            y._Transformer = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj._Transformer = self
            self._ServiceDeliveryPoints.append(obj)

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj._Transformer = None
            self._ServiceDeliveryPoints.remove(obj)

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
            self._TransformerInfo._Transformers.append(self)

    TransformerInfo = property(getTransformerInfo, setTransformerInfo)

