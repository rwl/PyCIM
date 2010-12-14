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

"""This package contains the information classes that support distribution management in general.
"""

nsPrefix = "cimCommon"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Common"

from CIM14.IEC61968.Common.Organisation import Organisation
from CIM14.IEC61968.Common.Status import Status
from CIM14.IEC61968.Common.Document import Document
from CIM14.IEC61968.Common.TimeSchedule import TimeSchedule
from CIM14.IEC61968.Common.TownDetail import TownDetail
from CIM14.IEC61968.Common.Location import Location
from CIM14.IEC61968.Common.PostalAddress import PostalAddress
from CIM14.IEC61968.Common.PositionPoint import PositionPoint
from CIM14.IEC61968.Common.ActivityRecord import ActivityRecord
from CIM14.IEC61968.Common.StreetAddress import StreetAddress
from CIM14.IEC61968.Common.TimePoint import TimePoint
from CIM14.IEC61968.Common.Agreement import Agreement
from CIM14.IEC61968.Common.DateTimeInterval import DateTimeInterval
from CIM14.IEC61968.Common.StreetDetail import StreetDetail
from CIM14.IEC61968.Common.ElectronicAddress import ElectronicAddress
from CIM14.IEC61968.Common.TelephoneNumber import TelephoneNumber
from CIM14.IEC61968.Common.UserAttribute import UserAttribute
from CIM14.IEC61968.Common.CoordinateSystem import CoordinateSystem
