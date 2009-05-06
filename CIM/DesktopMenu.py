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

""" Model view menus and menu items.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.pyface.api \
    import ImageResource

from enthought.traits.ui.menu \
    import MenuBar, ToolBar, Menu, Action

#------------------------------------------------------------------------------
#  File actions:
#------------------------------------------------------------------------------

new_action = Action( name        = "&New",
                     accelerator = "Ctrl+N",
                     action      = "new_model",
                     image       = ImageResource( "new" ),
                     tooltip     = "New (Ctrl+N)" )

open_action = Action( name        = "&Open",
                      accelerator = "Ctrl+O",
                      action      = "open_file",
                      image       = ImageResource( "open" ),
                      tooltip     = "Open (Ctrl+O)" )

save_action = Action( name        = "&Save",
                      accelerator = "Ctrl+S",
                      action      = "save",
                      image       = ImageResource("save"),
                      tooltip     = "Save (Ctrl+S)" )

save_as_action = Action( name        = "Save &As",
                         accelerator = "Ctrl+Shift+S",
                         action      = "save_as",
                         image       = ImageResource( "save" ),
                         tooltip     = "Save As (Ctrl+Shift+S)" )

#------------------------------------------------------------------------------
#  Revert all changes action.
#------------------------------------------------------------------------------

revert_action = Action( name         = "&Revert",
                        action       = "_on_revert",
                        defined_when = "ui.history is not None",
                        enabled_when = "ui.history.can_undo" )

#------------------------------------------------------------------------------
#  Close view window action.
#------------------------------------------------------------------------------

close_action = Action( name        = "E&xit",
                       accelerator = "Alt+X",
                       action      = "on_exit",
                       image       = ImageResource( "exit" ),
                       tooltip     = "Exit (Alt+X)" )

#------------------------------------------------------------------------------
#  Edit actions:
#------------------------------------------------------------------------------

undo_action = Action( name         = "Undo",
                      action       = "_on_undo",
                      accelerator  = "Ctrl+Z",
                      defined_when ="ui.history is not None",
                      enabled_when = "ui.history.can_undo",
                      image        = ImageResource( "undo" ),
                      tooltip      = "Undo (Ctrl+Z)" )

#------------------------------------------------------------------------------
#  Action to redo last undo.
#------------------------------------------------------------------------------

redo_action = Action( name         = "Redo",
                      action       = "_on_redo",
                      accelerator  = "Ctrl+Y",
                      defined_when = "ui.history is not None",
                      enabled_when = "ui.history.can_redo",
                      image        = ImageResource( "redo" ),
                      tooltip      = "Redo (Ctrl+Y)" )

options_action = Action( name = "Prefere&nces", action = "options" )

#------------------------------------------------------------------------------
#  Help actions:
#------------------------------------------------------------------------------

help_action = Action( name    = "Help",
                      action  = "show_help",
                      image   = ImageResource("help"),
                      tooltip = "Help" )

about_action = Action( name = "About",
                       action = "about",
                       image = ImageResource( "about" ),
                       tooltip = "About Application" )

#------------------------------------------------------------------------------
#  Menus:
#------------------------------------------------------------------------------

file_menu = Menu( "|", new_action, open_action, "_", save_action,
                                                     save_as_action,
                                                     revert_action,
                                                     "_",
                                                     close_action,
                                                     name="&File" )

edit_menu = Menu( "|", undo_action, redo_action, "_", options_action,
                                                      name="&Edit" )

help_menu = Menu( "|", about_action, name="&Help")

menubar = MenuBar( file_menu, edit_menu, help_menu )

#------------------------------------------------------------------------------
#  Model view tool bar:
#------------------------------------------------------------------------------

toolbar = ToolBar( "|", close_action, "_", new_action,
                                           open_action,
                                           save_action,
                                           save_as_action,
                                           "_",
                                           undo_action,
                                           redo_action,
                                           "_",
#                                           show_divider = False
                                           show_tool_names = False )

# EOF -------------------------------------------------------------------------
