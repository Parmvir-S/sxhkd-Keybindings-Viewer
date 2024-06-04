import subprocess

def generateKeybindingMap(keybindingsFileLocation):
    keybindingMap = {}
    fileLines = open(keybindingsFileLocation, "r")
    bindingComponents = []
    for fileLine in fileLines:
        fileLine = fileLine.strip()
        if fileLine == '#':
            description = bindingComponents[1]
            shortcut = bindingComponents[2]
            #command = bindingComponents[3]
            keybindingMap[description] = shortcut
            bindingComponents = []
        bindingComponents.append(fileLine)
    return keybindingMap

def formatKeybindings(keybindings):
    formatted = []
    max_prog_len = max(len(prog) for prog in keybindings.keys())
    max_key_len = max(len(key) for key in keybindings.values())
    for prog, key in keybindings.items():
        formatted.append(f"{prog.ljust(max_prog_len)}    {key.ljust(max_key_len)}")
    output = "\n".join(formatted)
    print(output)
    return output

def generateRofiMenuFromFormattedKeyBindings(formattedKeybindings):
    rofi_command = [
        'rofi', '-dmenu', '-i', '-no-custom', '-p', 'Keybindings', '-theme-str',
        'listview {columns: 1; lines: 10;}'
    ]
    subprocess.run(rofi_command, input=formattedKeybindings, text=True)

def main():
    keybindingsFileLocation = "/home/parm/.config/bspwm/scripts/keybindingsViewer/keybindings.txt"
    keybindingMap = generateKeybindingMap(keybindingsFileLocation)
    formattedKeybindings = formatKeybindings(keybindingMap)
    generateRofiMenuFromFormattedKeyBindings(formattedKeybindings)

if __name__ == "__main__":
    main()
