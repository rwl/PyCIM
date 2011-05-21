# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.IEC61970.Dynamics.MetaBlockParameter import MetaBlockParameter

class AttributeBlockParameter(MetaBlockParameter):
    """An attribute from the associated PowerSystemResource is used.   This is like reflection into the UML model as one must name the paramter the same as the CIM name of the desired attribute. Such parameters are not important for completely standard models as the relation to the CIM attributes is fixed.  This object is required for user defined models that use attributes already existing on the PowerSystemResource or its derived classes.   Using this class avoids creating new paramter instances (with values) when we already have the values as class attributes of the associated PowerSystemResource.   Standard block models might optinally use objects of this class to convey information about the internals of the standard block.
    """

    def __init__(self, attributeName='', *args, **kw_args):
        """Initialises a new 'AttributeBlockParameter' instance.

        @param attributeName: The name of the attribute in the information model. This could be any attribute of the derived class of the power system resource for which the block is intended to be used.  For example, if the one were using the xxx attribute from Generator class, one would specifiy this attribute as 'xxx'.  This would also limit the block to only those classes which have an 'xxx' attribute.  This attribute could be replaced by using the inherited IdentifiedObject.name value for the purpose described above. 
        """
        #: The name of the attribute in the information model. This could be any attribute of the derived class of the power system resource for which the block is intended to be used.  For example, if the one were using the xxx attribute from Generator class, one would specifiy this attribute as 'xxx'.  This would also limit the block to only those classes which have an 'xxx' attribute.  This attribute could be replaced by using the inherited IdentifiedObject.name value for the purpose described above.
        self.attributeName = attributeName

        super(AttributeBlockParameter, self).__init__(*args, **kw_args)

    _attrs = ["attributeName"]
    _attr_types = {"attributeName": str}
    _defaults = {"attributeName": ''}
    _enums = {}
    _refs = []
    _many_refs = []

