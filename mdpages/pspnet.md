# pspnet

The documentation for this module is being reconstructed. The accuracy of this page cannot be guaranteed.

---

## Table of Contents
1. [Classes](#classes)
   - [Error](#error)
2. [Functions](#functions)
   - [connectToAPCTL](#connecttoapctl)
   - [disconnectAPCTL](#disconnectapctl)
   - [enumConfigs](#enumconfigs)
   - [getAPCTLChannel](#getapctlchannel)
   - [getAPCTLSignalStrength](#getapctlsignalstrength)
   - [getAPCTLState](#getapctlstate)
   - [getIP](#getip)
   - [wlanEtherAddr](#wlanetheraddr)
   - [wlanIsPowered](#wlanispowered)
   - [wlanSwitchState](#wlanswitchstate)
3. [Data](#data)

---

## Classes

### [Error](#error)
#### Method resolution order:
- [Error](#Error)
- [exceptions.Exception](#Exception)
- [exceptions.BaseException](#BaseException)
- [__builtin__.object](#__builtin__.object)

#### Data descriptors defined here:
- **`__weakref__`**: list of weak references to the object (if defined)

#### Methods inherited from [exceptions.Exception](#Exception):
- **`__init__`**(...): x.<a href="#Error-__init__">`__init__`</a>(...) initializes x; see x.__class__.__doc__ for signature

#### Data and other attributes inherited from [exceptions.Exception](#Exception):
- **`__new__`** = `<built-in method __new__ of type object at 0x8abb148>`
  - T.<a href="#Error-__new__">`__new__`</a>(S, ...) → a new object with type S, a subtype of T

#### Methods inherited from [exceptions.BaseException](#BaseException):
- **`__delattr__`**(...): x.<a href="#Error-__delattr__">`__delattr__`</a>('name') <==> del x.name
- **`__getattribute__`**(...): x.<a href="#Error-__getattribute__">`__getattribute__`</a>('name') <==> x.name
- **`__getitem__`**(...): x.<a href="#Error-__getitem__">`__getitem__`</a>(y) <==> x[y]
- **`__getslice__`**(...): x.<a href="#Error-__getslice__">`__getslice__`</a>(i, j) <==> x[i:j]  
  (Use of negative indices is not supported.)
- **`__reduce__`**(...): MISSING_DOC
- **`__repr__`**(...): x.<a href="#Error-__repr__">`__repr__`</a>() <==> repr(x)
- **`__setattr__`**(...): x.<a href="#Error-__setattr__">`__setattr__`</a>('name', value) <==> x.name = value
- **`__setstate__`**(...): MISSING_DOC
- **`__str__`**(...): x.<a href="#Error-__str__">`__str__`</a>() <==> str(x)

#### Data descriptors inherited from [exceptions.BaseException](#BaseException):
- **`__dict__`**
- **`args`**
- **`message`**: exception message

---

## Functions

### [connectToAPCTL](#connecttoapctl)
**`connectToAPCTL`**(config=1, callback=None, timeout=None):  
- Description: Connects to an access point (AP) using the PSP's network configuration.
- Parameters:
    - config: (int, optional) Configuration option for the connection (default 1).
    - callback: (callable, optional) A callback function that gets called with the connection state during the process.
    - timeout: (int, optional) Timeout in seconds. If the connection process takes longer than this, it will abort.
- Returns: None if successful, raises an error if connection fails.
- Details:
    - Connects the PSP to the network using the specified configuration (starting with 1). 
    - If 'callback' is specified, it must be a callable that accepts one integer argument; it will be called on each connection state change with the new state as argument (0 through 4), and then once again with -1 as argument when the connection is established.
    - If 'timeout' is not specified, or less than 0, the function will block until the connection is established. If the Wifi switch is off, this means indefinitely. If 'timeout' is specified, and the connection couldn't be established after 'timeout' seconds, a pspnet.Error exception will be raised.  
    - This function may take keyword arguments, so you can write `connectToAPCTL(timeout=10)` if you want to specify only the timeout.

### [disconnectAPCTL](#disconnectapctl)
**`disconnectAPCTL`**():  
- Description: Disconnects the PSP from the currently connected access point.
- Parameters: None
- Returns: None

### [enumConfigs](#enumconfigs)
**`enumConfigs`**():  
- Description: Returns a list of (index, name, ipaddress) for each net configuration.
- Parameters: None
- Returns: A list of configurations, each represented as a tuple of (index, name, ip).
- Details: This function returns a list of network configuration profiles that the PSP has saved, including the configuration index, name, and associated IP address.

### [getAPCTLChannel](#getapctlchannel)
**`getAPCTLChannel`**():  
- Description: Retrieves the channel number of the access point the PSP is connected to.
- Parameters: None
- Returns: Integer representing the channel number of the AP.
- Details: Useful for identifying which channel the access point is using.

### [getAPCTLSignalStrength](#getapctlsignalstrength)
**`getAPCTLSignalStrength`**():  
- Description: Retrieves the signal strength of the currently connected access point.
- Parameters: None
- Returns: Integer representing the signal strength. The higher the value, the better the signal.

### [getAPCTLState](#getapctlstate)
**`getAPCTLState`**():  
- Description: Returns the current connection state.
- Parameters: None
- Returns: Integer representing the current state. Possible states include:
    - PSP_NET_APCTL_STATE_CONNECTED: Connected to the AP.
    - Other states such as scanning, joining, etc.
- Details: Useful to monitor the progress of an AP connection attempt.

### [getIP](#getip)
**`getIP`**():  
- Description: Returns the PSP IP address as a string in dotted decimal notation. Only use when connected.
- Parameters: None
- Returns: The IP address as a string.

### [wlanEtherAddr](#wlanetheraddr)
**`wlanEtherAddr`**():  
- Description: Retrieves the Ethernet (MAC) address of the PSP's WLAN interface.
- Parameters: None
- Returns: The MAC address as a string (6 bytes).

### [wlanIsPowered](#wlanispowered)
**`wlanIsPowered`**():  
- Description: Checks whether the PSP’s WLAN (Wi-Fi) is powered on.
- Parameters: None
- Returns: 1 if WLAN is powered on, 0 if it is off.

### [wlanSwitchState](#wlanswitchstate)
**`wlanSwitchState`**():  
- Description: Retrieves the state of the WLAN switch (on/off).
- Parameters: None
- Returns: 1 if the WLAN switch is on, 0 if it is off.

---

## Data

- **APCTL_STATE_CONNECTED** = -1
- **APCTL_STATE_DISCONNECTED** = 0
- **APCTL_STATE_EAP_AUTH** = 5
- **APCTL_STATE_GETTING_IP** = 3
- **APCTL_STATE_GOT_IP** = 4
- **APCTL_STATE_JOINING** = 2
- **APCTL_STATE_KEY_EXCHANGE** = 6
- **APCTL_STATE_SCANNING** = 1

---
