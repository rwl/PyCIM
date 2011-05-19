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

from CIM15.IEC61968.Common.Location import Location

class SDPLocation(Location):
    """Location of an individual service delivery point. For residential or most businesses, it is typically the location of a meter on the customer's premises. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party. The point(s) of delivery is specified in the service agreement.Location of an individual service delivery point. For residential or most businesses, it is typically the location of a meter on the customer's premises. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party. The point(s) of delivery is specified in the service agreement.
    """

    def __init__(self, accessMethod='', remark='', siteAccessProblem='', occupancyDate='', ServiceDeliveryPoints=None, *args, **kw_args):
        """Initialises a new 'SDPLocation' instance.

        @param accessMethod: Method for the service person to access this service delivery point location. For example, a description of where to obtain a key if the facility is unmanned and secured. 
        @param remark: Remarks about this location. 
        @param siteAccessProblem: Problems previously encountered when visiting or performing work at this service delivery point location. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc. 
        @param occupancyDate: Date when certificate of occupancy was provided for this location, 0 if valid certificate of occupancy does not exist for (inherited) 'Location.corporateCode'. 
        @param ServiceDeliveryPoints: All service delivery points at this location.
        """
        #: Method for the service person to access this service delivery point location. For example, a description of where to obtain a key if the facility is unmanned and secured.
        self.accessMethod = accessMethod

        #: Remarks about this location.
        self.remark = remark

        #: Problems previously encountered when visiting or performing work at this service delivery point location. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc.
        self.siteAccessProblem = siteAccessProblem

        #: Date when certificate of occupancy was provided for this location, 0 if valid certificate of occupancy does not exist for (inherited) 'Location.corporateCode'.
        self.occupancyDate = occupancyDate

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        super(SDPLocation, self).__init__(*args, **kw_args)

    _attrs = ["accessMethod", "remark", "siteAccessProblem", "occupancyDate"]
    _attr_types = {"accessMethod": str, "remark": str, "siteAccessProblem": str, "occupancyDate": str}
    _defaults = {"accessMethod": '', "remark": '', "siteAccessProblem": '', "occupancyDate": ''}
    _enums = {}
    _refs = ["ServiceDeliveryPoints"]
    _many_refs = ["ServiceDeliveryPoints"]

    def getServiceDeliveryPoints(self):
        """All service delivery points at this location.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for p in self._ServiceDeliveryPoints:
            filtered = [q for q in p.SDPLocations if q != self]
            self._ServiceDeliveryPoints._SDPLocations = filtered
        for r in value:
            if self not in r._SDPLocations:
                r._SDPLocations.append(self)
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            if self not in obj._SDPLocations:
                obj._SDPLocations.append(self)
            self._ServiceDeliveryPoints.append(obj)

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            if self in obj._SDPLocations:
                obj._SDPLocations.remove(self)
            self._ServiceDeliveryPoints.remove(obj)

