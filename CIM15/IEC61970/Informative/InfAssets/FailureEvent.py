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

from CIM15.IEC61968.Common.ActivityRecord import ActivityRecord

class FailureEvent(ActivityRecord):
    """An event where an asset has failed to perform its functions within specified parameters.An event where an asset has failed to perform its functions within specified parameters.
    """

    def __init__(self, failureIsolationMethod="fuse", corporateCode='', faultLocatingMethod='', location='', *args, **kw_args):
        """Initialises a new 'FailureEvent' instance.

        @param failureIsolationMethod: How the asset failure was isolated from the system. Values are: "fuse", "manuallyIsolated", "breakerOperation", "other", "burnedInTheClear"
        @param corporateCode: Code for asset failure. 
        @param faultLocatingMethod: The method used for locating the faulted part of the asset. For example, cable options include: Cap Discharge-Thumping, Bridge Method, Visual Inspection, Other. 
        @param location: Failure location on an object. 
        """
        #: How the asset failure was isolated from the system. Values are: "fuse", "manuallyIsolated", "breakerOperation", "other", "burnedInTheClear"
        self.failureIsolationMethod = failureIsolationMethod

        #: Code for asset failure.
        self.corporateCode = corporateCode

        #: The method used for locating the faulted part of the asset. For example, cable options include: Cap Discharge-Thumping, Bridge Method, Visual Inspection, Other.
        self.faultLocatingMethod = faultLocatingMethod

        #: Failure location on an object.
        self.location = location

        super(FailureEvent, self).__init__(*args, **kw_args)

    _attrs = ["failureIsolationMethod", "corporateCode", "faultLocatingMethod", "location"]
    _attr_types = {"failureIsolationMethod": str, "corporateCode": str, "faultLocatingMethod": str, "location": str}
    _defaults = {"failureIsolationMethod": "fuse", "corporateCode": '', "faultLocatingMethod": '', "location": ''}
    _enums = {"failureIsolationMethod": "FailureIsolationMethodKind"}
    _refs = []
    _many_refs = []

