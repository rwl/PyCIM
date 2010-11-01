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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class LimitSet(IdentifiedObject):
    """Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.
    """

    def __init__(self, isPercentageLimits=False, *args, **kw_args):
        """Initializes a new 'LimitSet' instance.

        @param isPercentageLimits: Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. 
        """
        #: Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. 
        self.isPercentageLimits = isPercentageLimits

        super(LimitSet, self).__init__(*args, **kw_args)

