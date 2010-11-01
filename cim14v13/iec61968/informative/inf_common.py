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

""" This package contains functions common for distribution management.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'Locations are logical entities which are related to a geographical position. Locations can be defined as points, lines or polygons. Location serves as a parent class for e.g. Zone, WorkLocation or ServiceLocation. Both Assets and PowerSystemResources are typically associated to a location. Aside from coordinates, useful properties of Locations can include Directions (i.e. driving instructions) and relationships to Organizations. ActivityRecord is a generalized class used to track the history of an object (e.g. Asset, PowerSystemResource, Customer, Location, Organisation or ErpContact). An ActivityRecord is a type of Document. Key properties of an ActivityRecord include statusDate, status, statusReason and remarks. TODO: Update attribute names. The graphical and geographical aspects of Assets, Locations and PowerSystemResources are managed using Graphical Markup Language (GML), which was defined by the Open GIS Consortium.  Using GML, a diagram is a collection of presentation objects. This package defines the classes Diagram and Presentation. TODO: These are now under Common package.'
"""

from cim14v13.iec61970.core import IdentifiedObject
from cim14v13.iec61968.common import Document
from cim14v13 import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimInfCommon"

ns_uri = "http://iec.ch/TC57/CIM-generic#InfCommon"

class Role(IdentifiedObject):
    """ Enumeration of potential roles that might be played by one object relative to another.
    """
    # <<< role
    # @generated
    def __init__(self, category='', status=None, *args, **kw_args):
        """ Initialises a new 'Role' instance.

        @param category: Category of role. 
        @param status:
        """
        # Category of role. 
        self.category = category


        self.status = status


        super(Role, self).__init__(*args, **kw_args)
    # >>> role

    # <<< status
    # @generated
    status = None
    # >>> status



class ScheduledEvent(IdentifiedObject):
    """ Signifies an event to trigger one or more activities, such as reading a meter, recalculating a bill, requesting work, when generating units must be scheduled for maintenance, when a transformer is scheduled to be refurbished, etc.
    """
    # <<< scheduled_event
    # @generated
    def __init__(self, duration=0.0, category='', document=None, assets=None, activity_record=None, schedule_parameter_info=None, status=None, time_point=None, *args, **kw_args):
        """ Initialises a new 'ScheduledEvent' instance.

        @param duration: Duration of the scheduled event, for example, the time to ramp between values. 
        @param category: Category of scheduled event. 
        @param document:
        @param assets:
        @param activity_record:
        @param schedule_parameter_info:
        @param status:
        @param time_point:
        """
        # Duration of the scheduled event, for example, the time to ramp between values. 
        self.duration = duration

        # Category of scheduled event. 
        self.category = category


        self._document = None
        self.document = document

        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []

        self._activity_record = None
        self.activity_record = activity_record

        self._schedule_parameter_info = None
        self.schedule_parameter_info = schedule_parameter_info

        self.status = status

        self._time_point = None
        self.time_point = time_point


        super(ScheduledEvent, self).__init__(*args, **kw_args)
    # >>> scheduled_event

    # <<< document
    # @generated
    def get_document(self):
        """ 
        """
        return self._document

    def set_document(self, value):
        if self._document is not None:
            filtered = [x for x in self.document.scheduled_events if x != self]
            self._document._scheduled_events = filtered

        self._document = value
        if self._document is not None:
            self._document._scheduled_events.append(self)

    document = property(get_document, set_document)
    # >>> document

    # <<< assets
    # @generated
    def get_assets(self):
        """ 
        """
        return self._assets

    def set_assets(self, value):
        for p in self._assets:
            filtered = [q for q in p.scheduled_events if q != self]
            self._assets._scheduled_events = filtered
        for r in value:
            if self not in r._scheduled_events:
                r._scheduled_events.append(self)
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            if self not in obj._scheduled_events:
                obj._scheduled_events.append(self)
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            if self in obj._scheduled_events:
                obj._scheduled_events.remove(self)
            self._assets.remove(obj)
    # >>> assets

    # <<< activity_record
    # @generated
    def get_activity_record(self):
        """ 
        """
        return self._activity_record

    def set_activity_record(self, value):
        if self._activity_record is not None:
            self._activity_record._scheduled_event = None

        self._activity_record = value
        if self._activity_record is not None:
            self._activity_record._scheduled_event = self

    activity_record = property(get_activity_record, set_activity_record)
    # >>> activity_record

    # <<< schedule_parameter_info
    # @generated
    def get_schedule_parameter_info(self):
        """ 
        """
        return self._schedule_parameter_info

    def set_schedule_parameter_info(self, value):
        if self._schedule_parameter_info is not None:
            filtered = [x for x in self.schedule_parameter_info.scheduled_events if x != self]
            self._schedule_parameter_info._scheduled_events = filtered

        self._schedule_parameter_info = value
        if self._schedule_parameter_info is not None:
            self._schedule_parameter_info._scheduled_events.append(self)

    schedule_parameter_info = property(get_schedule_parameter_info, set_schedule_parameter_info)
    # >>> schedule_parameter_info

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< time_point
    # @generated
    def get_time_point(self):
        """ 
        """
        return self._time_point

    def set_time_point(self, value):
        if self._time_point is not None:
            filtered = [x for x in self.time_point.scheduled_events if x != self]
            self._time_point._scheduled_events = filtered

        self._time_point = value
        if self._time_point is not None:
            self._time_point._scheduled_events.append(self)

    time_point = property(get_time_point, set_time_point)
    # >>> time_point



class Skill(Document):
    """ Proficiency level of a craft, which is required to operate or maintain a particular type of asset and/or perform certain types of work.
    """
    # <<< skill
    # @generated
    def __init__(self, level='master', effective_date_time='', crafts=None, qualification_requirements=None, erp_person=None, certification_period=None, *args, **kw_args):
        """ Initialises a new 'Skill' instance.

        @param level: Level of skill for a Craft. Values are: "master", "other", "standard", "apprentice"
        @param effective_date_time: Date and time the skill became effective. 
        @param crafts:
        @param qualification_requirements:
        @param erp_person:
        @param certification_period: Interval between the certification and its expiry.
        """
        # Level of skill for a Craft. Values are: "master", "other", "standard", "apprentice"
        self.level = level

        # Date and time the skill became effective. 
        self.effective_date_time = effective_date_time


        self._crafts = []
        if crafts is not None:
            self.crafts = crafts
        else:
            self.crafts = []

        self._qualification_requirements = []
        if qualification_requirements is not None:
            self.qualification_requirements = qualification_requirements
        else:
            self.qualification_requirements = []

        self._erp_person = None
        self.erp_person = erp_person

        self.certification_period = certification_period


        super(Skill, self).__init__(*args, **kw_args)
    # >>> skill

    # <<< crafts
    # @generated
    def get_crafts(self):
        """ 
        """
        return self._crafts

    def set_crafts(self, value):
        for p in self._crafts:
            filtered = [q for q in p.skills if q != self]
            self._crafts._skills = filtered
        for r in value:
            if self not in r._skills:
                r._skills.append(self)
        self._crafts = value

    crafts = property(get_crafts, set_crafts)

    def add_crafts(self, *crafts):
        for obj in crafts:
            if self not in obj._skills:
                obj._skills.append(self)
            self._crafts.append(obj)

    def remove_crafts(self, *crafts):
        for obj in crafts:
            if self in obj._skills:
                obj._skills.remove(self)
            self._crafts.remove(obj)
    # >>> crafts

    # <<< qualification_requirements
    # @generated
    def get_qualification_requirements(self):
        """ 
        """
        return self._qualification_requirements

    def set_qualification_requirements(self, value):
        for p in self._qualification_requirements:
            filtered = [q for q in p.skills if q != self]
            self._qualification_requirements._skills = filtered
        for r in value:
            if self not in r._skills:
                r._skills.append(self)
        self._qualification_requirements = value

    qualification_requirements = property(get_qualification_requirements, set_qualification_requirements)

    def add_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self not in obj._skills:
                obj._skills.append(self)
            self._qualification_requirements.append(obj)

    def remove_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self in obj._skills:
                obj._skills.remove(self)
            self._qualification_requirements.remove(obj)
    # >>> qualification_requirements

    # <<< erp_person
    # @generated
    def get_erp_person(self):
        """ 
        """
        return self._erp_person

    def set_erp_person(self, value):
        if self._erp_person is not None:
            filtered = [x for x in self.erp_person.skills if x != self]
            self._erp_person._skills = filtered

        self._erp_person = value
        if self._erp_person is not None:
            self._erp_person._skills.append(self)

    erp_person = property(get_erp_person, set_erp_person)
    # >>> erp_person

    # <<< certification_period
    # @generated
    # Interval between the certification and its expiry.
    certification_period = None
    # >>> certification_period



class BankAccount(Document):
    """ Bank account.
    """
    # <<< bank_account
    # @generated
    def __init__(self, account_number='', service_supplier=None, bank=None, bank_statements=None, *args, **kw_args):
        """ Initialises a new 'BankAccount' instance.

        @param account_number: Account reference number. 
        @param service_supplier: ServiceSupplier that is owner of this BankAccount.
        @param bank: Bank that provides this BankAccount.
        @param bank_statements: All bank statements generated from this bank account.
        """
        # Account reference number. 
        self.account_number = account_number


        self._service_supplier = None
        self.service_supplier = service_supplier

        self._bank = None
        self.bank = bank

        self._bank_statements = []
        if bank_statements is not None:
            self.bank_statements = bank_statements
        else:
            self.bank_statements = []


        super(BankAccount, self).__init__(*args, **kw_args)
    # >>> bank_account

    # <<< service_supplier
    # @generated
    def get_service_supplier(self):
        """ ServiceSupplier that is owner of this BankAccount.
        """
        return self._service_supplier

    def set_service_supplier(self, value):
        if self._service_supplier is not None:
            filtered = [x for x in self.service_supplier.bank_accounts if x != self]
            self._service_supplier._bank_accounts = filtered

        self._service_supplier = value
        if self._service_supplier is not None:
            self._service_supplier._bank_accounts.append(self)

    service_supplier = property(get_service_supplier, set_service_supplier)
    # >>> service_supplier

    # <<< bank
    # @generated
    def get_bank(self):
        """ Bank that provides this BankAccount.
        """
        return self._bank

    def set_bank(self, value):
        if self._bank is not None:
            filtered = [x for x in self.bank.bank_accounts if x != self]
            self._bank._bank_accounts = filtered

        self._bank = value
        if self._bank is not None:
            self._bank._bank_accounts.append(self)

    bank = property(get_bank, set_bank)
    # >>> bank

    # <<< bank_statements
    # @generated
    def get_bank_statements(self):
        """ All bank statements generated from this bank account.
        """
        return self._bank_statements

    def set_bank_statements(self, value):
        for x in self._bank_statements:
            x._bank_account = None
        for y in value:
            y._bank_account = self
        self._bank_statements = value

    bank_statements = property(get_bank_statements, set_bank_statements)

    def add_bank_statements(self, *bank_statements):
        for obj in bank_statements:
            obj._bank_account = self
            self._bank_statements.append(obj)

    def remove_bank_statements(self, *bank_statements):
        for obj in bank_statements:
            obj._bank_account = None
            self._bank_statements.remove(obj)
    # >>> bank_statements



class MarketRole(IdentifiedObject):
    """ Role an organisation plays in a market. Examples include one or more of values defined in MarketRoleKind.
    """
    # <<< market_role
    # @generated
    def __init__(self, kind='other', status=None, organisations=None, *args, **kw_args):
        """ Initialises a new 'MarketRole' instance.

        @param kind: Kind of role an organisation plays in a market. Values are: "other", "transmission_service_provider", "planning_authority", "reliability_authority", "transmission_owner", "transmission_planner", "generator_operator", "energy_service_consumer", "generator_owner", "transmission_operator", "compliance_monitor", "distribution_provider", "load_serving_entity", "interchange_authority", "purchasing_selling_entity", "resource_planner", "balancing_authority", "competitive_retailer", "standards_developer"
        @param status:
        @param organisations:
        """
        # Kind of role an organisation plays in a market. Values are: "other", "transmission_service_provider", "planning_authority", "reliability_authority", "transmission_owner", "transmission_planner", "generator_operator", "energy_service_consumer", "generator_owner", "transmission_operator", "compliance_monitor", "distribution_provider", "load_serving_entity", "interchange_authority", "purchasing_selling_entity", "resource_planner", "balancing_authority", "competitive_retailer", "standards_developer"
        self.kind = kind


        self.status = status

        self._organisations = []
        if organisations is not None:
            self.organisations = organisations
        else:
            self.organisations = []


        super(MarketRole, self).__init__(*args, **kw_args)
    # >>> market_role

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< organisations
    # @generated
    def get_organisations(self):
        """ 
        """
        return self._organisations

    def set_organisations(self, value):
        for p in self._organisations:
            filtered = [q for q in p.market_roles if q != self]
            self._organisations._market_roles = filtered
        for r in value:
            if self not in r._market_roles:
                r._market_roles.append(self)
        self._organisations = value

    organisations = property(get_organisations, set_organisations)

    def add_organisations(self, *organisations):
        for obj in organisations:
            if self not in obj._market_roles:
                obj._market_roles.append(self)
            self._organisations.append(obj)

    def remove_organisations(self, *organisations):
        for obj in organisations:
            if self in obj._market_roles:
                obj._market_roles.remove(self)
            self._organisations.remove(obj)
    # >>> organisations



class Diagram(Document):
    """ GML and/or other means are used for rendering objects on various types of displays(geographic, schematic, other) and maps associated with various coordinate systems.
    """
    # <<< diagram
    # @generated
    def __init__(self, kind='geographic', gml_diagram_objects=None, design_locations=None, gml_coordinate_system=None, *args, **kw_args):
        """ Initialises a new 'Diagram' instance.

        @param kind: Kind of this diagram. Values are: "geographic", "schematic", "design_sketch", "internal_view", "other"
        @param gml_diagram_objects:
        @param design_locations:
        @param gml_coordinate_system:
        """
        # Kind of this diagram. Values are: "geographic", "schematic", "design_sketch", "internal_view", "other"
        self.kind = kind


        self._gml_diagram_objects = []
        if gml_diagram_objects is not None:
            self.gml_diagram_objects = gml_diagram_objects
        else:
            self.gml_diagram_objects = []

        self._design_locations = []
        if design_locations is not None:
            self.design_locations = design_locations
        else:
            self.design_locations = []

        self._gml_coordinate_system = None
        self.gml_coordinate_system = gml_coordinate_system


        super(Diagram, self).__init__(*args, **kw_args)
    # >>> diagram

    # <<< gml_diagram_objects
    # @generated
    def get_gml_diagram_objects(self):
        """ 
        """
        return self._gml_diagram_objects

    def set_gml_diagram_objects(self, value):
        for p in self._gml_diagram_objects:
            filtered = [q for q in p.diagrams if q != self]
            self._gml_diagram_objects._diagrams = filtered
        for r in value:
            if self not in r._diagrams:
                r._diagrams.append(self)
        self._gml_diagram_objects = value

    gml_diagram_objects = property(get_gml_diagram_objects, set_gml_diagram_objects)

    def add_gml_diagram_objects(self, *gml_diagram_objects):
        for obj in gml_diagram_objects:
            if self not in obj._diagrams:
                obj._diagrams.append(self)
            self._gml_diagram_objects.append(obj)

    def remove_gml_diagram_objects(self, *gml_diagram_objects):
        for obj in gml_diagram_objects:
            if self in obj._diagrams:
                obj._diagrams.remove(self)
            self._gml_diagram_objects.remove(obj)
    # >>> gml_diagram_objects

    # <<< design_locations
    # @generated
    def get_design_locations(self):
        """ 
        """
        return self._design_locations

    def set_design_locations(self, value):
        for p in self._design_locations:
            filtered = [q for q in p.diagrams if q != self]
            self._design_locations._diagrams = filtered
        for r in value:
            if self not in r._diagrams:
                r._diagrams.append(self)
        self._design_locations = value

    design_locations = property(get_design_locations, set_design_locations)

    def add_design_locations(self, *design_locations):
        for obj in design_locations:
            if self not in obj._diagrams:
                obj._diagrams.append(self)
            self._design_locations.append(obj)

    def remove_design_locations(self, *design_locations):
        for obj in design_locations:
            if self in obj._diagrams:
                obj._diagrams.remove(self)
            self._design_locations.remove(obj)
    # >>> design_locations

    # <<< gml_coordinate_system
    # @generated
    def get_gml_coordinate_system(self):
        """ 
        """
        return self._gml_coordinate_system

    def set_gml_coordinate_system(self, value):
        if self._gml_coordinate_system is not None:
            filtered = [x for x in self.gml_coordinate_system.diagrams if x != self]
            self._gml_coordinate_system._diagrams = filtered

        self._gml_coordinate_system = value
        if self._gml_coordinate_system is not None:
            self._gml_coordinate_system._diagrams.append(self)

    gml_coordinate_system = property(get_gml_coordinate_system, set_gml_coordinate_system)
    # >>> gml_coordinate_system



class Ratio(Element):
    """ Fraction specified explicitly with a numerator and denominator, which can be used to calculate the quotient.
    """
    # <<< ratio
    # @generated
    def __init__(self, denominator=0.0, numerator=0.0, *args, **kw_args):
        """ Initialises a new 'Ratio' instance.

        @param denominator: The part of a fraction that is below the line and that functions as the divisor of the numerator. 
        @param numerator: The part of a fraction that is above the line and signifies the number to be divided by the denominator. 
        """
        # The part of a fraction that is below the line and that functions as the divisor of the numerator. 
        self.denominator = denominator

        # The part of a fraction that is above the line and signifies the number to be divided by the denominator. 
        self.numerator = numerator



        super(Ratio, self).__init__(*args, **kw_args)
    # >>> ratio



class BusinessPlan(Document):
    """ A BusinessPlan is an organized sequence of predetermined actions required to complete a future organizational objective. It is a type of document that typically references a schedule, physical and/or logical resources (assets and/or PowerSystemResources), locations, etc.
    """
    pass
    # <<< business_plan
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'BusinessPlan' instance.

        """


        super(BusinessPlan, self).__init__(*args, **kw_args)
    # >>> business_plan



class BusinessRole(IdentifiedObject):
    """ A business role that this organisation plays. A single organisation typically performs many functions, each one described as a role.
    """
    # <<< business_role
    # @generated
    def __init__(self, category='', organisations=None, status=None, *args, **kw_args):
        """ Initialises a new 'BusinessRole' instance.

        @param category: Category by utility's corporate standards and practices. 
        @param organisations:
        @param status:
        """
        # Category by utility's corporate standards and practices. 
        self.category = category


        self._organisations = []
        if organisations is not None:
            self.organisations = organisations
        else:
            self.organisations = []

        self.status = status


        super(BusinessRole, self).__init__(*args, **kw_args)
    # >>> business_role

    # <<< organisations
    # @generated
    def get_organisations(self):
        """ 
        """
        return self._organisations

    def set_organisations(self, value):
        for p in self._organisations:
            filtered = [q for q in p.business_roles if q != self]
            self._organisations._business_roles = filtered
        for r in value:
            if self not in r._business_roles:
                r._business_roles.append(self)
        self._organisations = value

    organisations = property(get_organisations, set_organisations)

    def add_organisations(self, *organisations):
        for obj in organisations:
            if self not in obj._business_roles:
                obj._business_roles.append(self)
            self._organisations.append(obj)

    def remove_organisations(self, *organisations):
        for obj in organisations:
            if self in obj._business_roles:
                obj._business_roles.remove(self)
            self._organisations.remove(obj)
    # >>> organisations

    # <<< status
    # @generated
    status = None
    # >>> status



class Craft(IdentifiedObject):
    """ Craft of a person or a crew. Examples include overhead electric, underground electric, high pressure gas, etc. This ensures necessary knowledge and skills before being allowed to perform certain types of work.
    """
    # <<< craft
    # @generated
    def __init__(self, category='', skills=None, erp_persons=None, status=None, capabilities=None, *args, **kw_args):
        """ Initialises a new 'Craft' instance.

        @param category: Category by utility's work mangement standards and practices. 
        @param skills:
        @param erp_persons:
        @param status:
        @param capabilities:
        """
        # Category by utility's work mangement standards and practices. 
        self.category = category


        self._skills = []
        if skills is not None:
            self.skills = skills
        else:
            self.skills = []

        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []

        self.status = status

        self._capabilities = []
        if capabilities is not None:
            self.capabilities = capabilities
        else:
            self.capabilities = []


        super(Craft, self).__init__(*args, **kw_args)
    # >>> craft

    # <<< skills
    # @generated
    def get_skills(self):
        """ 
        """
        return self._skills

    def set_skills(self, value):
        for p in self._skills:
            filtered = [q for q in p.crafts if q != self]
            self._skills._crafts = filtered
        for r in value:
            if self not in r._crafts:
                r._crafts.append(self)
        self._skills = value

    skills = property(get_skills, set_skills)

    def add_skills(self, *skills):
        for obj in skills:
            if self not in obj._crafts:
                obj._crafts.append(self)
            self._skills.append(obj)

    def remove_skills(self, *skills):
        for obj in skills:
            if self in obj._crafts:
                obj._crafts.remove(self)
            self._skills.remove(obj)
    # >>> skills

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for p in self._erp_persons:
            filtered = [q for q in p.crafts if q != self]
            self._erp_persons._crafts = filtered
        for r in value:
            if self not in r._crafts:
                r._crafts.append(self)
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self not in obj._crafts:
                obj._crafts.append(self)
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self in obj._crafts:
                obj._crafts.remove(self)
            self._erp_persons.remove(obj)
    # >>> erp_persons

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< capabilities
    # @generated
    def get_capabilities(self):
        """ 
        """
        return self._capabilities

    def set_capabilities(self, value):
        for p in self._capabilities:
            filtered = [q for q in p.crafts if q != self]
            self._capabilities._crafts = filtered
        for r in value:
            if self not in r._crafts:
                r._crafts.append(self)
        self._capabilities = value

    capabilities = property(get_capabilities, set_capabilities)

    def add_capabilities(self, *capabilities):
        for obj in capabilities:
            if self not in obj._crafts:
                obj._crafts.append(self)
            self._capabilities.append(obj)

    def remove_capabilities(self, *capabilities):
        for obj in capabilities:
            if self in obj._crafts:
                obj._crafts.remove(self)
            self._capabilities.remove(obj)
    # >>> capabilities



class ScheduleParameterInfo(IdentifiedObject):
    """ Schedule parameters for an activity that is to occur, is occurring, or has completed.
    """
    # <<< schedule_parameter_info
    # @generated
    def __init__(self, for_inspection_data_set=None, estimated_window=None, scheduled_events=None, status=None, documents=None, requested_window=None, *args, **kw_args):
        """ Initialises a new 'ScheduleParameterInfo' instance.

        @param for_inspection_data_set:
        @param estimated_window: Estimated date and time for activity execution (with earliest possibility of activity initiation and latest possibility of activity completion).
        @param scheduled_events:
        @param status:
        @param documents:
        @param requested_window: Requested date and time interval for activity execution.
        """

        self._for_inspection_data_set = None
        self.for_inspection_data_set = for_inspection_data_set

        self.estimated_window = estimated_window

        self._scheduled_events = []
        if scheduled_events is not None:
            self.scheduled_events = scheduled_events
        else:
            self.scheduled_events = []

        self.status = status

        self._documents = []
        if documents is not None:
            self.documents = documents
        else:
            self.documents = []

        self.requested_window = requested_window


        super(ScheduleParameterInfo, self).__init__(*args, **kw_args)
    # >>> schedule_parameter_info

    # <<< for_inspection_data_set
    # @generated
    def get_for_inspection_data_set(self):
        """ 
        """
        return self._for_inspection_data_set

    def set_for_inspection_data_set(self, value):
        if self._for_inspection_data_set is not None:
            filtered = [x for x in self.for_inspection_data_set.according_to_schedules if x != self]
            self._for_inspection_data_set._according_to_schedules = filtered

        self._for_inspection_data_set = value
        if self._for_inspection_data_set is not None:
            self._for_inspection_data_set._according_to_schedules.append(self)

    for_inspection_data_set = property(get_for_inspection_data_set, set_for_inspection_data_set)
    # >>> for_inspection_data_set

    # <<< estimated_window
    # @generated
    # Estimated date and time for activity execution (with earliest possibility of activity initiation and latest possibility of activity completion).
    estimated_window = None
    # >>> estimated_window

    # <<< scheduled_events
    # @generated
    def get_scheduled_events(self):
        """ 
        """
        return self._scheduled_events

    def set_scheduled_events(self, value):
        for x in self._scheduled_events:
            x._schedule_parameter_info = None
        for y in value:
            y._schedule_parameter_info = self
        self._scheduled_events = value

    scheduled_events = property(get_scheduled_events, set_scheduled_events)

    def add_scheduled_events(self, *scheduled_events):
        for obj in scheduled_events:
            obj._schedule_parameter_info = self
            self._scheduled_events.append(obj)

    def remove_scheduled_events(self, *scheduled_events):
        for obj in scheduled_events:
            obj._schedule_parameter_info = None
            self._scheduled_events.remove(obj)
    # >>> scheduled_events

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< documents
    # @generated
    def get_documents(self):
        """ 
        """
        return self._documents

    def set_documents(self, value):
        for p in self._documents:
            filtered = [q for q in p.schedule_parameter_infos if q != self]
            self._documents._schedule_parameter_infos = filtered
        for r in value:
            if self not in r._schedule_parameter_infos:
                r._schedule_parameter_infos.append(self)
        self._documents = value

    documents = property(get_documents, set_documents)

    def add_documents(self, *documents):
        for obj in documents:
            if self not in obj._schedule_parameter_infos:
                obj._schedule_parameter_infos.append(self)
            self._documents.append(obj)

    def remove_documents(self, *documents):
        for obj in documents:
            if self in obj._schedule_parameter_infos:
                obj._schedule_parameter_infos.remove(self)
            self._documents.remove(obj)
    # >>> documents

    # <<< requested_window
    # @generated
    # Requested date and time interval for activity execution.
    requested_window = None
    # >>> requested_window



class Map(Diagram):
    """ A type of diagram that is usually printed on paper. It normally depicts part of the earth's surface, showing utility assets, right of ways, topological data, coordinates, grids, etc. Maps vary depending on whether they are used for dispatch, design, schematic, etc.
    """
    # <<< map
    # @generated
    def __init__(self, map_loc_grid='', page_number=0, *args, **kw_args):
        """ Initialises a new 'Map' instance.

        @param map_loc_grid: Map grid number. 
        @param page_number: Page number for particular set of maps specified by 'category'. 
        """
        # Map grid number. 
        self.map_loc_grid = map_loc_grid

        # Page number for particular set of maps specified by 'category'. 
        self.page_number = page_number



        super(Map, self).__init__(*args, **kw_args)
    # >>> map



class DocPsrRole(Role):
    """ Potential roles that might played by a document relative to a type of PowerSystemResource.
    """
    # <<< doc_psr_role
    # @generated
    def __init__(self, document=None, power_system_resource=None, *args, **kw_args):
        """ Initialises a new 'DocPsrRole' instance.

        @param document:
        @param power_system_resource:
        """

        self._document = None
        self.document = document

        self._power_system_resource = None
        self.power_system_resource = power_system_resource


        super(DocPsrRole, self).__init__(*args, **kw_args)
    # >>> doc_psr_role

    # <<< document
    # @generated
    def get_document(self):
        """ 
        """
        return self._document

    def set_document(self, value):
        if self._document is not None:
            filtered = [x for x in self.document.power_system_resource_roles if x != self]
            self._document._power_system_resource_roles = filtered

        self._document = value
        if self._document is not None:
            self._document._power_system_resource_roles.append(self)

    document = property(get_document, set_document)
    # >>> document

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ 
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        if self._power_system_resource is not None:
            filtered = [x for x in self.power_system_resource.document_roles if x != self]
            self._power_system_resource._document_roles = filtered

        self._power_system_resource = value
        if self._power_system_resource is not None:
            self._power_system_resource._document_roles.append(self)

    power_system_resource = property(get_power_system_resource, set_power_system_resource)
    # >>> power_system_resource



class DocDocRole(Role):
    """ Roles played between Documents and other Documents.
    """
    # <<< doc_doc_role
    # @generated
    def __init__(self, to_document=None, from_document=None, *args, **kw_args):
        """ Initialises a new 'DocDocRole' instance.

        @param to_document:
        @param from_document:
        """

        self._to_document = None
        self.to_document = to_document

        self._from_document = None
        self.from_document = from_document


        super(DocDocRole, self).__init__(*args, **kw_args)
    # >>> doc_doc_role

    # <<< to_document
    # @generated
    def get_to_document(self):
        """ 
        """
        return self._to_document

    def set_to_document(self, value):
        if self._to_document is not None:
            filtered = [x for x in self.to_document.from_document_roles if x != self]
            self._to_document._from_document_roles = filtered

        self._to_document = value
        if self._to_document is not None:
            self._to_document._from_document_roles.append(self)

    to_document = property(get_to_document, set_to_document)
    # >>> to_document

    # <<< from_document
    # @generated
    def get_from_document(self):
        """ 
        """
        return self._from_document

    def set_from_document(self, value):
        if self._from_document is not None:
            filtered = [x for x in self.from_document.to_document_roles if x != self]
            self._from_document._to_document_roles = filtered

        self._from_document = value
        if self._from_document is not None:
            self._from_document._to_document_roles.append(self)

    from_document = property(get_from_document, set_from_document)
    # >>> from_document



# <<< inf_common
# @generated
# >>> inf_common
