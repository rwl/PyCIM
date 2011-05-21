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

from CIM14.Element import Element

class Status(Element):
    """Current status information relevant to an entity.
    """

    def __init__(self, reason='', remark='', value='', dateTime='', *args, **kw_args):
        """Initialises a new 'Status' instance.

        @param reason: Reason code or explanation for why an object went to the current status 'value'. 
        @param remark: Pertinent information regarding the current 'value', as free form text. 
        @param value: Status value at 'dateTime'; prior status changes may have been kept in instances of ActivityRecords associated with the object to which this Status applies. 
        @param dateTime: Date and time for which status 'value' applies. 
        """
        #: Reason code or explanation for why an object went to the current status 'value'.
        self.reason = reason

        #: Pertinent information regarding the current 'value', as free form text.
        self.remark = remark

        #: Status value at 'dateTime'; prior status changes may have been kept in instances of ActivityRecords associated with the object to which this Status applies.
        self.value = value

        #: Date and time for which status 'value' applies.
        self.dateTime = dateTime

        super(Status, self).__init__(*args, **kw_args)

    _attrs = ["reason", "remark", "value", "dateTime"]
    _attr_types = {"reason": str, "remark": str, "value": str, "dateTime": str}
    _defaults = {"reason": '', "remark": '', "value": '', "dateTime": ''}
    _enums = {}
    _refs = []
    _many_refs = []

