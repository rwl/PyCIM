# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

""" The ControlArea package models area specifications which can be used for a variety of purposes.  The package as a whole models potentially overlapping control area specifications for the purpose of actual generation control, load forecast area load capture, or powerflow based analysis.
"""

from cim14v13 import Element
from cim14v13.iec61970.core import PowerSystemResource

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimControlArea"

ns_uri = "http://iec.ch/TC57/CIM-generic#ControlArea"

class TieFlow(Element):
    """ A flow specification in terms of location and direction for a control area.
    """
    # <<< tie_flow
    # @generated
    def __init__(self, positive_flow_in=False, terminal=None, control_area=None, alt_tie_meas=None, *args, **kw_args):
        """ Initialises a new 'TieFlow' instance.

        @param positive_flow_in: The flow is positive into the terminal.  A flow is positive if it is an import into the control area. 
        @param terminal: The terminal to which this tie flow belongs.
        @param control_area: The control area of the tie flows.
        @param alt_tie_meas: The primary and alternate tie flow measurements associated with the tie flow.
        """
        # The flow is positive into the terminal.  A flow is positive if it is an import into the control area. 
        self.positive_flow_in = positive_flow_in


        self._terminal = None
        self.terminal = terminal

        self._control_area = None
        self.control_area = control_area

        self._alt_tie_meas = []
        if alt_tie_meas is not None:
            self.alt_tie_meas = alt_tie_meas
        else:
            self.alt_tie_meas = []


        super(TieFlow, self).__init__(*args, **kw_args)
    # >>> tie_flow

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal to which this tie flow belongs.
        """
        return self._terminal

    def set_terminal(self, value):
        if self._terminal is not None:
            filtered = [x for x in self.terminal.tie_flow if x != self]
            self._terminal._tie_flow = filtered

        self._terminal = value
        if self._terminal is not None:
            self._terminal._tie_flow.append(self)

    terminal = property(get_terminal, set_terminal)
    # >>> terminal

    # <<< control_area
    # @generated
    def get_control_area(self):
        """ The control area of the tie flows.
        """
        return self._control_area

    def set_control_area(self, value):
        if self._control_area is not None:
            filtered = [x for x in self.control_area.tie_flow if x != self]
            self._control_area._tie_flow = filtered

        self._control_area = value
        if self._control_area is not None:
            self._control_area._tie_flow.append(self)

    control_area = property(get_control_area, set_control_area)
    # >>> control_area

    # <<< alt_tie_meas
    # @generated
    def get_alt_tie_meas(self):
        """ The primary and alternate tie flow measurements associated with the tie flow.
        """
        return self._alt_tie_meas

    def set_alt_tie_meas(self, value):
        for x in self._alt_tie_meas:
            x._tie_flow = None
        for y in value:
            y._tie_flow = self
        self._alt_tie_meas = value

    alt_tie_meas = property(get_alt_tie_meas, set_alt_tie_meas)

    def add_alt_tie_meas(self, *alt_tie_meas):
        for obj in alt_tie_meas:
            obj._tie_flow = self
            self._alt_tie_meas.append(obj)

    def remove_alt_tie_meas(self, *alt_tie_meas):
        for obj in alt_tie_meas:
            obj._tie_flow = None
            self._alt_tie_meas.remove(obj)
    # >>> alt_tie_meas



class ControlArea(PowerSystemResource):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """
    # <<< control_area
    # @generated
    def __init__(self, type='interchange', p_tolerance=0.0, net_interchange=0.0, energy_area=None, control_area_generating_unit=None, tie_flow=None, *args, **kw_args):
        """ Initialises a new 'ControlArea' instance.

        @param type: The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. Values are: "interchange", "agc", "forecast"
        @param p_tolerance: Active power net interchange tolerance 
        @param net_interchange: The specified positive net interchange into the control area. 
        @param energy_area: The energy area that is forecast from this control area specification.
        @param control_area_generating_unit: The generating unit specificaitons for the control area.
        @param tie_flow: The tie flows associated with the control area.
        """
        # The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. Values are: "interchange", "agc", "forecast"
        self.type = type

        # Active power net interchange tolerance 
        self.p_tolerance = p_tolerance

        # The specified positive net interchange into the control area. 
        self.net_interchange = net_interchange


        self._energy_area = None
        self.energy_area = energy_area

        self._control_area_generating_unit = []
        if control_area_generating_unit is not None:
            self.control_area_generating_unit = control_area_generating_unit
        else:
            self.control_area_generating_unit = []

        self._tie_flow = []
        if tie_flow is not None:
            self.tie_flow = tie_flow
        else:
            self.tie_flow = []


        super(ControlArea, self).__init__(*args, **kw_args)
    # >>> control_area

    # <<< energy_area
    # @generated
    def get_energy_area(self):
        """ The energy area that is forecast from this control area specification.
        """
        return self._energy_area

    def set_energy_area(self, value):
        if self._energy_area is not None:
            self._energy_area._control_area = None

        self._energy_area = value
        if self._energy_area is not None:
            self._energy_area._control_area = self

    energy_area = property(get_energy_area, set_energy_area)
    # >>> energy_area

    # <<< control_area_generating_unit
    # @generated
    def get_control_area_generating_unit(self):
        """ The generating unit specificaitons for the control area.
        """
        return self._control_area_generating_unit

    def set_control_area_generating_unit(self, value):
        for x in self._control_area_generating_unit:
            x._control_area = None
        for y in value:
            y._control_area = self
        self._control_area_generating_unit = value

    control_area_generating_unit = property(get_control_area_generating_unit, set_control_area_generating_unit)

    def add_control_area_generating_unit(self, *control_area_generating_unit):
        for obj in control_area_generating_unit:
            obj._control_area = self
            self._control_area_generating_unit.append(obj)

    def remove_control_area_generating_unit(self, *control_area_generating_unit):
        for obj in control_area_generating_unit:
            obj._control_area = None
            self._control_area_generating_unit.remove(obj)
    # >>> control_area_generating_unit

    # <<< tie_flow
    # @generated
    def get_tie_flow(self):
        """ The tie flows associated with the control area.
        """
        return self._tie_flow

    def set_tie_flow(self, value):
        for x in self._tie_flow:
            x._control_area = None
        for y in value:
            y._control_area = self
        self._tie_flow = value

    tie_flow = property(get_tie_flow, set_tie_flow)

    def add_tie_flow(self, *tie_flow):
        for obj in tie_flow:
            obj._control_area = self
            self._tie_flow.append(obj)

    def remove_tie_flow(self, *tie_flow):
        for obj in tie_flow:
            obj._control_area = None
            self._tie_flow.remove(obj)
    # >>> tie_flow



class ControlAreaGeneratingUnit(Element):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """
    # <<< control_area_generating_unit
    # @generated
    def __init__(self, alt_generating_unit_meas=None, generating_unit=None, control_area=None, *args, **kw_args):
        """ Initialises a new 'ControlAreaGeneratingUnit' instance.

        @param alt_generating_unit_meas: The link to prioritized measurements for this GeneratingUnit.
        @param generating_unit: The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
        @param control_area: The parent control area for the generating unit specifications.
        """

        self._alt_generating_unit_meas = []
        if alt_generating_unit_meas is not None:
            self.alt_generating_unit_meas = alt_generating_unit_meas
        else:
            self.alt_generating_unit_meas = []

        self._generating_unit = None
        self.generating_unit = generating_unit

        self._control_area = None
        self.control_area = control_area


        super(ControlAreaGeneratingUnit, self).__init__(*args, **kw_args)
    # >>> control_area_generating_unit

    # <<< alt_generating_unit_meas
    # @generated
    def get_alt_generating_unit_meas(self):
        """ The link to prioritized measurements for this GeneratingUnit.
        """
        return self._alt_generating_unit_meas

    def set_alt_generating_unit_meas(self, value):
        for x in self._alt_generating_unit_meas:
            x._control_area_generating_unit = None
        for y in value:
            y._control_area_generating_unit = self
        self._alt_generating_unit_meas = value

    alt_generating_unit_meas = property(get_alt_generating_unit_meas, set_alt_generating_unit_meas)

    def add_alt_generating_unit_meas(self, *alt_generating_unit_meas):
        for obj in alt_generating_unit_meas:
            obj._control_area_generating_unit = self
            self._alt_generating_unit_meas.append(obj)

    def remove_alt_generating_unit_meas(self, *alt_generating_unit_meas):
        for obj in alt_generating_unit_meas:
            obj._control_area_generating_unit = None
            self._alt_generating_unit_meas.remove(obj)
    # >>> alt_generating_unit_meas

    # <<< generating_unit
    # @generated
    def get_generating_unit(self):
        """ The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
        """
        return self._generating_unit

    def set_generating_unit(self, value):
        if self._generating_unit is not None:
            filtered = [x for x in self.generating_unit.control_area_generating_unit if x != self]
            self._generating_unit._control_area_generating_unit = filtered

        self._generating_unit = value
        if self._generating_unit is not None:
            self._generating_unit._control_area_generating_unit.append(self)

    generating_unit = property(get_generating_unit, set_generating_unit)
    # >>> generating_unit

    # <<< control_area
    # @generated
    def get_control_area(self):
        """ The parent control area for the generating unit specifications.
        """
        return self._control_area

    def set_control_area(self, value):
        if self._control_area is not None:
            filtered = [x for x in self.control_area.control_area_generating_unit if x != self]
            self._control_area._control_area_generating_unit = filtered

        self._control_area = value
        if self._control_area is not None:
            self._control_area._control_area_generating_unit.append(self)

    control_area = property(get_control_area, set_control_area)
    # >>> control_area



class AltGeneratingUnitMeas(Element):
    """ A prioritized measurement to be used for the generating unit in the control area specificaiton.
    """
    # <<< alt_generating_unit_meas
    # @generated
    def __init__(self, priority=0, control_area_generating_unit=None, analog_value=None, *args, **kw_args):
        """ Initialises a new 'AltGeneratingUnitMeas' instance.

        @param priority: Priority of a measurement usage.   Lower numbers have first priority. 
        @param control_area_generating_unit: The control aread generating unit to which the prioritized measurement assignment is applied.
        @param analog_value: The specific analog value used as a source.
        """
        # Priority of a measurement usage.   Lower numbers have first priority. 
        self.priority = priority


        self._control_area_generating_unit = None
        self.control_area_generating_unit = control_area_generating_unit

        self._analog_value = None
        self.analog_value = analog_value


        super(AltGeneratingUnitMeas, self).__init__(*args, **kw_args)
    # >>> alt_generating_unit_meas

    # <<< control_area_generating_unit
    # @generated
    def get_control_area_generating_unit(self):
        """ The control aread generating unit to which the prioritized measurement assignment is applied.
        """
        return self._control_area_generating_unit

    def set_control_area_generating_unit(self, value):
        if self._control_area_generating_unit is not None:
            filtered = [x for x in self.control_area_generating_unit.alt_generating_unit_meas if x != self]
            self._control_area_generating_unit._alt_generating_unit_meas = filtered

        self._control_area_generating_unit = value
        if self._control_area_generating_unit is not None:
            self._control_area_generating_unit._alt_generating_unit_meas.append(self)

    control_area_generating_unit = property(get_control_area_generating_unit, set_control_area_generating_unit)
    # >>> control_area_generating_unit

    # <<< analog_value
    # @generated
    def get_analog_value(self):
        """ The specific analog value used as a source.
        """
        return self._analog_value

    def set_analog_value(self, value):
        if self._analog_value is not None:
            filtered = [x for x in self.analog_value.alt_generating_unit if x != self]
            self._analog_value._alt_generating_unit = filtered

        self._analog_value = value
        if self._analog_value is not None:
            self._analog_value._alt_generating_unit.append(self)

    analog_value = property(get_analog_value, set_analog_value)
    # >>> analog_value



class AltTieMeas(Element):
    """ A prioritized measurement to be used for the tie flow as part of the control area specification.
    """
    # <<< alt_tie_meas
    # @generated
    def __init__(self, priority=0, analog_value=None, tie_flow=None, *args, **kw_args):
        """ Initialises a new 'AltTieMeas' instance.

        @param priority: Priority of a measurement usage.   Lower numbers have first priority. 
        @param analog_value: The specific analog value used as a source.
        @param tie_flow: The tie flow of the alternate measurements.
        """
        # Priority of a measurement usage.   Lower numbers have first priority. 
        self.priority = priority


        self._analog_value = None
        self.analog_value = analog_value

        self._tie_flow = None
        self.tie_flow = tie_flow


        super(AltTieMeas, self).__init__(*args, **kw_args)
    # >>> alt_tie_meas

    # <<< analog_value
    # @generated
    def get_analog_value(self):
        """ The specific analog value used as a source.
        """
        return self._analog_value

    def set_analog_value(self, value):
        if self._analog_value is not None:
            filtered = [x for x in self.analog_value.alt_tie_meas if x != self]
            self._analog_value._alt_tie_meas = filtered

        self._analog_value = value
        if self._analog_value is not None:
            self._analog_value._alt_tie_meas.append(self)

    analog_value = property(get_analog_value, set_analog_value)
    # >>> analog_value

    # <<< tie_flow
    # @generated
    def get_tie_flow(self):
        """ The tie flow of the alternate measurements.
        """
        return self._tie_flow

    def set_tie_flow(self, value):
        if self._tie_flow is not None:
            filtered = [x for x in self.tie_flow.alt_tie_meas if x != self]
            self._tie_flow._alt_tie_meas = filtered

        self._tie_flow = value
        if self._tie_flow is not None:
            self._tie_flow._alt_tie_meas.append(self)

    tie_flow = property(get_tie_flow, set_tie_flow)
    # >>> tie_flow



# <<< control_area
# @generated
# >>> control_area
