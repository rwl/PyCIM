#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

""" This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.Core import PowerSystemResource
from CIM.Core import IdentifiedObject
from CIM.Wires import EnergyConsumer
from CIM import Element
from CIM.Core import RegularIntervalSchedule
from CIM.Domain import PerCent
from CIM.Domain import CurrentFlow



from enthought.traits.api import Instance, List, Property, Enum, Float, Bool, Date
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Name of season
SeasonName = Enum("winter", "summer", "fall", "spring", desc="Name of season")

#------------------------------------------------------------------------------
#  "PowerCutZone" class:
#------------------------------------------------------------------------------

class PowerCutZone(PowerSystemResource):
    """ An area or zone of the power system which is used for load shedding purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An energy consumer is assigned to a power cut zone
    EnergyConsumers = List(Instance("CIM.Wires.EnergyConsumer"),
        desc="An energy consumer is assigned to a power cut zone")

    # Second level (amount) of load to cut as a percentage of total zone load
    cutLevel2 = PerCent(desc="Second level (amount) of load to cut as a percentage of total zone load")

    # First level (amount) of load to cut as a percentage of total zone load
    cutLevel1 = PerCent(desc="First level (amount) of load to cut as a percentage of total zone load")

    #--------------------------------------------------------------------------
    #  Begin "PowerCutZone" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "cutLevel2", "cutLevel1",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "EnergyConsumers",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.PowerCutZone",
        title="PowerCutZone",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerCutZone" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadResponseCharacteristic" class:
#------------------------------------------------------------------------------

class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The set of loads that have the response characteristics.
    EnergyConsumer = List(Instance("CIM.Wires.EnergyConsumer"),
        desc="The set of loads that have the response characteristics.")

    # Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantPower = Float(desc="Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.")

    # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.
    qVoltageExponent = Float(desc="Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.")

    # Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantCurrent = Float(desc="Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.")

    # Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantImpedance = Float(desc="Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.")

    # Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used.
    exponentModel = Bool(desc="Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used.")

    # Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantCurrent = Float(desc="Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.")

    # Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantPower = Float(desc="Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.")

    # Exponent of per unit frequency effecting reactive power
    qFrequencyExponent = Float(desc="Exponent of per unit frequency effecting reactive power")

    # Exponent of per unit frequency effecting active power
    pFrequencyExponent = Float(desc="Exponent of per unit frequency effecting active power")

    # Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantImpedance = Float(desc="Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.")

    # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.
    pVoltageExponent = Float(desc="Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.")

    #--------------------------------------------------------------------------
    #  Begin "LoadResponseCharacteristic" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "pConstantPower", "qVoltageExponent", "pConstantCurrent", "qConstantImpedance", "exponentModel", "qConstantCurrent", "qConstantPower", "qFrequencyExponent", "pFrequencyExponent", "pConstantImpedance", "pVoltageExponent",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "EnergyConsumer",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.LoadResponseCharacteristic",
        title="LoadResponseCharacteristic",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadResponseCharacteristic" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergyArea" class:
#------------------------------------------------------------------------------

class EnergyArea(IdentifiedObject):
    """ The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The control area specification that is used for the load forecast.
    ControlArea = Instance("CIM.ControlArea.ControlArea",
        desc="The control area specification that is used for the load forecast.",
        transient=True,
        opposite="EnergyArea",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    #--------------------------------------------------------------------------
    #  Begin "EnergyArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.EnergyArea",
        title="EnergyArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StationSupply" class:
#------------------------------------------------------------------------------

class StationSupply(EnergyConsumer):
    """ Station supply with load derived from the station output.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "StationSupply" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "qfixedPct", "pfixedPct", "pfixed", "customerCount", "qfixed",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "LoadResponse", "PowerCutZone",
                label="References", columns=1),
            dock="tab"),
        id="CIM.LoadModel.StationSupply",
        title="StationSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StationSupply" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoad" class:
#------------------------------------------------------------------------------

class ConformLoad(EnergyConsumer):
    """ ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Group of this ConformLoad.
    LoadGroup = Instance("CIM.LoadModel.ConformLoadGroup",
        desc="Group of this ConformLoad.",
        transient=True,
        opposite="EnergyConsumers",
        editor=InstanceEditor(name="_conformloadgroups"))

    def _get_conformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.LoadModel.ConformLoadGroup" ]
        else:
            return []

    _conformloadgroups = Property(fget=_get_conformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "ConformLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "qfixedPct", "pfixedPct", "pfixed", "customerCount", "qfixed",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "LoadResponse", "PowerCutZone", "LoadGroup",
                label="References", columns=1),
            dock="tab"),
        id="CIM.LoadModel.ConformLoad",
        title="ConformLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonConformLoad" class:
#------------------------------------------------------------------------------

class NonConformLoad(EnergyConsumer):
    """ NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Group of this ConformLoad.
    LoadGroup = Instance("CIM.LoadModel.NonConformLoadGroup",
        desc="Group of this ConformLoad.",
        transient=True,
        opposite="EnergyConsumers",
        editor=InstanceEditor(name="_nonconformloadgroups"))

    def _get_nonconformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.LoadModel.NonConformLoadGroup" ]
        else:
            return []

    _nonconformloadgroups = Property(fget=_get_nonconformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "qfixedPct", "pfixedPct", "pfixed", "customerCount", "qfixed",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "LoadResponse", "PowerCutZone", "LoadGroup",
                label="References", columns=1),
            dock="tab"),
        id="CIM.LoadModel.NonConformLoad",
        title="NonConformLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonConformLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadGroup" class:
#------------------------------------------------------------------------------

class LoadGroup(IdentifiedObject):
    """ The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The SubLoadArea where the Loadgroup belongs.
    SubLoadArea = Instance("CIM.LoadModel.SubLoadArea",
        desc="The SubLoadArea where the Loadgroup belongs.",
        transient=True,
        opposite="LoadGroups",
        editor=InstanceEditor(name="_subloadareas"))

    def _get_subloadareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.LoadModel.SubLoadArea" ]
        else:
            return []

    _subloadareas = Property(fget=_get_subloadareas)

    #--------------------------------------------------------------------------
    #  Begin "LoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "SubLoadArea",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.LoadGroup",
        title="LoadGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Season" class:
#------------------------------------------------------------------------------

class Season(Element):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Schedules that use this Season.
    SeasonDayTypeSchedules = List(Instance("CIM.LoadModel.SeasonDayTypeSchedule"),
        desc="Schedules that use this Season.")

    # Name of the Season
    name = SeasonName(desc="Name of the Season")

    # Date season ends
    endDate = Date(desc="Date season ends")

    # Date season starts
    startDate = Date(desc="Date season starts")

    #--------------------------------------------------------------------------
    #  Begin "Season" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "name", "endDate", "startDate",
                label="Attributes"),
            VGroup("SeasonDayTypeSchedules",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.Season",
        title="Season",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Season" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SeasonDayTypeSchedule" class:
#------------------------------------------------------------------------------

class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """ The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # DayType for the Schedule.
    DayType = Instance("CIM.LoadModel.DayType",
        desc="DayType for the Schedule.",
        transient=True,
        opposite="SeasonDayTypeSchedules",
        editor=InstanceEditor(name="_daytypes"))

    def _get_daytypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.LoadModel.DayType" ]
        else:
            return []

    _daytypes = Property(fget=_get_daytypes)

    # Season for the Schedule.
    Season = Instance("CIM.LoadModel.Season",
        desc="Season for the Schedule.",
        transient=True,
        opposite="SeasonDayTypeSchedules",
        editor=InstanceEditor(name="_seasons"))

    def _get_seasons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.LoadModel.Season" ]
        else:
            return []

    _seasons = Property(fget=_get_seasons)

    #--------------------------------------------------------------------------
    #  Begin "SeasonDayTypeSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "value1Unit", "value2Multiplier", "value1Multiplier", "value2Unit", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "TimePoints", "DayType", "Season",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.SeasonDayTypeSchedule",
        title="SeasonDayTypeSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SeasonDayTypeSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DayType" class:
#------------------------------------------------------------------------------

class DayType(IdentifiedObject):
    """ Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Schedules that use this DayType.
    SeasonDayTypeSchedules = List(Instance("CIM.LoadModel.SeasonDayTypeSchedule"),
        desc="Schedules that use this DayType.")

    #--------------------------------------------------------------------------
    #  Begin "DayType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "SeasonDayTypeSchedules",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.DayType",
        title="DayType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DayType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadArea" class:
#------------------------------------------------------------------------------

class LoadArea(EnergyArea):
    """ The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The SubLoadAreas in the LoadArea.
    SubLoadAreas = List(Instance("CIM.LoadModel.SubLoadArea"),
        desc="The SubLoadAreas in the LoadArea.")

    #--------------------------------------------------------------------------
    #  Begin "LoadArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "ControlArea", "SubLoadAreas",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.LoadArea",
        title="LoadArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SubLoadArea" class:
#------------------------------------------------------------------------------

class SubLoadArea(EnergyArea):
    """ The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The LoadArea where the SubLoadArea belongs.
    LoadArea = Instance("CIM.LoadModel.LoadArea",
        desc="The LoadArea where the SubLoadArea belongs.",
        transient=True,
        opposite="SubLoadAreas",
        editor=InstanceEditor(name="_loadareas"))

    def _get_loadareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.LoadModel.LoadArea" ]
        else:
            return []

    _loadareas = Property(fget=_get_loadareas)

    # The Loadgroups in the SubLoadArea.
    LoadGroups = List(Instance("CIM.LoadModel.LoadGroup"),
        desc="The Loadgroups in the SubLoadArea.")

    #--------------------------------------------------------------------------
    #  Begin "SubLoadArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "ControlArea", "LoadArea", "LoadGroups",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.SubLoadArea",
        title="SubLoadArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubLoadArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Load" class:
#------------------------------------------------------------------------------

class Load(ConformLoad):
    """ A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The rated individual phase current.
    phaseRatedCurrent = CurrentFlow(desc="The rated individual phase current.")

    # The feeder's contribution to load management.
    feederLoadMgtFactor = PerCent(desc="The feeder's contribution to load management.")

    # The amount of nominal feeder active power that is picked up cold.
    coldPickUpFactorP = PerCent(desc="The amount of nominal feeder active power that is picked up cold.")

    # Permit assignment of loads on a participation factor basis. Given three equivalent loads with factors of 10, 25 and 15, a feeder load of 100 amps could be allocated on the feeder as 20, 50 and 30 amps.
    loadAllocationFactor = Float(desc="Permit assignment of loads on a participation factor basis. Given three equivalent loads with factors of 10, 25 and 15, a feeder load of 100 amps could be allocated on the feeder as 20, 50 and 30 amps.")

    # The amount of nominal feeder reactive power that is picked up cold.
    coldPickUpFactorQ = PerCent(desc="The amount of nominal feeder reactive power that is picked up cold.")

    #--------------------------------------------------------------------------
    #  Begin "Load" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "qfixedPct", "pfixedPct", "pfixed", "customerCount", "qfixed", "phaseRatedCurrent", "feederLoadMgtFactor", "coldPickUpFactorP", "loadAllocationFactor", "coldPickUpFactorQ",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "LoadResponse", "PowerCutZone", "LoadGroup",
                label="References", columns=1),
            dock="tab"),
        id="CIM.LoadModel.Load",
        title="Load",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Load" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "InductionMotorLoad" class:
#------------------------------------------------------------------------------

class InductionMotorLoad(NonConformLoad):
    """ Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "InductionMotorLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "qfixedPct", "pfixedPct", "pfixed", "customerCount", "qfixed",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "LoadResponse", "PowerCutZone", "LoadGroup",
                label="References", columns=1),
            dock="tab"),
        id="CIM.LoadModel.InductionMotorLoad",
        title="InductionMotorLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "InductionMotorLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonConformLoadGroup" class:
#------------------------------------------------------------------------------

class NonConformLoadGroup(LoadGroup):
    """ Loads that do not follow a daily and seasonal load variation pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The NonConformLoadSchedules in the NonConformLoadGroup.
    NonConformLoadSchedules = List(Instance("CIM.LoadModel.NonConformLoadSchedule"),
        desc="The NonConformLoadSchedules in the NonConformLoadGroup.")

    # Conform loads assigned to this ConformLoadGroup.
    EnergyConsumers = List(Instance("CIM.LoadModel.NonConformLoad"),
        desc="Conform loads assigned to this ConformLoadGroup.")

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "SubLoadArea", "NonConformLoadSchedules", "EnergyConsumers",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.NonConformLoadGroup",
        title="NonConformLoadGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoadSchedule" class:
#------------------------------------------------------------------------------

class ConformLoadSchedule(SeasonDayTypeSchedule):
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The ConformLoadGroup where the ConformLoadSchedule belongs.
    ConformLoadGroup = Instance("CIM.LoadModel.ConformLoadGroup",
        desc="The ConformLoadGroup where the ConformLoadSchedule belongs.",
        transient=True,
        opposite="ConformLoadSchedules",
        editor=InstanceEditor(name="_conformloadgroups"))

    def _get_conformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.LoadModel.ConformLoadGroup" ]
        else:
            return []

    _conformloadgroups = Property(fget=_get_conformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "ConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "value1Unit", "value2Multiplier", "value1Multiplier", "value2Unit", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "TimePoints", "DayType", "Season", "ConformLoadGroup",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.ConformLoadSchedule",
        title="ConformLoadSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonConformLoadSchedule" class:
#------------------------------------------------------------------------------

class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """ An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The NonConformLoadGroup where the NonConformLoadSchedule belongs.
    NonConformLoadGroup = Instance("CIM.LoadModel.NonConformLoadGroup",
        desc="The NonConformLoadGroup where the NonConformLoadSchedule belongs.",
        transient=True,
        opposite="NonConformLoadSchedules",
        editor=InstanceEditor(name="_nonconformloadgroups"))

    def _get_nonconformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.LoadModel.NonConformLoadGroup" ]
        else:
            return []

    _nonconformloadgroups = Property(fget=_get_nonconformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "value1Unit", "value2Multiplier", "value1Multiplier", "value2Unit", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "TimePoints", "DayType", "Season", "NonConformLoadGroup",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.NonConformLoadSchedule",
        title="NonConformLoadSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CustomerLoad" class:
#------------------------------------------------------------------------------

class CustomerLoad(ConformLoad):
    """ A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "CustomerLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "qfixedPct", "pfixedPct", "pfixed", "customerCount", "qfixed",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "LoadResponse", "PowerCutZone", "LoadGroup",
                label="References", columns=1),
            dock="tab"),
        id="CIM.LoadModel.CustomerLoad",
        title="CustomerLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CustomerLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoadGroup" class:
#------------------------------------------------------------------------------

class ConformLoadGroup(LoadGroup):
    """ Load that follows a daily and seasonal load variation pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The ConformLoadSchedules in the ConformLoadGroup.
    ConformLoadSchedules = List(Instance("CIM.LoadModel.ConformLoadSchedule"),
        desc="The ConformLoadSchedules in the ConformLoadGroup.")

    # Conform loads assigned to this ConformLoadGroup.
    EnergyConsumers = List(Instance("CIM.LoadModel.ConformLoad"),
        desc="Conform loads assigned to this ConformLoadGroup.")

    #--------------------------------------------------------------------------
    #  Begin "ConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "SubLoadArea", "ConformLoadSchedules", "EnergyConsumers",
                label="References"),
            dock="tab"),
        id="CIM.LoadModel.ConformLoadGroup",
        title="ConformLoadGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
