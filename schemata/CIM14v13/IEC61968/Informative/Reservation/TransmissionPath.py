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

from CIM14v13.Element import Element

class TransmissionPath(Element):
    """An electrical connection, link, or line consisting of one or more parallel transmission elements between two areas of the interconnected electric systems, or portions thereof. TransmissionCorridor and TransmissionRightOfWay refer to legal aspects. The TransmissionPath refers to the segments between a TransmissionProvider's ServicePoints.
    """

    def __init__(self, totalTransferCapability=0.0, parallelPathFlag=False, availTransferCapability=0.0, OfferedOn=None, DeliveryPointFor=None, PointOfReceiptFor=None, LocatedOn=None, For=None, **kw_args):
        """Initializes a new 'TransmissionPath' instance.

        @param totalTransferCapability: The total transmission capability of a transmission path in the reference direction 
        @param parallelPathFlag: Flag which indicates if the transmission path is also a designated interconnection 'parallel path' 
        @param availTransferCapability: The available transmission capability of a transmission path for the reference direction 
        @param OfferedOn: A transmission service is offered on a transmission path.
        @param DeliveryPointFor: A transmission path has a 'point-of-delivery' service point
        @param PointOfReceiptFor: A transmission path has a 'point-of-receipt' service point
        @param LocatedOn: A transmission product is located on a transmission path.
        @param For: A TransmissionPath is contained in a TransmissionCorridor.
        """
        #: The total transmission capability of a transmission path in the reference direction
        self.totalTransferCapability = totalTransferCapability

        #: Flag which indicates if the transmission path is also a designated interconnection 'parallel path'
        self.parallelPathFlag = parallelPathFlag

        #: The available transmission capability of a transmission path for the reference direction
        self.availTransferCapability = availTransferCapability

        self._OfferedOn = []
        self.OfferedOn = [] if OfferedOn is None else OfferedOn

        self._DeliveryPointFor = None
        self.DeliveryPointFor = DeliveryPointFor

        self._PointOfReceiptFor = None
        self.PointOfReceiptFor = PointOfReceiptFor

        self._LocatedOn = []
        self.LocatedOn = [] if LocatedOn is None else LocatedOn

        self._For = None
        self.For = For

        super(TransmissionPath, self).__init__(**kw_args)

    def getOfferedOn(self):
        """A transmission service is offered on a transmission path.
        """
        return self._OfferedOn

    def setOfferedOn(self, value):
        for p in self._OfferedOn:
            filtered = [q for q in p.Offering if q != self]
            self._OfferedOn._Offering = filtered
        for r in value:
            if self not in r._Offering:
                r._Offering.append(self)
        self._OfferedOn = value

    OfferedOn = property(getOfferedOn, setOfferedOn)

    def addOfferedOn(self, *OfferedOn):
        for obj in OfferedOn:
            if self not in obj._Offering:
                obj._Offering.append(self)
            self._OfferedOn.append(obj)

    def removeOfferedOn(self, *OfferedOn):
        for obj in OfferedOn:
            if self in obj._Offering:
                obj._Offering.remove(self)
            self._OfferedOn.remove(obj)

    def getDeliveryPointFor(self):
        """A transmission path has a 'point-of-delivery' service point
        """
        return self._DeliveryPointFor

    def setDeliveryPointFor(self, value):
        if self._DeliveryPointFor is not None:
            filtered = [x for x in self.DeliveryPointFor.HasAPOD_ if x != self]
            self._DeliveryPointFor._HasAPOD_ = filtered

        self._DeliveryPointFor = value
        if self._DeliveryPointFor is not None:
            self._DeliveryPointFor._HasAPOD_.append(self)

    DeliveryPointFor = property(getDeliveryPointFor, setDeliveryPointFor)

    def getPointOfReceiptFor(self):
        """A transmission path has a 'point-of-receipt' service point
        """
        return self._PointOfReceiptFor

    def setPointOfReceiptFor(self, value):
        if self._PointOfReceiptFor is not None:
            filtered = [x for x in self.PointOfReceiptFor.HasAPOR_ if x != self]
            self._PointOfReceiptFor._HasAPOR_ = filtered

        self._PointOfReceiptFor = value
        if self._PointOfReceiptFor is not None:
            self._PointOfReceiptFor._HasAPOR_.append(self)

    PointOfReceiptFor = property(getPointOfReceiptFor, setPointOfReceiptFor)

    def getLocatedOn(self):
        """A transmission product is located on a transmission path.
        """
        return self._LocatedOn

    def setLocatedOn(self, value):
        for p in self._LocatedOn:
            filtered = [q for q in p.LocationFor if q != self]
            self._LocatedOn._LocationFor = filtered
        for r in value:
            if self not in r._LocationFor:
                r._LocationFor.append(self)
        self._LocatedOn = value

    LocatedOn = property(getLocatedOn, setLocatedOn)

    def addLocatedOn(self, *LocatedOn):
        for obj in LocatedOn:
            if self not in obj._LocationFor:
                obj._LocationFor.append(self)
            self._LocatedOn.append(obj)

    def removeLocatedOn(self, *LocatedOn):
        for obj in LocatedOn:
            if self in obj._LocationFor:
                obj._LocationFor.remove(self)
            self._LocatedOn.remove(obj)

    def getFor(self):
        """A TransmissionPath is contained in a TransmissionCorridor.
        """
        return self._For

    def setFor(self, value):
        if self._For is not None:
            filtered = [x for x in self.For.ContainedIn if x != self]
            self._For._ContainedIn = filtered

        self._For = value
        if self._For is not None:
            self._For._ContainedIn.append(self)

    For = property(getFor, setFor)

