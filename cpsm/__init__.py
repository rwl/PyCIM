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



# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#"

class Element(object):
    # <<< element
    # @generated
    def __init__(self, uuid='', model=None, *args, **kw_args):
        """ Initialises a new 'Element' instance.

        @param uuid: 
        @param model:
        """
 
        self.uuid = uuid


        self.model = model


        super(Element, self).__init__(*args, **kw_args)
    # >>> element

    # <<< model
    # @generated
    model = None
    # >>> model



class Model(object):
    # <<< model
    # @generated
    def __init__(self, elements=None, *args, **kw_args):
        """ Initialises a new 'Model' instance.

        @param elements:
        """

        if elements is not None:
            self.elements = elements
        else:
            self.elements = []


        super(Model, self).__init__(*args, **kw_args)
    # >>> model

    # <<< elements
    # @generated
    def add_elements(self, *elements):
        for obj in elements:
            self.elements.append(obj)

    def remove_elements(self, *elements):
        for obj in elements:
            self.elements.remove(obj)
    # >>> elements



# <<< cpsm
# @generated
# >>> cpsm
