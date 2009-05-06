#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" Defines a viewer of models for desktop use.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import sys
from os.path import join, dirname, expanduser, isfile
import logging
import pickle

import enthought.traits

from enthought.traits.trait_base import ETSConfig

from enthought.traits.api import \
    HasTraits, Instance, File, Bool, Str, List, on_trait_change, \
    Float, Tuple, Property, Delegate, Code, Button, Directory, Callable

from enthought.traits.ui.api \
    import View, Handler, UIInfo, Group, Item, TableEditor, InstanceEditor, \
    Label, Tabbed, HGroup, VGroup, ModelView, FileEditor, StatusItem, \
    spring, TextEditor

from enthought.traits.ui.menu \
    import NoButtons, OKCancelButtons, Separator

#from enthought.logger.api \
#    import add_log_queue_handler

from enthought.logger.log_queue_handler \
    import LogQueueHandler

from enthought.pyface.api \
    import error, confirm, YES, FileDialog, OK

from enthought.pyface.image_resource \
    import ImageResource

from DesktopMenu \
    import menubar, toolbar

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

frame_icon = ImageResource( "frame.ico" )

license_label = \
"""
Copyright (c) 2009

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 2 dated June, 1991.

This software is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

"""

#------------------------------------------------------------------------------
#  "DesktopViewModel" class:
#------------------------------------------------------------------------------

class DesktopViewModel ( ModelView ):
    """ Defines a view model for desktop use.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Path to the pickled model.
    file = File( desc = "pickle path" )

    # Default directory file actions..
    wd = Directory( desc = "path to save file", label = "Working Directory" )

    # Exit confirmation.
    prompt_on_exit = Bool( False, desc = "exit confirmation request" )

    # Any callable that returns a new model.
    _model_factory = Callable

    # The current status of the model.
    status = Str

    # Tuple of library versions.
    versions = Str

    # Buffers up the log messages so that they can be displayed later
#    handler = Instance(LogQueueHandler)

    # Log history
#    log_entries = List(Instance(LogEntry))

    #--------------------------------------------------------------------------
    #  Views:
    #--------------------------------------------------------------------------

    traits_view = View( HGroup( Item( "model", show_label = False ) ),
                        id        = "desktop_view_model.traits_view",
                        title     = " ",
                        icon      = frame_icon,
                        resizable = True,
                        style     = "custom",
                        kind      = "live",
                        buttons   = NoButtons,
                        menubar   = menubar,
#                        toolbar   = toolbar,
#                        statusbar=[StatusItem(name="status"),
#                                   StatusItem(name="versions", width=200)],
                        dock      = "vertical" )

    #--------------------------------------------------------------------------
    #  Edit model view properties:
    #--------------------------------------------------------------------------

    options_view = View( Item("prompt_on_exit"),
                         "_",
                         Item("wd"),
                         id           = "desktop_view_model.options_view",
                         icon         = frame_icon,
                         kind         = "livemodal",
                         title        = "Options",
                         buttons      = OKCancelButtons,
                         close_result = True )

    #--------------------------------------------------------------------------
    #  About application view:
    #--------------------------------------------------------------------------

    about_view = View( Label( license_label ),
                       title   = "About",
                       buttons = ["OK"],
                       icon    = frame_icon )

    #--------------------------------------------------------------------------
    #  Trait initialisers:
    #--------------------------------------------------------------------------

    def _handler_default(self):
        """ Trait initialiser.
        """
        logger = getLogger()#__name__)
        handler = add_log_queue_handler(logger, level=LOG_LEVEL)
        # set the view to update when something is logged.
#        handler._view = self

        return handler


    def _versions_default(self):
        """ Trait initialiser.
        """
        # Get the version numbers.
        py_version = sys.version[0:sys.version.find("(")]

        if ETSConfig.toolkit == "wx":
            import wx
            toolkit_version = wx.VERSION_STRING
        elif ETSConfig.toolkit == "qt4":
            from PyQt4 import QtCore
            toolkit_version = QtCore.PYQT_VERSION_STR
        else:
            toolkit_verion = ""

        traits_version = enthought.traits.version.__version__

        return "%s, %s, %s" % (py_version, toolkit_version, traits_version)

    #--------------------------------------------------------------------------
    #  Event handlers:
    #--------------------------------------------------------------------------

    def update(self):
        """ Update the table if new records are available """



        if self.handler.has_new_records():

            records = self.handler.get()

            self.log_entries = []
            for record in records[:]:
                print "BLAPP ", record.message

#                level_name = record.levelname
#                time=record.asctime
#                message=record.message

                entry = LogEntry(level_name="name", time="12:00", message="foo")
                print entry
                self.log_entries.append(entry)

            print "RECORDS", len(records), len(self.log_entries)


            if self.log_entries:
                self.status = self.log_entries[-1].message

    #--------------------------------------------------------------------------
    #  Action handlers:
    #--------------------------------------------------------------------------

    def new_model(self, info):
        """ Handles the 'New Model' action.
        """
        if not info.initialized:
            return # Escape.

        retval = confirm(parent  = info.ui.control,
                         message = "Replace existing model?",
                         title   = "New Model",
                         default = YES)
        if retval == YES:
            factory = self._model_factory

            if factory is not None:
                self.model = factory()


    def open_file(self, info):
        """ Handles the open action.
        """
        if not info.initialized:
            return

        dialog = FileDialog( action   = "open",
                             wildcard = "Pickle Files (*.pkl)|*.pkl|" \
                             "All Files (*.*)|*.*",
                             default_directory = self.wd )

        if dialog.open() == OK:
            fd = None

            try:
                fd = open( dialog.path, "rb" )
                self.model = pickle.load( fd )

            finally:
                if fd is not None:
                    fd.close()

            self.file = dialog.path
            self.wd   = dialog.directory

        del dialog


    def save(self, info):
        """ Handles saving the current model to the last file.
        """
        save_file = self.file

        if not isfile( save_file ):
            self.save_as( info )

        else:
            fd = None
            try:
                fd = open( save_file, "wb" )
                pickle.dump(self.model, fd)

            finally:
                if fd is not None:
                    fd.close()


    def save_as(self, info):
        """ Handles saving the current model to file.
        """
        if not info.initialized:
            return

        dialog = FileDialog( action   = "save as",
                             wildcard = "Pickle Files (*.pkl)|*.pkl|" \
                             "All Files (*.*)|*.*",
                             default_directory = self.wd )

        if dialog.open() == OK:
            fd = None
            try:
                fd = open( dialog.path, "wb" )
                pickle.dump( self.model, fd )
            finally:
                if fd is not None:
                    fd.close()

            self.file = dialog.path
            self.wd   = dialog.directory

        del dialog


    def options(self, info):
        """ Handles display of the options menu.
        """
        if info.initialized:
            self.edit_traits( parent = info.ui.control,
                              kind   = "livemodal",
                              view   = "options_view" )

    #---------------------------------------------------------------------------
    #  Handles the application exit action:
    #---------------------------------------------------------------------------

    def on_exit(self, info):
        """ Handles the application exit action.
        """
        if self.prompt_on_exit:# and (not is_ok):
            retval = confirm(parent  = info.ui.control,
                             message = "Are you sure you wish to exit?",
                             title   = "Confirm Exit",
                             default = YES)
            if retval == YES:
                self._on_close( info )
        else:
            self._on_close( info )


    def about(self, info):
        """ Handles displaying the about view.
        """
        if info.initialized:
            self.edit_traits( view   = "about_view",
                              parent = info.ui.control,
                              kind   = "livemodal" )

#------------------------------------------------------------------------------
#  Stand-alone call:
#------------------------------------------------------------------------------

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging.DEBUG)

    class Model ( HasTraits ):
        name      = Str( "model" )
        transient = Bool( False )

    mv = DesktopViewModel( model = Model(), _model_factory = Model )

    mv.configure_traits()

# EOF -------------------------------------------------------------------------
