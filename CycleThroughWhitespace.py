import os, sublime, sublime_plugin

class CycleThroughWhitespaceCommand( sublime_plugin.TextCommand ):
    def run( self, edit ):
        view = self.view

        # Get the current white_space_type ('none', 'selection', 'all')
        white_space_type = view.settings().get("draw_white_space")

        # Get whether each option is allowed to be cycled through.
        # For instance, I can disable 'none' and simply alternate between 'selection' and 'all'.
        plugin_name = os.path.basename(__file__)[:-3]
        plugin_settings = sublime.load_settings(plugin_name + ".sublime-settings")

        if view.settings().has("cycle_whitespace_none"):
            cycle_none = plugin_settings.get("cycle_whitespace_none")
        elif plugin_settings.has("cycle_whitespace_none"):
            cycle_none = plugin_settings.get("cycle_whitespace_none")
        else:
            cycle_none = True

        if view.settings().has("cycle_whitespace_selection"):
            cycle_selection = plugin_settings.get("cycle_whitespace_selection")
        elif plugin_settings.has("cycle_whitespace_selection"):
            cycle_selection = plugin_settings.get("cycle_whitespace_selection")
        else:
            cycle_selection = True

        if view.settings().has("cycle_whitespace_all"):
            cycle_all = plugin_settings.get("cycle_whitespace_all")
        elif plugin_settings.has("cycle_whitespace_all"):
            cycle_all = plugin_settings.get("cycle_whitespace_all")
        else:
            cycle_all = True

        # Change the white_space_type based on preferences..
        if white_space_type == "all":
            if cycle_none:
                view.settings().set("draw_white_space", "none")
            elif cycle_selection:
                view.settings().set("draw_white_space", "selection")

        elif white_space_type == "none":
            if cycle_selection:
                view.settings().set("draw_white_space", "selection")
            elif cycle_all:
                view.settings().set("draw_white_space", "all")
        else:
            if cycle_all:
                view.settings().set("draw_white_space", "all")
            elif cycle_none:
                view.settings().set("draw_white_space", "none")
