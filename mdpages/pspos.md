# Python: built-in module pspos

---

## Table of Contents
1. [Classes](#classes)
   - [stat_result](#stat_result)
2. [Functions](#functions)
   - [access](#access)
   - [battery](#battery)
   - [chdir](#chdir)
   - [chmod](#chmod)
   - [close](#close)
   - [delenv](#delenv)
   - [fdopen](#fdopen)
   - [freemem](#freemem)
   - [freemsspace](#freemsspace)
   - [getbus](#getbus)
   - [getclock](#getclock)
   - [getclocks](#getclocks)
   - [getcwd](#getcwd)
   - [getenv](#getenv)
   - [getenvdict](#getenvdict)
   - [getnickname](#getnickname)
   - [getsystemparam](#getsystemparam)
   - [listdir](#listdir)
   - [lstat](#lstat)
   - [mkdir](#mkdir)
   - [open](#open)
   - [powertick](#powertick)
   - [putenv](#putenv)
   - [realmem](#realmem)
   - [remove](#remove)
   - [rename](#rename)
   - [rmdir](#rmdir)
   - [setbus](#setbus)
   - [setclock](#setclock)
   - [setclocks](#setclocks)
   - [stat](#stat)
   - [system](#system)
   - [unlink](#unlink)
   - [utime](#utime)
3. [Data](#data)

---

## Classes

### [stat_result](#stat_result)
**Result from `stat` or `lstat`.**  
This object may be accessed either as a tuple of (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) or via the attributes `st_mode`, `st_ino`, `st_dev`, `st_nlink`, `st_uid`, and so on.  
See `os.stat` for more information.

#### Methods defined here:
- **`__add__`(...):** x.<a href="#stat_result-__add__">`__add__`</a>(y) <==> x + y
- **`__contains__`(...):** x.<a href="#stat_result-__contains__">`__contains__`</a>(y) <==> y in x
- **`__eq__`(...):** x.<a href="#stat_result-__eq__">`__eq__`</a>(y) <==> x == y
- **`__ge__`(...):** x.<a href="#stat_result-__ge__">`__ge__`</a>(y) <==> x >= y
- **`__getitem__`(...):** x.<a href="#stat_result-__getitem__">`__getitem__`</a>(y) <==> x[y]
- **`__getslice__`(...):** x.<a href="#stat_result-__getslice__">`__getslice__`</a>(i, j) <==> x[i:j]  
  (Use of negative indices is not supported.)
- **`__gt__`(...):** x.<a href="#stat_result-__gt__">`__gt__`</a>(y) <==> x > y
- **`__hash__`(...):** x.<a href="#stat_result-__hash__">`__hash__`</a>() <==> hash(x)
- **`__le__`(...):** x.<a href="#stat_result-__le__">`__le__`</a>(y) <==> x <= y
- **`__len__`(...):** x.<a href="#stat_result-__len__">`__len__`</a>() <==> len(x)
- **`__lt__`(...):** x.<a href="#stat_result-__lt__">`__lt__`</a>(y) <==> x < y
- **`__mul__`(...):** x.<a href="#stat_result-__mul__">`__mul__`</a>(n) <==> x * n
- **`__ne__`(...):** x.<a href="#stat_result-__ne__">`__ne__`</a>(y) <==> x != y
- **`__reduce__`(...):** MISSING_DOC
- **`__repr__`(...):** x.<a href="#stat_result-__repr__">`__repr__`</a>() <==> repr(x)
- **`__rmul__`(...):** x.<a href="#stat_result-__rmul__">`__rmul__`</a>(n) <==> n * x

#### Data descriptors defined here:
- **`st_atime`**: time of last access
- **`st_ctime`**: time of last change
- **`st_dev`**: device
- **`st_gid`**: group ID of owner
- **`st_ino`**: inode
- **`st_mode`**: protection bits
- **`st_mtime`**: time of last modification
- **`st_nlink`**: number of hard links
- **`st_size`**: total size, in bytes
- **`st_uid`**: user ID of owner

#### Data and other attributes defined here:
- **`__new__`** = `<built-in method __new__ of type object at 0x8accd38>`  
  T.<a href="#stat_result-__new__">`__new__`</a>(S, ...) → a new object with type S, a subtype of T
- **`n_fields`** = 10
- **`n_sequence_fields`** = 10
- **`n_unnamed_fields`** = 0

---

## Functions

### [access](#access)
**`access`(...):**  
MISSING_DOC

### [battery](#battery)
**`battery`(...):**  
Returns a tuple (plugged, present, charging, lifep, lifet, temp, volt).  
- **plugged**: 1 if the PSP is plugged in, 0 else.
- **present**: 1 if the battery is present, 0 else.
- **charging**: 1 if the battery is charging, 0 else.
- **lifep**: life of the battery in percent.
- **lifet**: life of the battery in minutes (0 if the PSP is plugged in).
- **temp**: battery temperature (Celsius).
- **volt**: battery voltage (millivolts).

### [chdir](#chdir)
**`chdir`(...):**  
MISSING_DOC

### [chmod](#chmod)
**`chmod`(...):**  
MISSING_DOC

### [close](#close)
**`close`(...):**  
MISSING_DOC

### [delenv](#delenv)
**`delenv`(...):**  
MISSING_DOC

### [fdopen](#fdopen)
**`fdopen`(...):**  
MISSING_DOC

### [freemem](#freemem)
**`freemem`(...):**  
Returns the total free memory, in bytes. Note: this doesn't seem to work very well, see 'realmem' instead.

### [freemsspace](#freemsspace)
**`freemsspace`(...):**  
MISSING_DOC

### [getbus](#getbus)
**`getbus`(...):**  
Returns the bus speed in MHz.

### [getclock](#getclock)
**`getclock`(...):**  
Returns the CPU clock speed in MHz.

### [getclocks](#getclocks)
**`getclocks`(...):**  
MISSING_DOC

### [getcwd](#getcwd)
**`getcwd`(...):**  
MISSING_DOC

### [getenv](#getenv)
**`getenv`(...):**  
MISSING_DOC

### [getenvdict](#getenvdict)
**`getenvdict`(...):**  
MISSING_DOC

### [getnickname](#getnickname)
**`getnickname`(...):**  
MISSING_DOC

### [getsystemparam](#getsystemparam)
**`getsystemparam`(...):**  
MISSING_DOC

### [listdir](#listdir)
**`listdir`(...):**  
MISSING_DOC

### [lstat](#lstat)
**`lstat`(...):**  
MISSING_DOC

### [mkdir](#mkdir)
**`mkdir`(...):**  
MISSING_DOC

### [open](#open)
**`open`(...):**  
MISSING_DOC

### [powertick](#powertick)
**`powertick`(...):**  
Generates a power tick to prevent the PSP from going idle.

### [putenv](#putenv)
**`putenv`(...):**  
MISSING_DOC

### [realmem](#realmem)
**`realmem`(...):**  
Returns the actual free memory. Takes an optional parameter 'size'. This function works by allocating blocks of 'size' bytes until malloc() returns NULL, then freeing all the blocks. 'size' is 4096 by default.

### [remove](#remove)
**`remove`(...):**  
MISSING_DOC

### [rename](#rename)
**`rename`(...):**  
MISSING_DOC

### [rmdir](#rmdir)
**`rmdir`(...):**  
MISSING_DOC

### [setbus](#setbus)
**`setbus`(...):**  
Sets the bus speed. Valid values are 1 to 167; an OSError is raised for other values.

### [setclock](#setclock)
**`setclock`(...):**  
Sets the CPU clock speed. Valid values are 1 to 333; an OSError is raised for other values.

### [setclocks](#setclocks)
**`setclocks`(...):**  
MISSING_DOC

### [stat](#stat)
**`stat`(...):**  
MISSING_DOC

### [system](#system)
**`system`(...):**  
MISSING_DOC

### [unlink](#unlink)
**`unlink`(...):**  
MISSING_DOC

### [utime](#utime)
**`utime`(...):**  
MISSING_DOC

---

## Data

- **O_CREAT** = 512
- **O_EXCL** = 2048
- **O_RDONLY** = 0
- **O_RDWR** = 2
- **O_WRONLY** = 1
- **PSP_SYSTEMPARAM_ADHOC_CHANNEL_1** = 1
- **PSP_SYSTEMPARAM_ADHOC_CHANNEL_11** = 11
- **PSP_SYSTEMPARAM_ADHOC_CHANNEL_6** = 6
- **PSP_SYSTEMPARAM_ADHOC_CHANNEL_AUTOMATIC** = 0
- **PSP_SYSTEMPARAM_DATE_FORMAT_DDMMYYYY** = 2
- **PSP_SYSTEMPARAM_DATE_FORMAT_MMDDYYYY** = 1
- **PSP_SYSTEMPARAM_DATE_FORMAT_YYYYMMDD** = 0
- **PSP_SYSTEMPARAM_DAYLIGHTSAVINGS_SAVING** = 1
- **PSP_SYSTEMPARAM_DAYLIGHTSAVINGS_STD** = 0
- **PSP_SYSTEMPARAM_ID_INT_ADHOC_CHANNEL** = 2
- **PSP_SYSTEMPARAM_ID_INT_DATE_FORMAT** = 4
- **PSP_SYSTEMPARAM_ID_INT_DAYLIGHTSAVINGS** = 7
- **PSP_SYSTEMPARAM_ID_INT_LANGUAGE** = 8
- **PSP_SYSTEMPARAM_ID_INT_TIMEZONE** = 6
- **PSP_SYSTEMPARAM_ID_INT_TIME_FORMAT** = 5
- **PSP_SYSTEMPARAM_ID_INT_WLAN_POWERSAVE** = 3
- **PSP_SYSTEMPARAM_ID_STRING_NICKNAME** = 1
- **PSP_SYSTEMPARAM_LANGUAGE_DUTCH** = 6
- **PSP_SYSTEMPARAM_LANGUAGE_ENGLISH** = 1
- **PSP_SYSTEMPARAM_LANGUAGE_FRENCH** = 2
- **PSP_SYSTEMPARAM_LANGUAGE_GERMAN** = 4
- **PSP_SYSTEMPARAM_LANGUAGE_ITALIAN** = 5
- **PSP_SYSTEMPARAM_LANGUAGE_JAPANESE** = 0
- **PSP_SYSTEMPARAM_LANGUAGE_KOREAN** = 9
- **PSP_SYSTEMPARAM_LANGUAGE_PORTUGUESE** = 7
- **PSP_SYSTEMPARAM_LANGUAGE_SPANISH** = 3
- **PSP_SYSTEMPARAM_TIME_FORMAT_12HR** = 1
- **PSP_SYSTEMPARAM_TIME_FORMAT_24HR** = 0
- **PSP_SYSTEMPARAM_WLAN_POWERSAVE_OFF** = 0
- **PSP_SYSTEMPARAM_WLAN_POWERSAVE_ON** = 1

---
