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

""" The OperationalLimits package models a specification of limits associated with equipment and other operational entities.
"""

from cim14v13.iec61970.core import IdentifiedObject
from cim14v13 import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimOperationalLimits"

ns_uri = "http://iec.ch/TC57/CIM-generic#OperationalLimits"

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.
    """
    # <<< operational_limit
    # @generated
    def __init__(self, type='', operational_limit_type=None, operational_limit_set=None, *args, **kw_args):
        """ Initialises a new 'OperationalLimit' instance.

        @param type: Used to specify high/low and limit levels. 
        @param operational_limit_type: The limit type associated with this limit.
        @param operational_limit_set: The limit set to which the limit values belong.
        """
        # Used to specify high/low and limit levels. 
        self.type = type


        self._operational_limit_type = None
        self.operational_limit_type = operational_limit_type

        self._operational_limit_set = None
        self.operational_limit_set = operational_limit_set


        super(OperationalLimit, self).__init__(*args, **kw_args)
    # >>> operational_limit

    # <<< operational_limit_type
    # @generated
    def get_operational_limit_type(self):
        """ The limit type associated with this limit.
        """
        return self._operational_limit_type

    def set_operational_limit_type(self, value):
        if self._operational_limit_type is not None:
            filtered = [x for x in self.operational_limit_type.operational_limit if x != self]
            self._operational_limit_type._operational_limit = filtered

        self._operational_limit_type = value
        if self._operational_limit_type is not None:
            self._operational_limit_type._operational_limit.append(self)

    operational_limit_type = property(get_operational_limit_type, set_operational_limit_type)
    # >>> operational_limit_type

    # <<< operational_limit_set
    # @generated
    def get_operational_limit_set(self):
        """ The limit set to which the limit values belong.
        """
        return self._operational_limit_set

    def set_operational_limit_set(self, value):
        if self._operational_limit_set is not None:
            filtered = [x for x in self.operational_limit_set.operational_limit_value if x != self]
            self._operational_limit_set._operational_limit_value = filtered

        self._operational_limit_set = value
        if self._operational_limit_set is not None:
            self._operational_limit_set._operational_limit_value.append(self)

    operational_limit_set = property(get_operational_limit_set, set_operational_limit_set)
    # >>> operational_limit_set



class BranchGroup(IdentifiedObject):
    """ A group of branch terminals whose directed flow summation is to be monitored. Abranch group need not form a cutset of the network.
    """
    # <<< branch_group
    # @generated
    def __init__(self, maximum_active_power=0.0, monitor_reactive_power=False, minimum_active_power=0.0, minimum_reactive_power=0.0, monitor_active_power=False, maximum_reactive_power=0.0, branch_group_terminal=None, *args, **kw_args):
        """ Initialises a new 'BranchGroup' instance.

        @param maximum_active_power: The maximum active power flow. 
        @param monitor_reactive_power: Monitor the reactive power flow. 
        @param minimum_active_power: The minimum active power flow. 
        @param minimum_reactive_power: The minimum reactive power flow. 
        @param monitor_active_power: Monitor the active power flow. 
        @param maximum_reactive_power: The maximum reactive power flow. 
        @param branch_group_terminal: The directed branch group terminals to be summed.
        """
        # The maximum active power flow. 
        self.maximum_active_power = maximum_active_power

        # Monitor the reactive power flow. 
        self.monitor_reactive_power = monitor_reactive_power

        # The minimum active power flow. 
        self.minimum_active_power = minimum_active_power

        # The minimum reactive power flow. 
        self.minimum_reactive_power = minimum_reactive_power

        # Monitor the active power flow. 
        self.monitor_active_power = monitor_active_power

        # The maximum reactive power flow. 
        self.maximum_reactive_power = maximum_reactive_power


        self._branch_group_terminal = []
        if branch_group_terminal is not None:
            self.branch_group_terminal = branch_group_terminal
        else:
            self.branch_group_terminal = []


        super(BranchGroup, self).__init__(*args, **kw_args)
    # >>> branch_group

    # <<< branch_group_terminal
    # @generated
    def get_branch_group_terminal(self):
        """ The directed branch group terminals to be summed.
        """
        return self._branch_group_terminal

    def set_branch_group_terminal(self, value):
        for x in self._branch_group_terminal:
            x._branch_group = None
        for y in value:
            y._branch_group = self
        self._branch_group_terminal = value

    branch_group_terminal = property(get_branch_group_terminal, set_branch_group_terminal)

    def add_branch_group_terminal(self, *branch_group_terminal):
        for obj in branch_group_terminal:
            obj._branch_group = self
            self._branch_group_terminal.append(obj)

    def remove_branch_group_terminal(self, *branch_group_terminal):
        for obj in branch_group_terminal:
            obj._branch_group = None
            self._branch_group_terminal.remove(obj)
    # >>> branch_group_terminal



class BranchGroupTerminal(Element):
    """ A specific directed terminal flow for a branch group.
    """
    # <<< branch_group_terminal
    # @generated
    def __init__(self, positive_flow_in=False, branch_group=None, terminal=None, *args, **kw_args):
        """ Initialises a new 'BranchGroupTerminal' instance.

        @param positive_flow_in: The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false. 
        @param branch_group: The branch group to which the directed branch group terminals belong.
        @param terminal: The terminal to be summed.
        """
        # The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false. 
        self.positive_flow_in = positive_flow_in


        self._branch_group = None
        self.branch_group = branch_group

        self._terminal = None
        self.terminal = terminal


        super(BranchGroupTerminal, self).__init__(*args, **kw_args)
    # >>> branch_group_terminal

    # <<< branch_group
    # @generated
    def get_branch_group(self):
        """ The branch group to which the directed branch group terminals belong.
        """
        return self._branch_group

    def set_branch_group(self, value):
        if self._branch_group is not None:
            filtered = [x for x in self.branch_group.branch_group_terminal if x != self]
            self._branch_group._branch_group_terminal = filtered

        self._branch_group = value
        if self._branch_group is not None:
            self._branch_group._branch_group_terminal.append(self)

    branch_group = property(get_branch_group, set_branch_group)
    # >>> branch_group

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal to be summed.
        """
        return self._terminal

    def set_terminal(self, value):
        if self._terminal is not None:
            filtered = [x for x in self.terminal.branch_group_terminal if x != self]
            self._terminal._branch_group_terminal = filtered

        self._terminal = value
        if self._terminal is not None:
            self._terminal._branch_group_terminal.append(self)

    terminal = property(get_terminal, set_terminal)
    # >>> terminal



class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severities of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.
    """
    # <<< operational_limit_set
    # @generated
    def __init__(self, terminal=None, equipment=None, operational_limit_value=None, *args, **kw_args):
        """ Initialises a new 'OperationalLimitSet' instance.

        @param terminal: The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.
        @param equipment: The equpment to which the limit set applies.
        @param operational_limit_value: Values of equipment limits.
        """

        self._terminal = None
        self.terminal = terminal

        self._equipment = None
        self.equipment = equipment

        self._operational_limit_value = []
        if operational_limit_value is not None:
            self.operational_limit_value = operational_limit_value
        else:
            self.operational_limit_value = []


        super(OperationalLimitSet, self).__init__(*args, **kw_args)
    # >>> operational_limit_set

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.
        """
        return self._terminal

    def set_terminal(self, value):
        if self._terminal is not None:
            filtered = [x for x in self.terminal.operational_limit_set if x != self]
            self._terminal._operational_limit_set = filtered

        self._terminal = value
        if self._terminal is not None:
            self._terminal._operational_limit_set.append(self)

    terminal = property(get_terminal, set_terminal)
    # >>> terminal

    # <<< equipment
    # @generated
    def get_equipment(self):
        """ The equpment to which the limit set applies.
        """
        return self._equipment

    def set_equipment(self, value):
        if self._equipment is not None:
            filtered = [x for x in self.equipment.operational_limit_set if x != self]
            self._equipment._operational_limit_set = filtered

        self._equipment = value
        if self._equipment is not None:
            self._equipment._operational_limit_set.append(self)

    equipment = property(get_equipment, set_equipment)
    # >>> equipment

    # <<< operational_limit_value
    # @generated
    def get_operational_limit_value(self):
        """ Values of equipment limits.
        """
        return self._operational_limit_value

    def set_operational_limit_value(self, value):
        for x in self._operational_limit_value:
            x._operational_limit_set = None
        for y in value:
            y._operational_limit_set = self
        self._operational_limit_value = value

    operational_limit_value = property(get_operational_limit_value, set_operational_limit_value)

    def add_operational_limit_value(self, *operational_limit_value):
        for obj in operational_limit_value:
            obj._operational_limit_set = self
            self._operational_limit_value.append(obj)

    def remove_operational_limit_value(self, *operational_limit_value):
        for obj in operational_limit_value:
            obj._operational_limit_set = None
            self._operational_limit_value.remove(obj)
    # >>> operational_limit_value



class OperationalLimitType(Element):
    """ A type of limit.  The meaning of a specific limit is described in this class.
    """
    # <<< operational_limit_type
    # @generated
    def __init__(self, direction='absolute_value', acceptable_duration=0.0, operational_limit=None, *args, **kw_args):
        """ Initialises a new 'OperationalLimitType' instance.

        @param direction: The direction of the limit. Values are: "absolute_value", "high", "low"
        @param acceptable_duration: The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. 
        @param operational_limit: The operational limits associated with this type of limit.
        """
        # The direction of the limit. Values are: "absolute_value", "high", "low"
        self.direction = direction

        # The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. 
        self.acceptable_duration = acceptable_duration


        self._operational_limit = []
        if operational_limit is not None:
            self.operational_limit = operational_limit
        else:
            self.operational_limit = []


        super(OperationalLimitType, self).__init__(*args, **kw_args)
    # >>> operational_limit_type

    # <<< operational_limit
    # @generated
    def get_operational_limit(self):
        """ The operational limits associated with this type of limit.
        """
        return self._operational_limit

    def set_operational_limit(self, value):
        for x in self._operational_limit:
            x._operational_limit_type = None
        for y in value:
            y._operational_limit_type = self
        self._operational_limit = value

    operational_limit = property(get_operational_limit, set_operational_limit)

    def add_operational_limit(self, *operational_limit):
        for obj in operational_limit:
            obj._operational_limit_type = self
            self._operational_limit.append(obj)

    def remove_operational_limit(self, *operational_limit):
        for obj in operational_limit:
            obj._operational_limit_type = None
            self._operational_limit.remove(obj)
    # >>> operational_limit



class VoltageLimit(OperationalLimit):
    """ Operational limit applied to voltage.
    """
    # <<< voltage_limit
    # @generated
    def __init__(self, value=0.0, *args, **kw_args):
        """ Initialises a new 'VoltageLimit' instance.

        @param value: Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKind 
        """
        # Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKind 
        self.value = value



        super(VoltageLimit, self).__init__(*args, **kw_args)
    # >>> voltage_limit



class ApparentPowerLimit(OperationalLimit):
    """ Apparent power limit.
    """
    # <<< apparent_power_limit
    # @generated
    def __init__(self, value=0.0, *args, **kw_args):
        """ Initialises a new 'ApparentPowerLimit' instance.

        @param value: The apparent power limit. 
        """
        # The apparent power limit. 
        self.value = value



        super(ApparentPowerLimit, self).__init__(*args, **kw_args)
    # >>> apparent_power_limit



class ActivePowerLimit(OperationalLimit):
    """ Limit on active power flow.
    """
    # <<< active_power_limit
    # @generated
    def __init__(self, value=0.0, *args, **kw_args):
        """ Initialises a new 'ActivePowerLimit' instance.

        @param value: Value of active power limit. 
        """
        # Value of active power limit. 
        self.value = value



        super(ActivePowerLimit, self).__init__(*args, **kw_args)
    # >>> active_power_limit



class CurrentLimit(OperationalLimit):
    """ Operational limit on current.
    """
    # <<< current_limit
    # @generated
    def __init__(self, value=0.0, *args, **kw_args):
        """ Initialises a new 'CurrentLimit' instance.

        @param value: Limit on current flow. 
        """
        # Limit on current flow. 
        self.value = value



        super(CurrentLimit, self).__init__(*args, **kw_args)
    # >>> current_limit



# <<< operational_limits
# @generated
# >>> operational_limits
