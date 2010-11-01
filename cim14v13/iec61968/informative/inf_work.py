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

""" The package covers all types of work, including inspection, maintenance, repair, restoration, and construction. It covers the full life cycle including request, initiate, track and record work. Standardized designs (compatible units) are used where possible.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Work package is used to define classes related to work. There are several different aspects of work. The Work Initiation (Work, Project, Request). The Work Design package is used for managing designs (CompatibleUnit, Design, DesignLocation, WorkTask). The Work Schedule package is used for the scheduling and coordination of work (AccessPermit, MaterialItem, OneCallRequest, Regulation). The Work Closing package is used for tracking costs of work (CostType, LaborItem, WorkCostDetail, VehicleItem). The Work Standards package is used for the definition of compatible units (CULaborItem, CUVehicleItem, CUGroup). This package is used for inspection and maintenance (InspectionDataSet, Procedure). The WorkService package defines Appointment class.'
"""

from cim14v13.iec61970.core import IdentifiedObject
from cim14v13.iec61968.common import Document
from cim14v13.iec61968.informative.inf_common import ScheduledEvent
from cim14v13.iec61968.informative.inf_assets import ProcedureDataSet
from cim14v13.iec61968.common import ActivityRecord
from cim14v13.iec61968.common import Location

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimInfWork"

ns_uri = "http://iec.ch/TC57/CIM-generic#InfWork"

class DesignLocation(IdentifiedObject):
    """ A logical part of the design (e.g., pole and all equipment on a pole). This includes points and spans.
    """
    # <<< design_location
    # @generated
    def __init__(self, span_length=0.0, material_items=None, design_location_cus=None, designs=None, status=None, misc_cost_items=None, condition_factors=None, diagrams=None, erp_bom_item_datas=None, work_locations=None, *args, **kw_args):
        """ Initialises a new 'DesignLocation' instance.

        @param span_length: The legth of the span from the previous pole to this pole. 
        @param material_items:
        @param design_location_cus:
        @param designs:
        @param status:
        @param misc_cost_items:
        @param condition_factors:
        @param diagrams:
        @param erp_bom_item_datas:
        @param work_locations:
        """
        # The legth of the span from the previous pole to this pole. 
        self.span_length = span_length


        self._material_items = []
        if material_items is not None:
            self.material_items = material_items
        else:
            self.material_items = []

        self._design_location_cus = []
        if design_location_cus is not None:
            self.design_location_cus = design_location_cus
        else:
            self.design_location_cus = []

        self._designs = []
        if designs is not None:
            self.designs = designs
        else:
            self.designs = []

        self.status = status

        self._misc_cost_items = []
        if misc_cost_items is not None:
            self.misc_cost_items = misc_cost_items
        else:
            self.misc_cost_items = []

        self._condition_factors = []
        if condition_factors is not None:
            self.condition_factors = condition_factors
        else:
            self.condition_factors = []

        self._diagrams = []
        if diagrams is not None:
            self.diagrams = diagrams
        else:
            self.diagrams = []

        self._erp_bom_item_datas = []
        if erp_bom_item_datas is not None:
            self.erp_bom_item_datas = erp_bom_item_datas
        else:
            self.erp_bom_item_datas = []

        self._work_locations = []
        if work_locations is not None:
            self.work_locations = work_locations
        else:
            self.work_locations = []


        super(DesignLocation, self).__init__(*args, **kw_args)
    # >>> design_location

    # <<< material_items
    # @generated
    def get_material_items(self):
        """ 
        """
        return self._material_items

    def set_material_items(self, value):
        for x in self._material_items:
            x._design_location = None
        for y in value:
            y._design_location = self
        self._material_items = value

    material_items = property(get_material_items, set_material_items)

    def add_material_items(self, *material_items):
        for obj in material_items:
            obj._design_location = self
            self._material_items.append(obj)

    def remove_material_items(self, *material_items):
        for obj in material_items:
            obj._design_location = None
            self._material_items.remove(obj)
    # >>> material_items

    # <<< design_location_cus
    # @generated
    def get_design_location_cus(self):
        """ 
        """
        return self._design_location_cus

    def set_design_location_cus(self, value):
        for x in self._design_location_cus:
            x._design_location = None
        for y in value:
            y._design_location = self
        self._design_location_cus = value

    design_location_cus = property(get_design_location_cus, set_design_location_cus)

    def add_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            obj._design_location = self
            self._design_location_cus.append(obj)

    def remove_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            obj._design_location = None
            self._design_location_cus.remove(obj)
    # >>> design_location_cus

    # <<< designs
    # @generated
    def get_designs(self):
        """ 
        """
        return self._designs

    def set_designs(self, value):
        for p in self._designs:
            filtered = [q for q in p.design_locations if q != self]
            self._designs._design_locations = filtered
        for r in value:
            if self not in r._design_locations:
                r._design_locations.append(self)
        self._designs = value

    designs = property(get_designs, set_designs)

    def add_designs(self, *designs):
        for obj in designs:
            if self not in obj._design_locations:
                obj._design_locations.append(self)
            self._designs.append(obj)

    def remove_designs(self, *designs):
        for obj in designs:
            if self in obj._design_locations:
                obj._design_locations.remove(self)
            self._designs.remove(obj)
    # >>> designs

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< misc_cost_items
    # @generated
    def get_misc_cost_items(self):
        """ 
        """
        return self._misc_cost_items

    def set_misc_cost_items(self, value):
        for x in self._misc_cost_items:
            x._design_location = None
        for y in value:
            y._design_location = self
        self._misc_cost_items = value

    misc_cost_items = property(get_misc_cost_items, set_misc_cost_items)

    def add_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._design_location = self
            self._misc_cost_items.append(obj)

    def remove_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._design_location = None
            self._misc_cost_items.remove(obj)
    # >>> misc_cost_items

    # <<< condition_factors
    # @generated
    def get_condition_factors(self):
        """ 
        """
        return self._condition_factors

    def set_condition_factors(self, value):
        for p in self._condition_factors:
            filtered = [q for q in p.design_locations if q != self]
            self._condition_factors._design_locations = filtered
        for r in value:
            if self not in r._design_locations:
                r._design_locations.append(self)
        self._condition_factors = value

    condition_factors = property(get_condition_factors, set_condition_factors)

    def add_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self not in obj._design_locations:
                obj._design_locations.append(self)
            self._condition_factors.append(obj)

    def remove_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self in obj._design_locations:
                obj._design_locations.remove(self)
            self._condition_factors.remove(obj)
    # >>> condition_factors

    # <<< diagrams
    # @generated
    def get_diagrams(self):
        """ 
        """
        return self._diagrams

    def set_diagrams(self, value):
        for p in self._diagrams:
            filtered = [q for q in p.design_locations if q != self]
            self._diagrams._design_locations = filtered
        for r in value:
            if self not in r._design_locations:
                r._design_locations.append(self)
        self._diagrams = value

    diagrams = property(get_diagrams, set_diagrams)

    def add_diagrams(self, *diagrams):
        for obj in diagrams:
            if self not in obj._design_locations:
                obj._design_locations.append(self)
            self._diagrams.append(obj)

    def remove_diagrams(self, *diagrams):
        for obj in diagrams:
            if self in obj._design_locations:
                obj._design_locations.remove(self)
            self._diagrams.remove(obj)
    # >>> diagrams

    # <<< erp_bom_item_datas
    # @generated
    def get_erp_bom_item_datas(self):
        """ 
        """
        return self._erp_bom_item_datas

    def set_erp_bom_item_datas(self, value):
        for x in self._erp_bom_item_datas:
            x._design_location = None
        for y in value:
            y._design_location = self
        self._erp_bom_item_datas = value

    erp_bom_item_datas = property(get_erp_bom_item_datas, set_erp_bom_item_datas)

    def add_erp_bom_item_datas(self, *erp_bom_item_datas):
        for obj in erp_bom_item_datas:
            obj._design_location = self
            self._erp_bom_item_datas.append(obj)

    def remove_erp_bom_item_datas(self, *erp_bom_item_datas):
        for obj in erp_bom_item_datas:
            obj._design_location = None
            self._erp_bom_item_datas.remove(obj)
    # >>> erp_bom_item_datas

    # <<< work_locations
    # @generated
    def get_work_locations(self):
        """ 
        """
        return self._work_locations

    def set_work_locations(self, value):
        for p in self._work_locations:
            filtered = [q for q in p.design_locations if q != self]
            self._work_locations._design_locations = filtered
        for r in value:
            if self not in r._design_locations:
                r._design_locations.append(self)
        self._work_locations = value

    work_locations = property(get_work_locations, set_work_locations)

    def add_work_locations(self, *work_locations):
        for obj in work_locations:
            if self not in obj._design_locations:
                obj._design_locations.append(self)
            self._work_locations.append(obj)

    def remove_work_locations(self, *work_locations):
        for obj in work_locations:
            if self in obj._design_locations:
                obj._design_locations.remove(self)
            self._work_locations.remove(obj)
    # >>> work_locations



class Capability(IdentifiedObject):
    """ Capabilities of a crew.
    """
    # <<< capability
    # @generated
    def __init__(self, performance_factor='', category='', crew=None, status=None, work_tasks=None, validity_interval=None, crafts=None, *args, **kw_args):
        """ Initialises a new 'Capability' instance.

        @param performance_factor: Capability performance factor. 
        @param category: Category by utility's work management standards and practices. 
        @param crew:
        @param status:
        @param work_tasks:
        @param validity_interval: Date and time interval for which this capability is valid (when it became effective and when it expires).
        @param crafts:
        """
        # Capability performance factor. 
        self.performance_factor = performance_factor

        # Category by utility's work management standards and practices. 
        self.category = category


        self._crew = None
        self.crew = crew

        self.status = status

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self.validity_interval = validity_interval

        self._crafts = []
        if crafts is not None:
            self.crafts = crafts
        else:
            self.crafts = []


        super(Capability, self).__init__(*args, **kw_args)
    # >>> capability

    # <<< crew
    # @generated
    def get_crew(self):
        """ 
        """
        return self._crew

    def set_crew(self, value):
        if self._crew is not None:
            filtered = [x for x in self.crew.capabilities if x != self]
            self._crew._capabilities = filtered

        self._crew = value
        if self._crew is not None:
            self._crew._capabilities.append(self)

    crew = property(get_crew, set_crew)
    # >>> crew

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for p in self._work_tasks:
            filtered = [q for q in p.capabilities if q != self]
            self._work_tasks._capabilities = filtered
        for r in value:
            if self not in r._capabilities:
                r._capabilities.append(self)
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self not in obj._capabilities:
                obj._capabilities.append(self)
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self in obj._capabilities:
                obj._capabilities.remove(self)
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< validity_interval
    # @generated
    # Date and time interval for which this capability is valid (when it became effective and when it expires).
    validity_interval = None
    # >>> validity_interval

    # <<< crafts
    # @generated
    def get_crafts(self):
        """ 
        """
        return self._crafts

    def set_crafts(self, value):
        for p in self._crafts:
            filtered = [q for q in p.capabilities if q != self]
            self._crafts._capabilities = filtered
        for r in value:
            if self not in r._capabilities:
                r._capabilities.append(self)
        self._crafts = value

    crafts = property(get_crafts, set_crafts)

    def add_crafts(self, *crafts):
        for obj in crafts:
            if self not in obj._capabilities:
                obj._capabilities.append(self)
            self._crafts.append(obj)

    def remove_crafts(self, *crafts):
        for obj in crafts:
            if self in obj._capabilities:
                obj._capabilities.remove(self)
            self._crafts.remove(obj)
    # >>> crafts



class Design(Document):
    """ A design for consideration by customers, potential customers, or internal work. Note that the Version of design is the revision attribute that is inherited from Document.
    """
    # <<< design
    # @generated
    def __init__(self, kind='estimated', price=0.0, cost_estimate=0.0, design_locations_cus=None, work_cost_details=None, erp_quote_line_item=None, design_locations=None, work=None, erp_boms=None, condition_factors=None, work_tasks=None, *args, **kw_args):
        """ Initialises a new 'Design' instance.

        @param kind: Kind of this design. Values are: "estimated", "as_built", "other"
        @param price: Price to customer for implementing design. 
        @param cost_estimate: Estimated cost (not price) of design. 
        @param design_locations_cus:
        @param work_cost_details:
        @param erp_quote_line_item:
        @param design_locations:
        @param work:
        @param erp_boms:
        @param condition_factors:
        @param work_tasks:
        """
        # Kind of this design. Values are: "estimated", "as_built", "other"
        self.kind = kind

        # Price to customer for implementing design. 
        self.price = price

        # Estimated cost (not price) of design. 
        self.cost_estimate = cost_estimate


        self._design_locations_cus = []
        if design_locations_cus is not None:
            self.design_locations_cus = design_locations_cus
        else:
            self.design_locations_cus = []

        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []

        self._erp_quote_line_item = None
        self.erp_quote_line_item = erp_quote_line_item

        self._design_locations = []
        if design_locations is not None:
            self.design_locations = design_locations
        else:
            self.design_locations = []

        self._work = None
        self.work = work

        self._erp_boms = []
        if erp_boms is not None:
            self.erp_boms = erp_boms
        else:
            self.erp_boms = []

        self._condition_factors = []
        if condition_factors is not None:
            self.condition_factors = condition_factors
        else:
            self.condition_factors = []

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []


        super(Design, self).__init__(*args, **kw_args)
    # >>> design

    # <<< design_locations_cus
    # @generated
    def get_design_locations_cus(self):
        """ 
        """
        return self._design_locations_cus

    def set_design_locations_cus(self, value):
        for p in self._design_locations_cus:
            filtered = [q for q in p.designs if q != self]
            self._design_locations_cus._designs = filtered
        for r in value:
            if self not in r._designs:
                r._designs.append(self)
        self._design_locations_cus = value

    design_locations_cus = property(get_design_locations_cus, set_design_locations_cus)

    def add_design_locations_cus(self, *design_locations_cus):
        for obj in design_locations_cus:
            if self not in obj._designs:
                obj._designs.append(self)
            self._design_locations_cus.append(obj)

    def remove_design_locations_cus(self, *design_locations_cus):
        for obj in design_locations_cus:
            if self in obj._designs:
                obj._designs.remove(self)
            self._design_locations_cus.remove(obj)
    # >>> design_locations_cus

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for x in self._work_cost_details:
            x._design = None
        for y in value:
            y._design = self
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._design = self
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._design = None
            self._work_cost_details.remove(obj)
    # >>> work_cost_details

    # <<< erp_quote_line_item
    # @generated
    def get_erp_quote_line_item(self):
        """ 
        """
        return self._erp_quote_line_item

    def set_erp_quote_line_item(self, value):
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._design = None

        self._erp_quote_line_item = value
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._design = self

    erp_quote_line_item = property(get_erp_quote_line_item, set_erp_quote_line_item)
    # >>> erp_quote_line_item

    # <<< design_locations
    # @generated
    def get_design_locations(self):
        """ 
        """
        return self._design_locations

    def set_design_locations(self, value):
        for p in self._design_locations:
            filtered = [q for q in p.designs if q != self]
            self._design_locations._designs = filtered
        for r in value:
            if self not in r._designs:
                r._designs.append(self)
        self._design_locations = value

    design_locations = property(get_design_locations, set_design_locations)

    def add_design_locations(self, *design_locations):
        for obj in design_locations:
            if self not in obj._designs:
                obj._designs.append(self)
            self._design_locations.append(obj)

    def remove_design_locations(self, *design_locations):
        for obj in design_locations:
            if self in obj._designs:
                obj._designs.remove(self)
            self._design_locations.remove(obj)
    # >>> design_locations

    # <<< work
    # @generated
    def get_work(self):
        """ 
        """
        return self._work

    def set_work(self, value):
        if self._work is not None:
            filtered = [x for x in self.work.designs if x != self]
            self._work._designs = filtered

        self._work = value
        if self._work is not None:
            self._work._designs.append(self)

    work = property(get_work, set_work)
    # >>> work

    # <<< erp_boms
    # @generated
    def get_erp_boms(self):
        """ 
        """
        return self._erp_boms

    def set_erp_boms(self, value):
        for x in self._erp_boms:
            x._design = None
        for y in value:
            y._design = self
        self._erp_boms = value

    erp_boms = property(get_erp_boms, set_erp_boms)

    def add_erp_boms(self, *erp_boms):
        for obj in erp_boms:
            obj._design = self
            self._erp_boms.append(obj)

    def remove_erp_boms(self, *erp_boms):
        for obj in erp_boms:
            obj._design = None
            self._erp_boms.remove(obj)
    # >>> erp_boms

    # <<< condition_factors
    # @generated
    def get_condition_factors(self):
        """ 
        """
        return self._condition_factors

    def set_condition_factors(self, value):
        for p in self._condition_factors:
            filtered = [q for q in p.designs if q != self]
            self._condition_factors._designs = filtered
        for r in value:
            if self not in r._designs:
                r._designs.append(self)
        self._condition_factors = value

    condition_factors = property(get_condition_factors, set_condition_factors)

    def add_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self not in obj._designs:
                obj._designs.append(self)
            self._condition_factors.append(obj)

    def remove_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self in obj._designs:
                obj._designs.remove(self)
            self._condition_factors.remove(obj)
    # >>> condition_factors

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for x in self._work_tasks:
            x._design = None
        for y in value:
            y._design = self
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._design = self
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._design = None
            self._work_tasks.remove(obj)
    # >>> work_tasks



class LaborItem(IdentifiedObject):
    """ Labor used for work order.
    """
    # <<< labor_item
    # @generated
    def __init__(self, labor_rate=0.0, cost=0.0, activity_code='', labor_duration=0.0, work_cost_detail=None, erp_persons=None, status=None, work_task=None, *args, **kw_args):
        """ Initialises a new 'LaborItem' instance.

        @param labor_rate: The labor rate applied for work. 
        @param cost: Total cost for labor. Note that this may not be able to be derived from labor rate and time charged. 
        @param activity_code: Activity code identifies a specific and distinguishable unit of work. 
        @param labor_duration: Time required to perform work. 
        @param work_cost_detail:
        @param erp_persons:
        @param status:
        @param work_task:
        """
        # The labor rate applied for work. 
        self.labor_rate = labor_rate

        # Total cost for labor. Note that this may not be able to be derived from labor rate and time charged. 
        self.cost = cost

        # Activity code identifies a specific and distinguishable unit of work. 
        self.activity_code = activity_code

        # Time required to perform work. 
        self.labor_duration = labor_duration


        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail

        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []

        self.status = status

        self._work_task = None
        self.work_task = work_task


        super(LaborItem, self).__init__(*args, **kw_args)
    # >>> labor_item

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            filtered = [x for x in self.work_cost_detail.labor_items if x != self]
            self._work_cost_detail._labor_items = filtered

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._labor_items.append(self)

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for p in self._erp_persons:
            filtered = [q for q in p.labor_items if q != self]
            self._erp_persons._labor_items = filtered
        for r in value:
            if self not in r._labor_items:
                r._labor_items.append(self)
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self not in obj._labor_items:
                obj._labor_items.append(self)
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self in obj._labor_items:
                obj._labor_items.remove(self)
            self._erp_persons.remove(obj)
    # >>> erp_persons

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.labor_items if x != self]
            self._work_task._labor_items = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._labor_items.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task



class CUMaterialItem(IdentifiedObject):
    """ Compatible unit of a consumable supply item. For example, nuts, bolts, brackets, glue, etc.
    """
    # <<< cumaterial_item
    # @generated
    def __init__(self, corporate_code='', quantity=0, status=None, type_material=None, compatible_units=None, property_units=None, *args, **kw_args):
        """ Initialises a new 'CUMaterialItem' instance.

        @param corporate_code: Code for material. 
        @param quantity: Quantity of the TypeMaterial for this CU, used to determine estimated costs based on a per unit cost or a cost per unit length specified in the TypeMaterial. 
        @param status:
        @param type_material:
        @param compatible_units:
        @param property_units:
        """
        # Code for material. 
        self.corporate_code = corporate_code

        # Quantity of the TypeMaterial for this CU, used to determine estimated costs based on a per unit cost or a cost per unit length specified in the TypeMaterial. 
        self.quantity = quantity


        self.status = status

        self._type_material = None
        self.type_material = type_material

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self._property_units = []
        if property_units is not None:
            self.property_units = property_units
        else:
            self.property_units = []


        super(CUMaterialItem, self).__init__(*args, **kw_args)
    # >>> cumaterial_item

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< type_material
    # @generated
    def get_type_material(self):
        """ 
        """
        return self._type_material

    def set_type_material(self, value):
        if self._type_material is not None:
            filtered = [x for x in self.type_material.cumaterial_items if x != self]
            self._type_material._cumaterial_items = filtered

        self._type_material = value
        if self._type_material is not None:
            self._type_material._cumaterial_items.append(self)

    type_material = property(get_type_material, set_type_material)
    # >>> type_material

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.cumaterial_items if q != self]
            self._compatible_units._cumaterial_items = filtered
        for r in value:
            if self not in r._cumaterial_items:
                r._cumaterial_items.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._cumaterial_items:
                obj._cumaterial_items.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._cumaterial_items:
                obj._cumaterial_items.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< property_units
    # @generated
    def get_property_units(self):
        """ 
        """
        return self._property_units

    def set_property_units(self, value):
        for p in self._property_units:
            filtered = [q for q in p.cumaterial_items if q != self]
            self._property_units._cumaterial_items = filtered
        for r in value:
            if self not in r._cumaterial_items:
                r._cumaterial_items.append(self)
        self._property_units = value

    property_units = property(get_property_units, set_property_units)

    def add_property_units(self, *property_units):
        for obj in property_units:
            if self not in obj._cumaterial_items:
                obj._cumaterial_items.append(self)
            self._property_units.append(obj)

    def remove_property_units(self, *property_units):
        for obj in property_units:
            if self in obj._cumaterial_items:
                obj._cumaterial_items.remove(self)
            self._property_units.remove(obj)
    # >>> property_units



class NonStandardItem(Document):
    """ This document provides information for non-standard items like customer contributions (e.g., customer digs trench), vouchers (e.g., credit), and contractor bids.
    """
    # <<< non_standard_item
    # @generated
    def __init__(self, amount=0.0, code='', *args, **kw_args):
        """ Initialises a new 'NonStandardItem' instance.

        @param amount: The projected cost for this item. 
        @param code: The category of non-standard work. 
        """
        # The projected cost for this item. 
        self.amount = amount

        # The category of non-standard work. 
        self.code = code



        super(NonStandardItem, self).__init__(*args, **kw_args)
    # >>> non_standard_item



class TypeMaterial(Document):
    """ Documentation for a generic material item that may be used for design, work and other purposes. Any number of MaterialItems manufactured by various vendors may be used to perform this TypeMaterial. Note that class analagous to 'AssetModel' is not used for material items. This is because in some cases, for example, a utility sets up a Master material record for a 3 inch long half inch diameter steel bolt and they do not necessarily care what specific supplier is providing the material item. As different vendors are used to supply the part, the Stock Code of the material item can stay the same. In other cases, each time the vendor changes, a new stock code is set up so they can track material used by vendor. Therefore a Material Item 'Model' is not typically needed.
    """
    # <<< type_material
    # @generated
    def __init__(self, stock_item=False, quantity='', cost_type='', est_unit_cost=0.0, erp_req_line_items=None, erp_issue_inventories=None, cumaterial_items=None, material_items=None, *args, **kw_args):
        """ Initialises a new 'TypeMaterial' instance.

        @param stock_item: True if item is a stock item (default). 
        @param quantity: The value, unit of measure, and multiplier for the quantity. 
        @param cost_type: The category of cost to which this Material Item belongs. 
        @param est_unit_cost: The estimated unit cost of this type of material, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it. 
        @param erp_req_line_items:
        @param erp_issue_inventories:
        @param cumaterial_items:
        @param material_items:
        """
        # True if item is a stock item (default). 
        self.stock_item = stock_item

        # The value, unit of measure, and multiplier for the quantity. 
        self.quantity = quantity

        # The category of cost to which this Material Item belongs. 
        self.cost_type = cost_type

        # The estimated unit cost of this type of material, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it. 
        self.est_unit_cost = est_unit_cost


        self._erp_req_line_items = []
        if erp_req_line_items is not None:
            self.erp_req_line_items = erp_req_line_items
        else:
            self.erp_req_line_items = []

        self._erp_issue_inventories = []
        if erp_issue_inventories is not None:
            self.erp_issue_inventories = erp_issue_inventories
        else:
            self.erp_issue_inventories = []

        self._cumaterial_items = []
        if cumaterial_items is not None:
            self.cumaterial_items = cumaterial_items
        else:
            self.cumaterial_items = []

        self._material_items = []
        if material_items is not None:
            self.material_items = material_items
        else:
            self.material_items = []


        super(TypeMaterial, self).__init__(*args, **kw_args)
    # >>> type_material

    # <<< erp_req_line_items
    # @generated
    def get_erp_req_line_items(self):
        """ 
        """
        return self._erp_req_line_items

    def set_erp_req_line_items(self, value):
        for x in self._erp_req_line_items:
            x._type_material = None
        for y in value:
            y._type_material = self
        self._erp_req_line_items = value

    erp_req_line_items = property(get_erp_req_line_items, set_erp_req_line_items)

    def add_erp_req_line_items(self, *erp_req_line_items):
        for obj in erp_req_line_items:
            obj._type_material = self
            self._erp_req_line_items.append(obj)

    def remove_erp_req_line_items(self, *erp_req_line_items):
        for obj in erp_req_line_items:
            obj._type_material = None
            self._erp_req_line_items.remove(obj)
    # >>> erp_req_line_items

    # <<< erp_issue_inventories
    # @generated
    def get_erp_issue_inventories(self):
        """ 
        """
        return self._erp_issue_inventories

    def set_erp_issue_inventories(self, value):
        for x in self._erp_issue_inventories:
            x._type_material = None
        for y in value:
            y._type_material = self
        self._erp_issue_inventories = value

    erp_issue_inventories = property(get_erp_issue_inventories, set_erp_issue_inventories)

    def add_erp_issue_inventories(self, *erp_issue_inventories):
        for obj in erp_issue_inventories:
            obj._type_material = self
            self._erp_issue_inventories.append(obj)

    def remove_erp_issue_inventories(self, *erp_issue_inventories):
        for obj in erp_issue_inventories:
            obj._type_material = None
            self._erp_issue_inventories.remove(obj)
    # >>> erp_issue_inventories

    # <<< cumaterial_items
    # @generated
    def get_cumaterial_items(self):
        """ 
        """
        return self._cumaterial_items

    def set_cumaterial_items(self, value):
        for x in self._cumaterial_items:
            x._type_material = None
        for y in value:
            y._type_material = self
        self._cumaterial_items = value

    cumaterial_items = property(get_cumaterial_items, set_cumaterial_items)

    def add_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            obj._type_material = self
            self._cumaterial_items.append(obj)

    def remove_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            obj._type_material = None
            self._cumaterial_items.remove(obj)
    # >>> cumaterial_items

    # <<< material_items
    # @generated
    def get_material_items(self):
        """ 
        """
        return self._material_items

    def set_material_items(self, value):
        for x in self._material_items:
            x._type_material = None
        for y in value:
            y._type_material = self
        self._material_items = value

    material_items = property(get_material_items, set_material_items)

    def add_material_items(self, *material_items):
        for obj in material_items:
            obj._type_material = self
            self._material_items.append(obj)

    def remove_material_items(self, *material_items):
        for obj in material_items:
            obj._type_material = None
            self._material_items.remove(obj)
    # >>> material_items



class Appointment(ScheduledEvent):
    """ Meeting time and location.
    """
    # <<< appointment
    # @generated
    def __init__(self, remark='', call_ahead=False, erp_persons=None, call_back=None, address=None, meeting_interval=None, *args, **kw_args):
        """ Initialises a new 'Appointment' instance.

        @param remark: Information about the appointment. 
        @param call_ahead: True if requested to call customer when someone is about to arrive at their premises. 
        @param erp_persons:
        @param call_back:
        @param address: Address for appointment.
        @param meeting_interval: Date and time reserved for appointment.
        """
        # Information about the appointment. 
        self.remark = remark

        # True if requested to call customer when someone is about to arrive at their premises. 
        self.call_ahead = call_ahead


        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []

        self._call_back = None
        self.call_back = call_back

        self.address = address

        self.meeting_interval = meeting_interval


        super(Appointment, self).__init__(*args, **kw_args)
    # >>> appointment

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for p in self._erp_persons:
            filtered = [q for q in p.appointments if q != self]
            self._erp_persons._appointments = filtered
        for r in value:
            if self not in r._appointments:
                r._appointments.append(self)
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self not in obj._appointments:
                obj._appointments.append(self)
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self in obj._appointments:
                obj._appointments.remove(self)
            self._erp_persons.remove(obj)
    # >>> erp_persons

    # <<< call_back
    # @generated
    def get_call_back(self):
        """ 
        """
        return self._call_back

    def set_call_back(self, value):
        if self._call_back is not None:
            filtered = [x for x in self.call_back.appointments if x != self]
            self._call_back._appointments = filtered

        self._call_back = value
        if self._call_back is not None:
            self._call_back._appointments.append(self)

    call_back = property(get_call_back, set_call_back)
    # >>> call_back

    # <<< address
    # @generated
    # Address for appointment.
    address = None
    # >>> address

    # <<< meeting_interval
    # @generated
    # Date and time reserved for appointment.
    meeting_interval = None
    # >>> meeting_interval



class MaterialItem(IdentifiedObject):
    """ The physical consumable supply used for work and other purposes. It includes items such as nuts, bolts, brackets, glue, etc.
    """
    # <<< material_item
    # @generated
    def __init__(self, actual_cost=0.0, material_code='', quantity=0, cost_type='', cost_description='', external_ref_id='', account='', usages=None, design_location=None, status=None, work_task=None, erp_inventory_counts=None, erp_rec_delv_line_items=None, erp_poline_items=None, work_cost_detail=None, type_material=None, *args, **kw_args):
        """ Initialises a new 'MaterialItem' instance.

        @param actual_cost: The actual cost of this particular material in this particular quantity. 
        @param material_code: Code for material. 
        @param quantity: The quantity of material used. 
        @param cost_type: The category of cost to which this Material Item belongs. 
        @param cost_description: Description of the cost. 
        @param external_ref_id: External reference identifier for this actual material item such as a purchase order number, a serial number, etc. 
        @param account: The account to which this actual material item is charged. 
        @param usages:
        @param design_location:
        @param status:
        @param work_task:
        @param erp_inventory_counts:
        @param erp_rec_delv_line_items:
        @param erp_poline_items:
        @param work_cost_detail:
        @param type_material:
        """
        # The actual cost of this particular material in this particular quantity. 
        self.actual_cost = actual_cost

        # Code for material. 
        self.material_code = material_code

        # The quantity of material used. 
        self.quantity = quantity

        # The category of cost to which this Material Item belongs. 
        self.cost_type = cost_type

        # Description of the cost. 
        self.cost_description = cost_description

        # External reference identifier for this actual material item such as a purchase order number, a serial number, etc. 
        self.external_ref_id = external_ref_id

        # The account to which this actual material item is charged. 
        self.account = account


        self._usages = []
        if usages is not None:
            self.usages = usages
        else:
            self.usages = []

        self._design_location = None
        self.design_location = design_location

        self.status = status

        self._work_task = None
        self.work_task = work_task

        self._erp_inventory_counts = []
        if erp_inventory_counts is not None:
            self.erp_inventory_counts = erp_inventory_counts
        else:
            self.erp_inventory_counts = []

        self._erp_rec_delv_line_items = []
        if erp_rec_delv_line_items is not None:
            self.erp_rec_delv_line_items = erp_rec_delv_line_items
        else:
            self.erp_rec_delv_line_items = []

        self._erp_poline_items = []
        if erp_poline_items is not None:
            self.erp_poline_items = erp_poline_items
        else:
            self.erp_poline_items = []

        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail

        self._type_material = None
        self.type_material = type_material


        super(MaterialItem, self).__init__(*args, **kw_args)
    # >>> material_item

    # <<< usages
    # @generated
    def get_usages(self):
        """ 
        """
        return self._usages

    def set_usages(self, value):
        for x in self._usages:
            x._material_item = None
        for y in value:
            y._material_item = self
        self._usages = value

    usages = property(get_usages, set_usages)

    def add_usages(self, *usages):
        for obj in usages:
            obj._material_item = self
            self._usages.append(obj)

    def remove_usages(self, *usages):
        for obj in usages:
            obj._material_item = None
            self._usages.remove(obj)
    # >>> usages

    # <<< design_location
    # @generated
    def get_design_location(self):
        """ 
        """
        return self._design_location

    def set_design_location(self, value):
        if self._design_location is not None:
            filtered = [x for x in self.design_location.material_items if x != self]
            self._design_location._material_items = filtered

        self._design_location = value
        if self._design_location is not None:
            self._design_location._material_items.append(self)

    design_location = property(get_design_location, set_design_location)
    # >>> design_location

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.material_items if x != self]
            self._work_task._material_items = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._material_items.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< erp_inventory_counts
    # @generated
    def get_erp_inventory_counts(self):
        """ 
        """
        return self._erp_inventory_counts

    def set_erp_inventory_counts(self, value):
        for x in self._erp_inventory_counts:
            x._material_item = None
        for y in value:
            y._material_item = self
        self._erp_inventory_counts = value

    erp_inventory_counts = property(get_erp_inventory_counts, set_erp_inventory_counts)

    def add_erp_inventory_counts(self, *erp_inventory_counts):
        for obj in erp_inventory_counts:
            obj._material_item = self
            self._erp_inventory_counts.append(obj)

    def remove_erp_inventory_counts(self, *erp_inventory_counts):
        for obj in erp_inventory_counts:
            obj._material_item = None
            self._erp_inventory_counts.remove(obj)
    # >>> erp_inventory_counts

    # <<< erp_rec_delv_line_items
    # @generated
    def get_erp_rec_delv_line_items(self):
        """ 
        """
        return self._erp_rec_delv_line_items

    def set_erp_rec_delv_line_items(self, value):
        for p in self._erp_rec_delv_line_items:
            filtered = [q for q in p.material_items if q != self]
            self._erp_rec_delv_line_items._material_items = filtered
        for r in value:
            if self not in r._material_items:
                r._material_items.append(self)
        self._erp_rec_delv_line_items = value

    erp_rec_delv_line_items = property(get_erp_rec_delv_line_items, set_erp_rec_delv_line_items)

    def add_erp_rec_delv_line_items(self, *erp_rec_delv_line_items):
        for obj in erp_rec_delv_line_items:
            if self not in obj._material_items:
                obj._material_items.append(self)
            self._erp_rec_delv_line_items.append(obj)

    def remove_erp_rec_delv_line_items(self, *erp_rec_delv_line_items):
        for obj in erp_rec_delv_line_items:
            if self in obj._material_items:
                obj._material_items.remove(self)
            self._erp_rec_delv_line_items.remove(obj)
    # >>> erp_rec_delv_line_items

    # <<< erp_poline_items
    # @generated
    def get_erp_poline_items(self):
        """ 
        """
        return self._erp_poline_items

    def set_erp_poline_items(self, value):
        for x in self._erp_poline_items:
            x._material_item = None
        for y in value:
            y._material_item = self
        self._erp_poline_items = value

    erp_poline_items = property(get_erp_poline_items, set_erp_poline_items)

    def add_erp_poline_items(self, *erp_poline_items):
        for obj in erp_poline_items:
            obj._material_item = self
            self._erp_poline_items.append(obj)

    def remove_erp_poline_items(self, *erp_poline_items):
        for obj in erp_poline_items:
            obj._material_item = None
            self._erp_poline_items.remove(obj)
    # >>> erp_poline_items

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            filtered = [x for x in self.work_cost_detail.material_items if x != self]
            self._work_cost_detail._material_items = filtered

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._material_items.append(self)

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail

    # <<< type_material
    # @generated
    def get_type_material(self):
        """ 
        """
        return self._type_material

    def set_type_material(self, value):
        if self._type_material is not None:
            filtered = [x for x in self.type_material.material_items if x != self]
            self._type_material._material_items = filtered

        self._type_material = value
        if self._type_material is not None:
            self._type_material._material_items.append(self)

    type_material = property(get_type_material, set_type_material)
    # >>> type_material



class CUContractorItem(IdentifiedObject):
    """ Compatible unit contractor item.
    """
    # <<< cucontractor_item
    # @generated
    def __init__(self, bid_amount=0.0, activity_code='', compatible_units=None, status=None, *args, **kw_args):
        """ Initialises a new 'CUContractorItem' instance.

        @param bid_amount: The amount that a given contractor will charge for performing this unit of work. 
        @param activity_code: Activity code identifies a specific and distinguishable unit of work. 
        @param compatible_units:
        @param status:
        """
        # The amount that a given contractor will charge for performing this unit of work. 
        self.bid_amount = bid_amount

        # Activity code identifies a specific and distinguishable unit of work. 
        self.activity_code = activity_code


        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self.status = status


        super(CUContractorItem, self).__init__(*args, **kw_args)
    # >>> cucontractor_item

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.cucontractor_items if q != self]
            self._compatible_units._cucontractor_items = filtered
        for r in value:
            if self not in r._cucontractor_items:
                r._cucontractor_items.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._cucontractor_items:
                obj._cucontractor_items.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._cucontractor_items:
                obj._cucontractor_items.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< status
    # @generated
    status = None
    # >>> status



class CompatibleUnit(Document):
    """ A pre-planned job model containing labor, material, and accounting requirements for standardized job planning.
    """
    # <<< compatible_unit
    # @generated
    def __init__(self, est_cost=0.0, quantity='', cuwork_equipment_items=None, cucontractor_items=None, procedures=None, cuassets=None, cumaterial_items=None, property_unit=None, culabor_items=None, design_location_cus=None, cuallowable_action=None, cugroup=None, cost_type=None, *args, **kw_args):
        """ Initialises a new 'CompatibleUnit' instance.

        @param est_cost: Estimated total cost for perfoming CU. 
        @param quantity: The quantity, unit of measure, and multiplier at the CU level that applies to the materials. 
        @param cuwork_equipment_items:
        @param cucontractor_items:
        @param procedures:
        @param cuassets:
        @param cumaterial_items:
        @param property_unit:
        @param culabor_items:
        @param design_location_cus:
        @param cuallowable_action:
        @param cugroup:
        @param cost_type:
        """
        # Estimated total cost for perfoming CU. 
        self.est_cost = est_cost

        # The quantity, unit of measure, and multiplier at the CU level that applies to the materials. 
        self.quantity = quantity


        self._cuwork_equipment_items = []
        if cuwork_equipment_items is not None:
            self.cuwork_equipment_items = cuwork_equipment_items
        else:
            self.cuwork_equipment_items = []

        self._cucontractor_items = []
        if cucontractor_items is not None:
            self.cucontractor_items = cucontractor_items
        else:
            self.cucontractor_items = []

        self._procedures = []
        if procedures is not None:
            self.procedures = procedures
        else:
            self.procedures = []

        self._cuassets = []
        if cuassets is not None:
            self.cuassets = cuassets
        else:
            self.cuassets = []

        self._cumaterial_items = []
        if cumaterial_items is not None:
            self.cumaterial_items = cumaterial_items
        else:
            self.cumaterial_items = []

        self._property_unit = None
        self.property_unit = property_unit

        self._culabor_items = []
        if culabor_items is not None:
            self.culabor_items = culabor_items
        else:
            self.culabor_items = []

        self._design_location_cus = []
        if design_location_cus is not None:
            self.design_location_cus = design_location_cus
        else:
            self.design_location_cus = []

        self._cuallowable_action = None
        self.cuallowable_action = cuallowable_action

        self._cugroup = None
        self.cugroup = cugroup

        self._cost_type = None
        self.cost_type = cost_type


        super(CompatibleUnit, self).__init__(*args, **kw_args)
    # >>> compatible_unit

    # <<< cuwork_equipment_items
    # @generated
    def get_cuwork_equipment_items(self):
        """ 
        """
        return self._cuwork_equipment_items

    def set_cuwork_equipment_items(self, value):
        for p in self._cuwork_equipment_items:
            filtered = [q for q in p.compatible_units if q != self]
            self._cuwork_equipment_items._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._cuwork_equipment_items = value

    cuwork_equipment_items = property(get_cuwork_equipment_items, set_cuwork_equipment_items)

    def add_cuwork_equipment_items(self, *cuwork_equipment_items):
        for obj in cuwork_equipment_items:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._cuwork_equipment_items.append(obj)

    def remove_cuwork_equipment_items(self, *cuwork_equipment_items):
        for obj in cuwork_equipment_items:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._cuwork_equipment_items.remove(obj)
    # >>> cuwork_equipment_items

    # <<< cucontractor_items
    # @generated
    def get_cucontractor_items(self):
        """ 
        """
        return self._cucontractor_items

    def set_cucontractor_items(self, value):
        for p in self._cucontractor_items:
            filtered = [q for q in p.compatible_units if q != self]
            self._cucontractor_items._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._cucontractor_items = value

    cucontractor_items = property(get_cucontractor_items, set_cucontractor_items)

    def add_cucontractor_items(self, *cucontractor_items):
        for obj in cucontractor_items:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._cucontractor_items.append(obj)

    def remove_cucontractor_items(self, *cucontractor_items):
        for obj in cucontractor_items:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._cucontractor_items.remove(obj)
    # >>> cucontractor_items

    # <<< procedures
    # @generated
    def get_procedures(self):
        """ 
        """
        return self._procedures

    def set_procedures(self, value):
        for p in self._procedures:
            filtered = [q for q in p.compatible_units if q != self]
            self._procedures._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._procedures = value

    procedures = property(get_procedures, set_procedures)

    def add_procedures(self, *procedures):
        for obj in procedures:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._procedures.append(obj)

    def remove_procedures(self, *procedures):
        for obj in procedures:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._procedures.remove(obj)
    # >>> procedures

    # <<< cuassets
    # @generated
    def get_cuassets(self):
        """ 
        """
        return self._cuassets

    def set_cuassets(self, value):
        for p in self._cuassets:
            filtered = [q for q in p.compatible_units if q != self]
            self._cuassets._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._cuassets = value

    cuassets = property(get_cuassets, set_cuassets)

    def add_cuassets(self, *cuassets):
        for obj in cuassets:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._cuassets.append(obj)

    def remove_cuassets(self, *cuassets):
        for obj in cuassets:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._cuassets.remove(obj)
    # >>> cuassets

    # <<< cumaterial_items
    # @generated
    def get_cumaterial_items(self):
        """ 
        """
        return self._cumaterial_items

    def set_cumaterial_items(self, value):
        for p in self._cumaterial_items:
            filtered = [q for q in p.compatible_units if q != self]
            self._cumaterial_items._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._cumaterial_items = value

    cumaterial_items = property(get_cumaterial_items, set_cumaterial_items)

    def add_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._cumaterial_items.append(obj)

    def remove_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._cumaterial_items.remove(obj)
    # >>> cumaterial_items

    # <<< property_unit
    # @generated
    def get_property_unit(self):
        """ 
        """
        return self._property_unit

    def set_property_unit(self, value):
        if self._property_unit is not None:
            filtered = [x for x in self.property_unit.compatible_units if x != self]
            self._property_unit._compatible_units = filtered

        self._property_unit = value
        if self._property_unit is not None:
            self._property_unit._compatible_units.append(self)

    property_unit = property(get_property_unit, set_property_unit)
    # >>> property_unit

    # <<< culabor_items
    # @generated
    def get_culabor_items(self):
        """ 
        """
        return self._culabor_items

    def set_culabor_items(self, value):
        for p in self._culabor_items:
            filtered = [q for q in p.compatible_units if q != self]
            self._culabor_items._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._culabor_items = value

    culabor_items = property(get_culabor_items, set_culabor_items)

    def add_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._culabor_items.append(obj)

    def remove_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._culabor_items.remove(obj)
    # >>> culabor_items

    # <<< design_location_cus
    # @generated
    def get_design_location_cus(self):
        """ 
        """
        return self._design_location_cus

    def set_design_location_cus(self, value):
        for p in self._design_location_cus:
            filtered = [q for q in p.compatible_units if q != self]
            self._design_location_cus._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._design_location_cus = value

    design_location_cus = property(get_design_location_cus, set_design_location_cus)

    def add_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._design_location_cus.append(obj)

    def remove_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._design_location_cus.remove(obj)
    # >>> design_location_cus

    # <<< cuallowable_action
    # @generated
    def get_cuallowable_action(self):
        """ 
        """
        return self._cuallowable_action

    def set_cuallowable_action(self, value):
        if self._cuallowable_action is not None:
            filtered = [x for x in self.cuallowable_action.compatible_units if x != self]
            self._cuallowable_action._compatible_units = filtered

        self._cuallowable_action = value
        if self._cuallowable_action is not None:
            self._cuallowable_action._compatible_units.append(self)

    cuallowable_action = property(get_cuallowable_action, set_cuallowable_action)
    # >>> cuallowable_action

    # <<< cugroup
    # @generated
    def get_cugroup(self):
        """ 
        """
        return self._cugroup

    def set_cugroup(self, value):
        if self._cugroup is not None:
            filtered = [x for x in self.cugroup.compatible_units if x != self]
            self._cugroup._compatible_units = filtered

        self._cugroup = value
        if self._cugroup is not None:
            self._cugroup._compatible_units.append(self)

    cugroup = property(get_cugroup, set_cugroup)
    # >>> cugroup

    # <<< cost_type
    # @generated
    def get_cost_type(self):
        """ 
        """
        return self._cost_type

    def set_cost_type(self, value):
        if self._cost_type is not None:
            filtered = [x for x in self.cost_type.compatible_units if x != self]
            self._cost_type._compatible_units = filtered

        self._cost_type = value
        if self._cost_type is not None:
            self._cost_type._compatible_units.append(self)

    cost_type = property(get_cost_type, set_cost_type)
    # >>> cost_type



class InfoQuestion(Document):
    """ Questions and answers associated with a type of document for purposes of clarification. Questions may be predefined or ad hoc.
    """
    # <<< info_question
    # @generated
    def __init__(self, question_remark='', answer='', question_category='', question_code='', answer_date_time='', question_text='', answer_remark='', *args, **kw_args):
        """ Initialises a new 'InfoQuestion' instance.

        @param question_remark: Remarks to qualify the question in this situation. 
        @param answer: Answer to question. 
        @param question_category: The category of the question. 
        @param question_code: The question code. If blank, refer to questionText. 
        @param answer_date_time: The date and time the quesiton was answered. 
        @param question_text: For non-coded questions, the question is provided here. 
        @param answer_remark: Remarks to qualify the answer. 
        """
        # Remarks to qualify the question in this situation. 
        self.question_remark = question_remark

        # Answer to question. 
        self.answer = answer

        # The category of the question. 
        self.question_category = question_category

        # The question code. If blank, refer to questionText. 
        self.question_code = question_code

        # The date and time the quesiton was answered. 
        self.answer_date_time = answer_date_time

        # For non-coded questions, the question is provided here. 
        self.question_text = question_text

        # Remarks to qualify the answer. 
        self.answer_remark = answer_remark



        super(InfoQuestion, self).__init__(*args, **kw_args)
    # >>> info_question



class MaintenanceDataSet(ProcedureDataSet):
    """ The result of a maintenance activity, a type of Procedure, for a given attribute of an asset is documentated in an MaintenanceDataSet.
    """
    # <<< maintenance_data_set
    # @generated
    def __init__(self, condition_before='', maint_code='', condition_after='', *args, **kw_args):
        """ Initialises a new 'MaintenanceDataSet' instance.

        @param condition_before: Description of the condition of the asset just prior to maintenance being performed. 
        @param maint_code: Code for the type of maintenance performed. 
        @param condition_after: Condition of asset just following maintenance procedure. 
        """
        # Description of the condition of the asset just prior to maintenance being performed. 
        self.condition_before = condition_before

        # Code for the type of maintenance performed. 
        self.maint_code = maint_code

        # Condition of asset just following maintenance procedure. 
        self.condition_after = condition_after



        super(MaintenanceDataSet, self).__init__(*args, **kw_args)
    # >>> maintenance_data_set



class Regulation(Document):
    """ Special requirements and/or regulations may pertain to certain types of assets or work. For example, fire protection and scaffolding.
    """
    # <<< regulation
    # @generated
    def __init__(self, reference_number='', *args, **kw_args):
        """ Initialises a new 'Regulation' instance.

        @param reference_number: External reference to regulation, if applicable. 
        """
        # External reference to regulation, if applicable. 
        self.reference_number = reference_number



        super(Regulation, self).__init__(*args, **kw_args)
    # >>> regulation



class Usage(IdentifiedObject):
    """ The way material and assets are used to perform a certain type of work task. The way is described in text in the inheritied description attribute.
    """
    # <<< usage
    # @generated
    def __init__(self, material_item=None, work_task=None, status=None, work_equipment_asset=None, *args, **kw_args):
        """ Initialises a new 'Usage' instance.

        @param material_item:
        @param work_task:
        @param status:
        @param work_equipment_asset:
        """

        self._material_item = None
        self.material_item = material_item

        self._work_task = None
        self.work_task = work_task

        self.status = status

        self._work_equipment_asset = None
        self.work_equipment_asset = work_equipment_asset


        super(Usage, self).__init__(*args, **kw_args)
    # >>> usage

    # <<< material_item
    # @generated
    def get_material_item(self):
        """ 
        """
        return self._material_item

    def set_material_item(self, value):
        if self._material_item is not None:
            filtered = [x for x in self.material_item.usages if x != self]
            self._material_item._usages = filtered

        self._material_item = value
        if self._material_item is not None:
            self._material_item._usages.append(self)

    material_item = property(get_material_item, set_material_item)
    # >>> material_item

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.usages if x != self]
            self._work_task._usages = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._usages.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< work_equipment_asset
    # @generated
    def get_work_equipment_asset(self):
        """ 
        """
        return self._work_equipment_asset

    def set_work_equipment_asset(self, value):
        if self._work_equipment_asset is not None:
            filtered = [x for x in self.work_equipment_asset.usages if x != self]
            self._work_equipment_asset._usages = filtered

        self._work_equipment_asset = value
        if self._work_equipment_asset is not None:
            self._work_equipment_asset._usages.append(self)

    work_equipment_asset = property(get_work_equipment_asset, set_work_equipment_asset)
    # >>> work_equipment_asset



class AccessPermit(Document):
    """ A permit is sometimes needed to provide legal access to land or equipment. For example, local authority permission for road works.
    """
    # <<< access_permit
    # @generated
    def __init__(self, payment=0.0, application_number='', expiration_date='', effective_date='', permit_id='', *args, **kw_args):
        """ Initialises a new 'AccessPermit' instance.

        @param payment: Total cost of permit. 
        @param application_number: Permit application number that is used by municipality, state, province, etc. 
        @param expiration_date: Permit expiration date. 
        @param effective_date: Date that permit became official. 
        @param permit_id: Permit identifier. 
        """
        # Total cost of permit. 
        self.payment = payment

        # Permit application number that is used by municipality, state, province, etc. 
        self.application_number = application_number

        # Permit expiration date. 
        self.expiration_date = expiration_date

        # Date that permit became official. 
        self.effective_date = effective_date

        # Permit identifier. 
        self.permit_id = permit_id



        super(AccessPermit, self).__init__(*args, **kw_args)
    # >>> access_permit



class WorkStatusEntry(ActivityRecord):
    """ A type of ActivityRecord that records information about the status of an item, such as a Work or WorkTask, at a point in time.
    """
    # <<< work_status_entry
    # @generated
    def __init__(self, percent_complete=0.0, *args, **kw_args):
        """ Initialises a new 'WorkStatusEntry' instance.

        @param percent_complete: Estimated percentage of completion of this individual work task or overall work order. 
        """
        # Estimated percentage of completion of this individual work task or overall work order. 
        self.percent_complete = percent_complete



        super(WorkStatusEntry, self).__init__(*args, **kw_args)
    # >>> work_status_entry



class WorkTask(Document):
    """ A set of tasks is required to implement a design.
    """
    # <<< work_task
    # @generated
    def __init__(self, sched_override='', priority='', contractor_items=None, crews=None, work_cost_details=None, usages=None, qualification_requirements=None, work=None, work_flow_step=None, labor_items=None, material_items=None, equipment_items=None, design_location_cus=None, overhead_cost=None, assets=None, capabilities=None, misc_cost_items=None, switching_schedules=None, design=None, *args, **kw_args):
        """ Initialises a new 'WorkTask' instance.

        @param sched_override: If specified, override schedule and perform this task in accordance with instructions specified here. 
        @param priority: The priority of this work task. 
        @param contractor_items:
        @param crews: All Crews participating in this WorkTask.
        @param work_cost_details:
        @param usages:
        @param qualification_requirements:
        @param work:
        @param work_flow_step:
        @param labor_items:
        @param material_items:
        @param equipment_items:
        @param design_location_cus:
        @param overhead_cost:
        @param assets:
        @param capabilities:
        @param misc_cost_items:
        @param switching_schedules:
        @param design:
        """
        # If specified, override schedule and perform this task in accordance with instructions specified here. 
        self.sched_override = sched_override

        # The priority of this work task. 
        self.priority = priority


        self._contractor_items = []
        if contractor_items is not None:
            self.contractor_items = contractor_items
        else:
            self.contractor_items = []

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []

        self._usages = []
        if usages is not None:
            self.usages = usages
        else:
            self.usages = []

        self._qualification_requirements = []
        if qualification_requirements is not None:
            self.qualification_requirements = qualification_requirements
        else:
            self.qualification_requirements = []

        self._work = None
        self.work = work

        self._work_flow_step = None
        self.work_flow_step = work_flow_step

        self._labor_items = []
        if labor_items is not None:
            self.labor_items = labor_items
        else:
            self.labor_items = []

        self._material_items = []
        if material_items is not None:
            self.material_items = material_items
        else:
            self.material_items = []

        self._equipment_items = []
        if equipment_items is not None:
            self.equipment_items = equipment_items
        else:
            self.equipment_items = []

        self._design_location_cus = []
        if design_location_cus is not None:
            self.design_location_cus = design_location_cus
        else:
            self.design_location_cus = []

        self._overhead_cost = None
        self.overhead_cost = overhead_cost

        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []

        self._capabilities = []
        if capabilities is not None:
            self.capabilities = capabilities
        else:
            self.capabilities = []

        self._misc_cost_items = []
        if misc_cost_items is not None:
            self.misc_cost_items = misc_cost_items
        else:
            self.misc_cost_items = []

        self._switching_schedules = []
        if switching_schedules is not None:
            self.switching_schedules = switching_schedules
        else:
            self.switching_schedules = []

        self._design = None
        self.design = design


        super(WorkTask, self).__init__(*args, **kw_args)
    # >>> work_task

    # <<< contractor_items
    # @generated
    def get_contractor_items(self):
        """ 
        """
        return self._contractor_items

    def set_contractor_items(self, value):
        for x in self._contractor_items:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._contractor_items = value

    contractor_items = property(get_contractor_items, set_contractor_items)

    def add_contractor_items(self, *contractor_items):
        for obj in contractor_items:
            obj._work_task = self
            self._contractor_items.append(obj)

    def remove_contractor_items(self, *contractor_items):
        for obj in contractor_items:
            obj._work_task = None
            self._contractor_items.remove(obj)
    # >>> contractor_items

    # <<< crews
    # @generated
    def get_crews(self):
        """ All Crews participating in this WorkTask.
        """
        return self._crews

    def set_crews(self, value):
        for p in self._crews:
            filtered = [q for q in p.work_tasks if q != self]
            self._crews._work_tasks = filtered
        for r in value:
            if self not in r._work_tasks:
                r._work_tasks.append(self)
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            if self not in obj._work_tasks:
                obj._work_tasks.append(self)
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            if self in obj._work_tasks:
                obj._work_tasks.remove(self)
            self._crews.remove(obj)
    # >>> crews

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for x in self._work_cost_details:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._work_task = self
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._work_task = None
            self._work_cost_details.remove(obj)
    # >>> work_cost_details

    # <<< usages
    # @generated
    def get_usages(self):
        """ 
        """
        return self._usages

    def set_usages(self, value):
        for x in self._usages:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._usages = value

    usages = property(get_usages, set_usages)

    def add_usages(self, *usages):
        for obj in usages:
            obj._work_task = self
            self._usages.append(obj)

    def remove_usages(self, *usages):
        for obj in usages:
            obj._work_task = None
            self._usages.remove(obj)
    # >>> usages

    # <<< qualification_requirements
    # @generated
    def get_qualification_requirements(self):
        """ 
        """
        return self._qualification_requirements

    def set_qualification_requirements(self, value):
        for p in self._qualification_requirements:
            filtered = [q for q in p.work_tasks if q != self]
            self._qualification_requirements._work_tasks = filtered
        for r in value:
            if self not in r._work_tasks:
                r._work_tasks.append(self)
        self._qualification_requirements = value

    qualification_requirements = property(get_qualification_requirements, set_qualification_requirements)

    def add_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self not in obj._work_tasks:
                obj._work_tasks.append(self)
            self._qualification_requirements.append(obj)

    def remove_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self in obj._work_tasks:
                obj._work_tasks.remove(self)
            self._qualification_requirements.remove(obj)
    # >>> qualification_requirements

    # <<< work
    # @generated
    def get_work(self):
        """ 
        """
        return self._work

    def set_work(self, value):
        if self._work is not None:
            filtered = [x for x in self.work.work_tasks if x != self]
            self._work._work_tasks = filtered

        self._work = value
        if self._work is not None:
            self._work._work_tasks.append(self)

    work = property(get_work, set_work)
    # >>> work

    # <<< work_flow_step
    # @generated
    def get_work_flow_step(self):
        """ 
        """
        return self._work_flow_step

    def set_work_flow_step(self, value):
        if self._work_flow_step is not None:
            filtered = [x for x in self.work_flow_step.work_tasks if x != self]
            self._work_flow_step._work_tasks = filtered

        self._work_flow_step = value
        if self._work_flow_step is not None:
            self._work_flow_step._work_tasks.append(self)

    work_flow_step = property(get_work_flow_step, set_work_flow_step)
    # >>> work_flow_step

    # <<< labor_items
    # @generated
    def get_labor_items(self):
        """ 
        """
        return self._labor_items

    def set_labor_items(self, value):
        for x in self._labor_items:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._labor_items = value

    labor_items = property(get_labor_items, set_labor_items)

    def add_labor_items(self, *labor_items):
        for obj in labor_items:
            obj._work_task = self
            self._labor_items.append(obj)

    def remove_labor_items(self, *labor_items):
        for obj in labor_items:
            obj._work_task = None
            self._labor_items.remove(obj)
    # >>> labor_items

    # <<< material_items
    # @generated
    def get_material_items(self):
        """ 
        """
        return self._material_items

    def set_material_items(self, value):
        for x in self._material_items:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._material_items = value

    material_items = property(get_material_items, set_material_items)

    def add_material_items(self, *material_items):
        for obj in material_items:
            obj._work_task = self
            self._material_items.append(obj)

    def remove_material_items(self, *material_items):
        for obj in material_items:
            obj._work_task = None
            self._material_items.remove(obj)
    # >>> material_items

    # <<< equipment_items
    # @generated
    def get_equipment_items(self):
        """ 
        """
        return self._equipment_items

    def set_equipment_items(self, value):
        for x in self._equipment_items:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._equipment_items = value

    equipment_items = property(get_equipment_items, set_equipment_items)

    def add_equipment_items(self, *equipment_items):
        for obj in equipment_items:
            obj._work_task = self
            self._equipment_items.append(obj)

    def remove_equipment_items(self, *equipment_items):
        for obj in equipment_items:
            obj._work_task = None
            self._equipment_items.remove(obj)
    # >>> equipment_items

    # <<< design_location_cus
    # @generated
    def get_design_location_cus(self):
        """ 
        """
        return self._design_location_cus

    def set_design_location_cus(self, value):
        for p in self._design_location_cus:
            filtered = [q for q in p.work_tasks if q != self]
            self._design_location_cus._work_tasks = filtered
        for r in value:
            if self not in r._work_tasks:
                r._work_tasks.append(self)
        self._design_location_cus = value

    design_location_cus = property(get_design_location_cus, set_design_location_cus)

    def add_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self not in obj._work_tasks:
                obj._work_tasks.append(self)
            self._design_location_cus.append(obj)

    def remove_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self in obj._work_tasks:
                obj._work_tasks.remove(self)
            self._design_location_cus.remove(obj)
    # >>> design_location_cus

    # <<< overhead_cost
    # @generated
    def get_overhead_cost(self):
        """ 
        """
        return self._overhead_cost

    def set_overhead_cost(self, value):
        if self._overhead_cost is not None:
            filtered = [x for x in self.overhead_cost.work_tasks if x != self]
            self._overhead_cost._work_tasks = filtered

        self._overhead_cost = value
        if self._overhead_cost is not None:
            self._overhead_cost._work_tasks.append(self)

    overhead_cost = property(get_overhead_cost, set_overhead_cost)
    # >>> overhead_cost

    # <<< assets
    # @generated
    def get_assets(self):
        """ 
        """
        return self._assets

    def set_assets(self, value):
        for x in self._assets:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            obj._work_task = self
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            obj._work_task = None
            self._assets.remove(obj)
    # >>> assets

    # <<< capabilities
    # @generated
    def get_capabilities(self):
        """ 
        """
        return self._capabilities

    def set_capabilities(self, value):
        for p in self._capabilities:
            filtered = [q for q in p.work_tasks if q != self]
            self._capabilities._work_tasks = filtered
        for r in value:
            if self not in r._work_tasks:
                r._work_tasks.append(self)
        self._capabilities = value

    capabilities = property(get_capabilities, set_capabilities)

    def add_capabilities(self, *capabilities):
        for obj in capabilities:
            if self not in obj._work_tasks:
                obj._work_tasks.append(self)
            self._capabilities.append(obj)

    def remove_capabilities(self, *capabilities):
        for obj in capabilities:
            if self in obj._work_tasks:
                obj._work_tasks.remove(self)
            self._capabilities.remove(obj)
    # >>> capabilities

    # <<< misc_cost_items
    # @generated
    def get_misc_cost_items(self):
        """ 
        """
        return self._misc_cost_items

    def set_misc_cost_items(self, value):
        for x in self._misc_cost_items:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._misc_cost_items = value

    misc_cost_items = property(get_misc_cost_items, set_misc_cost_items)

    def add_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._work_task = self
            self._misc_cost_items.append(obj)

    def remove_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._work_task = None
            self._misc_cost_items.remove(obj)
    # >>> misc_cost_items

    # <<< switching_schedules
    # @generated
    def get_switching_schedules(self):
        """ 
        """
        return self._switching_schedules

    def set_switching_schedules(self, value):
        for x in self._switching_schedules:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._switching_schedules = value

    switching_schedules = property(get_switching_schedules, set_switching_schedules)

    def add_switching_schedules(self, *switching_schedules):
        for obj in switching_schedules:
            obj._work_task = self
            self._switching_schedules.append(obj)

    def remove_switching_schedules(self, *switching_schedules):
        for obj in switching_schedules:
            obj._work_task = None
            self._switching_schedules.remove(obj)
    # >>> switching_schedules

    # <<< design
    # @generated
    def get_design(self):
        """ 
        """
        return self._design

    def set_design(self, value):
        if self._design is not None:
            filtered = [x for x in self.design.work_tasks if x != self]
            self._design._work_tasks = filtered

        self._design = value
        if self._design is not None:
            self._design._work_tasks.append(self)

    design = property(get_design, set_design)
    # >>> design



class Request(Document):
    """ A request for work, service or project.
    """
    # <<< request
    # @generated
    def __init__(self, corporate_code='', priority='', action_needed='', organisation=None, projects=None, erp_quote_line_item=None, works=None, *args, **kw_args):
        """ Initialises a new 'Request' instance.

        @param corporate_code: The corporate code for this request. 
        @param priority: The priority of this request. 
        @param action_needed: Based on the current 'Status.status', the action that is needed before this Request can transition to the desired state, such as initiating the requested Work. For example, missing or additionally needed information may be required from the requesting organisation before a work Design may be created. 
        @param organisation:
        @param projects:
        @param erp_quote_line_item:
        @param works:
        """
        # The corporate code for this request. 
        self.corporate_code = corporate_code

        # The priority of this request. 
        self.priority = priority

        # Based on the current 'Status.status', the action that is needed before this Request can transition to the desired state, such as initiating the requested Work. For example, missing or additionally needed information may be required from the requesting organisation before a work Design may be created. 
        self.action_needed = action_needed


        self._organisation = None
        self.organisation = organisation

        self._projects = []
        if projects is not None:
            self.projects = projects
        else:
            self.projects = []

        self._erp_quote_line_item = None
        self.erp_quote_line_item = erp_quote_line_item

        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []


        super(Request, self).__init__(*args, **kw_args)
    # >>> request

    # <<< organisation
    # @generated
    def get_organisation(self):
        """ 
        """
        return self._organisation

    def set_organisation(self, value):
        if self._organisation is not None:
            filtered = [x for x in self.organisation.requests if x != self]
            self._organisation._requests = filtered

        self._organisation = value
        if self._organisation is not None:
            self._organisation._requests.append(self)

    organisation = property(get_organisation, set_organisation)
    # >>> organisation

    # <<< projects
    # @generated
    def get_projects(self):
        """ 
        """
        return self._projects

    def set_projects(self, value):
        for p in self._projects:
            filtered = [q for q in p.requests if q != self]
            self._projects._requests = filtered
        for r in value:
            if self not in r._requests:
                r._requests.append(self)
        self._projects = value

    projects = property(get_projects, set_projects)

    def add_projects(self, *projects):
        for obj in projects:
            if self not in obj._requests:
                obj._requests.append(self)
            self._projects.append(obj)

    def remove_projects(self, *projects):
        for obj in projects:
            if self in obj._requests:
                obj._requests.remove(self)
            self._projects.remove(obj)
    # >>> projects

    # <<< erp_quote_line_item
    # @generated
    def get_erp_quote_line_item(self):
        """ 
        """
        return self._erp_quote_line_item

    def set_erp_quote_line_item(self, value):
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._request = None

        self._erp_quote_line_item = value
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._request = self

    erp_quote_line_item = property(get_erp_quote_line_item, set_erp_quote_line_item)
    # >>> erp_quote_line_item

    # <<< works
    # @generated
    def get_works(self):
        """ 
        """
        return self._works

    def set_works(self, value):
        for x in self._works:
            x._request = None
        for y in value:
            y._request = self
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            obj._request = self
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            obj._request = None
            self._works.remove(obj)
    # >>> works



class CUAllowableAction(IdentifiedObject):
    """ Allowed actions: Install, Remove, Transfer, Abandon, etc.
    """
    # <<< cuallowable_action
    # @generated
    def __init__(self, compatible_units=None, status=None, *args, **kw_args):
        """ Initialises a new 'CUAllowableAction' instance.

        @param compatible_units:
        @param status:
        """

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self.status = status


        super(CUAllowableAction, self).__init__(*args, **kw_args)
    # >>> cuallowable_action

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for x in self._compatible_units:
            x._cuallowable_action = None
        for y in value:
            y._cuallowable_action = self
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cuallowable_action = self
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cuallowable_action = None
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< status
    # @generated
    status = None
    # >>> status



class Project(Document):
    """ A collection of related work. For construction projects and maintenance projects, multiple phases may be performed.
    """
    # <<< project
    # @generated
    def __init__(self, budget=0.0, erp_project_accounting=None, works=None, business_case=None, requests=None, parent_project=None, sub_projects=None, *args, **kw_args):
        """ Initialises a new 'Project' instance.

        @param budget: Overall project budget. 
        @param erp_project_accounting:
        @param works:
        @param business_case:
        @param requests:
        @param parent_project:
        @param sub_projects:
        """
        # Overall project budget. 
        self.budget = budget


        self._erp_project_accounting = None
        self.erp_project_accounting = erp_project_accounting

        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []

        self._business_case = None
        self.business_case = business_case

        self._requests = []
        if requests is not None:
            self.requests = requests
        else:
            self.requests = []

        self._parent_project = None
        self.parent_project = parent_project

        self._sub_projects = []
        if sub_projects is not None:
            self.sub_projects = sub_projects
        else:
            self.sub_projects = []


        super(Project, self).__init__(*args, **kw_args)
    # >>> project

    # <<< erp_project_accounting
    # @generated
    def get_erp_project_accounting(self):
        """ 
        """
        return self._erp_project_accounting

    def set_erp_project_accounting(self, value):
        if self._erp_project_accounting is not None:
            filtered = [x for x in self.erp_project_accounting.projects if x != self]
            self._erp_project_accounting._projects = filtered

        self._erp_project_accounting = value
        if self._erp_project_accounting is not None:
            self._erp_project_accounting._projects.append(self)

    erp_project_accounting = property(get_erp_project_accounting, set_erp_project_accounting)
    # >>> erp_project_accounting

    # <<< works
    # @generated
    def get_works(self):
        """ 
        """
        return self._works

    def set_works(self, value):
        for x in self._works:
            x._project = None
        for y in value:
            y._project = self
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            obj._project = self
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            obj._project = None
            self._works.remove(obj)
    # >>> works

    # <<< business_case
    # @generated
    def get_business_case(self):
        """ 
        """
        return self._business_case

    def set_business_case(self, value):
        if self._business_case is not None:
            filtered = [x for x in self.business_case.projects if x != self]
            self._business_case._projects = filtered

        self._business_case = value
        if self._business_case is not None:
            self._business_case._projects.append(self)

    business_case = property(get_business_case, set_business_case)
    # >>> business_case

    # <<< requests
    # @generated
    def get_requests(self):
        """ 
        """
        return self._requests

    def set_requests(self, value):
        for p in self._requests:
            filtered = [q for q in p.projects if q != self]
            self._requests._projects = filtered
        for r in value:
            if self not in r._projects:
                r._projects.append(self)
        self._requests = value

    requests = property(get_requests, set_requests)

    def add_requests(self, *requests):
        for obj in requests:
            if self not in obj._projects:
                obj._projects.append(self)
            self._requests.append(obj)

    def remove_requests(self, *requests):
        for obj in requests:
            if self in obj._projects:
                obj._projects.remove(self)
            self._requests.remove(obj)
    # >>> requests

    # <<< parent_project
    # @generated
    def get_parent_project(self):
        """ 
        """
        return self._parent_project

    def set_parent_project(self, value):
        if self._parent_project is not None:
            filtered = [x for x in self.parent_project.sub_projects if x != self]
            self._parent_project._sub_projects = filtered

        self._parent_project = value
        if self._parent_project is not None:
            self._parent_project._sub_projects.append(self)

    parent_project = property(get_parent_project, set_parent_project)
    # >>> parent_project

    # <<< sub_projects
    # @generated
    def get_sub_projects(self):
        """ 
        """
        return self._sub_projects

    def set_sub_projects(self, value):
        for x in self._sub_projects:
            x._parent_project = None
        for y in value:
            y._parent_project = self
        self._sub_projects = value

    sub_projects = property(get_sub_projects, set_sub_projects)

    def add_sub_projects(self, *sub_projects):
        for obj in sub_projects:
            obj._parent_project = self
            self._sub_projects.append(obj)

    def remove_sub_projects(self, *sub_projects):
        for obj in sub_projects:
            obj._parent_project = None
            self._sub_projects.remove(obj)
    # >>> sub_projects



class CUAsset(IdentifiedObject):
    """ Compatible unit for various types of assets such as transformers switches, substation fences, poles, etc..
    """
    # <<< cuasset
    # @generated
    def __init__(self, quantity=0, type_asset_code='', compatible_units=None, type_asset=None, status=None, *args, **kw_args):
        """ Initialises a new 'CUAsset' instance.

        @param quantity: Quantity of the type asset within the CU. 
        @param type_asset_code: The code for this type of asset. 
        @param compatible_units:
        @param type_asset:
        @param status:
        """
        # Quantity of the type asset within the CU. 
        self.quantity = quantity

        # The code for this type of asset. 
        self.type_asset_code = type_asset_code


        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self._type_asset = None
        self.type_asset = type_asset

        self.status = status


        super(CUAsset, self).__init__(*args, **kw_args)
    # >>> cuasset

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.cuassets if q != self]
            self._compatible_units._cuassets = filtered
        for r in value:
            if self not in r._cuassets:
                r._cuassets.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._cuassets:
                obj._cuassets.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._cuassets:
                obj._cuassets.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< type_asset
    # @generated
    def get_type_asset(self):
        """ 
        """
        return self._type_asset

    def set_type_asset(self, value):
        if self._type_asset is not None:
            self._type_asset._cuasset = None

        self._type_asset = value
        if self._type_asset is not None:
            self._type_asset._cuasset = self

    type_asset = property(get_type_asset, set_type_asset)
    # >>> type_asset

    # <<< status
    # @generated
    status = None
    # >>> status



class PropertyUnit(IdentifiedObject):
    """ Unit of property for reporting purposes.
    """
    # <<< property_unit
    # @generated
    def __init__(self, activity_code='install', accounting_usage='', property_account='', cumaterial_items=None, compatible_units=None, status=None, work_cost_details=None, *args, **kw_args):
        """ Initialises a new 'PropertyUnit' instance.

        @param activity_code: Activity code identifies a specific and distinguishable work action. Values are: "install", "remove", "transfer", "abandon"
        @param accounting_usage: A code that identifies appropriate type of property accounts such as distribution, streetlgihts, communications. 
        @param property_account: Used for property record accounting. For example, in the USA, this would be a FERC account. 
        @param cumaterial_items:
        @param compatible_units:
        @param status:
        @param work_cost_details:
        """
        # Activity code identifies a specific and distinguishable work action. Values are: "install", "remove", "transfer", "abandon"
        self.activity_code = activity_code

        # A code that identifies appropriate type of property accounts such as distribution, streetlgihts, communications. 
        self.accounting_usage = accounting_usage

        # Used for property record accounting. For example, in the USA, this would be a FERC account. 
        self.property_account = property_account


        self._cumaterial_items = []
        if cumaterial_items is not None:
            self.cumaterial_items = cumaterial_items
        else:
            self.cumaterial_items = []

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self.status = status

        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []


        super(PropertyUnit, self).__init__(*args, **kw_args)
    # >>> property_unit

    # <<< cumaterial_items
    # @generated
    def get_cumaterial_items(self):
        """ 
        """
        return self._cumaterial_items

    def set_cumaterial_items(self, value):
        for p in self._cumaterial_items:
            filtered = [q for q in p.property_units if q != self]
            self._cumaterial_items._property_units = filtered
        for r in value:
            if self not in r._property_units:
                r._property_units.append(self)
        self._cumaterial_items = value

    cumaterial_items = property(get_cumaterial_items, set_cumaterial_items)

    def add_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            if self not in obj._property_units:
                obj._property_units.append(self)
            self._cumaterial_items.append(obj)

    def remove_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            if self in obj._property_units:
                obj._property_units.remove(self)
            self._cumaterial_items.remove(obj)
    # >>> cumaterial_items

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for x in self._compatible_units:
            x._property_unit = None
        for y in value:
            y._property_unit = self
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._property_unit = self
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._property_unit = None
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for p in self._work_cost_details:
            filtered = [q for q in p.property_units if q != self]
            self._work_cost_details._property_units = filtered
        for r in value:
            if self not in r._property_units:
                r._property_units.append(self)
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            if self not in obj._property_units:
                obj._property_units.append(self)
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            if self in obj._property_units:
                obj._property_units.remove(self)
            self._work_cost_details.remove(obj)
    # >>> work_cost_details



class InspectionDataSet(ProcedureDataSet):
    """ Documents the result of one inspection, a type of Procedure, for a given attribute of an asset.
    """
    # <<< inspection_data_set
    # @generated
    def __init__(self, location_condition='', according_to_schedules=None, *args, **kw_args):
        """ Initialises a new 'InspectionDataSet' instance.

        @param location_condition: Description of the conditions of the location where the asset resides. 
        @param according_to_schedules:
        """
        # Description of the conditions of the location where the asset resides. 
        self.location_condition = location_condition


        self._according_to_schedules = []
        if according_to_schedules is not None:
            self.according_to_schedules = according_to_schedules
        else:
            self.according_to_schedules = []


        super(InspectionDataSet, self).__init__(*args, **kw_args)
    # >>> inspection_data_set

    # <<< according_to_schedules
    # @generated
    def get_according_to_schedules(self):
        """ 
        """
        return self._according_to_schedules

    def set_according_to_schedules(self, value):
        for x in self._according_to_schedules:
            x._for_inspection_data_set = None
        for y in value:
            y._for_inspection_data_set = self
        self._according_to_schedules = value

    according_to_schedules = property(get_according_to_schedules, set_according_to_schedules)

    def add_according_to_schedules(self, *according_to_schedules):
        for obj in according_to_schedules:
            obj._for_inspection_data_set = self
            self._according_to_schedules.append(obj)

    def remove_according_to_schedules(self, *according_to_schedules):
        for obj in according_to_schedules:
            obj._for_inspection_data_set = None
            self._according_to_schedules.remove(obj)
    # >>> according_to_schedules



class CostType(IdentifiedObject):
    """ A categorization for resources, often costs, in accounting transactions. Examples include: material components, building in service, coal sales, overhead, etc.
    """
    # <<< cost_type
    # @generated
    def __init__(self, code='', amount_assignment_flag=False, level='', stage='', work_cost_details=None, erp_journal_entries=None, child_cost_types=None, parent_cost_type=None, status=None, compatible_units=None, *args, **kw_args):
        """ Initialises a new 'CostType' instance.

        @param code: A codified representation of the resource element. 
        @param amount_assignment_flag: True if an amount can be assigned to the resource element (e.g., building in service, transmission plant, software development capital); false otherwise (e.g., internal labor, material components). 
        @param level: The level of the resource element in the hierarchy of resource elements (recursive relationship). 
        @param stage: The stage for which this costType applies: estimated design, estimated actual or actual actual. 
        @param work_cost_details:
        @param erp_journal_entries:
        @param child_cost_types:
        @param parent_cost_type:
        @param status:
        @param compatible_units:
        """
        # A codified representation of the resource element. 
        self.code = code

        # True if an amount can be assigned to the resource element (e.g., building in service, transmission plant, software development capital); false otherwise (e.g., internal labor, material components). 
        self.amount_assignment_flag = amount_assignment_flag

        # The level of the resource element in the hierarchy of resource elements (recursive relationship). 
        self.level = level

        # The stage for which this costType applies: estimated design, estimated actual or actual actual. 
        self.stage = stage


        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []

        self._erp_journal_entries = []
        if erp_journal_entries is not None:
            self.erp_journal_entries = erp_journal_entries
        else:
            self.erp_journal_entries = []

        self._child_cost_types = []
        if child_cost_types is not None:
            self.child_cost_types = child_cost_types
        else:
            self.child_cost_types = []

        self._parent_cost_type = None
        self.parent_cost_type = parent_cost_type

        self.status = status

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []


        super(CostType, self).__init__(*args, **kw_args)
    # >>> cost_type

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for x in self._work_cost_details:
            x._cost_type = None
        for y in value:
            y._cost_type = self
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._cost_type = self
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._cost_type = None
            self._work_cost_details.remove(obj)
    # >>> work_cost_details

    # <<< erp_journal_entries
    # @generated
    def get_erp_journal_entries(self):
        """ 
        """
        return self._erp_journal_entries

    def set_erp_journal_entries(self, value):
        for p in self._erp_journal_entries:
            filtered = [q for q in p.cost_types if q != self]
            self._erp_journal_entries._cost_types = filtered
        for r in value:
            if self not in r._cost_types:
                r._cost_types.append(self)
        self._erp_journal_entries = value

    erp_journal_entries = property(get_erp_journal_entries, set_erp_journal_entries)

    def add_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            if self not in obj._cost_types:
                obj._cost_types.append(self)
            self._erp_journal_entries.append(obj)

    def remove_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            if self in obj._cost_types:
                obj._cost_types.remove(self)
            self._erp_journal_entries.remove(obj)
    # >>> erp_journal_entries

    # <<< child_cost_types
    # @generated
    def get_child_cost_types(self):
        """ 
        """
        return self._child_cost_types

    def set_child_cost_types(self, value):
        for x in self._child_cost_types:
            x._parent_cost_type = None
        for y in value:
            y._parent_cost_type = self
        self._child_cost_types = value

    child_cost_types = property(get_child_cost_types, set_child_cost_types)

    def add_child_cost_types(self, *child_cost_types):
        for obj in child_cost_types:
            obj._parent_cost_type = self
            self._child_cost_types.append(obj)

    def remove_child_cost_types(self, *child_cost_types):
        for obj in child_cost_types:
            obj._parent_cost_type = None
            self._child_cost_types.remove(obj)
    # >>> child_cost_types

    # <<< parent_cost_type
    # @generated
    def get_parent_cost_type(self):
        """ 
        """
        return self._parent_cost_type

    def set_parent_cost_type(self, value):
        if self._parent_cost_type is not None:
            filtered = [x for x in self.parent_cost_type.child_cost_types if x != self]
            self._parent_cost_type._child_cost_types = filtered

        self._parent_cost_type = value
        if self._parent_cost_type is not None:
            self._parent_cost_type._child_cost_types.append(self)

    parent_cost_type = property(get_parent_cost_type, set_parent_cost_type)
    # >>> parent_cost_type

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for x in self._compatible_units:
            x._cost_type = None
        for y in value:
            y._cost_type = self
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cost_type = self
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cost_type = None
            self._compatible_units.remove(obj)
    # >>> compatible_units



class WorkCostSummary(Document):
    """ A roll up by cost category for the entire cost of a work order. For example, total labor.
    """
    # <<< work_cost_summary
    # @generated
    def __init__(self, work_cost_detail=None, *args, **kw_args):
        """ Initialises a new 'WorkCostSummary' instance.

        @param work_cost_detail:
        """

        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail


        super(WorkCostSummary, self).__init__(*args, **kw_args)
    # >>> work_cost_summary

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            self._work_cost_detail._work_cost_summary = None

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._work_cost_summary = self

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail



class MiscCostItem(IdentifiedObject):
    """ Various cost items that are not associated with compatible units. Examples include rental equipment, labor, materials, contractor costs, permits - anything not covered in a CU.
    """
    # <<< misc_cost_item
    # @generated
    def __init__(self, cost_per_unit=0.0, external_ref_id='', cost_type='', quantity=0, account='', work_cost_detail=None, design_location=None, work_task=None, status=None, *args, **kw_args):
        """ Initialises a new 'MiscCostItem' instance.

        @param cost_per_unit: The cost per unit for this misc. item. 
        @param external_ref_id: External Reference ID (e.g. PO#, Serial #) 
        @param cost_type: The cost category for accounting, such as material, labor, vehicle, contractor, equipment, overhead. 
        @param quantity: The quantity of the misc. item being assigned to this location. 
        @param account: This drives the accounting treatment for this misc. item. 
        @param work_cost_detail:
        @param design_location:
        @param work_task:
        @param status:
        """
        # The cost per unit for this misc. item. 
        self.cost_per_unit = cost_per_unit

        # External Reference ID (e.g. PO#, Serial #) 
        self.external_ref_id = external_ref_id

        # The cost category for accounting, such as material, labor, vehicle, contractor, equipment, overhead. 
        self.cost_type = cost_type

        # The quantity of the misc. item being assigned to this location. 
        self.quantity = quantity

        # This drives the accounting treatment for this misc. item. 
        self.account = account


        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail

        self._design_location = None
        self.design_location = design_location

        self._work_task = None
        self.work_task = work_task

        self.status = status


        super(MiscCostItem, self).__init__(*args, **kw_args)
    # >>> misc_cost_item

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            filtered = [x for x in self.work_cost_detail.misc_cost_items if x != self]
            self._work_cost_detail._misc_cost_items = filtered

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._misc_cost_items.append(self)

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail

    # <<< design_location
    # @generated
    def get_design_location(self):
        """ 
        """
        return self._design_location

    def set_design_location(self, value):
        if self._design_location is not None:
            filtered = [x for x in self.design_location.misc_cost_items if x != self]
            self._design_location._misc_cost_items = filtered

        self._design_location = value
        if self._design_location is not None:
            self._design_location._misc_cost_items.append(self)

    design_location = property(get_design_location, set_design_location)
    # >>> design_location

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.misc_cost_items if x != self]
            self._work_task._misc_cost_items = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._misc_cost_items.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< status
    # @generated
    status = None
    # >>> status



class CULaborItem(IdentifiedObject):
    """ Compatible unit labor item.
    """
    # <<< culabor_item
    # @generated
    def __init__(self, labor_rate=0.0, activity_code='', labor_duration=0.0, qualification_requirements=None, culabor_code=None, status=None, compatible_units=None, *args, **kw_args):
        """ Initialises a new 'CULaborItem' instance.

        @param labor_rate: The labor rate applied for work. 
        @param activity_code: Activity code identifies a specific and distinguishable unit of work. 
        @param labor_duration: Estimated time to perform work. 
        @param qualification_requirements:
        @param culabor_code:
        @param status:
        @param compatible_units:
        """
        # The labor rate applied for work. 
        self.labor_rate = labor_rate

        # Activity code identifies a specific and distinguishable unit of work. 
        self.activity_code = activity_code

        # Estimated time to perform work. 
        self.labor_duration = labor_duration


        self._qualification_requirements = []
        if qualification_requirements is not None:
            self.qualification_requirements = qualification_requirements
        else:
            self.qualification_requirements = []

        self._culabor_code = None
        self.culabor_code = culabor_code

        self.status = status

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []


        super(CULaborItem, self).__init__(*args, **kw_args)
    # >>> culabor_item

    # <<< qualification_requirements
    # @generated
    def get_qualification_requirements(self):
        """ 
        """
        return self._qualification_requirements

    def set_qualification_requirements(self, value):
        for p in self._qualification_requirements:
            filtered = [q for q in p.culabor_items if q != self]
            self._qualification_requirements._culabor_items = filtered
        for r in value:
            if self not in r._culabor_items:
                r._culabor_items.append(self)
        self._qualification_requirements = value

    qualification_requirements = property(get_qualification_requirements, set_qualification_requirements)

    def add_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self not in obj._culabor_items:
                obj._culabor_items.append(self)
            self._qualification_requirements.append(obj)

    def remove_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self in obj._culabor_items:
                obj._culabor_items.remove(self)
            self._qualification_requirements.remove(obj)
    # >>> qualification_requirements

    # <<< culabor_code
    # @generated
    def get_culabor_code(self):
        """ 
        """
        return self._culabor_code

    def set_culabor_code(self, value):
        if self._culabor_code is not None:
            filtered = [x for x in self.culabor_code.culabor_items if x != self]
            self._culabor_code._culabor_items = filtered

        self._culabor_code = value
        if self._culabor_code is not None:
            self._culabor_code._culabor_items.append(self)

    culabor_code = property(get_culabor_code, set_culabor_code)
    # >>> culabor_code

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.culabor_items if q != self]
            self._compatible_units._culabor_items = filtered
        for r in value:
            if self not in r._culabor_items:
                r._culabor_items.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._culabor_items:
                obj._culabor_items.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._culabor_items:
                obj._culabor_items.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units



class CULaborCode(IdentifiedObject):
    """ Labor code associated with various compatible unit labor items.
    """
    # <<< culabor_code
    # @generated
    def __init__(self, code='', culabor_items=None, status=None, *args, **kw_args):
        """ Initialises a new 'CULaborCode' instance.

        @param code: Labor code. 
        @param culabor_items:
        @param status:
        """
        # Labor code. 
        self.code = code


        self._culabor_items = []
        if culabor_items is not None:
            self.culabor_items = culabor_items
        else:
            self.culabor_items = []

        self.status = status


        super(CULaborCode, self).__init__(*args, **kw_args)
    # >>> culabor_code

    # <<< culabor_items
    # @generated
    def get_culabor_items(self):
        """ 
        """
        return self._culabor_items

    def set_culabor_items(self, value):
        for x in self._culabor_items:
            x._culabor_code = None
        for y in value:
            y._culabor_code = self
        self._culabor_items = value

    culabor_items = property(get_culabor_items, set_culabor_items)

    def add_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            obj._culabor_code = self
            self._culabor_items.append(obj)

    def remove_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            obj._culabor_code = None
            self._culabor_items.remove(obj)
    # >>> culabor_items

    # <<< status
    # @generated
    status = None
    # >>> status



class ShiftPattern(IdentifiedObject):
    """ The patterns of shifts worked by people or crews.
    """
    # <<< shift_pattern
    # @generated
    def __init__(self, cycle_count=0, assignment_type='', validity_interval=None, crews=None, status=None, *args, **kw_args):
        """ Initialises a new 'ShiftPattern' instance.

        @param cycle_count: Number of cycles for a temporary shift. 
        @param assignment_type: Type of assignement intended to be worked on this shift, for example, temporary, standard, etc. 
        @param validity_interval: Date and time interval for which this shift pattern is valid (when it became effective and when it expires).
        @param crews:
        @param status:
        """
        # Number of cycles for a temporary shift. 
        self.cycle_count = cycle_count

        # Type of assignement intended to be worked on this shift, for example, temporary, standard, etc. 
        self.assignment_type = assignment_type


        self.validity_interval = validity_interval

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self.status = status


        super(ShiftPattern, self).__init__(*args, **kw_args)
    # >>> shift_pattern

    # <<< validity_interval
    # @generated
    # Date and time interval for which this shift pattern is valid (when it became effective and when it expires).
    validity_interval = None
    # >>> validity_interval

    # <<< crews
    # @generated
    def get_crews(self):
        """ 
        """
        return self._crews

    def set_crews(self, value):
        for p in self._crews:
            filtered = [q for q in p.shift_patterns if q != self]
            self._crews._shift_patterns = filtered
        for r in value:
            if self not in r._shift_patterns:
                r._shift_patterns.append(self)
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            if self not in obj._shift_patterns:
                obj._shift_patterns.append(self)
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            if self in obj._shift_patterns:
                obj._shift_patterns.remove(self)
            self._crews.remove(obj)
    # >>> crews

    # <<< status
    # @generated
    status = None
    # >>> status



class OverheadCost(IdentifiedObject):
    """ Overhead cost applied to work order.
    """
    # <<< overhead_cost
    # @generated
    def __init__(self, cost=0.0, code='', work_cost_details=None, work_tasks=None, status=None, *args, **kw_args):
        """ Initialises a new 'OverheadCost' instance.

        @param cost: The overhead cost to be applied. 
        @param code: Overhead code. 
        @param work_cost_details:
        @param work_tasks:
        @param status:
        """
        # The overhead cost to be applied. 
        self.cost = cost

        # Overhead code. 
        self.code = code


        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self.status = status


        super(OverheadCost, self).__init__(*args, **kw_args)
    # >>> overhead_cost

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for x in self._work_cost_details:
            x._overhead_cost = None
        for y in value:
            y._overhead_cost = self
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._overhead_cost = self
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._overhead_cost = None
            self._work_cost_details.remove(obj)
    # >>> work_cost_details

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for x in self._work_tasks:
            x._overhead_cost = None
        for y in value:
            y._overhead_cost = self
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._overhead_cost = self
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._overhead_cost = None
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< status
    # @generated
    status = None
    # >>> status



class DesignLocationCU(IdentifiedObject):
    """ Compatible unit at a given design location.
    """
    # <<< design_location_cu
    # @generated
    def __init__(self, cu_action='install', removal_year='', cu_usage='', cu_account='', cu_quantity=0, energization_flag=False, designs=None, design_location=None, cugroups=None, condition_factors=None, work_tasks=None, compatible_units=None, status=None, *args, **kw_args):
        """ Initialises a new 'DesignLocationCU' instance.

        @param cu_action: A code that instructs the crew what action to perform. Values are: "install", "remove", "transfer", "abandon"
        @param removal_year: Year when a CU that represents an asset is removed. 
        @param cu_usage: As the same CU can be used for different purposes and accounting purposes, usage must be specified. Examples include: distribution, transmission, substation. 
        @param cu_account: A code that helps direct accounting (capital, expense, or accounting treatment). 
        @param cu_quantity: The quantity of the CU being assigned to this location. 
        @param energization_flag: True if associated electrical equipment is intended to be energized while work is being performed. 
        @param designs:
        @param design_location:
        @param cugroups:
        @param condition_factors:
        @param work_tasks:
        @param compatible_units:
        @param status:
        """
        # A code that instructs the crew what action to perform. Values are: "install", "remove", "transfer", "abandon"
        self.cu_action = cu_action

        # Year when a CU that represents an asset is removed. 
        self.removal_year = removal_year

        # As the same CU can be used for different purposes and accounting purposes, usage must be specified. Examples include: distribution, transmission, substation. 
        self.cu_usage = cu_usage

        # A code that helps direct accounting (capital, expense, or accounting treatment). 
        self.cu_account = cu_account

        # The quantity of the CU being assigned to this location. 
        self.cu_quantity = cu_quantity

        # True if associated electrical equipment is intended to be energized while work is being performed. 
        self.energization_flag = energization_flag


        self._designs = []
        if designs is not None:
            self.designs = designs
        else:
            self.designs = []

        self._design_location = None
        self.design_location = design_location

        self._cugroups = []
        if cugroups is not None:
            self.cugroups = cugroups
        else:
            self.cugroups = []

        self._condition_factors = []
        if condition_factors is not None:
            self.condition_factors = condition_factors
        else:
            self.condition_factors = []

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self.status = status


        super(DesignLocationCU, self).__init__(*args, **kw_args)
    # >>> design_location_cu

    # <<< designs
    # @generated
    def get_designs(self):
        """ 
        """
        return self._designs

    def set_designs(self, value):
        for p in self._designs:
            filtered = [q for q in p.design_locations_cus if q != self]
            self._designs._design_locations_cus = filtered
        for r in value:
            if self not in r._design_locations_cus:
                r._design_locations_cus.append(self)
        self._designs = value

    designs = property(get_designs, set_designs)

    def add_designs(self, *designs):
        for obj in designs:
            if self not in obj._design_locations_cus:
                obj._design_locations_cus.append(self)
            self._designs.append(obj)

    def remove_designs(self, *designs):
        for obj in designs:
            if self in obj._design_locations_cus:
                obj._design_locations_cus.remove(self)
            self._designs.remove(obj)
    # >>> designs

    # <<< design_location
    # @generated
    def get_design_location(self):
        """ 
        """
        return self._design_location

    def set_design_location(self, value):
        if self._design_location is not None:
            filtered = [x for x in self.design_location.design_location_cus if x != self]
            self._design_location._design_location_cus = filtered

        self._design_location = value
        if self._design_location is not None:
            self._design_location._design_location_cus.append(self)

    design_location = property(get_design_location, set_design_location)
    # >>> design_location

    # <<< cugroups
    # @generated
    def get_cugroups(self):
        """ 
        """
        return self._cugroups

    def set_cugroups(self, value):
        for p in self._cugroups:
            filtered = [q for q in p.design_location_cus if q != self]
            self._cugroups._design_location_cus = filtered
        for r in value:
            if self not in r._design_location_cus:
                r._design_location_cus.append(self)
        self._cugroups = value

    cugroups = property(get_cugroups, set_cugroups)

    def add_cugroups(self, *cugroups):
        for obj in cugroups:
            if self not in obj._design_location_cus:
                obj._design_location_cus.append(self)
            self._cugroups.append(obj)

    def remove_cugroups(self, *cugroups):
        for obj in cugroups:
            if self in obj._design_location_cus:
                obj._design_location_cus.remove(self)
            self._cugroups.remove(obj)
    # >>> cugroups

    # <<< condition_factors
    # @generated
    def get_condition_factors(self):
        """ 
        """
        return self._condition_factors

    def set_condition_factors(self, value):
        for p in self._condition_factors:
            filtered = [q for q in p.design_location_cus if q != self]
            self._condition_factors._design_location_cus = filtered
        for r in value:
            if self not in r._design_location_cus:
                r._design_location_cus.append(self)
        self._condition_factors = value

    condition_factors = property(get_condition_factors, set_condition_factors)

    def add_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self not in obj._design_location_cus:
                obj._design_location_cus.append(self)
            self._condition_factors.append(obj)

    def remove_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self in obj._design_location_cus:
                obj._design_location_cus.remove(self)
            self._condition_factors.remove(obj)
    # >>> condition_factors

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for p in self._work_tasks:
            filtered = [q for q in p.design_location_cus if q != self]
            self._work_tasks._design_location_cus = filtered
        for r in value:
            if self not in r._design_location_cus:
                r._design_location_cus.append(self)
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self not in obj._design_location_cus:
                obj._design_location_cus.append(self)
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self in obj._design_location_cus:
                obj._design_location_cus.remove(self)
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.design_location_cus if q != self]
            self._compatible_units._design_location_cus = filtered
        for r in value:
            if self not in r._design_location_cus:
                r._design_location_cus.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._design_location_cus:
                obj._design_location_cus.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._design_location_cus:
                obj._design_location_cus.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< status
    # @generated
    status = None
    # >>> status



class WorkFlowStep(IdentifiedObject):
    """ A pre-defined set of work steps for a given type of work.
    """
    # <<< work_flow_step
    # @generated
    def __init__(self, sequence_number=0, work=None, work_tasks=None, status=None, *args, **kw_args):
        """ Initialises a new 'WorkFlowStep' instance.

        @param sequence_number: Used to define dependencies of each work flow step, which is for the instance of WorkTask associated with a given instance of WorkFlow. 
        @param work:
        @param work_tasks:
        @param status:
        """
        # Used to define dependencies of each work flow step, which is for the instance of WorkTask associated with a given instance of WorkFlow. 
        self.sequence_number = sequence_number


        self._work = None
        self.work = work

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self.status = status


        super(WorkFlowStep, self).__init__(*args, **kw_args)
    # >>> work_flow_step

    # <<< work
    # @generated
    def get_work(self):
        """ 
        """
        return self._work

    def set_work(self, value):
        if self._work is not None:
            filtered = [x for x in self.work.work_flow_steps if x != self]
            self._work._work_flow_steps = filtered

        self._work = value
        if self._work is not None:
            self._work._work_flow_steps.append(self)

    work = property(get_work, set_work)
    # >>> work

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for x in self._work_tasks:
            x._work_flow_step = None
        for y in value:
            y._work_flow_step = self
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._work_flow_step = self
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._work_flow_step = None
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< status
    # @generated
    status = None
    # >>> status



class ConditionFactor(IdentifiedObject):
    """ This is to specify the various condition factors for a design that may alter the cost estimate or the allocation.
    """
    # <<< condition_factor
    # @generated
    def __init__(self, kind='labor', cf_value='', status=None, design_location_cus=None, design_locations=None, designs=None, *args, **kw_args):
        """ Initialises a new 'ConditionFactor' instance.

        @param kind: Kind of this condition factor. Values are: "labor", "account_allocation", "travel", "other", "material"
        @param cf_value: The actual value of the condition factor, such as labor flat fee or percentage. 
        @param status:
        @param design_location_cus:
        @param design_locations:
        @param designs:
        """
        # Kind of this condition factor. Values are: "labor", "account_allocation", "travel", "other", "material"
        self.kind = kind

        # The actual value of the condition factor, such as labor flat fee or percentage. 
        self.cf_value = cf_value


        self.status = status

        self._design_location_cus = []
        if design_location_cus is not None:
            self.design_location_cus = design_location_cus
        else:
            self.design_location_cus = []

        self._design_locations = []
        if design_locations is not None:
            self.design_locations = design_locations
        else:
            self.design_locations = []

        self._designs = []
        if designs is not None:
            self.designs = designs
        else:
            self.designs = []


        super(ConditionFactor, self).__init__(*args, **kw_args)
    # >>> condition_factor

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< design_location_cus
    # @generated
    def get_design_location_cus(self):
        """ 
        """
        return self._design_location_cus

    def set_design_location_cus(self, value):
        for p in self._design_location_cus:
            filtered = [q for q in p.condition_factors if q != self]
            self._design_location_cus._condition_factors = filtered
        for r in value:
            if self not in r._condition_factors:
                r._condition_factors.append(self)
        self._design_location_cus = value

    design_location_cus = property(get_design_location_cus, set_design_location_cus)

    def add_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self not in obj._condition_factors:
                obj._condition_factors.append(self)
            self._design_location_cus.append(obj)

    def remove_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self in obj._condition_factors:
                obj._condition_factors.remove(self)
            self._design_location_cus.remove(obj)
    # >>> design_location_cus

    # <<< design_locations
    # @generated
    def get_design_locations(self):
        """ 
        """
        return self._design_locations

    def set_design_locations(self, value):
        for p in self._design_locations:
            filtered = [q for q in p.condition_factors if q != self]
            self._design_locations._condition_factors = filtered
        for r in value:
            if self not in r._condition_factors:
                r._condition_factors.append(self)
        self._design_locations = value

    design_locations = property(get_design_locations, set_design_locations)

    def add_design_locations(self, *design_locations):
        for obj in design_locations:
            if self not in obj._condition_factors:
                obj._condition_factors.append(self)
            self._design_locations.append(obj)

    def remove_design_locations(self, *design_locations):
        for obj in design_locations:
            if self in obj._condition_factors:
                obj._condition_factors.remove(self)
            self._design_locations.remove(obj)
    # >>> design_locations

    # <<< designs
    # @generated
    def get_designs(self):
        """ 
        """
        return self._designs

    def set_designs(self, value):
        for p in self._designs:
            filtered = [q for q in p.condition_factors if q != self]
            self._designs._condition_factors = filtered
        for r in value:
            if self not in r._condition_factors:
                r._condition_factors.append(self)
        self._designs = value

    designs = property(get_designs, set_designs)

    def add_designs(self, *designs):
        for obj in designs:
            if self not in obj._condition_factors:
                obj._condition_factors.append(self)
            self._designs.append(obj)

    def remove_designs(self, *designs):
        for obj in designs:
            if self in obj._condition_factors:
                obj._condition_factors.remove(self)
            self._designs.remove(obj)
    # >>> designs



class OneCallRequest(Document):
    """ A request for other utilities to mark their underground facilities prior to commencement of construction and/or maintenance.
    """
    # <<< one_call_request
    # @generated
    def __init__(self, marking_instruction='', marked_indicator=False, explosives_used=False, work_locations=None, *args, **kw_args):
        """ Initialises a new 'OneCallRequest' instance.

        @param marking_instruction: Instructions for marking a dig area, if applicable. 
        @param marked_indicator: True if work location has been marked, for example for a dig area. 
        @param explosives_used: True if explosives have been or are planned to be used. 
        @param work_locations:
        """
        # Instructions for marking a dig area, if applicable. 
        self.marking_instruction = marking_instruction

        # True if work location has been marked, for example for a dig area. 
        self.marked_indicator = marked_indicator

        # True if explosives have been or are planned to be used. 
        self.explosives_used = explosives_used


        self._work_locations = []
        if work_locations is not None:
            self.work_locations = work_locations
        else:
            self.work_locations = []


        super(OneCallRequest, self).__init__(*args, **kw_args)
    # >>> one_call_request

    # <<< work_locations
    # @generated
    def get_work_locations(self):
        """ 
        """
        return self._work_locations

    def set_work_locations(self, value):
        for x in self._work_locations:
            x._one_call_request = None
        for y in value:
            y._one_call_request = self
        self._work_locations = value

    work_locations = property(get_work_locations, set_work_locations)

    def add_work_locations(self, *work_locations):
        for obj in work_locations:
            obj._one_call_request = self
            self._work_locations.append(obj)

    def remove_work_locations(self, *work_locations):
        for obj in work_locations:
            obj._one_call_request = None
            self._work_locations.remove(obj)
    # >>> work_locations



class Assignment(Document):
    """ An assignment is given to an ErpPerson, Crew, Organisation, Equipment Item, Tool, etc. and may be used to perform Work, WorkTasks, Procedures, etc. TimeSchedules may be set up directly for Assignments or indirectly via the associated WorkTask. Note that these associations are all inherited through the recursive relationship on Document.
    """
    # <<< assignment
    # @generated
    def __init__(self, crews=None, effective_period=None, *args, **kw_args):
        """ Initialises a new 'Assignment' instance.

        @param crews: All Crews having this Assignment.
        @param effective_period: Period between the assignment becoming effective and its expiration.
        """

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self.effective_period = effective_period


        super(Assignment, self).__init__(*args, **kw_args)
    # >>> assignment

    # <<< crews
    # @generated
    def get_crews(self):
        """ All Crews having this Assignment.
        """
        return self._crews

    def set_crews(self, value):
        for p in self._crews:
            filtered = [q for q in p.assignments if q != self]
            self._crews._assignments = filtered
        for r in value:
            if self not in r._assignments:
                r._assignments.append(self)
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            if self not in obj._assignments:
                obj._assignments.append(self)
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            if self in obj._assignments:
                obj._assignments.remove(self)
            self._crews.remove(obj)
    # >>> crews

    # <<< effective_period
    # @generated
    # Period between the assignment becoming effective and its expiration.
    effective_period = None
    # >>> effective_period



class QualificationRequirement(IdentifiedObject):
    """ Certain skills are required and must be certified in order for a person (typically a member of a crew) to be qualified to work on types of equipment.
    """
    # <<< qualification_requirement
    # @generated
    def __init__(self, qualification_id='', specifications=None, work_tasks=None, culabor_items=None, skills=None, *args, **kw_args):
        """ Initialises a new 'QualificationRequirement' instance.

        @param qualification_id: Qualification identifier. 
        @param specifications:
        @param work_tasks:
        @param culabor_items:
        @param skills:
        """
        # Qualification identifier. 
        self.qualification_id = qualification_id


        self._specifications = []
        if specifications is not None:
            self.specifications = specifications
        else:
            self.specifications = []

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self._culabor_items = []
        if culabor_items is not None:
            self.culabor_items = culabor_items
        else:
            self.culabor_items = []

        self._skills = []
        if skills is not None:
            self.skills = skills
        else:
            self.skills = []


        super(QualificationRequirement, self).__init__(*args, **kw_args)
    # >>> qualification_requirement

    # <<< specifications
    # @generated
    def get_specifications(self):
        """ 
        """
        return self._specifications

    def set_specifications(self, value):
        for p in self._specifications:
            filtered = [q for q in p.qualification_requirements if q != self]
            self._specifications._qualification_requirements = filtered
        for r in value:
            if self not in r._qualification_requirements:
                r._qualification_requirements.append(self)
        self._specifications = value

    specifications = property(get_specifications, set_specifications)

    def add_specifications(self, *specifications):
        for obj in specifications:
            if self not in obj._qualification_requirements:
                obj._qualification_requirements.append(self)
            self._specifications.append(obj)

    def remove_specifications(self, *specifications):
        for obj in specifications:
            if self in obj._qualification_requirements:
                obj._qualification_requirements.remove(self)
            self._specifications.remove(obj)
    # >>> specifications

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for p in self._work_tasks:
            filtered = [q for q in p.qualification_requirements if q != self]
            self._work_tasks._qualification_requirements = filtered
        for r in value:
            if self not in r._qualification_requirements:
                r._qualification_requirements.append(self)
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self not in obj._qualification_requirements:
                obj._qualification_requirements.append(self)
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self in obj._qualification_requirements:
                obj._qualification_requirements.remove(self)
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< culabor_items
    # @generated
    def get_culabor_items(self):
        """ 
        """
        return self._culabor_items

    def set_culabor_items(self, value):
        for p in self._culabor_items:
            filtered = [q for q in p.qualification_requirements if q != self]
            self._culabor_items._qualification_requirements = filtered
        for r in value:
            if self not in r._qualification_requirements:
                r._qualification_requirements.append(self)
        self._culabor_items = value

    culabor_items = property(get_culabor_items, set_culabor_items)

    def add_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            if self not in obj._qualification_requirements:
                obj._qualification_requirements.append(self)
            self._culabor_items.append(obj)

    def remove_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            if self in obj._qualification_requirements:
                obj._qualification_requirements.remove(self)
            self._culabor_items.remove(obj)
    # >>> culabor_items

    # <<< skills
    # @generated
    def get_skills(self):
        """ 
        """
        return self._skills

    def set_skills(self, value):
        for p in self._skills:
            filtered = [q for q in p.qualification_requirements if q != self]
            self._skills._qualification_requirements = filtered
        for r in value:
            if self not in r._qualification_requirements:
                r._qualification_requirements.append(self)
        self._skills = value

    skills = property(get_skills, set_skills)

    def add_skills(self, *skills):
        for obj in skills:
            if self not in obj._qualification_requirements:
                obj._qualification_requirements.append(self)
            self._skills.append(obj)

    def remove_skills(self, *skills):
        for obj in skills:
            if self in obj._qualification_requirements:
                obj._qualification_requirements.remove(self)
            self._skills.remove(obj)
    # >>> skills



class Crew(IdentifiedObject):
    """ A crew is a group of people (ErpPersons) with specific skills, tools, and vehicles.
    """
    # <<< crew
    # @generated
    def __init__(self, category='', capabilities=None, work_tasks=None, vehicles=None, crew_members=None, assignments=None, tools=None, route=None, outage_steps=None, work_equipment_assets=None, locations=None, shift_patterns=None, switching_schedules=None, organisations=None, *args, **kw_args):
        """ Initialises a new 'Crew' instance.

        @param category: Category by utility's work management standards and practices. 
        @param capabilities:
        @param work_tasks: All WorkTasks this Crew participates in.
        @param vehicles:
        @param crew_members: All ErpPersons that are members of this Crew.
        @param assignments: All Assignments for this Crew.
        @param tools:
        @param route:
        @param outage_steps:
        @param work_equipment_assets:
        @param locations:
        @param shift_patterns:
        @param switching_schedules: All SwitchingSchedules executed by this Crew.
        @param organisations:
        """
        # Category by utility's work management standards and practices. 
        self.category = category


        self._capabilities = []
        if capabilities is not None:
            self.capabilities = capabilities
        else:
            self.capabilities = []

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self._vehicles = []
        if vehicles is not None:
            self.vehicles = vehicles
        else:
            self.vehicles = []

        self._crew_members = []
        if crew_members is not None:
            self.crew_members = crew_members
        else:
            self.crew_members = []

        self._assignments = []
        if assignments is not None:
            self.assignments = assignments
        else:
            self.assignments = []

        self._tools = []
        if tools is not None:
            self.tools = tools
        else:
            self.tools = []

        self._route = None
        self.route = route

        self._outage_steps = []
        if outage_steps is not None:
            self.outage_steps = outage_steps
        else:
            self.outage_steps = []

        self._work_equipment_assets = []
        if work_equipment_assets is not None:
            self.work_equipment_assets = work_equipment_assets
        else:
            self.work_equipment_assets = []

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self._shift_patterns = []
        if shift_patterns is not None:
            self.shift_patterns = shift_patterns
        else:
            self.shift_patterns = []

        self._switching_schedules = []
        if switching_schedules is not None:
            self.switching_schedules = switching_schedules
        else:
            self.switching_schedules = []

        self._organisations = []
        if organisations is not None:
            self.organisations = organisations
        else:
            self.organisations = []


        super(Crew, self).__init__(*args, **kw_args)
    # >>> crew

    # <<< capabilities
    # @generated
    def get_capabilities(self):
        """ 
        """
        return self._capabilities

    def set_capabilities(self, value):
        for x in self._capabilities:
            x._crew = None
        for y in value:
            y._crew = self
        self._capabilities = value

    capabilities = property(get_capabilities, set_capabilities)

    def add_capabilities(self, *capabilities):
        for obj in capabilities:
            obj._crew = self
            self._capabilities.append(obj)

    def remove_capabilities(self, *capabilities):
        for obj in capabilities:
            obj._crew = None
            self._capabilities.remove(obj)
    # >>> capabilities

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ All WorkTasks this Crew participates in.
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for p in self._work_tasks:
            filtered = [q for q in p.crews if q != self]
            self._work_tasks._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self not in obj._crews:
                obj._crews.append(self)
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self in obj._crews:
                obj._crews.remove(self)
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< vehicles
    # @generated
    def get_vehicles(self):
        """ 
        """
        return self._vehicles

    def set_vehicles(self, value):
        for x in self._vehicles:
            x._crew = None
        for y in value:
            y._crew = self
        self._vehicles = value

    vehicles = property(get_vehicles, set_vehicles)

    def add_vehicles(self, *vehicles):
        for obj in vehicles:
            obj._crew = self
            self._vehicles.append(obj)

    def remove_vehicles(self, *vehicles):
        for obj in vehicles:
            obj._crew = None
            self._vehicles.remove(obj)
    # >>> vehicles

    # <<< crew_members
    # @generated
    def get_crew_members(self):
        """ All ErpPersons that are members of this Crew.
        """
        return self._crew_members

    def set_crew_members(self, value):
        for p in self._crew_members:
            filtered = [q for q in p.crews if q != self]
            self._crew_members._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._crew_members = value

    crew_members = property(get_crew_members, set_crew_members)

    def add_crew_members(self, *crew_members):
        for obj in crew_members:
            if self not in obj._crews:
                obj._crews.append(self)
            self._crew_members.append(obj)

    def remove_crew_members(self, *crew_members):
        for obj in crew_members:
            if self in obj._crews:
                obj._crews.remove(self)
            self._crew_members.remove(obj)
    # >>> crew_members

    # <<< assignments
    # @generated
    def get_assignments(self):
        """ All Assignments for this Crew.
        """
        return self._assignments

    def set_assignments(self, value):
        for p in self._assignments:
            filtered = [q for q in p.crews if q != self]
            self._assignments._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._assignments = value

    assignments = property(get_assignments, set_assignments)

    def add_assignments(self, *assignments):
        for obj in assignments:
            if self not in obj._crews:
                obj._crews.append(self)
            self._assignments.append(obj)

    def remove_assignments(self, *assignments):
        for obj in assignments:
            if self in obj._crews:
                obj._crews.remove(self)
            self._assignments.remove(obj)
    # >>> assignments

    # <<< tools
    # @generated
    def get_tools(self):
        """ 
        """
        return self._tools

    def set_tools(self, value):
        for x in self._tools:
            x._crew = None
        for y in value:
            y._crew = self
        self._tools = value

    tools = property(get_tools, set_tools)

    def add_tools(self, *tools):
        for obj in tools:
            obj._crew = self
            self._tools.append(obj)

    def remove_tools(self, *tools):
        for obj in tools:
            obj._crew = None
            self._tools.remove(obj)
    # >>> tools

    # <<< route
    # @generated
    def get_route(self):
        """ 
        """
        return self._route

    def set_route(self, value):
        if self._route is not None:
            filtered = [x for x in self.route.crews if x != self]
            self._route._crews = filtered

        self._route = value
        if self._route is not None:
            self._route._crews.append(self)

    route = property(get_route, set_route)
    # >>> route

    # <<< outage_steps
    # @generated
    def get_outage_steps(self):
        """ 
        """
        return self._outage_steps

    def set_outage_steps(self, value):
        for p in self._outage_steps:
            filtered = [q for q in p.crews if q != self]
            self._outage_steps._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._outage_steps = value

    outage_steps = property(get_outage_steps, set_outage_steps)

    def add_outage_steps(self, *outage_steps):
        for obj in outage_steps:
            if self not in obj._crews:
                obj._crews.append(self)
            self._outage_steps.append(obj)

    def remove_outage_steps(self, *outage_steps):
        for obj in outage_steps:
            if self in obj._crews:
                obj._crews.remove(self)
            self._outage_steps.remove(obj)
    # >>> outage_steps

    # <<< work_equipment_assets
    # @generated
    def get_work_equipment_assets(self):
        """ 
        """
        return self._work_equipment_assets

    def set_work_equipment_assets(self, value):
        for x in self._work_equipment_assets:
            x._crew = None
        for y in value:
            y._crew = self
        self._work_equipment_assets = value

    work_equipment_assets = property(get_work_equipment_assets, set_work_equipment_assets)

    def add_work_equipment_assets(self, *work_equipment_assets):
        for obj in work_equipment_assets:
            obj._crew = self
            self._work_equipment_assets.append(obj)

    def remove_work_equipment_assets(self, *work_equipment_assets):
        for obj in work_equipment_assets:
            obj._crew = None
            self._work_equipment_assets.remove(obj)
    # >>> work_equipment_assets

    # <<< locations
    # @generated
    def get_locations(self):
        """ 
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.crews if q != self]
            self._locations._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._crews:
                obj._crews.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._crews:
                obj._crews.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< shift_patterns
    # @generated
    def get_shift_patterns(self):
        """ 
        """
        return self._shift_patterns

    def set_shift_patterns(self, value):
        for p in self._shift_patterns:
            filtered = [q for q in p.crews if q != self]
            self._shift_patterns._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._shift_patterns = value

    shift_patterns = property(get_shift_patterns, set_shift_patterns)

    def add_shift_patterns(self, *shift_patterns):
        for obj in shift_patterns:
            if self not in obj._crews:
                obj._crews.append(self)
            self._shift_patterns.append(obj)

    def remove_shift_patterns(self, *shift_patterns):
        for obj in shift_patterns:
            if self in obj._crews:
                obj._crews.remove(self)
            self._shift_patterns.remove(obj)
    # >>> shift_patterns

    # <<< switching_schedules
    # @generated
    def get_switching_schedules(self):
        """ All SwitchingSchedules executed by this Crew.
        """
        return self._switching_schedules

    def set_switching_schedules(self, value):
        for p in self._switching_schedules:
            filtered = [q for q in p.crews if q != self]
            self._switching_schedules._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._switching_schedules = value

    switching_schedules = property(get_switching_schedules, set_switching_schedules)

    def add_switching_schedules(self, *switching_schedules):
        for obj in switching_schedules:
            if self not in obj._crews:
                obj._crews.append(self)
            self._switching_schedules.append(obj)

    def remove_switching_schedules(self, *switching_schedules):
        for obj in switching_schedules:
            if self in obj._crews:
                obj._crews.remove(self)
            self._switching_schedules.remove(obj)
    # >>> switching_schedules

    # <<< organisations
    # @generated
    def get_organisations(self):
        """ 
        """
        return self._organisations

    def set_organisations(self, value):
        for p in self._organisations:
            filtered = [q for q in p.crews if q != self]
            self._organisations._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._organisations = value

    organisations = property(get_organisations, set_organisations)

    def add_organisations(self, *organisations):
        for obj in organisations:
            if self not in obj._crews:
                obj._crews.append(self)
            self._organisations.append(obj)

    def remove_organisations(self, *organisations):
        for obj in organisations:
            if self in obj._crews:
                obj._crews.remove(self)
            self._organisations.remove(obj)
    # >>> organisations



class DiagnosisDataSet(ProcedureDataSet):
    """ The result of a problem (typically an asset failure) diagnosis.
    """
    # <<< diagnosis_data_set
    # @generated
    def __init__(self, phase_code='bc', failure_mode='', root_remark='', root_cause='', final_origin='', final_cause='', preliminary_code='', effect='', preliminary_remark='', root_origin='', final_code='', final_remark='', preliminary_date_time='', *args, **kw_args):
        """ Initialises a new 'DiagnosisDataSet' instance.

        @param phase_code: Phase(s) diagnosed. Values are: "bc", "ab", "b", "ac", "abc", "split_secondary1_n", "abn", "abcn", "cn", "an", "split_secondary12_n", "bcn", "split_secondary2_n", "acn", "a", "c", "n", "bn"
        @param failure_mode: Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to contain oil; Failure to provide ground plane; Other. 
        @param root_remark: Remarks pertaining to root cause findings during problem diagnosis. 
        @param root_cause: Root cause of problem determined during diagnosis. 
        @param final_origin: Origin of problem determined during diagnosis. 
        @param final_cause: Cause of problem determined during diagnosis. 
        @param preliminary_code: Code for problem category determined during preliminary assessment. 
        @param effect: Effect of problem. 
        @param preliminary_remark: Remarks pertaining to preliminary assessment of problem. 
        @param root_origin: Root origin of problem determined during diagnosis. 
        @param final_code: Code for diagnosed probem category. 
        @param final_remark: Remarks pertaining to findings during problem diagnosis. 
        @param preliminary_date_time: Date and time preliminary assessment of problem was performed. 
        """
        # Phase(s) diagnosed. Values are: "bc", "ab", "b", "ac", "abc", "split_secondary1_n", "abn", "abcn", "cn", "an", "split_secondary12_n", "bcn", "split_secondary2_n", "acn", "a", "c", "n", "bn"
        self.phase_code = phase_code

        # Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to contain oil; Failure to provide ground plane; Other. 
        self.failure_mode = failure_mode

        # Remarks pertaining to root cause findings during problem diagnosis. 
        self.root_remark = root_remark

        # Root cause of problem determined during diagnosis. 
        self.root_cause = root_cause

        # Origin of problem determined during diagnosis. 
        self.final_origin = final_origin

        # Cause of problem determined during diagnosis. 
        self.final_cause = final_cause

        # Code for problem category determined during preliminary assessment. 
        self.preliminary_code = preliminary_code

        # Effect of problem. 
        self.effect = effect

        # Remarks pertaining to preliminary assessment of problem. 
        self.preliminary_remark = preliminary_remark

        # Root origin of problem determined during diagnosis. 
        self.root_origin = root_origin

        # Code for diagnosed probem category. 
        self.final_code = final_code

        # Remarks pertaining to findings during problem diagnosis. 
        self.final_remark = final_remark

        # Date and time preliminary assessment of problem was performed. 
        self.preliminary_date_time = preliminary_date_time



        super(DiagnosisDataSet, self).__init__(*args, **kw_args)
    # >>> diagnosis_data_set



class ContractorItem(IdentifiedObject):
    """ Contractor information for work task.
    """
    # <<< contractor_item
    # @generated
    def __init__(self, cost=0.0, bid_amount=0.0, activity_code='', work_task=None, work_cost_detail=None, erp_payables=None, status=None, *args, **kw_args):
        """ Initialises a new 'ContractorItem' instance.

        @param cost: The total amount charged. 
        @param bid_amount: The amount that a given contractor will charge for performing this unit of work. 
        @param activity_code: Activity code identifies a specific and distinguishable unit of work. 
        @param work_task:
        @param work_cost_detail:
        @param erp_payables:
        @param status:
        """
        # The total amount charged. 
        self.cost = cost

        # The amount that a given contractor will charge for performing this unit of work. 
        self.bid_amount = bid_amount

        # Activity code identifies a specific and distinguishable unit of work. 
        self.activity_code = activity_code


        self._work_task = None
        self.work_task = work_task

        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail

        self._erp_payables = []
        if erp_payables is not None:
            self.erp_payables = erp_payables
        else:
            self.erp_payables = []

        self.status = status


        super(ContractorItem, self).__init__(*args, **kw_args)
    # >>> contractor_item

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.contractor_items if x != self]
            self._work_task._contractor_items = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._contractor_items.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            filtered = [x for x in self.work_cost_detail.contractor_items if x != self]
            self._work_cost_detail._contractor_items = filtered

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._contractor_items.append(self)

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail

    # <<< erp_payables
    # @generated
    def get_erp_payables(self):
        """ 
        """
        return self._erp_payables

    def set_erp_payables(self, value):
        for p in self._erp_payables:
            filtered = [q for q in p.contractor_items if q != self]
            self._erp_payables._contractor_items = filtered
        for r in value:
            if self not in r._contractor_items:
                r._contractor_items.append(self)
        self._erp_payables = value

    erp_payables = property(get_erp_payables, set_erp_payables)

    def add_erp_payables(self, *erp_payables):
        for obj in erp_payables:
            if self not in obj._contractor_items:
                obj._contractor_items.append(self)
            self._erp_payables.append(obj)

    def remove_erp_payables(self, *erp_payables):
        for obj in erp_payables:
            if self in obj._contractor_items:
                obj._contractor_items.remove(self)
            self._erp_payables.remove(obj)
    # >>> erp_payables

    # <<< status
    # @generated
    status = None
    # >>> status



class CUGroup(IdentifiedObject):
    """ A Compatible Unit Group identifies a set of compatible units which may be jointly utilized for estimating and designating jobs.
    """
    # <<< cugroup
    # @generated
    def __init__(self, parent_cugroups=None, child_cugroups=None, design_location_cus=None, status=None, compatible_units=None, *args, **kw_args):
        """ Initialises a new 'CUGroup' instance.

        @param parent_cugroups:
        @param child_cugroups:
        @param design_location_cus:
        @param status:
        @param compatible_units:
        """

        self._parent_cugroups = []
        if parent_cugroups is not None:
            self.parent_cugroups = parent_cugroups
        else:
            self.parent_cugroups = []

        self._child_cugroups = []
        if child_cugroups is not None:
            self.child_cugroups = child_cugroups
        else:
            self.child_cugroups = []

        self._design_location_cus = []
        if design_location_cus is not None:
            self.design_location_cus = design_location_cus
        else:
            self.design_location_cus = []

        self.status = status

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []


        super(CUGroup, self).__init__(*args, **kw_args)
    # >>> cugroup

    # <<< parent_cugroups
    # @generated
    def get_parent_cugroups(self):
        """ 
        """
        return self._parent_cugroups

    def set_parent_cugroups(self, value):
        for p in self._parent_cugroups:
            filtered = [q for q in p.child_cugroups if q != self]
            self._parent_cugroups._child_cugroups = filtered
        for r in value:
            if self not in r._child_cugroups:
                r._child_cugroups.append(self)
        self._parent_cugroups = value

    parent_cugroups = property(get_parent_cugroups, set_parent_cugroups)

    def add_parent_cugroups(self, *parent_cugroups):
        for obj in parent_cugroups:
            if self not in obj._child_cugroups:
                obj._child_cugroups.append(self)
            self._parent_cugroups.append(obj)

    def remove_parent_cugroups(self, *parent_cugroups):
        for obj in parent_cugroups:
            if self in obj._child_cugroups:
                obj._child_cugroups.remove(self)
            self._parent_cugroups.remove(obj)
    # >>> parent_cugroups

    # <<< child_cugroups
    # @generated
    def get_child_cugroups(self):
        """ 
        """
        return self._child_cugroups

    def set_child_cugroups(self, value):
        for p in self._child_cugroups:
            filtered = [q for q in p.parent_cugroups if q != self]
            self._child_cugroups._parent_cugroups = filtered
        for r in value:
            if self not in r._parent_cugroups:
                r._parent_cugroups.append(self)
        self._child_cugroups = value

    child_cugroups = property(get_child_cugroups, set_child_cugroups)

    def add_child_cugroups(self, *child_cugroups):
        for obj in child_cugroups:
            if self not in obj._parent_cugroups:
                obj._parent_cugroups.append(self)
            self._child_cugroups.append(obj)

    def remove_child_cugroups(self, *child_cugroups):
        for obj in child_cugroups:
            if self in obj._parent_cugroups:
                obj._parent_cugroups.remove(self)
            self._child_cugroups.remove(obj)
    # >>> child_cugroups

    # <<< design_location_cus
    # @generated
    def get_design_location_cus(self):
        """ 
        """
        return self._design_location_cus

    def set_design_location_cus(self, value):
        for p in self._design_location_cus:
            filtered = [q for q in p.cugroups if q != self]
            self._design_location_cus._cugroups = filtered
        for r in value:
            if self not in r._cugroups:
                r._cugroups.append(self)
        self._design_location_cus = value

    design_location_cus = property(get_design_location_cus, set_design_location_cus)

    def add_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self not in obj._cugroups:
                obj._cugroups.append(self)
            self._design_location_cus.append(obj)

    def remove_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self in obj._cugroups:
                obj._cugroups.remove(self)
            self._design_location_cus.remove(obj)
    # >>> design_location_cus

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for x in self._compatible_units:
            x._cugroup = None
        for y in value:
            y._cugroup = self
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cugroup = self
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cugroup = None
            self._compatible_units.remove(obj)
    # >>> compatible_units



class CUWorkEquipmentItem(IdentifiedObject):
    """ Compatible unit for various types of WorkEquipmentAssets, including vehicles.
    """
    # <<< cuwork_equipment_item
    # @generated
    def __init__(self, equip_code='', rate=0.0, compatible_units=None, type_asset=None, status=None, *args, **kw_args):
        """ Initialises a new 'CUWorkEquipmentItem' instance.

        @param equip_code: The equipment type code. 
        @param rate: Standard usage rate for the type of vehicle. 
        @param compatible_units:
        @param type_asset:
        @param status:
        """
        # The equipment type code. 
        self.equip_code = equip_code

        # Standard usage rate for the type of vehicle. 
        self.rate = rate


        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self._type_asset = None
        self.type_asset = type_asset

        self.status = status


        super(CUWorkEquipmentItem, self).__init__(*args, **kw_args)
    # >>> cuwork_equipment_item

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.cuwork_equipment_items if q != self]
            self._compatible_units._cuwork_equipment_items = filtered
        for r in value:
            if self not in r._cuwork_equipment_items:
                r._cuwork_equipment_items.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._cuwork_equipment_items:
                obj._cuwork_equipment_items.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._cuwork_equipment_items:
                obj._cuwork_equipment_items.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< type_asset
    # @generated
    def get_type_asset(self):
        """ 
        """
        return self._type_asset

    def set_type_asset(self, value):
        if self._type_asset is not None:
            self._type_asset._cuwork_equipment_asset = None

        self._type_asset = value
        if self._type_asset is not None:
            self._type_asset._cuwork_equipment_asset = self

    type_asset = property(get_type_asset, set_type_asset)
    # >>> type_asset

    # <<< status
    # @generated
    status = None
    # >>> status



class WorkLocation(Location):
    """ Information about a particular location for various forms of work such as a one call request.
    """
    # <<< work_location
    # @generated
    def __init__(self, block='', nearest_intersection='', subdivision='', lot='', one_call_request=None, design_locations=None, *args, **kw_args):
        """ Initialises a new 'WorkLocation' instance.

        @param block: Name, identifier, or description of the block, if applicable, in which work is to occur. 
        @param nearest_intersection: The names of streets at the nearest intersection to work area. 
        @param subdivision: Name, identifier, or description of the subdivision, if applicable, in which work is to occur. 
        @param lot: Name, identifier, or description of the lot, if applicable, in which work is to occur. 
        @param one_call_request:
        @param design_locations:
        """
        # Name, identifier, or description of the block, if applicable, in which work is to occur. 
        self.block = block

        # The names of streets at the nearest intersection to work area. 
        self.nearest_intersection = nearest_intersection

        # Name, identifier, or description of the subdivision, if applicable, in which work is to occur. 
        self.subdivision = subdivision

        # Name, identifier, or description of the lot, if applicable, in which work is to occur. 
        self.lot = lot


        self._one_call_request = None
        self.one_call_request = one_call_request

        self._design_locations = []
        if design_locations is not None:
            self.design_locations = design_locations
        else:
            self.design_locations = []


        super(WorkLocation, self).__init__(*args, **kw_args)
    # >>> work_location

    # <<< one_call_request
    # @generated
    def get_one_call_request(self):
        """ 
        """
        return self._one_call_request

    def set_one_call_request(self, value):
        if self._one_call_request is not None:
            filtered = [x for x in self.one_call_request.work_locations if x != self]
            self._one_call_request._work_locations = filtered

        self._one_call_request = value
        if self._one_call_request is not None:
            self._one_call_request._work_locations.append(self)

    one_call_request = property(get_one_call_request, set_one_call_request)
    # >>> one_call_request

    # <<< design_locations
    # @generated
    def get_design_locations(self):
        """ 
        """
        return self._design_locations

    def set_design_locations(self, value):
        for p in self._design_locations:
            filtered = [q for q in p.work_locations if q != self]
            self._design_locations._work_locations = filtered
        for r in value:
            if self not in r._work_locations:
                r._work_locations.append(self)
        self._design_locations = value

    design_locations = property(get_design_locations, set_design_locations)

    def add_design_locations(self, *design_locations):
        for obj in design_locations:
            if self not in obj._work_locations:
                obj._work_locations.append(self)
            self._design_locations.append(obj)

    def remove_design_locations(self, *design_locations):
        for obj in design_locations:
            if self in obj._work_locations:
                obj._work_locations.remove(self)
            self._design_locations.remove(obj)
    # >>> design_locations



class WorkCostDetail(Document):
    """ A collection of all of the individual cost items collected from multiple sources.
    """
    # <<< work_cost_detail
    # @generated
    def __init__(self, amount=0.0, is_debit=False, transaction_date_time='', type='', overhead_cost=None, work_task=None, labor_items=None, erp_project_accounting=None, equipment_items=None, work_cost_summary=None, design=None, misc_cost_items=None, cost_type=None, works=None, contractor_items=None, material_items=None, property_units=None, *args, **kw_args):
        """ Initialises a new 'WorkCostDetail' instance.

        @param amount: Amount in designated currency for work, either a total or an individual element. As defined in the attribute 'type,' multiple instances are applicable to each work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted cost, other. 
        @param is_debit: True if 'amount' is a debit, false if it is a credit. 
        @param transaction_date_time: Date and time that 'amount' is posted to the work. 
        @param type: Type of work cost. 
        @param overhead_cost:
        @param work_task:
        @param labor_items:
        @param erp_project_accounting:
        @param equipment_items:
        @param work_cost_summary:
        @param design:
        @param misc_cost_items:
        @param cost_type:
        @param works:
        @param contractor_items:
        @param material_items:
        @param property_units:
        """
        # Amount in designated currency for work, either a total or an individual element. As defined in the attribute 'type,' multiple instances are applicable to each work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted cost, other. 
        self.amount = amount

        # True if 'amount' is a debit, false if it is a credit. 
        self.is_debit = is_debit

        # Date and time that 'amount' is posted to the work. 
        self.transaction_date_time = transaction_date_time

        # Type of work cost. 
        self.type = type


        self._overhead_cost = None
        self.overhead_cost = overhead_cost

        self._work_task = None
        self.work_task = work_task

        self._labor_items = []
        if labor_items is not None:
            self.labor_items = labor_items
        else:
            self.labor_items = []

        self._erp_project_accounting = None
        self.erp_project_accounting = erp_project_accounting

        self._equipment_items = []
        if equipment_items is not None:
            self.equipment_items = equipment_items
        else:
            self.equipment_items = []

        self._work_cost_summary = None
        self.work_cost_summary = work_cost_summary

        self._design = None
        self.design = design

        self._misc_cost_items = []
        if misc_cost_items is not None:
            self.misc_cost_items = misc_cost_items
        else:
            self.misc_cost_items = []

        self._cost_type = None
        self.cost_type = cost_type

        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []

        self._contractor_items = []
        if contractor_items is not None:
            self.contractor_items = contractor_items
        else:
            self.contractor_items = []

        self._material_items = []
        if material_items is not None:
            self.material_items = material_items
        else:
            self.material_items = []

        self._property_units = []
        if property_units is not None:
            self.property_units = property_units
        else:
            self.property_units = []


        super(WorkCostDetail, self).__init__(*args, **kw_args)
    # >>> work_cost_detail

    # <<< overhead_cost
    # @generated
    def get_overhead_cost(self):
        """ 
        """
        return self._overhead_cost

    def set_overhead_cost(self, value):
        if self._overhead_cost is not None:
            filtered = [x for x in self.overhead_cost.work_cost_details if x != self]
            self._overhead_cost._work_cost_details = filtered

        self._overhead_cost = value
        if self._overhead_cost is not None:
            self._overhead_cost._work_cost_details.append(self)

    overhead_cost = property(get_overhead_cost, set_overhead_cost)
    # >>> overhead_cost

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.work_cost_details if x != self]
            self._work_task._work_cost_details = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._work_cost_details.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< labor_items
    # @generated
    def get_labor_items(self):
        """ 
        """
        return self._labor_items

    def set_labor_items(self, value):
        for x in self._labor_items:
            x._work_cost_detail = None
        for y in value:
            y._work_cost_detail = self
        self._labor_items = value

    labor_items = property(get_labor_items, set_labor_items)

    def add_labor_items(self, *labor_items):
        for obj in labor_items:
            obj._work_cost_detail = self
            self._labor_items.append(obj)

    def remove_labor_items(self, *labor_items):
        for obj in labor_items:
            obj._work_cost_detail = None
            self._labor_items.remove(obj)
    # >>> labor_items

    # <<< erp_project_accounting
    # @generated
    def get_erp_project_accounting(self):
        """ 
        """
        return self._erp_project_accounting

    def set_erp_project_accounting(self, value):
        if self._erp_project_accounting is not None:
            filtered = [x for x in self.erp_project_accounting.work_cost_details if x != self]
            self._erp_project_accounting._work_cost_details = filtered

        self._erp_project_accounting = value
        if self._erp_project_accounting is not None:
            self._erp_project_accounting._work_cost_details.append(self)

    erp_project_accounting = property(get_erp_project_accounting, set_erp_project_accounting)
    # >>> erp_project_accounting

    # <<< equipment_items
    # @generated
    def get_equipment_items(self):
        """ 
        """
        return self._equipment_items

    def set_equipment_items(self, value):
        for x in self._equipment_items:
            x._work_cost_detail = None
        for y in value:
            y._work_cost_detail = self
        self._equipment_items = value

    equipment_items = property(get_equipment_items, set_equipment_items)

    def add_equipment_items(self, *equipment_items):
        for obj in equipment_items:
            obj._work_cost_detail = self
            self._equipment_items.append(obj)

    def remove_equipment_items(self, *equipment_items):
        for obj in equipment_items:
            obj._work_cost_detail = None
            self._equipment_items.remove(obj)
    # >>> equipment_items

    # <<< work_cost_summary
    # @generated
    def get_work_cost_summary(self):
        """ 
        """
        return self._work_cost_summary

    def set_work_cost_summary(self, value):
        if self._work_cost_summary is not None:
            self._work_cost_summary._work_cost_detail = None

        self._work_cost_summary = value
        if self._work_cost_summary is not None:
            self._work_cost_summary._work_cost_detail = self

    work_cost_summary = property(get_work_cost_summary, set_work_cost_summary)
    # >>> work_cost_summary

    # <<< design
    # @generated
    def get_design(self):
        """ 
        """
        return self._design

    def set_design(self, value):
        if self._design is not None:
            filtered = [x for x in self.design.work_cost_details if x != self]
            self._design._work_cost_details = filtered

        self._design = value
        if self._design is not None:
            self._design._work_cost_details.append(self)

    design = property(get_design, set_design)
    # >>> design

    # <<< misc_cost_items
    # @generated
    def get_misc_cost_items(self):
        """ 
        """
        return self._misc_cost_items

    def set_misc_cost_items(self, value):
        for x in self._misc_cost_items:
            x._work_cost_detail = None
        for y in value:
            y._work_cost_detail = self
        self._misc_cost_items = value

    misc_cost_items = property(get_misc_cost_items, set_misc_cost_items)

    def add_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._work_cost_detail = self
            self._misc_cost_items.append(obj)

    def remove_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._work_cost_detail = None
            self._misc_cost_items.remove(obj)
    # >>> misc_cost_items

    # <<< cost_type
    # @generated
    def get_cost_type(self):
        """ 
        """
        return self._cost_type

    def set_cost_type(self, value):
        if self._cost_type is not None:
            filtered = [x for x in self.cost_type.work_cost_details if x != self]
            self._cost_type._work_cost_details = filtered

        self._cost_type = value
        if self._cost_type is not None:
            self._cost_type._work_cost_details.append(self)

    cost_type = property(get_cost_type, set_cost_type)
    # >>> cost_type

    # <<< works
    # @generated
    def get_works(self):
        """ 
        """
        return self._works

    def set_works(self, value):
        for p in self._works:
            filtered = [q for q in p.work_cost_details if q != self]
            self._works._work_cost_details = filtered
        for r in value:
            if self not in r._work_cost_details:
                r._work_cost_details.append(self)
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            if self not in obj._work_cost_details:
                obj._work_cost_details.append(self)
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            if self in obj._work_cost_details:
                obj._work_cost_details.remove(self)
            self._works.remove(obj)
    # >>> works

    # <<< contractor_items
    # @generated
    def get_contractor_items(self):
        """ 
        """
        return self._contractor_items

    def set_contractor_items(self, value):
        for x in self._contractor_items:
            x._work_cost_detail = None
        for y in value:
            y._work_cost_detail = self
        self._contractor_items = value

    contractor_items = property(get_contractor_items, set_contractor_items)

    def add_contractor_items(self, *contractor_items):
        for obj in contractor_items:
            obj._work_cost_detail = self
            self._contractor_items.append(obj)

    def remove_contractor_items(self, *contractor_items):
        for obj in contractor_items:
            obj._work_cost_detail = None
            self._contractor_items.remove(obj)
    # >>> contractor_items

    # <<< material_items
    # @generated
    def get_material_items(self):
        """ 
        """
        return self._material_items

    def set_material_items(self, value):
        for x in self._material_items:
            x._work_cost_detail = None
        for y in value:
            y._work_cost_detail = self
        self._material_items = value

    material_items = property(get_material_items, set_material_items)

    def add_material_items(self, *material_items):
        for obj in material_items:
            obj._work_cost_detail = self
            self._material_items.append(obj)

    def remove_material_items(self, *material_items):
        for obj in material_items:
            obj._work_cost_detail = None
            self._material_items.remove(obj)
    # >>> material_items

    # <<< property_units
    # @generated
    def get_property_units(self):
        """ 
        """
        return self._property_units

    def set_property_units(self, value):
        for p in self._property_units:
            filtered = [q for q in p.work_cost_details if q != self]
            self._property_units._work_cost_details = filtered
        for r in value:
            if self not in r._work_cost_details:
                r._work_cost_details.append(self)
        self._property_units = value

    property_units = property(get_property_units, set_property_units)

    def add_property_units(self, *property_units):
        for obj in property_units:
            if self not in obj._work_cost_details:
                obj._work_cost_details.append(self)
            self._property_units.append(obj)

    def remove_property_units(self, *property_units):
        for obj in property_units:
            if self in obj._work_cost_details:
                obj._work_cost_details.remove(self)
            self._property_units.remove(obj)
    # >>> property_units



class EquipmentItem(IdentifiedObject):
    """ An equipment item, such as a vehicle, used for a work order.
    """
    # <<< equipment_item
    # @generated
    def __init__(self, cost=0.0, code='', work_cost_detail=None, work_task=None, status=None, *args, **kw_args):
        """ Initialises a new 'EquipmentItem' instance.

        @param cost: The cost for vehicle usage. 
        @param code: Code for type of vehicle. 
        @param work_cost_detail:
        @param work_task:
        @param status:
        """
        # The cost for vehicle usage. 
        self.cost = cost

        # Code for type of vehicle. 
        self.code = code


        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail

        self._work_task = None
        self.work_task = work_task

        self.status = status


        super(EquipmentItem, self).__init__(*args, **kw_args)
    # >>> equipment_item

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            filtered = [x for x in self.work_cost_detail.equipment_items if x != self]
            self._work_cost_detail._equipment_items = filtered

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._equipment_items.append(self)

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.equipment_items if x != self]
            self._work_task._equipment_items = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._equipment_items.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< status
    # @generated
    status = None
    # >>> status



class BusinessCase(Document):
    """ Business justification for capital expenditures, usually addressing operations and maintenance costs as well.
    """
    # <<< business_case
    # @generated
    def __init__(self, corporate_code='', works=None, projects=None, *args, **kw_args):
        """ Initialises a new 'BusinessCase' instance.

        @param corporate_code: A codified representation of the business case (i.e., codes for highway relocation, replace substation transformers, etc.). 
        @param works:
        @param projects:
        """
        # A codified representation of the business case (i.e., codes for highway relocation, replace substation transformers, etc.). 
        self.corporate_code = corporate_code


        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []

        self._projects = []
        if projects is not None:
            self.projects = projects
        else:
            self.projects = []


        super(BusinessCase, self).__init__(*args, **kw_args)
    # >>> business_case

    # <<< works
    # @generated
    def get_works(self):
        """ 
        """
        return self._works

    def set_works(self, value):
        for x in self._works:
            x._business_case = None
        for y in value:
            y._business_case = self
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            obj._business_case = self
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            obj._business_case = None
            self._works.remove(obj)
    # >>> works

    # <<< projects
    # @generated
    def get_projects(self):
        """ 
        """
        return self._projects

    def set_projects(self, value):
        for x in self._projects:
            x._business_case = None
        for y in value:
            y._business_case = self
        self._projects = value

    projects = property(get_projects, set_projects)

    def add_projects(self, *projects):
        for obj in projects:
            obj._business_case = self
            self._projects.append(obj)

    def remove_projects(self, *projects):
        for obj in projects:
            obj._business_case = None
            self._projects.remove(obj)
    # >>> projects



# <<< inf_work
# @generated
# >>> inf_work
