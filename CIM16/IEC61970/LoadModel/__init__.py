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

"""This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""

from CIM16.IEC61970.LoadModel.ConformLoad import ConformLoad
from CIM16.IEC61970.LoadModel.ConformLoadGroup import ConformLoadGroup
from CIM16.IEC61970.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule
from CIM16.IEC61970.LoadModel.LoadGroup import LoadGroup
from CIM16.IEC61970.LoadModel.ConformLoadSchedule import ConformLoadSchedule
from CIM16.IEC61970.LoadModel.LoadArea import LoadArea
from CIM16.IEC61970.LoadModel.PowerCutZone import PowerCutZone
from CIM16.IEC61970.LoadModel.LoadResponseCharacteristic import LoadResponseCharacteristic
from CIM16.IEC61970.LoadModel.NonConformLoad import NonConformLoad
from CIM16.IEC61970.LoadModel.StationSupply import StationSupply
from CIM16.IEC61970.LoadModel.EnergyArea import EnergyArea
from CIM16.IEC61970.LoadModel.NonConformLoadSchedule import NonConformLoadSchedule
from CIM16.IEC61970.LoadModel.NonConformLoadGroup import NonConformLoadGroup
from CIM16.IEC61970.LoadModel.DayType import DayType
from CIM16.IEC61970.LoadModel.SubLoadArea import SubLoadArea
from CIM16.IEC61970.LoadModel.Season import Season

nsURI = "http://iec.ch/TC57/2013/CIM-schema-cim16#LoadModel"
nsPrefix = "cimLoadModel"


class SeasonName(str):
    """Values are: winter, summer, fall, spring
    """
    pass
