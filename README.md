
# SublimeCycleThroughWhitespace

Cycle's through Sublime Text's three options for displaying white space: none, selection, and all.

# Features

 * One shortcut key to cycle through the three possible modes of showing whitespace.
 * Configure which options to cycle through in the settings.
 * Provides a Whitespace menu (under View) to change whitespace.


# Installation

## Install The Plugin

Clone into your sublime packages directory.

OR, use Package Control, `Cycle Through Whitespace`.


## Install Requirements

 * Sublime Text 3
 * I don't know if it works with Sublime Text 2 or not.


# Configuration

## CycleThroughWhitespace.sublime-settings

Turn each option on or off here. If you want to alternate all three view options from your shortcut key, then set each to `true`. If you only want to alternate between `selection` and `all`, set only those two properties to `true`.

    {
        // Can be one or more of the following: "none", "selection", or "all"
        "cycle_whitespace": [ "none", "selection", "all" ]
    }

## Default (Windows).sublime-keymap

My default key bindings mirror that of Visual Studio. Feel free to change it to whatever you want.

    [
        { "keys": ["ctrl+r", "ctrl+w"], "command": "cycle_through_whitespace" }
    ]

## Authors

Many thanks to [skuroda](http://stackoverflow.com/users/1852931/skuroda) for his extremely helpful comment on [Stack Overflow](http://stackoverflow.com/questions/18496991/i-cant-get-this-to-work-in-sublime-text-3-i-am-trying-to-alternate-a-settin).

[wasatchwizard](http://stackoverflow.com/users/139793/wasatchwizard)
[skuroda](http://stackoverflow.com/users/1852931/skuroda)

