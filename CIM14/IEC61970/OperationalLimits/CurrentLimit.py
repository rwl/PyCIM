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

from CIM14.IEC61970.OperationalLimits.OperationalLimit import OperationalLimit

class CurrentLimit(OperationalLimit):
    """Operational limit on current.
    """

    def __init__(self, value=0.0, *args, **kw_args):
        """Initialises a new 'CurrentLimit' instance.

        @param value: Limit on current flow. 
        """
        #: Limit on current flow.
        self.value = value

        super(CurrentLimit, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": float}
    _defaults = {"value": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

