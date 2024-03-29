#ifndef KEYBOARD_MAP_H
#define KEYBOARD_MAP_H

#include <map>
#include <string>

std::map<string, char> keyboard = {
        { "NONE", 0x00 },
        { "SHIFT", 0x02 },
        { "a", 0x04 },
        { "b", 0x05 },
        { "c", 0x06 },
        { "d", 0x07 },
        { "e", 0x08 },
        { "f", 0x09 },
        { "g", 0x0a },
        { "h", 0x0b },
        { "i", 0x0c },
        { "j", 0x0d },
        { "k", 0x0e },
        { "l", 0x0f },
        { "m", 0x10 },
        { "n", 0x11 },
        { "o", 0x12 },
        { "p", 0x13 },
        { "q", 0x14 },
        { "r", 0x15 },
        { "s", 0x16 },
        { "t", 0x17 },
        { "u", 0x18 },
        { "v", 0x19 },
        { "w", 0x1a },
        { "x", 0x1b },
        { "y", 0x1c },
        { "z", 0x1d },
        { "1", 0x1e },
        { "2", 0x1f },
        { "3", 0x20 },
        { "4", 0x21 },
        { "5", 0x22 },
        { "6", 0x23 },
        { "7", 0x24 },
        { "8", 0x25 },
        { "9", 0x26 },
        { "0", 0x27 },
        { "ENTER", 0x28 },
        { "ESC", 0x29 },
        { "BACKSPACE", 0x2a },
        { "TAB", 0x2b },
        { "SPACE", 0x2c },
        { "-", 0x2d },
        { "=", 0x2e },
        { "[", 0x2f },
        { "]", 0x30 },
        { "\\", 0x31 },
        { "EUROPE1", 0x32 },
        { ";", 0x33 },
        { "'", 0x34 },
};

#endif //KEYBOARD_MAP_H