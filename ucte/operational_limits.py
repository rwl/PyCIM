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

""" The OperationalLimits package models a specification of limits associated with equipment and other operational entities.The OperationalLimits package models a specification of limits associated with equipment and other operational entities.
"""

from ucte.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_OperationalLimits"

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.A value associated with a specific kind of limit.
    """
    # <<< operational_limit
    # @generated
    def __init__(self, operational_limit_set=None, operational_limit_type=None, **kw_args):
        """ Initialises a new 'OperationalLimit' instance.
        """

        self._operational_limit_set = None
        self.operational_limit_set = operational_limit_set

        self._operational_limit_type = None
        self.operational_limit_type = operational_limit_type


        super(OperationalLimit, self).__init__(**kw_args)
    # >>> operational_limit

    # <<< operational_limit_set
    # @generated
    def get_operational_limit_set(self):
        """ The limit set to which the limit values belong.The limit set to which the limit values belong.
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
        """ The limit type associated with this limit.The limit type associated with this limit.
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


    def __str__(self):
        """ Returns a string representation of the OperationalLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< operational_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OperationalLimit.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OperationalLimit", self.uri)
        if format:
            indent += ' ' * depth

        if self.operational_limit_set is not None:
            s += '%s<%s:OperationalLimit.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operational_limit_set.uri)
        if self.operational_limit_type is not None:
            s += '%s<%s:OperationalLimit.operational_limit_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operational_limit_type.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OperationalLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> operational_limit.serialize


class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.
    """
    # <<< operational_limit_set
    # @generated
    def __init__(self, terminal=None, operational_limit_value=None, **kw_args):
        """ Initialises a new 'OperationalLimitSet' instance.
        """

        self._terminal = None
        self.terminal = terminal

        self._operational_limit_value = []
        if operational_limit_value is not None:
            self.operational_limit_value = operational_limit_value
        else:
            self.operational_limit_value = []


        super(OperationalLimitSet, self).__init__(**kw_args)
    # >>> operational_limit_set

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal.The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal.
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
        """ Values of equipment limits.Values of equipment limits.
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


    def __str__(self):
        """ Returns a string representation of the OperationalLimitSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< operational_limit_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OperationalLimitSet.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OperationalLimitSet", self.uri)
        if format:
            indent += ' ' * depth

        if self.terminal is not None:
            s += '%s<%s:OperationalLimitSet.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        for obj in self.operational_limit_value:
            s += '%s<%s:OperationalLimitSet.operational_limit_value rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OperationalLimitSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> operational_limit_set.serialize


class OperationalLimitType(IdentifiedObject):
    """ A type of limit.  The meaning of a specific limit is described in this class.A type of limit.  The meaning of a specific limit is described in this class.
    """
    # <<< operational_limit_type
    # @generated
    def __init__(self, direction='high', acceptable_duration=0.0, operational_limit=None, **kw_args):
        """ Initialises a new 'OperationalLimitType' instance.
        """
        # The direction of the limit.The direction of the limit. Values are: "high", "absolute_value", "low"
        self.direction = 'high'

        # The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. 
        self.acceptable_duration = acceptable_duration


        self._operational_limit = []
        if operational_limit is not None:
            self.operational_limit = operational_limit
        else:
            self.operational_limit = []


        super(OperationalLimitType, self).__init__(**kw_args)
    # >>> operational_limit_type

    # <<< operational_limit
    # @generated
    def get_operational_limit(self):
        """ The operational limits associated with this type of limit.The operational limits associated with this type of limit.
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


    def __str__(self):
        """ Returns a string representation of the OperationalLimitType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< operational_limit_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OperationalLimitType.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OperationalLimitType", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.operational_limit:
            s += '%s<%s:OperationalLimitType.operational_limit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:OperationalLimitType.direction>%s</%s:OperationalLimitType.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:OperationalLimitType.acceptable_duration>%s</%s:OperationalLimitType.acceptable_duration>' % \
            (indent, ns_prefix, self.acceptable_duration, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OperationalLimitType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> operational_limit_type.serialize


class CurrentLimit(OperationalLimit):
    """ Operational limit on current.Operational limit on current.
    """
    # <<< current_limit
    # @generated
    def __init__(self, value=0.0, **kw_args):
        """ Initialises a new 'CurrentLimit' instance.
        """
        # Limit on current flow.Limit on current flow. 
        self.value = value



        super(CurrentLimit, self).__init__(**kw_args)
    # >>> current_limit


    def __str__(self):
        """ Returns a string representation of the CurrentLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< current_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CurrentLimit.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CurrentLimit", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:CurrentLimit.value>%s</%s:CurrentLimit.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.operational_limit_set is not None:
            s += '%s<%s:OperationalLimit.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operational_limit_set.uri)
        if self.operational_limit_type is not None:
            s += '%s<%s:OperationalLimit.operational_limit_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operational_limit_type.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CurrentLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> current_limit.serialize


class VoltageLimit(OperationalLimit):
    """ Operational limit applied to voltage.Operational limit applied to voltage.
    """
    # <<< voltage_limit
    # @generated
    def __init__(self, value=0.0, **kw_args):
        """ Initialises a new 'VoltageLimit' instance.
        """
        # Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKindLimit on voltage. High or low limit depends on the OperatoinalLimit.limitKind 
        self.value = value



        super(VoltageLimit, self).__init__(**kw_args)
    # >>> voltage_limit


    def __str__(self):
        """ Returns a string representation of the VoltageLimit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< voltage_limit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the VoltageLimit.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "VoltageLimit", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:VoltageLimit.value>%s</%s:VoltageLimit.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.operational_limit_set is not None:
            s += '%s<%s:OperationalLimit.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operational_limit_set.uri)
        if self.operational_limit_type is not None:
            s += '%s<%s:OperationalLimit.operational_limit_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.operational_limit_type.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "VoltageLimit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> voltage_limit.serialize


# <<< operational_limits
# @generated
# >>> operational_limits
