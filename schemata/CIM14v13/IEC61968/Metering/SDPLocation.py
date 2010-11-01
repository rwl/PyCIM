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

from CIM14v13.IEC61968.Common.Location import Location

class SDPLocation(Location):
    """Location of an individual service delivery point. For residential or most businesses, it is typically the location of a meter on the customer's premises. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party. The point(s) of delivery is specified in the Service Agreement.
    """

    def __init__(self, accessMethod='', siteAccessProblem='', remark='', occupancyDate='', ServiceDeliveryPoints=None, *args, **kw_args):
        """Initializes a new 'SDPLocation' instance.

        @param accessMethod: Method for the service person to access this service delivery point location. For example, a description of where to obtain a key if the facility is unmanned and secured. 
        @param siteAccessProblem: Problems previously encountered when visiting or performing work at this service delivery point location. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc. 
        @param remark: Remarks about this location. 
        @param occupancyDate: Date when certificate of occupancy was provided for this location, 0 if valid certificate of occupancy does not exist for (inherited) 'Location.corporateCode'. 
        @param ServiceDeliveryPoints: All service delivery points at this location.
        """
        #: Method for the service person to access this service delivery point location. For example, a description of where to obtain a key if the facility is unmanned and secured. 
        self.accessMethod = accessMethod

        #: Problems previously encountered when visiting or performing work at this service delivery point location. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc. 
        self.siteAccessProblem = siteAccessProblem

        #: Remarks about this location. 
        self.remark = remark

        #: Date when certificate of occupancy was provided for this location, 0 if valid certificate of occupancy does not exist for (inherited) 'Location.corporateCode'. 
        self.occupancyDate = occupancyDate

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        super(SDPLocation, self).__init__(*args, **kw_args)

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

