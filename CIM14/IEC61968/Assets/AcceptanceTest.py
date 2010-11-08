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

from CIM14.Element import Element

class AcceptanceTest(Element):
    """Acceptance test for assets.
    """

    def __init__(self, success=False, type='', dateTime='', *args, **kw_args):
        """Initialises a new 'AcceptanceTest' instance.

        @param success: True if asset has passed acceptance test and may be placed in or is in service. It is set to false if asset is removed from service and is required to be tested again before being placed back in service, possibly in a new location. Since asset may go through multiple tests during its life cycle, the date of each acceptance test may be recorded in Asset.ActivityRecord.status.dateTime. 
        @param type: Type of test or group of tests that was conducted on 'dateTime'. 
        @param dateTime: Date and time the asset was last tested using the 'type' of test and yielding the current status in 'success' attribute. 
        """
        #: True if asset has passed acceptance test and may be placed in or is in service. It is set to false if asset is removed from service and is required to be tested again before being placed back in service, possibly in a new location. Since asset may go through multiple tests during its life cycle, the date of each acceptance test may be recorded in Asset.ActivityRecord.status.dateTime.
        self.success = success

        #: Type of test or group of tests that was conducted on 'dateTime'.
        self.type = type

        #: Date and time the asset was last tested using the 'type' of test and yielding the current status in 'success' attribute.
        self.dateTime = dateTime

        super(AcceptanceTest, self).__init__(*args, **kw_args)

    _attrs = ["success", "type", "dateTime"]
    _attr_types = {"success": bool, "type": str, "dateTime": str}
    _defaults = {"success": False, "type": '', "dateTime": ''}
    _enums = {}
    _refs = []
    _many_refs = []

