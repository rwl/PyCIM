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

from CIM14.CPSM.StateVariables.Element import Element

class SvShuntCompensatorSections(Element):
    """State variable for the number of sections in service for a shunt compensator.
    """

    def __init__(self, sections=0, continuousSections=0.0, ShuntCompensator=None, *args, **kw_args):
        """Initialises a new 'SvShuntCompensatorSections' instance.

        @param sections: The number of sections in service. 
        @param continuousSections: The number of sections in service as a continous variable. 
        @param ShuntCompensator: The shunt compensator for which the state applies.
        """
        #: The number of sections in service.
        self.sections = sections

        #: The number of sections in service as a continous variable.
        self.continuousSections = continuousSections

        self._ShuntCompensator = None
        self.ShuntCompensator = ShuntCompensator

        super(SvShuntCompensatorSections, self).__init__(*args, **kw_args)

    _attrs = ["sections", "continuousSections"]
    _attr_types = {"sections": int, "continuousSections": float}
    _defaults = {"sections": 0, "continuousSections": 0.0}
    _enums = {}
    _refs = ["ShuntCompensator"]
    _many_refs = []

    def getShuntCompensator(self):
        """The shunt compensator for which the state applies.
        """
        return self._ShuntCompensator

    def setShuntCompensator(self, value):
        if self._ShuntCompensator is not None:
            self._ShuntCompensator._SvShuntCompensatorSections = None

        self._ShuntCompensator = value
        if self._ShuntCompensator is not None:
            self._ShuntCompensator.SvShuntCompensatorSections = None
            self._ShuntCompensator._SvShuntCompensatorSections = self

    ShuntCompensator = property(getShuntCompensator, setShuntCompensator)

