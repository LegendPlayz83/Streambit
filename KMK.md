## Flashing nd Configuring the Keyboard

Steps to install the firmware and configure the keyboard:-

### 1. Downloading the Repository
Download or clone this repository to your computer.
https://github.com/LegendPlayz83/Streambit.git

### 2. Enter Boot Mode on the Pico
1. Unplug the Raspberry Pi Pico from your computer.
2. Hold down the **BOOTSEL** button on the Pico.
3. While holding the button, plug the Pico into your computer using a USB cable.
4. The computer will detect a new drive, namely **RPI-RP2**.

### 3. Flash the Firmware
1. Download the `.uf2` firmware file from this repo.
2. Drag and drop the file onto the **RPI-RP2** drive.

Once the file finishes copying, the Pico will reboot automatically.

### 4. Install KMK Files
After rebooting, the Pico will appear as a new drive (usually named **CIRCUITPY**).

Copy the KMK firmware files from this repository onto the Pico if they are not already included.

### 5. Configure the Keymap
The keyboard layout can be customised in the `code.py` (or `keymap.py`) file.

Open the file in a text editor nd edit the keymap section to match the layout you want.  
After saving the file, the keyboard will automatically reload with the new configuration.

### 6. Test the Keyboard
Unplug and reconnect the keyboard, open a text editor, and press some keys to make sure everything works.

<h1>KABOOM!</h1>
ITS DONE!!!
