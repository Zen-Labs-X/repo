# 1.0.2

[Full change logs](https://www.mobileread.com/forums/showpost.php?p=4557691&postcount=84)

# 1.0.1

[Full change logs](https://www.mobileread.com/forums/showpost.php?p=4556415&postcount=78)

# 1.0.0

[Full change logs](https://www.mobileread.com/forums/showpost.php?p=4556114&postcount=66)

# v0.2.0

KOReader Bluetooth Page Turner Plugin for Kobo Devices

The KOReader Bluetooth Page Turner Plugin enables seamless Bluetooth functionality on Kobo e-readers, allowing users to connect devices like page turners directly to KOReader. This plugin provides enhanced control over navigation, font adjustments, and more, with features designed for an optimized reading experience (now without needing to restart KOReader).

Features

**Core Commands:**
**Refresh Device Input:** Re-establishes input listening when connection is lost and automatically reconnected.
Connect to Device: Sends a connection request to a paired Bluetooth device.
**Bluetooth On/Off:** Manage Bluetooth and WiFi directly from KOReader to conserve battery life.
**Automatic Listening:** Automatically listens to connected Bluetooth devices without needing a restart.
**Dedicated Bluetooth Events:** Custom events like "BTGotoNextChapter," "BTLeft," "BTRight," "BTDecreaseFontSize," "BTToggleBookmark," and more allow precise control over reading and device functions.
**Gesture Integration:** Commands can be triggered using customizable gestures.
**Installation:** Includes steps for pairing, configuring device.lua, and setting up connect.sh for easy Bluetooth connection.
Example device.lua Configuration


```lua
event_map = {
    -- Bluetooth device mappings
    [46]  = "BTGotoNextChapter",   
    [45]  = "BTGotoPrevChapter",   
    [32]  = "BTDecreaseFontSize",  
    [23]  = "BTIncreaseFontSize",  
    [48]  = "BTToggleBookmark",    
    [25]  = "BTLeft",              
    [49]  = "BTRight",             
    [19]  = "BTIterateRotation",   
    [109] = "BTBluetoothOff",      
}
```

This plugin has been tested on Clara 2E, with detailed configuration instructions provided for other devices like Libra 2. Contributions are welcome, with ongoing efforts to automate and expand support across more Kobo devices. For detailed installation steps and further customization, please refer to the repository.
