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

from entsoe.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_OperationalLimits"

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.
    """
    # <<< operational_limit
    # @generated
    def __init__(self, operational_limit_set=None, operational_limit_type=None, *args, **kw_args):
        """ Initialises a new 'OperationalLimit' instance.

        @param operational_limit_set: The limit set to which the limit values belong.
        @param operational_limit_type: The limit type associated with this limit.
        """

        self._operational_limit_set = None
        self.operational_limit_set = operational_limit_set

        self._operational_limit_type = None
        self.operational_limit_type = operational_limit_type


        super(OperationalLimit, self).__init__(*args, **kw_args)
    # >>> operational_limit

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



class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.
    """
    # <<< operational_limit_set
    # @generated
    def __init__(self, terminal=None, operational_limit_value=None, *args, **kw_args):
        """ Initialises a new 'OperationalLimitSet' instance.

        @param terminal: The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal.
        @param operational_limit_value: Values of equipment limits.
        """

        self._terminal = None
        self.terminal = terminal

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
        """ The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal.
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



class OperationalLimitType(IdentifiedObject):
    """ A type of limit.  The meaning of a specific limit is described in this class.
    """
    # <<< operational_limit_type
    # @generated
    def __init__(self, direction='high', acceptable_duration=0.0, operational_limit=None, *args, **kw_args):
        """ Initialises a new 'OperationalLimitType' instance.

        @param direction: The direction of the limit. Values are: "high", "absolute_value", "low"
        @param acceptable_duration: The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. 
        @param operational_limit: The operational limits associated with this type of limit.
        """
        # The direction of the limit. Values are: "high", "absolute_value", "low"
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



# <<< operational_limits
# @generated
# >>> operational_limits
