# SXHKD Keybindings Viewer With Rofi

## Project Overview

This project is designed to facilitate the search and viewing of `sxhkd` keybindings using a Rofi menu. `sxhkd` (Simple X HotKey Daemon) is a simple X hotkey daemon that reacts to input events by executing commands. This project reads keybindings from a configuration file, formats them, and presents them in a searchable and user-friendly Rofi menu.

## Features

- **Read Keybindings**: Parses a keybindings file to extract shortcuts and their descriptions.
- **Format Keybindings**: Formats the keybindings for a clean and readable display.
- **Rofi Menu Integration**: Displays the formatted keybindings in a Rofi menu for easy searching and selection.

## Project Components

### `generateKeybindingMap`

This function reads the keybindings file, processes each line to extract descriptions and shortcuts, and stores them in a dictionary.

### `formatKeybindings`

This function takes the dictionary of keybindings and formats them into a clean, readable string for display.

### `generateRofiMenuFromFormattedKeyBindings`

This function takes the formatted keybindings string and uses Rofi to display them in a menu.

### `main`

The main function orchestrates the reading, formatting, and displaying of keybindings.

## What I Learned

- **File I/O in Python**: Reading from and writing to files, handling file paths, and processing file contents.
- **String Formatting**: Aligning text for clean display, calculating maximum string lengths for formatting purposes.
- **Subprocess Module**: Using Python’s `subprocess` module to execute external commands and pass inputs.
- **Rofi Integration**: Integrating Python scripts with Rofi to create interactive menus.

## Motivation

The motivation behind this project was to create a simple and efficient way to search for `sxhkd` keybindings. As a frequent user of `sxhkd`, I found it cumbersome to manually search through the keybindings file. By integrating with Rofi, I can quickly and easily find the keybindings I need, improving my workflow and productivity.

## Future Improvements

- **Dynamic File Path**: Allow users to specify the keybindings file location via command-line arguments or a configuration setting.
- **Error Handling**: Implement robust error handling to manage issues such as missing files or incorrect file formats.
- **Customization**: Allow customization of the Rofi theme and display options.
