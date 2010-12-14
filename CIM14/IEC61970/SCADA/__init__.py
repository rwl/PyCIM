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

"""Contains entities to model information used by Supervisory Control and Data Acquisition (SCADA) applications. Supervisory control supports operator control of equipment, such as opening or closing a breaker. Data acquisition gathers telemetered data from various sources.  The subtypes of the Telemetry entity deliberately match the UCA and IEC 61850 definitions.  This package also supports alarm presentation but it is not expected to be used by other applications.
"""

nsPrefix = "cimSCADA"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#SCADA"

from CIM14.IEC61970.SCADA.RemotePoint import RemotePoint
from CIM14.IEC61970.SCADA.RemoteControl import RemoteControl
from CIM14.IEC61970.SCADA.RemoteUnit import RemoteUnit
from CIM14.IEC61970.SCADA.CommunicationLink import CommunicationLink
from CIM14.IEC61970.SCADA.RemoteSource import RemoteSource

class RemoteUnitType(str):
    """Type of remote unit.
    Values are: IED, ControlCenter, RTU, SubstationControlSystem
    """
    pass

class Source(str):
    """Source gives information related to the origin of a value.
    Values are: SUBSTITUTED, DEFAULTED, PROCESS
    """
    pass
