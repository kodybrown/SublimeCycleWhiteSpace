
# SublimeCycleThroughWhitespace

Cycle's through Sublime Text's three options for displaying white space: none, selection, and all.

# Features

 * Configure which options to cycle through in the settings.


# Installation

## Install The Plugin

Either clone into your sublime packages directory. Sorry, I haven't even looked at using [Package Control](https://github.com/wbond/sublime_package_control/) yet.

## Install Requirements

 * Sublime Text 3
 * I don't know if it works with ST2.


# Configuration

## CycleThroughWhitespace.sublime-settings

Turn each option on or off here. If you want to alternate all three view options from your shortcut key, then set each to `true`. If you only want to alternate between `selection` and `all`, set only those two properties to `true`.

    {
        "cycle_whitespace_none": true,
        "cycle_whitespace_selection": true,
        "cycle_whitespace_all": true
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

