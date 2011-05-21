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

from CIM14.IEC61968.Assets.AssetContainer import AssetContainer

class EndDeviceAsset(AssetContainer):
    """AssetContainer that performs one or more end device functions. One type of EndDeviceAsset is a MeterAsset which can perform metering, load management, connect/disconnect, accounting functions, etc. Some EndDeviceAssets, such as ones monitoring and controlling air conditioner, refrigerator, pool pumps may be connected to a MeterAsset. All EndDeviceAssets may have communication capability defined by the associated ComFunction(s). An EndDeviceAsset may be owned by a consumer, a service provider, utility or otherwise. There may be a related end device function that identifies a sensor or control point within a metering application or communications systems (e.g., water, gas, electricity). Some devices may use an optical port that conforms to the ANSI C12.18 standard for communications.
    """

    def __init__(self, readRequest=False, demandResponse=False, relayCapable=False, amrSystem='', ratedCurrent=0.0, phaseCount=0, reverseFlowHandling=False, metrology=False, timeZoneOffset=0.0, outageReport=False, dstEnabled=False, disconnect=False, ratedVoltage=0.0, loadControl=False, EndDeviceGroups=None, ServiceLocation=None, EndDeviceModel=None, DeviceFunctions=None, ServiceDeliveryPoint=None, Readings=None, EndDeviceControls=None, Customer=None, *args, **kw_args):
        """Initialises a new 'EndDeviceAsset' instance.

        @param readRequest: True if this end device asset is capable of supporting on-request reads for this end device. 
        @param demandResponse: True if this end device asset is capable of supporting demand response functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        @param relayCapable: True if this end device asset is capable of supporting one or more relays. The relays may be programmable in the meter and tied to TOU, time pulse, load control or other functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        @param amrSystem: Automated meter reading (AMR) system responsible for communications to this end device. 
        @param ratedCurrent: Rated current. 
        @param phaseCount: Number of potential phases the asset supports, typically 0, 1 or 3. 
        @param reverseFlowHandling: True if this EndDeviceAsset is capable of supporting detection and monitoring of reverse flow. 
        @param metrology: True if this end device asset is capable of supporting the presentation of metered values to a user or another system (always true for a meter, but might not be true for a load control unit.) 
        @param timeZoneOffset: Time zone offset relative to GMT for the location of this end device. 
        @param outageReport: True if this end device asset is capable of supporting the means to report historical power interruption data. 
        @param dstEnabled: True if this end device asset is capable of supporting the autonomous application of daylight savings time (DST). 
        @param disconnect: True if this end device asset is capable of supporting remote whole-house disconnect capability. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the ConnectDisconnectFunction contained by this end device asset. For example, to be able to remotely disconnect the device, the following values of attributes must hold: - EndDeviceAsset.disconnect = true (device supports disconnect) - ConnectDisconnectFunction.disabled (inherited from DeviceFunction) = false (function enabled) - ConnectDisconnectFunction.isConnected = true (currently connected). 
        @param ratedVoltage: Rated voltage. 
        @param loadControl: True if this end device asset is capable of supporting load control functions through either the meter or the AMR option. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        @param EndDeviceGroups: All end device groups referring to this end device asset.
        @param ServiceLocation: Service location whose service delivery is measured by this end device asset.
        @param EndDeviceModel: Product documentation for this end device asset.
        @param DeviceFunctions: All device functions this end device asset performs.
        @param ServiceDeliveryPoint: Service delivery point to which this end device asset belongs.
        @param Readings:
        @param EndDeviceControls: All end device controls sending commands to this end device asset.
        @param Customer: Customer owning this end device asset.
        """
        #: True if this end device asset is capable of supporting on-request reads for this end device.
        self.readRequest = readRequest

        #: True if this end device asset is capable of supporting demand response functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.
        self.demandResponse = demandResponse

        #: True if this end device asset is capable of supporting one or more relays. The relays may be programmable in the meter and tied to TOU, time pulse, load control or other functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.
        self.relayCapable = relayCapable

        #: Automated meter reading (AMR) system responsible for communications to this end device.
        self.amrSystem = amrSystem

        #: Rated current.
        self.ratedCurrent = ratedCurrent

        #: Number of potential phases the asset supports, typically 0, 1 or 3.
        self.phaseCount = phaseCount

        #: True if this EndDeviceAsset is capable of supporting detection and monitoring of reverse flow.
        self.reverseFlowHandling = reverseFlowHandling

        #: True if this end device asset is capable of supporting the presentation of metered values to a user or another system (always true for a meter, but might not be true for a load control unit.)
        self.metrology = metrology

        #: Time zone offset relative to GMT for the location of this end device.
        self.timeZoneOffset = timeZoneOffset

        #: True if this end device asset is capable of supporting the means to report historical power interruption data.
        self.outageReport = outageReport

        #: True if this end device asset is capable of supporting the autonomous application of daylight savings time (DST).
        self.dstEnabled = dstEnabled

        #: True if this end device asset is capable of supporting remote whole-house disconnect capability. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the ConnectDisconnectFunction contained by this end device asset. For example, to be able to remotely disconnect the device, the following values of attributes must hold: - EndDeviceAsset.disconnect = true (device supports disconnect) - ConnectDisconnectFunction.disabled (inherited from DeviceFunction) = false (function enabled) - ConnectDisconnectFunction.isConnected = true (currently connected).
        self.disconnect = disconnect

        #: Rated voltage.
        self.ratedVoltage = ratedVoltage

        #: True if this end device asset is capable of supporting load control functions through either the meter or the AMR option. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.
        self.loadControl = loadControl

        self._EndDeviceGroups = []
        self.EndDeviceGroups = [] if EndDeviceGroups is None else EndDeviceGroups

        self._ServiceLocation = None
        self.ServiceLocation = ServiceLocation

        self._EndDeviceModel = None
        self.EndDeviceModel = EndDeviceModel

        self._DeviceFunctions = []
        self.DeviceFunctions = [] if DeviceFunctions is None else DeviceFunctions

        self._ServiceDeliveryPoint = None
        self.ServiceDeliveryPoint = ServiceDeliveryPoint

        self._Readings = []
        self.Readings = [] if Readings is None else Readings

        self._EndDeviceControls = []
        self.EndDeviceControls = [] if EndDeviceControls is None else EndDeviceControls

        self._Customer = None
        self.Customer = Customer

        super(EndDeviceAsset, self).__init__(*args, **kw_args)

    _attrs = ["readRequest", "demandResponse", "relayCapable", "amrSystem", "ratedCurrent", "phaseCount", "reverseFlowHandling", "metrology", "timeZoneOffset", "outageReport", "dstEnabled", "disconnect", "ratedVoltage", "loadControl"]
    _attr_types = {"readRequest": bool, "demandResponse": bool, "relayCapable": bool, "amrSystem": str, "ratedCurrent": float, "phaseCount": int, "reverseFlowHandling": bool, "metrology": bool, "timeZoneOffset": float, "outageReport": bool, "dstEnabled": bool, "disconnect": bool, "ratedVoltage": float, "loadControl": bool}
    _defaults = {"readRequest": False, "demandResponse": False, "relayCapable": False, "amrSystem": '', "ratedCurrent": 0.0, "phaseCount": 0, "reverseFlowHandling": False, "metrology": False, "timeZoneOffset": 0.0, "outageReport": False, "dstEnabled": False, "disconnect": False, "ratedVoltage": 0.0, "loadControl": False}
    _enums = {}
    _refs = ["EndDeviceGroups", "ServiceLocation", "EndDeviceModel", "DeviceFunctions", "ServiceDeliveryPoint", "Readings", "EndDeviceControls", "Customer"]
    _many_refs = ["EndDeviceGroups", "DeviceFunctions", "Readings", "EndDeviceControls"]

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
            if self not in self._ServiceLocation._EndDeviceAssets:
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
            if self not in self._EndDeviceModel._EndDeviceAssets:
                self._EndDeviceModel._EndDeviceAssets.append(self)

    EndDeviceModel = property(getEndDeviceModel, setEndDeviceModel)

    def getDeviceFunctions(self):
        """All device functions this end device asset performs.
        """
        return self._DeviceFunctions

    def setDeviceFunctions(self, value):
        for x in self._DeviceFunctions:
            x.EndDeviceAsset = None
        for y in value:
            y._EndDeviceAsset = self
        self._DeviceFunctions = value

    DeviceFunctions = property(getDeviceFunctions, setDeviceFunctions)

    def addDeviceFunctions(self, *DeviceFunctions):
        for obj in DeviceFunctions:
            obj.EndDeviceAsset = self

    def removeDeviceFunctions(self, *DeviceFunctions):
        for obj in DeviceFunctions:
            obj.EndDeviceAsset = None

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
            if self not in self._ServiceDeliveryPoint._EndDeviceAssets:
                self._ServiceDeliveryPoint._EndDeviceAssets.append(self)

    ServiceDeliveryPoint = property(getServiceDeliveryPoint, setServiceDeliveryPoint)

    def getReadings(self):
        
        return self._Readings

    def setReadings(self, value):
        for x in self._Readings:
            x.EndDeviceAsset = None
        for y in value:
            y._EndDeviceAsset = self
        self._Readings = value

    Readings = property(getReadings, setReadings)

    def addReadings(self, *Readings):
        for obj in Readings:
            obj.EndDeviceAsset = self

    def removeReadings(self, *Readings):
        for obj in Readings:
            obj.EndDeviceAsset = None

    def getEndDeviceControls(self):
        """All end device controls sending commands to this end device asset.
        """
        return self._EndDeviceControls

    def setEndDeviceControls(self, value):
        for x in self._EndDeviceControls:
            x.EndDeviceAsset = None
        for y in value:
            y._EndDeviceAsset = self
        self._EndDeviceControls = value

    EndDeviceControls = property(getEndDeviceControls, setEndDeviceControls)

    def addEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj.EndDeviceAsset = self

    def removeEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj.EndDeviceAsset = None

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
            if self not in self._Customer._EndDeviceAssets:
                self._Customer._EndDeviceAssets.append(self)

    Customer = property(getCustomer, setCustomer)

