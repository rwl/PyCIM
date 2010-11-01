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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class SecurityConstraints(IdentifiedObject):
    """Typical for regional transmission operators (RTOs), these constraints include transmission as well as generation group constraints identified in both base case and critical contingency cases.
    """

    def __init__(self, maxMW=0.0, actualMW=0.0, minMW=0.0, RTO=None, *args, **kw_args):
        """Initializes a new 'SecurityConstraints' instance.

        @param maxMW: Maximum MW limit 
        @param actualMW: Actual branch or group of branches MW flow (only for transmission constraints) 
        @param minMW: Minimum MW limit (only for transmission constraints). 
        @param RTO:
        """
        #: Maximum MW limit 
        self.maxMW = maxMW

        #: Actual branch or group of branches MW flow (only for transmission constraints) 
        self.actualMW = actualMW

        #: Minimum MW limit (only for transmission constraints). 
        self.minMW = minMW

        self._RTO = None
        self.RTO = RTO

        super(SecurityConstraints, self).__init__(*args, **kw_args)

    def getRTO(self):
        
        return self._RTO

    def setRTO(self, value):
        if self._RTO is not None:
            filtered = [x for x in self.RTO.SecurityConstraints if x != self]
            self._RTO._SecurityConstraints = filtered

        self._RTO = value
        if self._RTO is not None:
            self._RTO._SecurityConstraints.append(self)

    RTO = property(getRTO, setRTO)

