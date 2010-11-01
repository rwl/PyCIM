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

""" Contingencies to be studied.
"""

from cim15v01.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimContingency"

ns_uri = "http://iec.ch/TC57/CIM-generic#Contingency"

class Contingency(IdentifiedObject):
    """ An event threatening system reliability, consisting of one or more contingency elements.
    """
    # <<< contingency
    # @generated
    def __init__(self, must_study=False, contingency_constraint_limit=None, contingency_element=None, *args, **kw_args):
        """ Initialises a new 'Contingency' instance.

        @param must_study: Set true if must study this contingency. 
        @param contingency_constraint_limit:
        @param contingency_element: A contingency can have any number of contingency elements.
        """
        # Set true if must study this contingency. 
        self.must_study = must_study


        self._contingency_constraint_limit = []
        if contingency_constraint_limit is not None:
            self.contingency_constraint_limit = contingency_constraint_limit
        else:
            self.contingency_constraint_limit = []

        self._contingency_element = []
        if contingency_element is not None:
            self.contingency_element = contingency_element
        else:
            self.contingency_element = []


        super(Contingency, self).__init__(*args, **kw_args)
    # >>> contingency

    # <<< contingency_constraint_limit
    # @generated
    def get_contingency_constraint_limit(self):
        """ 
        """
        return self._contingency_constraint_limit

    def set_contingency_constraint_limit(self, value):
        for x in self._contingency_constraint_limit:
            x._contingency = None
        for y in value:
            y._contingency = self
        self._contingency_constraint_limit = value

    contingency_constraint_limit = property(get_contingency_constraint_limit, set_contingency_constraint_limit)

    def add_contingency_constraint_limit(self, *contingency_constraint_limit):
        for obj in contingency_constraint_limit:
            obj._contingency = self
            self._contingency_constraint_limit.append(obj)

    def remove_contingency_constraint_limit(self, *contingency_constraint_limit):
        for obj in contingency_constraint_limit:
            obj._contingency = None
            self._contingency_constraint_limit.remove(obj)
    # >>> contingency_constraint_limit

    # <<< contingency_element
    # @generated
    def get_contingency_element(self):
        """ A contingency can have any number of contingency elements.
        """
        return self._contingency_element

    def set_contingency_element(self, value):
        for x in self._contingency_element:
            x._contingency = None
        for y in value:
            y._contingency = self
        self._contingency_element = value

    contingency_element = property(get_contingency_element, set_contingency_element)

    def add_contingency_element(self, *contingency_element):
        for obj in contingency_element:
            obj._contingency = self
            self._contingency_element.append(obj)

    def remove_contingency_element(self, *contingency_element):
        for obj in contingency_element:
            obj._contingency = None
            self._contingency_element.remove(obj)
    # >>> contingency_element



class ContingencyElement(IdentifiedObject):
    """ An element of a system event to be studied by contingency analysis, representing a change in status of a single piece of equipment.
    """
    # <<< contingency_element
    # @generated
    def __init__(self, contingency=None, *args, **kw_args):
        """ Initialises a new 'ContingencyElement' instance.

        @param contingency: A contingency element belongs to one contingency.
        """

        self._contingency = None
        self.contingency = contingency


        super(ContingencyElement, self).__init__(*args, **kw_args)
    # >>> contingency_element

    # <<< contingency
    # @generated
    def get_contingency(self):
        """ A contingency element belongs to one contingency.
        """
        return self._contingency

    def set_contingency(self, value):
        if self._contingency is not None:
            filtered = [x for x in self.contingency.contingency_element if x != self]
            self._contingency._contingency_element = filtered

        self._contingency = value
        if self._contingency is not None:
            self._contingency._contingency_element.append(self)

    contingency = property(get_contingency, set_contingency)
    # >>> contingency



class ContingencyEquipment(ContingencyElement):
    """ A equipment to which the in service status is to change such as a power transformer or AC line segment.
    """
    # <<< contingency_equipment
    # @generated
    def __init__(self, contingent_status='in_service', equipment=None, *args, **kw_args):
        """ Initialises a new 'ContingencyEquipment' instance.

        @param contingent_status: The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied. Values are: "in_service", "out_of_service"
        @param equipment: The single piece of equipment to which to apply the contingency.
        """
        # The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied. Values are: "in_service", "out_of_service"
        self.contingent_status = contingent_status


        self._equipment = None
        self.equipment = equipment


        super(ContingencyEquipment, self).__init__(*args, **kw_args)
    # >>> contingency_equipment

    # <<< equipment
    # @generated
    def get_equipment(self):
        """ The single piece of equipment to which to apply the contingency.
        """
        return self._equipment

    def set_equipment(self, value):
        if self._equipment is not None:
            filtered = [x for x in self.equipment.contingency_equipment if x != self]
            self._equipment._contingency_equipment = filtered

        self._equipment = value
        if self._equipment is not None:
            self._equipment._contingency_equipment.append(self)

    equipment = property(get_equipment, set_equipment)
    # >>> equipment



# <<< contingency
# @generated
# >>> contingency
