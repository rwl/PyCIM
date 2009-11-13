# Copyright (C) 2009 Richard W. Lincoln
# All rights reserved.
""" An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.
"""


# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#"

class Element(object):
    # <<< element
    # @generated
    def __init__(self, uri='', parent=None, **kw_args):
        """ Initialises a new 'Element' instance.
        """
 
        self.uri = uri


        self._parent = None
        self.parent = parent


        super(Element, self).__init__(**kw_args)
    # >>> element

    # <<< parent
    # @generated
    def get_parent(self):
        """ 
        """
        return self._parent

    def set_parent(self, value):
        if self._parent is not None:
            filtered = [x for x in self.parent.elements if x != self]
            self._parent._elements = filtered

        self._parent = value
        if self._parent is not None:
            self._parent._elements.append(self)

    parent = property(get_parent, set_parent)
    # >>> parent


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

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Element")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> element.serialize


class CommonPowerSystemModel(object):
    # <<< common_power_system_model
    # @generated
    def __init__(self, elements=None, **kw_args):
        """ Initialises a new 'CommonPowerSystemModel' instance.
        """

        self._elements = []
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []


        super(CommonPowerSystemModel, self).__init__(**kw_args)
    # >>> common_power_system_model

    # <<< elements
    # @generated
    def get_elements(self):
        """ 
        """
        return self._elements

    def set_elements(self, value):
        for x in self._elements:
            x._parent = None
        for y in value:
            y._parent = self
        self._elements = value

    elements = property(get_elements, set_elements)

    def add_elements(self, *elements):
        for obj in elements:
            obj._parent = self
            self._elements.append(obj)

    def remove_elements(self, *elements):
        for obj in elements:
            obj._parent = None
            self._elements.remove(obj)
    # >>> elements

    # <<< read
    def read(self, rdfxml):
        """ @generated
        """
        pass
    # >>> read
    # <<< write
    def write(self, rdfxml):
        """ @generated
        """
        pass
    # >>> write

    def __str__(self):
        """ Returns a string representation of the CommonPowerSystemModel.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< common_power_system_model.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CommonPowerSystemModel.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CommonPowerSystemModel", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.elements:
            s += '%s<%s:CommonPowerSystemModel.elements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CommonPowerSystemModel")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> common_power_system_model.serialize


class IEC61970CIMVersion(Element):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.This is the IEC 61970 CIM version number assigned to this UML model file.
    """
    # <<< iec61970_cimversion
    # @generated
    def __init__(self, version='', date='', **kw_args):
        """ Initialises a new 'IEC61970CIMVersion' instance.
        """
 
        self.version = version

 
        self.date = date



        super(IEC61970CIMVersion, self).__init__(**kw_args)
    # >>> iec61970_cimversion


    def __str__(self):
        """ Returns a string representation of the IEC61970CIMVersion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< iec61970_cimversion.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the IEC61970CIMVersion.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "IEC61970CIMVersion", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:IEC61970CIMVersion.version>%s</%s:IEC61970CIMVersion.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)
        s += '%s<%s:IEC61970CIMVersion.date>%s</%s:IEC61970CIMVersion.date>' % \
            (indent, ns_prefix, self.date, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "IEC61970CIMVersion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> iec61970_cimversion.serialize


# <<< cpsm
# @generated
# >>> cpsm
