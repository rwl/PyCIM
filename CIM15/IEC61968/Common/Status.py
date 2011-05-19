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


class Status(object):
    """Current status information relevant to an entity.Current status information relevant to an entity.
    """

    def __init__(self, reason='', dateTime='', value='', remark=''):
        """Initialises a new 'Status' instance.

        @param reason: Reason code or explanation for why an object went to the current status 'value'. 
        @param dateTime: Date and time for which status 'value' applies. 
        @param value: Status value at 'dateTime'; prior status changes may have been kept in instances of activity records associated with the object to which this status applies. 
        @param remark: Pertinent information regarding the current 'value', as free form text. 
        """
        #: Reason code or explanation for why an object went to the current status 'value'.
        self.reason = reason

        #: Date and time for which status 'value' applies.
        self.dateTime = dateTime

        #: Status value at 'dateTime'; prior status changes may have been kept in instances of activity records associated with the object to which this status applies.
        self.value = value

        #: Pertinent information regarding the current 'value', as free form text.
        self.remark = remark


    _attrs = ["reason", "dateTime", "value", "remark"]
    _attr_types = {"reason": str, "dateTime": str, "value": str, "remark": str}
    _defaults = {"reason": '', "dateTime": '', "value": '', "remark": ''}
    _enums = {}
    _refs = []
    _many_refs = []

