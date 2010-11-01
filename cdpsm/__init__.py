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

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#"

class Element(object):
    # <<< element
    # @generated
    def __init__(self, uuid='', model=None, *args, **kw_args):
        """ Initialises a new 'Element' instance.

        @param uuid: 
        @param model:
        """
 
        self.uuid = uuid


        self._model = None
        self.model = model


        super(Element, self).__init__(*args, **kw_args)
    # >>> element

    # <<< model
    # @generated
    def get_model(self):
        """ 
        """
        return self._model

    def set_model(self, value):
        if self._model is not None:
            filtered = [x for x in self.model.elements if x != self]
            self._model._elements = filtered

        self._model = value
        if self._model is not None:
            self._model._elements.append(self)

    model = property(get_model, set_model)
    # >>> model



class Model(object):
    # <<< model
    # @generated
    def __init__(self, elements=None, *args, **kw_args):
        """ Initialises a new 'Model' instance.

        @param elements:
        """

        self._elements = []
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []


        super(Model, self).__init__(*args, **kw_args)
    # >>> model

    # <<< elements
    # @generated
    def get_elements(self):
        """ 
        """
        return self._elements

    def set_elements(self, value):
        for x in self._elements:
            x._model = None
        for y in value:
            y._model = self
        self._elements = value

    elements = property(get_elements, set_elements)

    def add_elements(self, *elements):
        for obj in elements:
            obj._model = self
            self._elements.append(obj)

    def remove_elements(self, *elements):
        for obj in elements:
            obj._model = None
            self._elements.remove(obj)
    # >>> elements



# <<< cdpsm
# @generated
# >>> cdpsm
