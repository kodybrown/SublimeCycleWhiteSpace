import os, sublime, sublime_plugin

def set_whitespace( self, mode ):
    view = self.view
    view.settings().set("draw_white_space", mode)

class ShowNoWhitespaceCommand( sublime_plugin.TextCommand ):
    def run( self, edit ):
        set_whitespace(self, 'none')

class ShowSelectionWhitespaceCommand( sublime_plugin.TextCommand ):
    def run( self, edit ):
        set_whitespace(self, 'selection')

class ShowAllWhitespaceCommand( sublime_plugin.TextCommand ):
    def run( self, edit ):
        set_whitespace(self, 'all')

class CycleThroughWhitespaceCommand( sublime_plugin.TextCommand ):
    def run( self, edit ):
        view = self.view

        # Get the current white_space_type ('none', 'selection', 'all')
        white_space_type = view.settings().get("draw_white_space")

        # Get whether each option is allowed to be cycled through.
        # For instance, I can disable 'none' and simply alternate between 'selection' and 'all'.
        plugin_name = os.path.basename(__file__)[:-3]
        plugin_settings = sublime.load_settings(plugin_name + ".sublime-settings")

        allowed = plugin_settings.get("cycle_whitespace")

        # Change the white_space_type based on preferences..
        if white_space_type == "all":
            if 'none' in allowed:
                view.settings().set("draw_white_space", "none")
            elif 'selection' in allowed:
                view.settings().set("draw_white_space", "selection")

        elif white_space_type == "none":
            if 'selection' in allowed:
                view.settings().set("draw_white_space", "selection")
            elif 'all' in allowed:
                view.settings().set("draw_white_space", "all")
        else:
            if 'all' in allowed:
                view.settings().set("draw_white_space", "all")
            elif 'none' in allowed:
                view.settings().set("draw_white_space", "none")
