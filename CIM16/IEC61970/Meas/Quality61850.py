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

from CIM16.Element import Element

class Quality61850(Element):
    """Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.
    """

    def __init__(self, overFlow=False, estimatorReplaced=False, validity="QUESTIONABLE", operatorBlocked=False, oldData=False, failure=False, source="SUBSTITUTED", outOfRange=False, badReference=False, suspect=False, test=False, oscillatory=False, *args, **kw_args):
        """Initialises a new 'Quality61850' instance.

        @param overFlow: Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero. 
        @param estimatorReplaced: Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience. 
        @param validity: Validity of the measurement value. Values are: "QUESTIONABLE", "INVALID", "GOOD"
        @param operatorBlocked: Measurement value is blocked and hence unavailable for transmission. 
        @param oldData: Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval. 
        @param failure: This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure. 
        @param source: Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted. Values are: "SUBSTITUTED", "DEFAULTED", "PROCESS"
        @param outOfRange: Measurement value is beyond a predefined range of value. 
        @param badReference: Measurement value may be incorrect due to a reference being out of calibration. 
        @param suspect: A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator. 
        @param test: Measurement value is transmitted for test purposes. 
        @param oscillatory: To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only). 
        """
        #: Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero.
        self.overFlow = overFlow

        #: Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience.
        self.estimatorReplaced = estimatorReplaced

        #: Validity of the measurement value. Values are: "QUESTIONABLE", "INVALID", "GOOD"
        self.validity = validity

        #: Measurement value is blocked and hence unavailable for transmission.
        self.operatorBlocked = operatorBlocked

        #: Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval.
        self.oldData = oldData

        #: This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure.
        self.failure = failure

        #: Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted. Values are: "SUBSTITUTED", "DEFAULTED", "PROCESS"
        self.source = source

        #: Measurement value is beyond a predefined range of value.
        self.outOfRange = outOfRange

        #: Measurement value may be incorrect due to a reference being out of calibration.
        self.badReference = badReference

        #: A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator.
        self.suspect = suspect

        #: Measurement value is transmitted for test purposes.
        self.test = test

        #: To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only).
        self.oscillatory = oscillatory

        super(Quality61850, self).__init__(*args, **kw_args)

    _attrs = ["overFlow", "estimatorReplaced", "validity", "operatorBlocked", "oldData", "failure", "source", "outOfRange", "badReference", "suspect", "test", "oscillatory"]
    _attr_types = {"overFlow": bool, "estimatorReplaced": bool, "validity": str, "operatorBlocked": bool, "oldData": bool, "failure": bool, "source": str, "outOfRange": bool, "badReference": bool, "suspect": bool, "test": bool, "oscillatory": bool}
    _defaults = {"overFlow": False, "estimatorReplaced": False, "validity": "QUESTIONABLE", "operatorBlocked": False, "oldData": False, "failure": False, "source": "SUBSTITUTED", "outOfRange": False, "badReference": False, "suspect": False, "test": False, "oscillatory": False}
    _enums = {"validity": "Validity", "source": "Source"}
    _refs = []
    _many_refs = []

