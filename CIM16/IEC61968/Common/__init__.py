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

"""This package contains the information classes that support distribution management in general.
"""

from CIM16.IEC61968.Common.PostalAddress import PostalAddress
from CIM16.IEC61968.Common.Status import Status
from CIM16.IEC61968.Common.ElectronicAddress import ElectronicAddress
from CIM16.IEC61968.Common.Location import Location
from CIM16.IEC61968.Common.TownDetail import TownDetail
from CIM16.IEC61968.Common.CoordinateSystem import CoordinateSystem
from CIM16.IEC61968.Common.Document import Document
from CIM16.IEC61968.Common.PositionPoint import PositionPoint
from CIM16.IEC61968.Common.UserAttribute import UserAttribute
from CIM16.IEC61968.Common.StreetAddress import StreetAddress
from CIM16.IEC61968.Common.StreetDetail import StreetDetail
from CIM16.IEC61968.Common.TimeSchedule import TimeSchedule
from CIM16.IEC61968.Common.ActivityRecord import ActivityRecord
from CIM16.IEC61968.Common.TimePoint import TimePoint
from CIM16.IEC61968.Common.Organisation import Organisation
from CIM16.IEC61968.Common.TelephoneNumber import TelephoneNumber
from CIM16.IEC61968.Common.Agreement import Agreement

nsURI = "http://iec.ch/TC57/2013/CIM-schema-cim16#Common"
nsPrefix = "cimCommon"

