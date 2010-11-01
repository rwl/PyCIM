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

class ComPort(IdentifiedObject):
    """Port information used for communication connectivity purposes. The 'port' names the physical association to another device from the perspective of the parent asset. For example, a communications module may need to list the meters which it can talk to as meter serial number '123' is on 'port 0', S/N '456' is on port '1', etc. A meter or load control device may need to know that a hot-water heater load is on 'port 0', and an air-conditioner on 'port 1'.
    """

    def __init__(self, *args, **kw_args):
        """Initializes a new 'ComPort' instance.

        """
        super(ComPort, self).__init__(*args, **kw_args)

