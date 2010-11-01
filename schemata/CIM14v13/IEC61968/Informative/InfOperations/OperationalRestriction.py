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

from CIM14v13.IEC61968.Common.Document import Document

class OperationalRestriction(Document):
    """A document that can be associated with a device to describe any sort of restrictions compared with the original manufacturer's specification e.g. temporary maximum loadings, maximum switching current, do not operate if bus couplers are open etc etc.  Since it is used in the network operations domain, it is associated with ConductingEquipment. In the UK, for example, if a breaker or switch ever mal-operates, this is reported centrally and utilities use their asset systems to identify all the installed devices of the same manufacturer's type. They then apply operational restrictions in the operational systems to warn operators of potential problems. After appropriate inspection and maintenance, the operational restrictions may be removed.
    """

    def __init__(self, activePeriod=None, *args, **kw_args):
        """Initializes a new 'OperationalRestriction' instance.

        @param activePeriod: Interval during which the restriction is applied.
        """
        self.activePeriod = activePeriod

        super(OperationalRestriction, self).__init__(*args, **kw_args)

    # Interval during which the restriction is applied.
    activePeriod = None

