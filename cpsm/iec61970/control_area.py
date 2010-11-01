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


from cpsm.iec61970.core import PowerSystemResource
from cpsm import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_ControlArea"

class ControlArea(PowerSystemResource):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """
    # <<< control_area
    # @generated
    def __init__(self, net_interchange=0.0, type='forecast', control_area_generating_unit=None, energy_area=None, tie_flow=None, *args, **kw_args):
        """ Initialises a new 'ControlArea' instance.

        @param net_interchange: The specified positive net interchange into the control area. 
        @param type: The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. Values are: "forecast", "interchange", "agc"
        @param control_area_generating_unit: The generating unit specificaitons for the control area.
        @param energy_area: The energy area that is forecast from this control area specification.
        @param tie_flow: The tie flows associated with the control area.
        """
        # The specified positive net interchange into the control area. 
        self.net_interchange = net_interchange

        # The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. Values are: "forecast", "interchange", "agc"
        self.type = type


        self._control_area_generating_unit = []
        if control_area_generating_unit is not None:
            self.control_area_generating_unit = control_area_generating_unit
        else:
            self.control_area_generating_unit = []

        self._energy_area = None
        self.energy_area = energy_area

        self._tie_flow = []
        if tie_flow is not None:
            self.tie_flow = tie_flow
        else:
            self.tie_flow = []


        super(ControlArea, self).__init__(*args, **kw_args)
    # >>> control_area

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



class TieFlow(Element):
    """ A flow specification in terms of location and direction for a control area.
    """
    # <<< tie_flow
    # @generated
    def __init__(self, positive_flow_in=False, control_area=None, *args, **kw_args):
        """ Initialises a new 'TieFlow' instance.

        @param positive_flow_in: The flow is positive into the terminal.  A flow is positive if it is an import into the control area. 
        @param control_area: The control area of the tie flows.
        """
        # The flow is positive into the terminal.  A flow is positive if it is an import into the control area. 
        self.positive_flow_in = positive_flow_in


        self._control_area = None
        self.control_area = control_area


        super(TieFlow, self).__init__(*args, **kw_args)
    # >>> tie_flow

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



class ControlAreaGeneratingUnit(Element):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """
    # <<< control_area_generating_unit
    # @generated
    def __init__(self, control_area=None, generating_unit=None, *args, **kw_args):
        """ Initialises a new 'ControlAreaGeneratingUnit' instance.

        @param control_area: The parent control area for the generating unit specifications.
        @param generating_unit: The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
        """

        self._control_area = None
        self.control_area = control_area

        self._generating_unit = None
        self.generating_unit = generating_unit


        super(ControlAreaGeneratingUnit, self).__init__(*args, **kw_args)
    # >>> control_area_generating_unit

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
# >>> control_area
