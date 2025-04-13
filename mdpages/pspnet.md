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
- **`__init__`(...):** x.<a href="#Error-__init__">`__init__`</a>(...) initializes x; see x.__class__.__doc__ for signature

#### Data and other attributes inherited from [exceptions.Exception](#Exception):
- **`__new__`** = `<built-in method __new__ of type object at 0x8abb148>`
  - T.<a href="#Error-__new__">`__new__`</a>(S, ...) → a new object with type S, a subtype of T

#### Methods inherited from [exceptions.BaseException](#BaseException):
- **`__delattr__`(...):** x.<a href="#Error-__delattr__">`__delattr__`</a>('name') <==> del x.name
- **`__getattribute__`(...):** x.<a href="#Error-__getattribute__">`__getattribute__`</a>('name') <==> x.name
- **`__getitem__`(...):** x.<a href="#Error-__getitem__">`__getitem__`</a>(y) <==> x[y]
- **`__getslice__`(...):** x.<a href="#Error-__getslice__">`__getslice__`</a>(i, j) <==> x[i:j]  
  (Use of negative indices is not supported.)
- **`__reduce__`(...):** MISSING_DOC
- **`__repr__`(...):** x.<a href="#Error-__repr__">`__repr__`</a>() <==> repr(x)
- **`__setattr__`(...):** x.<a href="#Error-__setattr__">`__setattr__`</a>('name', value) <==> x.name = value
- **`__setstate__`(...):** MISSING_DOC
- **`__str__`(...):** x.<a href="#Error-__str__">`__str__`</a>() <==> str(x)

#### Data descriptors inherited from [exceptions.BaseException](#BaseException):
- **`__dict__`**
- **`args`**
- **`message`**: exception message

---

## Functions

### [connectToAPCTL](#connecttoapctl)
**`connectToAPCTL`(...):**  
Connects the PSP to the network using the specified configuration (starting with 1). If 'callback' is specified, it must be a callable that accepts one integer argument; it will be called on each connection state change with the new state as argument (0 through 4), and then once again with -1 as argument when the connection is established.  
If 'timeout' is not specified, or less than 0, the function will block until the connection is established. If the Wifi switch is off, this means indefinitely. If 'timeout' is specified, and the connection couldn't be established after 'timeout' seconds, a pspnet.Error exception will be raised.  
This function may take keyword arguments, so you can write `connectToAPCTL(timeout=10)` if you want to specify only the timeout.

### [disconnectAPCTL](#disconnectapctl)
**`disconnectAPCTL`(...):**  
Disconnects the PSP.

### [enumConfigs](#enumconfigs)
**`enumConfigs`(...):**  
Returns a list of (index, name, ipaddress) for each net configuration.

### [getAPCTLChannel](#getapctlchannel)
**`getAPCTLChannel`(...):**  
MISSING_DOC

### [getAPCTLSignalStrength](#getapctlsignalstrength)
**`getAPCTLSignalStrength`(...):**  
MISSING_DOC

### [getAPCTLState](#getapctlstate)
**`getAPCTLState`(...):**  
Returns the current connection state.

### [getIP](#getip)
**`getIP`(...):**  
Returns the PSP IP address as a string in dotted decimal notation. Only use when connected.

### [wlanEtherAddr](#wlanetheraddr)
**`wlanEtherAddr`(...):**  
Returns the Ethernet address of the WLAN device.

### [wlanIsPowered](#wlanispowered)
**`wlanIsPowered`(...):**  
Returns whether the WLAN device is powered on.

### [wlanSwitchState](#wlanswitchstate)
**`wlanSwitchState`(...):**  
Returns the state of the WLAN switch.

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
