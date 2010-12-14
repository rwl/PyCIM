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


nsPrefix = "cimLoads"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Loads"

from CIM14.Dynamics.Loads.AggregateLoad import AggregateLoad
from CIM14.Dynamics.Loads.LoadStatic import LoadStatic
from CIM14.Dynamics.Loads.LoadStaticSystem import LoadStaticSystem
from CIM14.Dynamics.Loads.LoadStaticOwner import LoadStaticOwner
from CIM14.Dynamics.Loads.LoadStaticZone import LoadStaticZone
from CIM14.Dynamics.Loads.LoadStaticBus import LoadStaticBus
from CIM14.Dynamics.Loads.LoadStaticArea import LoadStaticArea
from CIM14.Dynamics.Loads.LoadMotor import LoadMotor

class StaticLoadType(str):
    """Type of static load
    Values are: ZIP1, exponential, ZIP2
    """
    pass
