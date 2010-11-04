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

from CIM14v13.Element import Element

class Status(Element):
    """Current status information relevant to an entity.
    """

    def __init__(self, dateTime='', reason='', value='', remark='', *args, **kw_args):
        """Initializes a new 'Status' instance.

        @param dateTime: Date and time for which status 'value' applies. 
        @param reason: Reason code or explanation for why an object went to the current status 'value'. 
        @param value: Status value at 'dateTime'; prior status changes may have been kept in instances of ActivityRecords associated with the object to which this Status applies. 
        @param remark: Pertinent information regarding the current 'value', as free form text. 
        """
        #: Date and time for which status 'value' applies.
        self.dateTime = dateTime

        #: Reason code or explanation for why an object went to the current status 'value'.
        self.reason = reason

        #: Status value at 'dateTime'; prior status changes may have been kept in instances of ActivityRecords associated with the object to which this Status applies.
        self.value = value

        #: Pertinent information regarding the current 'value', as free form text.
        self.remark = remark

        super(Status, self).__init__(*args, **kw_args)

