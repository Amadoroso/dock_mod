# DockMod

A Python script to modify the macOS Dock autohide delay and adjust its animation speed. 

## Usage

Run the script to access the interactive prompt. You can choose to:
* **1**: Speed up the Dock. Prompts for an animation speed between `0` and `1` (defaults to `0.15` if left blank).
* **0**: Revert the Dock to default settings.
* **q**: Quit.

## Technical Details

The program uses the `subprocess` module to execute standard macOS commands. It modifies or deletes the following `com.apple.dock` keys and restarts the Dock via `killall`:
* `autohide-delay`
* `autohide-time-modifier`
* `autohide-fullscreen-delayed`

Terminal output includes basic color formatting (blue, red, green) for readability.

## Requirements

Python3
