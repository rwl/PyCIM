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

""" The equivalents package models equivalent networks.
"""

from cim15v01.iec61970.core import ConductingEquipment
from cim15v01.iec61970.core import ConnectivityNodeContainer

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimEquivalents"

ns_uri = "http://iec.ch/TC57/CIM-generic#Equivalents"

class EquivalentEquipment(ConductingEquipment):
    """ The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.
    """
    # <<< equivalent_equipment
    # @generated
    def __init__(self, equivalent_network=None, *args, **kw_args):
        """ Initialises a new 'EquivalentEquipment' instance.

        @param equivalent_network: The equivalent where the reduced model belongs.
        """

        self._equivalent_network = None
        self.equivalent_network = equivalent_network


        super(EquivalentEquipment, self).__init__(*args, **kw_args)
    # >>> equivalent_equipment

    # <<< equivalent_network
    # @generated
    def get_equivalent_network(self):
        """ The equivalent where the reduced model belongs.
        """
        return self._equivalent_network

    def set_equivalent_network(self, value):
        if self._equivalent_network is not None:
            filtered = [x for x in self.equivalent_network.equivalent_equipments if x != self]
            self._equivalent_network._equivalent_equipments = filtered

        self._equivalent_network = value
        if self._equivalent_network is not None:
            self._equivalent_network._equivalent_equipments.append(self)

    equivalent_network = property(get_equivalent_network, set_equivalent_network)
    # >>> equivalent_network



class EquivalentNetwork(ConnectivityNodeContainer):
    """ A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.
    """
    # <<< equivalent_network
    # @generated
    def __init__(self, equivalent_equipments=None, *args, **kw_args):
        """ Initialises a new 'EquivalentNetwork' instance.

        @param equivalent_equipments: The associated reduced equivalents.
        """

        self._equivalent_equipments = []
        if equivalent_equipments is not None:
            self.equivalent_equipments = equivalent_equipments
        else:
            self.equivalent_equipments = []


        super(EquivalentNetwork, self).__init__(*args, **kw_args)
    # >>> equivalent_network

    # <<< equivalent_equipments
    # @generated
    def get_equivalent_equipments(self):
        """ The associated reduced equivalents.
        """
        return self._equivalent_equipments

    def set_equivalent_equipments(self, value):
        for x in self._equivalent_equipments:
            x._equivalent_network = None
        for y in value:
            y._equivalent_network = self
        self._equivalent_equipments = value

    equivalent_equipments = property(get_equivalent_equipments, set_equivalent_equipments)

    def add_equivalent_equipments(self, *equivalent_equipments):
        for obj in equivalent_equipments:
            obj._equivalent_network = self
            self._equivalent_equipments.append(obj)

    def remove_equivalent_equipments(self, *equivalent_equipments):
        for obj in equivalent_equipments:
            obj._equivalent_network = None
            self._equivalent_equipments.remove(obj)
    # >>> equivalent_equipments



class EquivalentBranch(EquivalentEquipment):
    """ The class represents equivalent branches.
    """
    # <<< equivalent_branch
    # @generated
    def __init__(self, r=0.0, x=0.0, *args, **kw_args):
        """ Initialises a new 'EquivalentBranch' instance.

        @param r: Positive sequence series resistance of the reduced branch. 
        @param x: Positive sequence series reactance of the reduced branch. 
        """
        # Positive sequence series resistance of the reduced branch. 
        self.r = r

        # Positive sequence series reactance of the reduced branch. 
        self.x = x



        super(EquivalentBranch, self).__init__(*args, **kw_args)
    # >>> equivalent_branch



class EquivalentShunt(EquivalentEquipment):
    """ The class represents equivalent shunts.
    """
    # <<< equivalent_shunt
    # @generated
    def __init__(self, b=0.0, g=0.0, *args, **kw_args):
        """ Initialises a new 'EquivalentShunt' instance.

        @param b: Positive sequence shunt susceptance. 
        @param g: Positive sequence shunt conductance. 
        """
        # Positive sequence shunt susceptance. 
        self.b = b

        # Positive sequence shunt conductance. 
        self.g = g



        super(EquivalentShunt, self).__init__(*args, **kw_args)
    # >>> equivalent_shunt



class EquivalentInjection(EquivalentEquipment):
    """ This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the local connectivity node.
    """
    # <<< equivalent_injection
    # @generated
    def __init__(self, regulation_status=False, regulation_capability=False, min_p=0.0, max_p=0.0, regulation_target=0.0, *args, **kw_args):
        """ Initialises a new 'EquivalentInjection' instance.

        @param regulation_status: Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating. 
        @param regulation_capability: Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage. 
        @param min_p: Maximum active power of the injection. 
        @param max_p: Minimum active power of the injection. 
        @param regulation_target: The target voltage for voltage regulation. 
        """
        # Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating. 
        self.regulation_status = regulation_status

        # Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage. 
        self.regulation_capability = regulation_capability

        # Maximum active power of the injection. 
        self.min_p = min_p

        # Minimum active power of the injection. 
        self.max_p = max_p

        # The target voltage for voltage regulation. 
        self.regulation_target = regulation_target



        super(EquivalentInjection, self).__init__(*args, **kw_args)
    # >>> equivalent_injection



# <<< equivalents
# @generated
# >>> equivalents
