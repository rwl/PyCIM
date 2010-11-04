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

from CIM14v13.IEC61968.Informative.MarketOperations.ResourceBid import ResourceBid

class GeneratingBid(ResourceBid):

    def __init__(self, maxEmergencyMW=0.0, maximumEconomicMW=0.0, minimumEconomicMW=0.0, startUpRampRate=None, downTimeMax=0.0, operatingMode='', startupTime=0.0, minEmergencyMW=0.0, noLoadCost=0.0, minimumDownTime=0.0, startUpType=0, upTimeMin=0.0, upTimeMax=0.0, notificationTime=0.0, NotificationTimeCurve=None, RegisteredGenerator=None, StartUpCostCurve=None, BidSet=None, StartUpTimeCurve=None, *args, **kw_args):
        """Initializes a new 'GeneratingBid' instance.

        @param maxEmergencyMW: Power rating available for unit under emergency conditions greater than or equal to maximum economic limit. 
        @param maximumEconomicMW: Maximum high economic MW limit, that should not exceed the maximum operating MW limit 
        @param minimumEconomicMW: Low economic MW limit that must be greater than or equal to the minimum operating MW limit 
        @param startUpRampRate: Resource startup ramp rate (MW/minute) 
        @param downTimeMax: Maximum down time. 
        @param operatingMode: Bid operating mode ('C' - cycling, 'F' - fixed, 'M' - must run, 'U' - unavailable) 
        @param startupTime: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied 
        @param minEmergencyMW: Minimum power rating for unit under emergency conditions, which is less than or equal to the economic minimum. 
        @param noLoadCost: Resource fixed no load cost. 
        @param minimumDownTime: Minimum time interval between unit shutdown and startup 
        @param startUpType: Resource startup type:  1 - Fixed startup time and fixed startup cost  2 - Startup time as a function of down time and fixed startup cost  3 - Startup cost as a function of down time 
        @param upTimeMin: Minimum up time. 
        @param upTimeMax: Maximum up time. 
        @param notificationTime: Time required for crew notification prior to start up of the unit. 
        @param NotificationTimeCurve:
        @param RegisteredGenerator:
        @param StartUpCostCurve:
        @param BidSet:
        @param StartUpTimeCurve:
        """
        #: Power rating available for unit under emergency conditions greater than or equal to maximum economic limit.
        self.maxEmergencyMW = maxEmergencyMW

        #: Maximum high economic MW limit, that should not exceed the maximum operating MW limit
        self.maximumEconomicMW = maximumEconomicMW

        #: Low economic MW limit that must be greater than or equal to the minimum operating MW limit
        self.minimumEconomicMW = minimumEconomicMW

        #: Resource startup ramp rate (MW/minute)
        self.startUpRampRate = startUpRampRate

        #: Maximum down time.
        self.downTimeMax = downTimeMax

        #: Bid operating mode ('C' - cycling, 'F' - fixed, 'M' - must run, 'U' - unavailable)
        self.operatingMode = operatingMode

        #: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied
        self.startupTime = startupTime

        #: Minimum power rating for unit under emergency conditions, which is less than or equal to the economic minimum.
        self.minEmergencyMW = minEmergencyMW

        #: Resource fixed no load cost.
        self.noLoadCost = noLoadCost

        #: Minimum time interval between unit shutdown and startup
        self.minimumDownTime = minimumDownTime

        #: Resource startup type:  1 - Fixed startup time and fixed startup cost  2 - Startup time as a function of down time and fixed startup cost  3 - Startup cost as a function of down time
        self.startUpType = startUpType

        #: Minimum up time.
        self.upTimeMin = upTimeMin

        #: Maximum up time.
        self.upTimeMax = upTimeMax

        #: Time required for crew notification prior to start up of the unit.
        self.notificationTime = notificationTime

        self._NotificationTimeCurve = None
        self.NotificationTimeCurve = NotificationTimeCurve

        self._RegisteredGenerator = None
        self.RegisteredGenerator = RegisteredGenerator

        self._StartUpCostCurve = None
        self.StartUpCostCurve = StartUpCostCurve

        self._BidSet = None
        self.BidSet = BidSet

        self._StartUpTimeCurve = None
        self.StartUpTimeCurve = StartUpTimeCurve

        super(GeneratingBid, self).__init__(*args, **kw_args)

    def getNotificationTimeCurve(self):
        
        return self._NotificationTimeCurve

    def setNotificationTimeCurve(self, value):
        if self._NotificationTimeCurve is not None:
            filtered = [x for x in self.NotificationTimeCurve.GeneratingBids if x != self]
            self._NotificationTimeCurve._GeneratingBids = filtered

        self._NotificationTimeCurve = value
        if self._NotificationTimeCurve is not None:
            self._NotificationTimeCurve._GeneratingBids.append(self)

    NotificationTimeCurve = property(getNotificationTimeCurve, setNotificationTimeCurve)

    def getRegisteredGenerator(self):
        
        return self._RegisteredGenerator

    def setRegisteredGenerator(self, value):
        if self._RegisteredGenerator is not None:
            filtered = [x for x in self.RegisteredGenerator.GeneratingBids if x != self]
            self._RegisteredGenerator._GeneratingBids = filtered

        self._RegisteredGenerator = value
        if self._RegisteredGenerator is not None:
            self._RegisteredGenerator._GeneratingBids.append(self)

    RegisteredGenerator = property(getRegisteredGenerator, setRegisteredGenerator)

    def getStartUpCostCurve(self):
        
        return self._StartUpCostCurve

    def setStartUpCostCurve(self, value):
        if self._StartUpCostCurve is not None:
            filtered = [x for x in self.StartUpCostCurve.GeneratingBids if x != self]
            self._StartUpCostCurve._GeneratingBids = filtered

        self._StartUpCostCurve = value
        if self._StartUpCostCurve is not None:
            self._StartUpCostCurve._GeneratingBids.append(self)

    StartUpCostCurve = property(getStartUpCostCurve, setStartUpCostCurve)

    def getBidSet(self):
        
        return self._BidSet

    def setBidSet(self, value):
        if self._BidSet is not None:
            filtered = [x for x in self.BidSet.GeneratingBids if x != self]
            self._BidSet._GeneratingBids = filtered

        self._BidSet = value
        if self._BidSet is not None:
            self._BidSet._GeneratingBids.append(self)

    BidSet = property(getBidSet, setBidSet)

    def getStartUpTimeCurve(self):
        
        return self._StartUpTimeCurve

    def setStartUpTimeCurve(self, value):
        if self._StartUpTimeCurve is not None:
            filtered = [x for x in self.StartUpTimeCurve.GeneratingBids if x != self]
            self._StartUpTimeCurve._GeneratingBids = filtered

        self._StartUpTimeCurve = value
        if self._StartUpTimeCurve is not None:
            self._StartUpTimeCurve._GeneratingBids.append(self)

    StartUpTimeCurve = property(getStartUpTimeCurve, setStartUpTimeCurve)

