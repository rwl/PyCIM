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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class StartupModel(IdentifiedObject):
    """Unit start up characteristics depending on how long the unit has been off line
    """

    def __init__(self, incrementalMaintCost=0.0, startupDate='', startupCost=0.0, stbyAuxP=0.0, startupPriority=0, fixedMaintCost=0.0, minimumDownTime=0.0, riskFactorCost=0.0, minimumRunTime=0.0, hotStandbyHeat=0.0, StartMainFuelCurve=None, StartIgnFuelCurve=None, StartRampCurve=None, ThermalGeneratingUnit=None, **kw_args):
        """Initializes a new 'StartupModel' instance.

        @param incrementalMaintCost: Incremental Maintenance Cost 
        @param startupDate: The date and time of the most recent generating unit startup 
        @param startupCost: Total miscellaneous start up costs 
        @param stbyAuxP: The unit's auxiliary active power consumption to maintain standby mode 
        @param startupPriority: Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority. 
        @param fixedMaintCost: Fixed Maintenance Cost 
        @param minimumDownTime: The minimum number of hours the unit must be down before restart 
        @param riskFactorCost: The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit. 
        @param minimumRunTime: The minimum number of hours the unit must be operating before being allowed to shut down 
        @param hotStandbyHeat: The amount of heat input per time uint required for hot standby operation 
        @param StartMainFuelCurve: The unit's startup model may have a startup main fuel curve
        @param StartIgnFuelCurve: The unit's startup model may have a startup ignition fuel curve
        @param StartRampCurve: The unit's startup model may have a startup ramp curve
        @param ThermalGeneratingUnit: A thermal generating unit may have a startup model
        """
        #: Incremental Maintenance Cost
        self.incrementalMaintCost = incrementalMaintCost

        #: The date and time of the most recent generating unit startup
        self.startupDate = startupDate

        #: Total miscellaneous start up costs
        self.startupCost = startupCost

        #: The unit's auxiliary active power consumption to maintain standby mode
        self.stbyAuxP = stbyAuxP

        #: Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority.
        self.startupPriority = startupPriority

        #: Fixed Maintenance Cost
        self.fixedMaintCost = fixedMaintCost

        #: The minimum number of hours the unit must be down before restart
        self.minimumDownTime = minimumDownTime

        #: The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit.
        self.riskFactorCost = riskFactorCost

        #: The minimum number of hours the unit must be operating before being allowed to shut down
        self.minimumRunTime = minimumRunTime

        #: The amount of heat input per time uint required for hot standby operation
        self.hotStandbyHeat = hotStandbyHeat

        self._StartMainFuelCurve = None
        self.StartMainFuelCurve = StartMainFuelCurve

        self._StartIgnFuelCurve = None
        self.StartIgnFuelCurve = StartIgnFuelCurve

        self._StartRampCurve = None
        self.StartRampCurve = StartRampCurve

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(StartupModel, self).__init__(**kw_args)

    def getStartMainFuelCurve(self):
        """The unit's startup model may have a startup main fuel curve
        """
        return self._StartMainFuelCurve

    def setStartMainFuelCurve(self, value):
        if self._StartMainFuelCurve is not None:
            self._StartMainFuelCurve._StartupModel = None

        self._StartMainFuelCurve = value
        if self._StartMainFuelCurve is not None:
            self._StartMainFuelCurve._StartupModel = self

    StartMainFuelCurve = property(getStartMainFuelCurve, setStartMainFuelCurve)

    def getStartIgnFuelCurve(self):
        """The unit's startup model may have a startup ignition fuel curve
        """
        return self._StartIgnFuelCurve

    def setStartIgnFuelCurve(self, value):
        if self._StartIgnFuelCurve is not None:
            self._StartIgnFuelCurve._StartupModel = None

        self._StartIgnFuelCurve = value
        if self._StartIgnFuelCurve is not None:
            self._StartIgnFuelCurve._StartupModel = self

    StartIgnFuelCurve = property(getStartIgnFuelCurve, setStartIgnFuelCurve)

    def getStartRampCurve(self):
        """The unit's startup model may have a startup ramp curve
        """
        return self._StartRampCurve

    def setStartRampCurve(self, value):
        if self._StartRampCurve is not None:
            self._StartRampCurve._StartupModel = None

        self._StartRampCurve = value
        if self._StartRampCurve is not None:
            self._StartRampCurve._StartupModel = self

    StartRampCurve = property(getStartRampCurve, setStartRampCurve)

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have a startup model
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._StartupModel = None

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._StartupModel = self

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

