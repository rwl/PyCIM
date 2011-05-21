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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class StartupModel(IdentifiedObject):
    """Unit start up characteristics depending on how long the unit has been off line
    """

    def __init__(self, stbyAuxP=0.0, incrementalMaintCost=0.0, hotStandbyHeat=0.0, startupPriority=0, fixedMaintCost=0.0, startupDate='', minimumRunTime=0.0, startupCost=0.0, riskFactorCost=0.0, minimumDownTime=0.0, ThermalGeneratingUnit=None, StartRampCurve=None, StartMainFuelCurve=None, StartIgnFuelCurve=None, *args, **kw_args):
        """Initialises a new 'StartupModel' instance.

        @param stbyAuxP: The unit's auxiliary active power consumption to maintain standby mode 
        @param incrementalMaintCost: Incremental Maintenance Cost 
        @param hotStandbyHeat: The amount of heat input per time uint required for hot standby operation 
        @param startupPriority: Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority. 
        @param fixedMaintCost: Fixed Maintenance Cost 
        @param startupDate: The date and time of the most recent generating unit startup 
        @param minimumRunTime: The minimum number of hours the unit must be operating before being allowed to shut down 
        @param startupCost: Total miscellaneous start up costs 
        @param riskFactorCost: The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit. 
        @param minimumDownTime: The minimum number of hours the unit must be down before restart 
        @param ThermalGeneratingUnit: A thermal generating unit may have a startup model
        @param StartRampCurve: The unit's startup model may have a startup ramp curve
        @param StartMainFuelCurve: The unit's startup model may have a startup main fuel curve
        @param StartIgnFuelCurve: The unit's startup model may have a startup ignition fuel curve
        """
        #: The unit's auxiliary active power consumption to maintain standby mode
        self.stbyAuxP = stbyAuxP

        #: Incremental Maintenance Cost
        self.incrementalMaintCost = incrementalMaintCost

        #: The amount of heat input per time uint required for hot standby operation
        self.hotStandbyHeat = hotStandbyHeat

        #: Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority.
        self.startupPriority = startupPriority

        #: Fixed Maintenance Cost
        self.fixedMaintCost = fixedMaintCost

        #: The date and time of the most recent generating unit startup
        self.startupDate = startupDate

        #: The minimum number of hours the unit must be operating before being allowed to shut down
        self.minimumRunTime = minimumRunTime

        #: Total miscellaneous start up costs
        self.startupCost = startupCost

        #: The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit.
        self.riskFactorCost = riskFactorCost

        #: The minimum number of hours the unit must be down before restart
        self.minimumDownTime = minimumDownTime

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        self._StartRampCurve = None
        self.StartRampCurve = StartRampCurve

        self._StartMainFuelCurve = None
        self.StartMainFuelCurve = StartMainFuelCurve

        self._StartIgnFuelCurve = None
        self.StartIgnFuelCurve = StartIgnFuelCurve

        super(StartupModel, self).__init__(*args, **kw_args)

    _attrs = ["stbyAuxP", "incrementalMaintCost", "hotStandbyHeat", "startupPriority", "fixedMaintCost", "startupDate", "minimumRunTime", "startupCost", "riskFactorCost", "minimumDownTime"]
    _attr_types = {"stbyAuxP": float, "incrementalMaintCost": float, "hotStandbyHeat": float, "startupPriority": int, "fixedMaintCost": float, "startupDate": str, "minimumRunTime": float, "startupCost": float, "riskFactorCost": float, "minimumDownTime": float}
    _defaults = {"stbyAuxP": 0.0, "incrementalMaintCost": 0.0, "hotStandbyHeat": 0.0, "startupPriority": 0, "fixedMaintCost": 0.0, "startupDate": '', "minimumRunTime": 0.0, "startupCost": 0.0, "riskFactorCost": 0.0, "minimumDownTime": 0.0}
    _enums = {}
    _refs = ["ThermalGeneratingUnit", "StartRampCurve", "StartMainFuelCurve", "StartIgnFuelCurve"]
    _many_refs = []

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have a startup model
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._StartupModel = None

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit.StartupModel = None
            self._ThermalGeneratingUnit._StartupModel = self

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

    def getStartRampCurve(self):
        """The unit's startup model may have a startup ramp curve
        """
        return self._StartRampCurve

    def setStartRampCurve(self, value):
        if self._StartRampCurve is not None:
            self._StartRampCurve._StartupModel = None

        self._StartRampCurve = value
        if self._StartRampCurve is not None:
            self._StartRampCurve.StartupModel = None
            self._StartRampCurve._StartupModel = self

    StartRampCurve = property(getStartRampCurve, setStartRampCurve)

    def getStartMainFuelCurve(self):
        """The unit's startup model may have a startup main fuel curve
        """
        return self._StartMainFuelCurve

    def setStartMainFuelCurve(self, value):
        if self._StartMainFuelCurve is not None:
            self._StartMainFuelCurve._StartupModel = None

        self._StartMainFuelCurve = value
        if self._StartMainFuelCurve is not None:
            self._StartMainFuelCurve.StartupModel = None
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
            self._StartIgnFuelCurve.StartupModel = None
            self._StartIgnFuelCurve._StartupModel = self

    StartIgnFuelCurve = property(getStartIgnFuelCurve, setStartIgnFuelCurve)

