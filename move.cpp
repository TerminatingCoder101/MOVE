#include <iostream>
#include <cstring>
#include <fstream>
#include <keyboard_map.h>

#define TO_HEX(i) std::stoi(i, nullptr, 16)

void send(std::string file, char data[], size_t size) {
    std::ofstream hidg(file, std::ios::out | std::ios::binary);

    // Write the data to the HID device
    hidg.write(data, size);

    // Close the file
    hidg.close();
}

bool check_args(int argc, char *argv[]) {
    if (strcmp(argv[1], "mouse") == 0) {
        if (argc < 4) return false;
        else return true;
    } else if (strcmp(argv[1], "keyboard") == 0) {
        if (argc < 4) return false;
        else return true;
    } else {
        return false;
    }
}

/**
 * Mouse: two signed values for x and y
 * Keyboard: two strings, the first is a modifier ("NONE" for no modifier) and the second is a key
 * @param argc
 * @param argv
 * @return
 */
int main(int argc, char *argv[]) {
    // check if the arguments are valid
    if (!check_args(argc, argv)) {
        std::cerr << "Invalid arguments\n";
        return 1;
    }

    if (strcmp(argv[1], "mouse") == 0) {
        char data[] = {0x00, TO_HEX(argv[2]), TO_HEX(argv[3]), 0x00};
        send("/dev/hidg1", data, sizeof(data));
    } else if (strcmp(argv[1], "keyboard") == 0) {
        char data[] = {keyboard[argv[2]], keyboard[argv[3]], 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
        send("/dev/hidg0", data, sizeof(data));
        char release[] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
        send("/dev/hidg0", release, sizeof(release));
    } else if (strcmp(argv[1], "release") == 0) {
        char data[] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
        send("/dev/hidg0", data, sizeof(data));
    }
}