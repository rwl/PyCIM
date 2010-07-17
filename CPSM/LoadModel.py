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

""" This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CPSM.Wires import EnergyConsumer
from CPSM.Core import IdentifiedObject
from CPSM import Element
from CPSM.Core import RegularIntervalSchedule



from enthought.traits.api import Instance, List, Property, Enum, Date, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


SeasonName = Enum("fall", "winter", "spring", "summer")

#------------------------------------------------------------------------------
#  "NonConformLoad" class:
#------------------------------------------------------------------------------

class NonConformLoad(EnergyConsumer):
    """ NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Group of this ConformLoad.Group of this ConformLoad.
    LoadGroup = Instance("CPSM.LoadModel.NonConformLoadGroup", allow_none=False,
        desc="Group of this ConformLoad.Group of this ConformLoad.",
        transient=True,
        opposite="EnergyConsumers",
        editor=InstanceEditor(name="_nonconformloadgroups"))

    def _get_nonconformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.LoadModel.NonConformLoadGroup" ]
        else:
            return []

    _nonconformloadgroups = Property(fget=_get_nonconformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "qfixedPct", "pfixed", "qfixed", "pfixedPct",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "LoadResponse", "LoadGroup",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.NonConformLoad",
        title="NonConformLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonConformLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DayType" class:
#------------------------------------------------------------------------------

class DayType(IdentifiedObject):
    """ Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Schedules that use this DayType.Schedules that use this DayType.
    SeasonDayTypeSchedules = List(Instance("CPSM.LoadModel.SeasonDayTypeSchedule"),
        desc="Schedules that use this DayType.Schedules that use this DayType.")

    #--------------------------------------------------------------------------
    #  Begin "DayType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "SeasonDayTypeSchedules",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.DayType",
        title="DayType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DayType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Season" class:
#------------------------------------------------------------------------------

class Season(Element):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, WinterA specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Schedules that use this Season.Schedules that use this Season.
    SeasonDayTypeSchedules = List(Instance("CPSM.LoadModel.SeasonDayTypeSchedule"),
        desc="Schedules that use this Season.Schedules that use this Season.")

    # Date season endsDate season ends
    endDate = Date(desc="Date season endsDate season ends")

    # Date season startsDate season starts
    startDate = Date(desc="Date season startsDate season starts")

    # Name of the SeasonName of the Season
    name = SeasonName(desc="Name of the SeasonName of the Season")

    #--------------------------------------------------------------------------
    #  Begin "Season" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "endDate", "startDate", "name",
                label="Attributes"),
            VGroup("Model", "SeasonDayTypeSchedules",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.Season",
        title="Season",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Season" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StationSupply" class:
#------------------------------------------------------------------------------

class StationSupply(EnergyConsumer):
    """ Station supply with load derived from the station output.Station supply with load derived from the station output.
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
            VGroup("URI", "pathName", "description", "aliasName", "name", "qfixedPct", "pfixed", "qfixed", "pfixedPct",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "LoadResponse",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.StationSupply",
        title="StationSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StationSupply" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SeasonDayTypeSchedule" class:
#------------------------------------------------------------------------------

class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """ The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # DayType for the Schedule.DayType for the Schedule.
    DayType = Instance("CPSM.LoadModel.DayType", allow_none=False,
        desc="DayType for the Schedule.DayType for the Schedule.",
        transient=True,
        opposite="SeasonDayTypeSchedules",
        editor=InstanceEditor(name="_daytypes"))

    def _get_daytypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.LoadModel.DayType" ]
        else:
            return []

    _daytypes = Property(fget=_get_daytypes)

    # Season for the Schedule.Season for the Schedule.
    Season = Instance("CPSM.LoadModel.Season", allow_none=False,
        desc="Season for the Schedule.Season for the Schedule.",
        transient=True,
        opposite="SeasonDayTypeSchedules",
        editor=InstanceEditor(name="_seasons"))

    def _get_seasons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.LoadModel.Season" ]
        else:
            return []

    _seasons = Property(fget=_get_seasons)

    #--------------------------------------------------------------------------
    #  Begin "SeasonDayTypeSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "startTime", "value1Unit", "value2Unit", "endTime", "timeStep",
                label="Attributes"),
            VGroup("Model", "TimePoints", "DayType", "Season",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.SeasonDayTypeSchedule",
        title="SeasonDayTypeSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SeasonDayTypeSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadGroup" class:
#------------------------------------------------------------------------------

class LoadGroup(IdentifiedObject):
    """ The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The SubLoadArea where the Loadgroup belongs.The SubLoadArea where the Loadgroup belongs.
    SubLoadArea = Instance("CPSM.LoadModel.SubLoadArea", allow_none=False,
        desc="The SubLoadArea where the Loadgroup belongs.The SubLoadArea where the Loadgroup belongs.",
        transient=True,
        opposite="LoadGroups",
        editor=InstanceEditor(name="_subloadareas"))

    def _get_subloadareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.LoadModel.SubLoadArea" ]
        else:
            return []

    _subloadareas = Property(fget=_get_subloadareas)

    #--------------------------------------------------------------------------
    #  Begin "LoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "SubLoadArea",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.LoadGroup",
        title="LoadGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergyArea" class:
#------------------------------------------------------------------------------

class EnergyArea(IdentifiedObject):
    """ The class describes an area having energy production or consumption. The class is the basis for further specialization.The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The control area specification that is used for the load forecast.The control area specification that is used for the load forecast.
    ControlArea = Instance("CPSM.ControlArea.ControlArea",
        desc="The control area specification that is used for the load forecast.The control area specification that is used for the load forecast.",
        transient=True,
        opposite="EnergyArea",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    #--------------------------------------------------------------------------
    #  Begin "EnergyArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "ControlArea",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.EnergyArea",
        title="EnergyArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadResponseCharacteristic" class:
#------------------------------------------------------------------------------

class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The set of loads that have the response characteristics.The set of loads that have the response characteristics.
    EnergyConsumer = List(Instance("CPSM.Wires.EnergyConsumer"),
        desc="The set of loads that have the response characteristics.The set of loads that have the response characteristics.")

    # Exponent of per unit frequency effecting active powerExponent of per unit frequency effecting active power
    pFrequencyExponent = Float(desc="Exponent of per unit frequency effecting active powerExponent of per unit frequency effecting active power")

    # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.
    qVoltageExponent = Float(desc="Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.")

    # Exponent of per unit frequency effecting reactive powerExponent of per unit frequency effecting reactive power
    qFrequencyExponent = Float(desc="Exponent of per unit frequency effecting reactive powerExponent of per unit frequency effecting reactive power")

    # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.
    pVoltageExponent = Float(desc="Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.")

    #--------------------------------------------------------------------------
    #  Begin "LoadResponseCharacteristic" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "pFrequencyExponent", "qVoltageExponent", "qFrequencyExponent", "pVoltageExponent",
                label="Attributes"),
            VGroup("Model", "EnergyConsumer",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.LoadResponseCharacteristic",
        title="LoadResponseCharacteristic",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadResponseCharacteristic" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoad" class:
#------------------------------------------------------------------------------

class ConformLoad(EnergyConsumer):
    """ ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Group of this ConformLoad.Group of this ConformLoad.
    LoadGroup = Instance("CPSM.LoadModel.ConformLoadGroup", allow_none=False,
        desc="Group of this ConformLoad.Group of this ConformLoad.",
        transient=True,
        opposite="EnergyConsumers",
        editor=InstanceEditor(name="_conformloadgroups"))

    def _get_conformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.LoadModel.ConformLoadGroup" ]
        else:
            return []

    _conformloadgroups = Property(fget=_get_conformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "ConformLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "qfixedPct", "pfixed", "qfixed", "pfixedPct",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "LoadResponse", "LoadGroup",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.ConformLoad",
        title="ConformLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonConformLoadGroup" class:
#------------------------------------------------------------------------------

class NonConformLoadGroup(LoadGroup):
    """ Loads that do not follow a daily and seasonal load variation pattern.Loads that do not follow a daily and seasonal load variation pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The NonConformLoadSchedules in the NonConformLoadGroup.The NonConformLoadSchedules in the NonConformLoadGroup.
    NonConformLoadSchedules = List(Instance("CPSM.LoadModel.NonConformLoadSchedule"),
        desc="The NonConformLoadSchedules in the NonConformLoadGroup.The NonConformLoadSchedules in the NonConformLoadGroup.")

    # Conform loads assigned to this ConformLoadGroup.Conform loads assigned to this ConformLoadGroup.
    EnergyConsumers = List(Instance("CPSM.LoadModel.NonConformLoad"),
        desc="Conform loads assigned to this ConformLoadGroup.Conform loads assigned to this ConformLoadGroup.")

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "SubLoadArea", "NonConformLoadSchedules", "EnergyConsumers",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.NonConformLoadGroup",
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
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The ConformLoadGroup where the ConformLoadSchedule belongs.The ConformLoadGroup where the ConformLoadSchedule belongs.
    ConformLoadGroup = Instance("CPSM.LoadModel.ConformLoadGroup", allow_none=False,
        desc="The ConformLoadGroup where the ConformLoadSchedule belongs.The ConformLoadGroup where the ConformLoadSchedule belongs.",
        transient=True,
        opposite="ConformLoadSchedules",
        editor=InstanceEditor(name="_conformloadgroups"))

    def _get_conformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.LoadModel.ConformLoadGroup" ]
        else:
            return []

    _conformloadgroups = Property(fget=_get_conformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "ConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "startTime", "value1Unit", "value2Unit", "endTime", "timeStep",
                label="Attributes"),
            VGroup("Model", "TimePoints", "DayType", "Season", "ConformLoadGroup",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.ConformLoadSchedule",
        title="ConformLoadSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CustomerLoad" class:
#------------------------------------------------------------------------------

class CustomerLoad(ConformLoad):
    """ A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.
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
            VGroup("URI", "pathName", "description", "aliasName", "name", "qfixedPct", "pfixed", "qfixed", "pfixedPct",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "LoadResponse", "LoadGroup",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.CustomerLoad",
        title="CustomerLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CustomerLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Load" class:
#------------------------------------------------------------------------------

class Load(ConformLoad):
    """ A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Load" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "qfixedPct", "pfixed", "qfixed", "pfixedPct",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "LoadResponse", "LoadGroup",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.Load",
        title="Load",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Load" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoadGroup" class:
#------------------------------------------------------------------------------

class ConformLoadGroup(LoadGroup):
    """ Load that follows a daily and seasonal load variation pattern.Load that follows a daily and seasonal load variation pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Conform loads assigned to this ConformLoadGroup.Conform loads assigned to this ConformLoadGroup.
    EnergyConsumers = List(Instance("CPSM.LoadModel.ConformLoad"),
        desc="Conform loads assigned to this ConformLoadGroup.Conform loads assigned to this ConformLoadGroup.")

    # The ConformLoadSchedules in the ConformLoadGroup.The ConformLoadSchedules in the ConformLoadGroup.
    ConformLoadSchedules = List(Instance("CPSM.LoadModel.ConformLoadSchedule"),
        desc="The ConformLoadSchedules in the ConformLoadGroup.The ConformLoadSchedules in the ConformLoadGroup.")

    #--------------------------------------------------------------------------
    #  Begin "ConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "SubLoadArea", "EnergyConsumers", "ConformLoadSchedules",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.ConformLoadGroup",
        title="ConformLoadGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadArea" class:
#------------------------------------------------------------------------------

class LoadArea(EnergyArea):
    """ The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The SubLoadAreas in the LoadArea.The SubLoadAreas in the LoadArea.
    SubLoadAreas = List(Instance("CPSM.LoadModel.SubLoadArea"),
        desc="The SubLoadAreas in the LoadArea.The SubLoadAreas in the LoadArea.")

    #--------------------------------------------------------------------------
    #  Begin "LoadArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "ControlArea", "SubLoadAreas",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.LoadArea",
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
    """ The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Loadgroups in the SubLoadArea.The Loadgroups in the SubLoadArea.
    LoadGroups = List(Instance("CPSM.LoadModel.LoadGroup"),
        desc="The Loadgroups in the SubLoadArea.The Loadgroups in the SubLoadArea.")

    # The LoadArea where the SubLoadArea belongs.The LoadArea where the SubLoadArea belongs.
    LoadArea = Instance("CPSM.LoadModel.LoadArea", allow_none=False,
        desc="The LoadArea where the SubLoadArea belongs.The LoadArea where the SubLoadArea belongs.",
        transient=True,
        opposite="SubLoadAreas",
        editor=InstanceEditor(name="_loadareas"))

    def _get_loadareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.LoadModel.LoadArea" ]
        else:
            return []

    _loadareas = Property(fget=_get_loadareas)

    #--------------------------------------------------------------------------
    #  Begin "SubLoadArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "ControlArea", "LoadGroups", "LoadArea",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.SubLoadArea",
        title="SubLoadArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubLoadArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonConformLoadSchedule" class:
#------------------------------------------------------------------------------

class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """ An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The NonConformLoadGroup where the NonConformLoadSchedule belongs.The NonConformLoadGroup where the NonConformLoadSchedule belongs.
    NonConformLoadGroup = Instance("CPSM.LoadModel.NonConformLoadGroup", allow_none=False,
        desc="The NonConformLoadGroup where the NonConformLoadSchedule belongs.The NonConformLoadGroup where the NonConformLoadSchedule belongs.",
        transient=True,
        opposite="NonConformLoadSchedules",
        editor=InstanceEditor(name="_nonconformloadgroups"))

    def _get_nonconformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.LoadModel.NonConformLoadGroup" ]
        else:
            return []

    _nonconformloadgroups = Property(fget=_get_nonconformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "startTime", "value1Unit", "value2Unit", "endTime", "timeStep",
                label="Attributes"),
            VGroup("Model", "TimePoints", "DayType", "Season", "NonConformLoadGroup",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.NonConformLoadSchedule",
        title="NonConformLoadSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "InductionMotorLoad" class:
#------------------------------------------------------------------------------

class InductionMotorLoad(NonConformLoad):
    """ Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).
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
            VGroup("URI", "pathName", "description", "aliasName", "name", "qfixedPct", "pfixed", "qfixed", "pfixedPct",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "LoadResponse", "LoadGroup",
                label="References"),
            dock="tab"),
        id="CPSM.LoadModel.InductionMotorLoad",
        title="InductionMotorLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "InductionMotorLoad" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
