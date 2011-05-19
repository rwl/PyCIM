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

from CIM15.IEC61970.Generation.Production.Reservoir import Reservoir
from CIM15.IEC61970.Generation.Production.CogenerationPlant import CogenerationPlant
from CIM15.IEC61970.Generation.Production.GenUnitOpSchedule import GenUnitOpSchedule
from CIM15.IEC61970.Generation.Production.FuelAllocationSchedule import FuelAllocationSchedule
from CIM15.IEC61970.Generation.Production.GrossToNetActivePowerCurve import GrossToNetActivePowerCurve
from CIM15.IEC61970.Generation.Production.LevelVsVolumeCurve import LevelVsVolumeCurve
from CIM15.IEC61970.Generation.Production.StartRampCurve import StartRampCurve
from CIM15.IEC61970.Generation.Production.NuclearGeneratingUnit import NuclearGeneratingUnit
from CIM15.IEC61970.Generation.Production.EmissionCurve import EmissionCurve
from CIM15.IEC61970.Generation.Production.HydroPumpOpSchedule import HydroPumpOpSchedule
from CIM15.IEC61970.Generation.Production.SteamSendoutSchedule import SteamSendoutSchedule
from CIM15.IEC61970.Generation.Production.TargetLevelSchedule import TargetLevelSchedule
from CIM15.IEC61970.Generation.Production.CombinedCyclePlant import CombinedCyclePlant
from CIM15.IEC61970.Generation.Production.HeatRateCurve import HeatRateCurve
from CIM15.IEC61970.Generation.Production.ThermalGeneratingUnit import ThermalGeneratingUnit
from CIM15.IEC61970.Generation.Production.EmissionAccount import EmissionAccount
from CIM15.IEC61970.Generation.Production.PenstockLossCurve import PenstockLossCurve
from CIM15.IEC61970.Generation.Production.StartupModel import StartupModel
from CIM15.IEC61970.Generation.Production.HydroGeneratingUnit import HydroGeneratingUnit
from CIM15.IEC61970.Generation.Production.GenUnitOpCostCurve import GenUnitOpCostCurve
from CIM15.IEC61970.Generation.Production.IncrementalHeatRateCurve import IncrementalHeatRateCurve
from CIM15.IEC61970.Generation.Production.FossilFuel import FossilFuel
from CIM15.IEC61970.Generation.Production.GeneratingUnit import GeneratingUnit
from CIM15.IEC61970.Generation.Production.StartIgnFuelCurve import StartIgnFuelCurve
from CIM15.IEC61970.Generation.Production.StartMainFuelCurve import StartMainFuelCurve
from CIM15.IEC61970.Generation.Production.TailbayLossCurve import TailbayLossCurve
from CIM15.IEC61970.Generation.Production.HydroPump import HydroPump
from CIM15.IEC61970.Generation.Production.InflowForecast import InflowForecast
from CIM15.IEC61970.Generation.Production.HydroGeneratingEfficiencyCurve import HydroGeneratingEfficiencyCurve
from CIM15.IEC61970.Generation.Production.ShutdownCurve import ShutdownCurve
from CIM15.IEC61970.Generation.Production.HydroPowerPlant import HydroPowerPlant
from CIM15.IEC61970.Generation.Production.CAESPlant import CAESPlant
from CIM15.IEC61970.Generation.Production.AirCompressor import AirCompressor
from CIM15.IEC61970.Generation.Production.HeatInputCurve import HeatInputCurve
from CIM15.IEC61970.Generation.Production.WindGeneratingUnit import WindGeneratingUnit

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#Production"
nsPrefix = "cimProduction"


class FuelType(str):
    """Values are: oil, coal, lignite, gas
    """
    pass

class GeneratorOperatingMode(str):
    """Values are: MRN, EDC, LFC, fixed, REG, AGC, manual, off
    """
    pass

class GeneratorControlMode(str):
    """Values are: setpoint, pulse
    """
    pass

class HydroPlantType(str):
    """Values are: pumpedStorage, runOfRiver, minorStorage, majorStorage
    """
    pass

class HydroEnergyConversionKind(str):
    """Values are: generator, pumpAndGenerator
    """
    pass

class PenstockType(str):
    pass

class EmissionValueSource(str):
    """Values are: calculated, measured
    """
    pass

class GeneratorControlSource(str):
    """Values are: plantControl, offAGC, unavailable, onAGC
    """
    pass

class SpillwayGateType(str):
    pass

class SurgeTankCode(str):
    pass

class EmissionType(str):
    """Values are: carbonDisulfide, sulfurDioxide, hydrogenSulfide, chlorine, carbonDioxide, nitrogenOxide
    """
    pass

class Classification(str):
    """1..n, with 1 the most detailed, highest priority, etc.
    """
    pass

class HeatRate(float):
    """Heat generated, in energy pertime unit of elapsed time
    """
    pass

class CostPerHeatUnit(float):
    """Cost, in units of currency, per quantity of heat generated
    """
    pass

class Emission(float):
    """Quantity of emission per fuel heat content
    """
    pass
