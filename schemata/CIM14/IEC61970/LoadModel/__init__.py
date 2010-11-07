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

"""This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""

nsPrefix = "cimLoadModel"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#LoadModel"

from CIM14.IEC61970.LoadModel.PowerCutZone import PowerCutZone
from CIM14.IEC61970.LoadModel.LoadResponseCharacteristic import LoadResponseCharacteristic
from CIM14.IEC61970.LoadModel.EnergyArea import EnergyArea
from CIM14.IEC61970.LoadModel.LoadArea import LoadArea
from CIM14.IEC61970.LoadModel.StationSupply import StationSupply
from CIM14.IEC61970.LoadModel.SubLoadArea import SubLoadArea
from CIM14.IEC61970.LoadModel.LoadGroup import LoadGroup
from CIM14.IEC61970.LoadModel.NonConformLoadGroup import NonConformLoadGroup
from CIM14.IEC61970.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule
from CIM14.IEC61970.LoadModel.Season import Season
from CIM14.IEC61970.LoadModel.ConformLoadSchedule import ConformLoadSchedule
from CIM14.IEC61970.LoadModel.NonConformLoad import NonConformLoad
from CIM14.IEC61970.LoadModel.ConformLoad import ConformLoad
from CIM14.IEC61970.LoadModel.NonConformLoadSchedule import NonConformLoadSchedule
from CIM14.IEC61970.LoadModel.DayType import DayType
from CIM14.IEC61970.LoadModel.ConformLoadGroup import ConformLoadGroup

