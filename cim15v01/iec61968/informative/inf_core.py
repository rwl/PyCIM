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


from cim15v01.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimInfCore"

ns_uri = "http://iec.ch/TC57/CIM-generic#InfCore"

class ModelingAuthority(IdentifiedObject):
    """ A Modeling Authority is an entity responsible for supplying and maintaining the data defining a specific set of objects in a network model.
    """
    # <<< modeling_authority
    # @generated
    def __init__(self, modeling_authority_sets=None, *args, **kw_args):
        """ Initialises a new 'ModelingAuthority' instance.

        @param modeling_authority_sets: A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        """

        self._modeling_authority_sets = []
        if modeling_authority_sets is not None:
            self.modeling_authority_sets = modeling_authority_sets
        else:
            self.modeling_authority_sets = []


        super(ModelingAuthority, self).__init__(*args, **kw_args)
    # >>> modeling_authority

    # <<< modeling_authority_sets
    # @generated
    def get_modeling_authority_sets(self):
        """ A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        """
        return self._modeling_authority_sets

    def set_modeling_authority_sets(self, value):
        for x in self._modeling_authority_sets:
            x._modeling_authority = None
        for y in value:
            y._modeling_authority = self
        self._modeling_authority_sets = value

    modeling_authority_sets = property(get_modeling_authority_sets, set_modeling_authority_sets)

    def add_modeling_authority_sets(self, *modeling_authority_sets):
        for obj in modeling_authority_sets:
            obj._modeling_authority = self
            self._modeling_authority_sets.append(obj)

    def remove_modeling_authority_sets(self, *modeling_authority_sets):
        for obj in modeling_authority_sets:
            obj._modeling_authority = None
            self._modeling_authority_sets.remove(obj)
    # >>> modeling_authority_sets



class ModelingAuthoritySet(IdentifiedObject):
    """ A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority.
    """
    # <<< modeling_authority_set
    # @generated
    def __init__(self, modeling_authority=None, identified_objects=None, *args, **kw_args):
        """ Initialises a new 'ModelingAuthoritySet' instance.

        @param modeling_authority: A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        @param identified_objects: An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """

        self._modeling_authority = None
        self.modeling_authority = modeling_authority

        self._identified_objects = []
        if identified_objects is not None:
            self.identified_objects = identified_objects
        else:
            self.identified_objects = []


        super(ModelingAuthoritySet, self).__init__(*args, **kw_args)
    # >>> modeling_authority_set

    # <<< modeling_authority
    # @generated
    def get_modeling_authority(self):
        """ A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        """
        return self._modeling_authority

    def set_modeling_authority(self, value):
        if self._modeling_authority is not None:
            filtered = [x for x in self.modeling_authority.modeling_authority_sets if x != self]
            self._modeling_authority._modeling_authority_sets = filtered

        self._modeling_authority = value
        if self._modeling_authority is not None:
            self._modeling_authority._modeling_authority_sets.append(self)

    modeling_authority = property(get_modeling_authority, set_modeling_authority)
    # >>> modeling_authority

    # <<< identified_objects
    # @generated
    def get_identified_objects(self):
        """ An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        return self._identified_objects

    def set_identified_objects(self, value):
        for x in self._identified_objects:
            x._modeling_authority_set = None
        for y in value:
            y._modeling_authority_set = self
        self._identified_objects = value

    identified_objects = property(get_identified_objects, set_identified_objects)

    def add_identified_objects(self, *identified_objects):
        for obj in identified_objects:
            obj._modeling_authority_set = self
            self._identified_objects.append(obj)

    def remove_identified_objects(self, *identified_objects):
        for obj in identified_objects:
            obj._modeling_authority_set = None
            self._identified_objects.remove(obj)
    # >>> identified_objects



# <<< inf_core
# @generated
# >>> inf_core
