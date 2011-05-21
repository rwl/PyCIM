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

"""The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.
"""

from CIM14.IEC61970.Generation.Production.LevelVsVolumeCurve import LevelVsVolumeCurve
from CIM14.IEC61970.Generation.Production.FossilFuel import FossilFuel
from CIM14.IEC61970.Generation.Production.SteamSendoutSchedule import SteamSendoutSchedule
from CIM14.IEC61970.Generation.Production.EmissionCurve import EmissionCurve
from CIM14.IEC61970.Generation.Production.CombinedCyclePlant import CombinedCyclePlant
from CIM14.IEC61970.Generation.Production.StartIgnFuelCurve import StartIgnFuelCurve
from CIM14.IEC61970.Generation.Production.HydroGeneratingEfficiencyCurve import HydroGeneratingEfficiencyCurve
from CIM14.IEC61970.Generation.Production.StartRampCurve import StartRampCurve
from CIM14.IEC61970.Generation.Production.GeneratingUnit import GeneratingUnit
from CIM14.IEC61970.Generation.Production.NuclearGeneratingUnit import NuclearGeneratingUnit
from CIM14.IEC61970.Generation.Production.WindGeneratingUnit import WindGeneratingUnit
from CIM14.IEC61970.Generation.Production.StartMainFuelCurve import StartMainFuelCurve
from CIM14.IEC61970.Generation.Production.StartupModel import StartupModel
from CIM14.IEC61970.Generation.Production.AirCompressor import AirCompressor
from CIM14.IEC61970.Generation.Production.HeatInputCurve import HeatInputCurve
from CIM14.IEC61970.Generation.Production.CogenerationPlant import CogenerationPlant
from CIM14.IEC61970.Generation.Production.ShutdownCurve import ShutdownCurve
from CIM14.IEC61970.Generation.Production.InflowForecast import InflowForecast
from CIM14.IEC61970.Generation.Production.HydroGeneratingUnit import HydroGeneratingUnit
from CIM14.IEC61970.Generation.Production.TargetLevelSchedule import TargetLevelSchedule
from CIM14.IEC61970.Generation.Production.EmissionAccount import EmissionAccount
from CIM14.IEC61970.Generation.Production.GrossToNetActivePowerCurve import GrossToNetActivePowerCurve
from CIM14.IEC61970.Generation.Production.HydroPumpOpSchedule import HydroPumpOpSchedule
from CIM14.IEC61970.Generation.Production.Reservoir import Reservoir
from CIM14.IEC61970.Generation.Production.CAESPlant import CAESPlant
from CIM14.IEC61970.Generation.Production.GenUnitOpCostCurve import GenUnitOpCostCurve
from CIM14.IEC61970.Generation.Production.PenstockLossCurve import PenstockLossCurve
from CIM14.IEC61970.Generation.Production.HydroPump import HydroPump
from CIM14.IEC61970.Generation.Production.GenUnitOpSchedule import GenUnitOpSchedule
from CIM14.IEC61970.Generation.Production.FuelAllocationSchedule import FuelAllocationSchedule
from CIM14.IEC61970.Generation.Production.HeatRateCurve import HeatRateCurve
from CIM14.IEC61970.Generation.Production.IncrementalHeatRateCurve import IncrementalHeatRateCurve
from CIM14.IEC61970.Generation.Production.ThermalGeneratingUnit import ThermalGeneratingUnit
from CIM14.IEC61970.Generation.Production.TailbayLossCurve import TailbayLossCurve
from CIM14.IEC61970.Generation.Production.HydroPowerPlant import HydroPowerPlant

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Production"
nsPrefix = "cimProduction"


class HydroPlantType(str):
    """The type of hydro power plant.
    Values are: runOfRiver, minorStorage, majorStorage, pumpedStorage
    """
    pass

class EmissionValueSource(str):
    """The source of the emission value.
    Values are: measured, calculated
    """
    pass

class GeneratorControlMode(str):
    """Unit control modes.
    Values are: setpoint, pulse
    """
    pass

class FuelType(str):
    """Type of fuel.
    Values are: lignite, coal, oil, gas
    """
    pass

class GeneratorControlSource(str):
    """The source of controls for a generating unit.
    Values are: unavailable, onAGC, plantControl, offAGC
    """
    pass

class HydroEnergyConversionKind(str):
    """Specifies the capability of the hydro generating unit to convert energy as a generator or pump.
    Values are: generator, pumpAndGenerator
    """
    pass

class SpillwayGateType(str):
    """Type of spillway gate.
    """
    pass

class SurgeTankCode(str):
    """Type (or absence) of surge tank that is associated with the hydro power plant.
    """
    pass

class EmissionType(str):
    """The type of emission
    Values are: chlorine, carbonDioxide, hydrogenSulfide, nitrogenOxide, sulfurDioxide, carbonDisulfide
    """
    pass

class GeneratorOperatingMode(str):
    """Operating mode for secondary generator control.
    Values are: fixed, EDC, manual, off, MRN, LFC, AGC, REG
    """
    pass

class PenstockType(str):
    """Type of hydro plant penstock.
    """
    pass

class Emission(float):
    """Quantity of emission per fuel heat content
    """
    pass

class HeatRate(float):
    """Heat generated, in energy pertime unit of elapsed time
    """
    pass

class Classification(int):
    """1..n, with 1 the most detailed, highest priority, etc.
    """
    pass

class CostPerHeatUnit(float):
    """Cost, in units of currency, per quantity of heat generated
    """
    pass
