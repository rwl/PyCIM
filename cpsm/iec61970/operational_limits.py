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

""" The specificatoin of limits associated with equipment and other operational entities.
"""

from cpsm.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_OperationalLimits"

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.
    """
    # <<< operational_limit
    # @generated
    def __init__(self, type='', operational_limit_set=None, *args, **kw_args):
        """ Initialises a new 'OperationalLimit' instance.

        @param type: Used to specify high/low and limit levels. 
        @param operational_limit_set: The limit set to which the limit values belong.
        """
        # Used to specify high/low and limit levels. 
        self.type = type


        self._operational_limit_set = None
        self.operational_limit_set = operational_limit_set


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



class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.
    """
    # <<< operational_limit_set
    # @generated
    def __init__(self, equipment=None, operational_limit_value=None, *args, **kw_args):
        """ Initialises a new 'OperationalLimitSet' instance.

        @param equipment: The equpment to which the limit set applies.
        @param operational_limit_value: Values of equipment limits.
        """

        self._equipment = None
        self.equipment = equipment

        self._operational_limit_value = []
        if operational_limit_value is not None:
            self.operational_limit_value = operational_limit_value
        else:
            self.operational_limit_value = []


        super(OperationalLimitSet, self).__init__(*args, **kw_args)
    # >>> operational_limit_set

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



class CurrentLimit(OperationalLimit):
    """ OIoeratuibak kimit on current.
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
