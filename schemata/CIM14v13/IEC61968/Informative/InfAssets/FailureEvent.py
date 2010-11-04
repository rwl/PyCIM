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

from CIM14v13.IEC61968.Common.ActivityRecord import ActivityRecord

class FailureEvent(ActivityRecord):
    """An event where an asset has failed to perform its functions within specified parameters.
    """

    def __init__(self, failureIsolationMethod='manuallyIsolated', corporateCode='', faultLocatingMethod='', location='', **kw_args):
        """Initializes a new 'FailureEvent' instance.

        @param failureIsolationMethod: How the asset failure was isolated from the system. Values are: "manuallyIsolated", "burnedInTheClear", "fuse", "other", "breakerOperation"
        @param corporateCode: Code for asset failure. 
        @param faultLocatingMethod: The method used for locating the faulted part of the asset. For example, cable options include: Cap Discharge-Thumping, Bridge Method, Visual Inspection, Other. 
        @param location: Failure location on an object. 
        """
        #: How the asset failure was isolated from the system.Values are: "manuallyIsolated", "burnedInTheClear", "fuse", "other", "breakerOperation"
        self.failureIsolationMethod = failureIsolationMethod

        #: Code for asset failure.
        self.corporateCode = corporateCode

        #: The method used for locating the faulted part of the asset. For example, cable options include: Cap Discharge-Thumping, Bridge Method, Visual Inspection, Other.
        self.faultLocatingMethod = faultLocatingMethod

        #: Failure location on an object.
        self.location = location

        super(FailureEvent, self).__init__(**kw_args)

