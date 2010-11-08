# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.IEC61970.StateVariables.StateVariable import StateVariable

class SvShuntCompensatorSections(StateVariable):
    """State variable for the number of sections in service for a shunt compensator.
    """

    def __init__(self, continuousSections=0.0, sections=0, ShuntCompensator=None, *args, **kw_args):
        """Initialises a new 'SvShuntCompensatorSections' instance.

        @param continuousSections: The number of sections in service as a continous variable. 
        @param sections: The number of sections in service. 
        @param ShuntCompensator: The shunt compensator for which the state applies.
        """
        #: The number of sections in service as a continous variable.
        self.continuousSections = continuousSections

        #: The number of sections in service.
        self.sections = sections

        self._ShuntCompensator = None
        self.ShuntCompensator = ShuntCompensator

        super(SvShuntCompensatorSections, self).__init__(*args, **kw_args)

    _attrs = ["continuousSections", "sections"]
    _attr_types = {"continuousSections": float, "sections": int}
    _defaults = {"continuousSections": 0.0, "sections": 0}
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
            self._ShuntCompensator._SvShuntCompensatorSections = self

    ShuntCompensator = property(getShuntCompensator, setShuntCompensator)

