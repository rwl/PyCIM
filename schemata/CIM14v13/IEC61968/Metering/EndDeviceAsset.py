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

from CIM14v13.IEC61968.Assets.AssetContainer import AssetContainer

class EndDeviceAsset(AssetContainer):
    """AssetContainer that performs one or more end device functions. One type of EndDeviceAsset is a MeterAsset which can perform metering, load management, connect/disconnect, accounting functions, etc. Some EndDeviceAssets, such as ones monitoring and controlling air conditioner, refrigerator, pool pumps may be connected to a MeterAsset. All EndDeviceAssets may have communication capability defined by the associated ComFunction(s). An EndDeviceAsset may be owned by a consumer, a service provider, utility or otherwise. There may be a related end device function that identifies a sensor or control point within a metering application or communications systems (e.g., water, gas, electricity). Some devices may use an optical port that conforms to the ANSI C12.18 standard for communications.
    """

    def __init__(self, readRequest=False, metrology=False, disconnect=False, relayCapable=False, outageReport=False, amrSystem='', reverseFlowHandling=False, loadControl=False, dstEnabled=False, timeZoneOffset=0.0, demandResponse=False, EndDeviceGroups=None, EndDeviceControls=None, ElectricalInfos=None, Readings=None, ServiceLocation=None, EndDeviceModel=None, DeviceFunctions=None, Customer=None, ServiceDeliveryPoint=None, *args, **kw_args):
        """Initializes a new 'EndDeviceAsset' instance.

        @param readRequest: True if this end device asset is capable of supporting on-request reads for this end device. 
        @param metrology: True if this end device asset is capable of supporting the presentation of metered values to a user or another system (always true for a meter, but might not be true for a load control unit.) 
        @param disconnect: True if this end device asset is capable of supporting remote whole-house disconnect capability. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the ConnectDisconnectFunction contained by this end device asset. 
        @param relayCapable: True if this end device asset is capable of supporting one or more relays. The relays may be programmable in the meter and tied to TOU, time pulse, load control or other functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        @param outageReport: True if this end device asset is capable of supporting the means to report historical power interruption data. 
        @param amrSystem: Automated meter reading (AMR) system responsible for communications to this end device. 
        @param reverseFlowHandling: True if this EndDeviceAsset is capable of supporting detection and monitoring of reverse flow. 
        @param loadControl: True if this end device asset is capable of supporting load control functions through either the meter or the AMR option. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        @param dstEnabled: True if this end device asset is capable of supporting the autonomous application of daylight savings time (DST). 
        @param timeZoneOffset: Time zone offset relative to GMT for the location of this end device. 
        @param demandResponse: True if this end device asset is capable of supporting demand response functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        @param EndDeviceGroups: All end device groups referring to this end device asset.
        @param EndDeviceControls: All end device controls sending commands to this end device asset.
        @param ElectricalInfos: All sets of electrical properties for this end device asset.
        @param Readings:
        @param ServiceLocation: Service location whose service delivery is measured by this end device asset.
        @param EndDeviceModel: Product documentation for this end device asset.
        @param DeviceFunctions: All device functions this end device asset performs.
        @param Customer: Customer owning this end device asset.
        @param ServiceDeliveryPoint: Service delivery point to which this end device asset belongs.
        """
        #: True if this end device asset is capable of supporting on-request reads for this end device. 
        self.readRequest = readRequest

        #: True if this end device asset is capable of supporting the presentation of metered values to a user or another system (always true for a meter, but might not be true for a load control unit.) 
        self.metrology = metrology

        #: True if this end device asset is capable of supporting remote whole-house disconnect capability. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the ConnectDisconnectFunction contained by this end device asset. 
        self.disconnect = disconnect

        #: True if this end device asset is capable of supporting one or more relays. The relays may be programmable in the meter and tied to TOU, time pulse, load control or other functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        self.relayCapable = relayCapable

        #: True if this end device asset is capable of supporting the means to report historical power interruption data. 
        self.outageReport = outageReport

        #: Automated meter reading (AMR) system responsible for communications to this end device. 
        self.amrSystem = amrSystem

        #: True if this EndDeviceAsset is capable of supporting detection and monitoring of reverse flow. 
        self.reverseFlowHandling = reverseFlowHandling

        #: True if this end device asset is capable of supporting load control functions through either the meter or the AMR option. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        self.loadControl = loadControl

        #: True if this end device asset is capable of supporting the autonomous application of daylight savings time (DST). 
        self.dstEnabled = dstEnabled

        #: Time zone offset relative to GMT for the location of this end device. 
        self.timeZoneOffset = timeZoneOffset

        #: True if this end device asset is capable of supporting demand response functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        self.demandResponse = demandResponse

        self._EndDeviceGroups = []
        self.EndDeviceGroups = [] if EndDeviceGroups is None else EndDeviceGroups

        self._EndDeviceControls = []
        self.EndDeviceControls = [] if EndDeviceControls is None else EndDeviceControls

        self._ElectricalInfos = []
        self.ElectricalInfos = [] if ElectricalInfos is None else ElectricalInfos

        self._Readings = []
        self.Readings = [] if Readings is None else Readings

        self._ServiceLocation = None
        self.ServiceLocation = ServiceLocation

        self._EndDeviceModel = None
        self.EndDeviceModel = EndDeviceModel

        self._DeviceFunctions = []
        self.DeviceFunctions = [] if DeviceFunctions is None else DeviceFunctions

        self._Customer = None
        self.Customer = Customer

        self._ServiceDeliveryPoint = None
        self.ServiceDeliveryPoint = ServiceDeliveryPoint

        super(EndDeviceAsset, self).__init__(*args, **kw_args)

    def getEndDeviceGroups(self):
        """All end device groups referring to this end device asset.
        """
        return self._EndDeviceGroups

    def setEndDeviceGroups(self, value):
        for p in self._EndDeviceGroups:
            filtered = [q for q in p.EndDeviceAssets if q != self]
            self._EndDeviceGroups._EndDeviceAssets = filtered
        for r in value:
            if self not in r._EndDeviceAssets:
                r._EndDeviceAssets.append(self)
        self._EndDeviceGroups = value

    EndDeviceGroups = property(getEndDeviceGroups, setEndDeviceGroups)

    def addEndDeviceGroups(self, *EndDeviceGroups):
        for obj in EndDeviceGroups:
            if self not in obj._EndDeviceAssets:
                obj._EndDeviceAssets.append(self)
            self._EndDeviceGroups.append(obj)

    def removeEndDeviceGroups(self, *EndDeviceGroups):
        for obj in EndDeviceGroups:
            if self in obj._EndDeviceAssets:
                obj._EndDeviceAssets.remove(self)
            self._EndDeviceGroups.remove(obj)

    def getEndDeviceControls(self):
        """All end device controls sending commands to this end device asset.
        """
        return self._EndDeviceControls

    def setEndDeviceControls(self, value):
        for x in self._EndDeviceControls:
            x._EndDeviceAsset = None
        for y in value:
            y._EndDeviceAsset = self
        self._EndDeviceControls = value

    EndDeviceControls = property(getEndDeviceControls, setEndDeviceControls)

    def addEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj._EndDeviceAsset = self
            self._EndDeviceControls.append(obj)

    def removeEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj._EndDeviceAsset = None
            self._EndDeviceControls.remove(obj)

    def getElectricalInfos(self):
        """All sets of electrical properties for this end device asset.
        """
        return self._ElectricalInfos

    def setElectricalInfos(self, value):
        for p in self._ElectricalInfos:
            filtered = [q for q in p.EndDeviceAssets if q != self]
            self._ElectricalInfos._EndDeviceAssets = filtered
        for r in value:
            if self not in r._EndDeviceAssets:
                r._EndDeviceAssets.append(self)
        self._ElectricalInfos = value

    ElectricalInfos = property(getElectricalInfos, setElectricalInfos)

    def addElectricalInfos(self, *ElectricalInfos):
        for obj in ElectricalInfos:
            if self not in obj._EndDeviceAssets:
                obj._EndDeviceAssets.append(self)
            self._ElectricalInfos.append(obj)

    def removeElectricalInfos(self, *ElectricalInfos):
        for obj in ElectricalInfos:
            if self in obj._EndDeviceAssets:
                obj._EndDeviceAssets.remove(self)
            self._ElectricalInfos.remove(obj)

    def getReadings(self):
        
        return self._Readings

    def setReadings(self, value):
        for x in self._Readings:
            x._EndDeviceAsset = None
        for y in value:
            y._EndDeviceAsset = self
        self._Readings = value

    Readings = property(getReadings, setReadings)

    def addReadings(self, *Readings):
        for obj in Readings:
            obj._EndDeviceAsset = self
            self._Readings.append(obj)

    def removeReadings(self, *Readings):
        for obj in Readings:
            obj._EndDeviceAsset = None
            self._Readings.remove(obj)

    def getServiceLocation(self):
        """Service location whose service delivery is measured by this end device asset.
        """
        return self._ServiceLocation

    def setServiceLocation(self, value):
        if self._ServiceLocation is not None:
            filtered = [x for x in self.ServiceLocation.EndDeviceAssets if x != self]
            self._ServiceLocation._EndDeviceAssets = filtered

        self._ServiceLocation = value
        if self._ServiceLocation is not None:
            self._ServiceLocation._EndDeviceAssets.append(self)

    ServiceLocation = property(getServiceLocation, setServiceLocation)

    def getEndDeviceModel(self):
        """Product documentation for this end device asset.
        """
        return self._EndDeviceModel

    def setEndDeviceModel(self, value):
        if self._EndDeviceModel is not None:
            filtered = [x for x in self.EndDeviceModel.EndDeviceAssets if x != self]
            self._EndDeviceModel._EndDeviceAssets = filtered

        self._EndDeviceModel = value
        if self._EndDeviceModel is not None:
            self._EndDeviceModel._EndDeviceAssets.append(self)

    EndDeviceModel = property(getEndDeviceModel, setEndDeviceModel)

    def getDeviceFunctions(self):
        """All device functions this end device asset performs.
        """
        return self._DeviceFunctions

    def setDeviceFunctions(self, value):
        for x in self._DeviceFunctions:
            x._EndDeviceAsset = None
        for y in value:
            y._EndDeviceAsset = self
        self._DeviceFunctions = value

    DeviceFunctions = property(getDeviceFunctions, setDeviceFunctions)

    def addDeviceFunctions(self, *DeviceFunctions):
        for obj in DeviceFunctions:
            obj._EndDeviceAsset = self
            self._DeviceFunctions.append(obj)

    def removeDeviceFunctions(self, *DeviceFunctions):
        for obj in DeviceFunctions:
            obj._EndDeviceAsset = None
            self._DeviceFunctions.remove(obj)

    def getCustomer(self):
        """Customer owning this end device asset.
        """
        return self._Customer

    def setCustomer(self, value):
        if self._Customer is not None:
            filtered = [x for x in self.Customer.EndDeviceAssets if x != self]
            self._Customer._EndDeviceAssets = filtered

        self._Customer = value
        if self._Customer is not None:
            self._Customer._EndDeviceAssets.append(self)

    Customer = property(getCustomer, setCustomer)

    def getServiceDeliveryPoint(self):
        """Service delivery point to which this end device asset belongs.
        """
        return self._ServiceDeliveryPoint

    def setServiceDeliveryPoint(self, value):
        if self._ServiceDeliveryPoint is not None:
            filtered = [x for x in self.ServiceDeliveryPoint.EndDeviceAssets if x != self]
            self._ServiceDeliveryPoint._EndDeviceAssets = filtered

        self._ServiceDeliveryPoint = value
        if self._ServiceDeliveryPoint is not None:
            self._ServiceDeliveryPoint._EndDeviceAssets.append(self)

    ServiceDeliveryPoint = property(getServiceDeliveryPoint, setServiceDeliveryPoint)

