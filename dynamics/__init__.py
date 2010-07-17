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

""" Contains entities that describe dynamic measurement data exchanged between applications.Contains entities that describe dynamic measurement data exchanged between applications.
"""


# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#"

class Element(object):
    # <<< element
    # @generated
    def __init__(self, uri='', model=None, **kw_args):
        """ Initialises a new 'Element' instance.
        """
 
        self.uri = uri


        self._model = None
        self.model = model


        super(Element, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the Element.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< element.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Element.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Element", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Element")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> element.serialize


class Model(object):
    # <<< model
    # @generated
    def __init__(self, uri='', elements=None, **kw_args):
        """ Initialises a new 'Model' instance.
        """
 
        self.uri = uri


        self._elements = []
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []


        super(Model, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the Model.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< model.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Model.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Model", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.elements:
            s += '%s<%s:Model.elements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Model.uri>%s</%s:Model.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Model")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> model.serialize


# <<< dynamics
# @generated
# >>> dynamics
