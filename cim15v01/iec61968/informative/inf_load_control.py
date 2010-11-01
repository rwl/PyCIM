# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA


from cim15v01.iec61968.metering import DeviceFunction
from cim15v01.iec61968.common import ActivityRecord

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimInfLoadControl"

ns_uri = "http://iec.ch/TC57/CIM-generic#InfLoadControl"

class LoadMgmtFunction(DeviceFunction):
    """ A collective function at an end device that manages the customer load.
    """
    # <<< load_mgmt_function
    # @generated
    def __init__(self, scheduling_basis='tariff_based', load_status='no_load', manual_over_ride=False, over_ride_time_out=0.0, remote_over_ride=False, is_auto_op=False, switches=None, load_mgmt_records=None, *args, **kw_args):
        """ Initialises a new 'LoadMgmtFunction' instance.

        @param scheduling_basis: The basis of Load Management scheduling used here: Time Based, Tariff Based, Remote Control and Manual Control. Values are: "tariff_based", "remote_control", "manual_control", "time_based"
        @param load_status: The present state of the load being either shed (noLoad), limited (limitedLoad) or fully connected (fullLoad). This refers only to the portion of the customer load that is under control of the LoadMgmtFunction. Values are: "no_load", "full_load", "limited_load"
        @param manual_over_ride: True if the currently active schedule is being manually over-ridden to either shed load or to limit load. 
        @param over_ride_time_out: After a command had been received to activate the mannualOverRide state or remoteOverRideState, the normal (halted) schedule will resume after this specified time duration had elapsed. 
        @param remote_over_ride: True if the currently active schedule is being remotely over-ridden to either shed load or to limit load. 
        @param is_auto_op: True if LoadMgmtFunction operates under automatic control, otherwise it operates under manual control. 
        @param switches:
        @param load_mgmt_records:
        """
        # The basis of Load Management scheduling used here: Time Based, Tariff Based, Remote Control and Manual Control. Values are: "tariff_based", "remote_control", "manual_control", "time_based"
        self.scheduling_basis = scheduling_basis

        # The present state of the load being either shed (noLoad), limited (limitedLoad) or fully connected (fullLoad). This refers only to the portion of the customer load that is under control of the LoadMgmtFunction. Values are: "no_load", "full_load", "limited_load"
        self.load_status = load_status

        # True if the currently active schedule is being manually over-ridden to either shed load or to limit load. 
        self.manual_over_ride = manual_over_ride

        # After a command had been received to activate the mannualOverRide state or remoteOverRideState, the normal (halted) schedule will resume after this specified time duration had elapsed. 
        self.over_ride_time_out = over_ride_time_out

        # True if the currently active schedule is being remotely over-ridden to either shed load or to limit load. 
        self.remote_over_ride = remote_over_ride

        # True if LoadMgmtFunction operates under automatic control, otherwise it operates under manual control. 
        self.is_auto_op = is_auto_op


        self._switches = []
        if switches is not None:
            self.switches = switches
        else:
            self.switches = []

        self._load_mgmt_records = []
        if load_mgmt_records is not None:
            self.load_mgmt_records = load_mgmt_records
        else:
            self.load_mgmt_records = []


        super(LoadMgmtFunction, self).__init__(*args, **kw_args)
    # >>> load_mgmt_function

    # <<< switches
    # @generated
    def get_switches(self):
        """ 
        """
        return self._switches

    def set_switches(self, value):
        for p in self._switches:
            filtered = [q for q in p.load_mgmt_functions if q != self]
            self._switches._load_mgmt_functions = filtered
        for r in value:
            if self not in r._load_mgmt_functions:
                r._load_mgmt_functions.append(self)
        self._switches = value

    switches = property(get_switches, set_switches)

    def add_switches(self, *switches):
        for obj in switches:
            if self not in obj._load_mgmt_functions:
                obj._load_mgmt_functions.append(self)
            self._switches.append(obj)

    def remove_switches(self, *switches):
        for obj in switches:
            if self in obj._load_mgmt_functions:
                obj._load_mgmt_functions.remove(self)
            self._switches.remove(obj)
    # >>> switches

    # <<< load_mgmt_records
    # @generated
    def get_load_mgmt_records(self):
        """ 
        """
        return self._load_mgmt_records

    def set_load_mgmt_records(self, value):
        for x in self._load_mgmt_records:
            x._load_mgmt_function = None
        for y in value:
            y._load_mgmt_function = self
        self._load_mgmt_records = value

    load_mgmt_records = property(get_load_mgmt_records, set_load_mgmt_records)

    def add_load_mgmt_records(self, *load_mgmt_records):
        for obj in load_mgmt_records:
            obj._load_mgmt_function = self
            self._load_mgmt_records.append(obj)

    def remove_load_mgmt_records(self, *load_mgmt_records):
        for obj in load_mgmt_records:
            obj._load_mgmt_function = None
            self._load_mgmt_records.remove(obj)
    # >>> load_mgmt_records



class LoadMgmtRecord(ActivityRecord):
    """ A log of actual measured load reductions as a result of load shed operations.
    """
    # <<< load_mgmt_record
    # @generated
    def __init__(self, load_reduction=0.0, load_mgmt_function=None, *args, **kw_args):
        """ Initialises a new 'LoadMgmtRecord' instance.

        @param load_reduction: The measured reduction of the total load power as a result of the load shed activation. Thus it is the difference in power before and after the load shed operation. 
        @param load_mgmt_function:
        """
        # The measured reduction of the total load power as a result of the load shed activation. Thus it is the difference in power before and after the load shed operation. 
        self.load_reduction = load_reduction


        self._load_mgmt_function = None
        self.load_mgmt_function = load_mgmt_function


        super(LoadMgmtRecord, self).__init__(*args, **kw_args)
    # >>> load_mgmt_record

    # <<< load_mgmt_function
    # @generated
    def get_load_mgmt_function(self):
        """ 
        """
        return self._load_mgmt_function

    def set_load_mgmt_function(self, value):
        if self._load_mgmt_function is not None:
            filtered = [x for x in self.load_mgmt_function.load_mgmt_records if x != self]
            self._load_mgmt_function._load_mgmt_records = filtered

        self._load_mgmt_function = value
        if self._load_mgmt_function is not None:
            self._load_mgmt_function._load_mgmt_records.append(self)

    load_mgmt_function = property(get_load_mgmt_function, set_load_mgmt_function)
    # >>> load_mgmt_function



class LoadLimitFunction(LoadMgmtFunction):
    """ A kind of LoadMgmtFunction that limits the customer load to a given value.
    """
    # <<< load_limit_function
    # @generated
    def __init__(self, is_auto_recon_op=False, disconnect_time_delay=0.0, reconnect_time_delay=0.0, maximum_load=0.0, *args, **kw_args):
        """ Initialises a new 'LoadLimitFunction' instance.

        @param is_auto_recon_op: True if the switch will reconnect automatically, otherwise it will reconnect under manual control. 
        @param disconnect_time_delay: From the point when the maximumLoad threshold is crossed there may be a finite delay before the switch actually disconnects the load. Typically this is to buffer against transient load fluctuations. 
        @param reconnect_time_delay: From the point when the load recovers from an overload condition and crosses the maximumLoad threshold going down, there may be a finite time delay before the switch actually reconnects the load. Typically this is to give overload conditions sufficient time to clear, thus preventing unnecessary load switching activity. 
        @param maximum_load: The power level, to which the customer load is being limited when this function activates. When the maximum load is exceeded the switch will typically open to shed the complete customer load. 
        """
        # True if the switch will reconnect automatically, otherwise it will reconnect under manual control. 
        self.is_auto_recon_op = is_auto_recon_op

        # From the point when the maximumLoad threshold is crossed there may be a finite delay before the switch actually disconnects the load. Typically this is to buffer against transient load fluctuations. 
        self.disconnect_time_delay = disconnect_time_delay

        # From the point when the load recovers from an overload condition and crosses the maximumLoad threshold going down, there may be a finite time delay before the switch actually reconnects the load. Typically this is to give overload conditions sufficient time to clear, thus preventing unnecessary load switching activity. 
        self.reconnect_time_delay = reconnect_time_delay

        # The power level, to which the customer load is being limited when this function activates. When the maximum load is exceeded the switch will typically open to shed the complete customer load. 
        self.maximum_load = maximum_load



        super(LoadLimitFunction, self).__init__(*args, **kw_args)
    # >>> load_limit_function



class LoadShedFunction(LoadMgmtFunction):
    """ A kind of LoadMgmtFunction that sheds a part of the customer load.
    """
    # <<< load_shed_function
    # @generated
    def __init__(self, switched_load=0.0, *args, **kw_args):
        """ Initialises a new 'LoadShedFunction' instance.

        @param switched_load: The value of the load that is connected to the shedding switch. Typically this is a noted nominal value rather than a measured value. 
        """
        # The value of the load that is connected to the shedding switch. Typically this is a noted nominal value rather than a measured value. 
        self.switched_load = switched_load



        super(LoadShedFunction, self).__init__(*args, **kw_args)
    # >>> load_shed_function



# <<< inf_load_control
# @generated
# >>> inf_load_control
