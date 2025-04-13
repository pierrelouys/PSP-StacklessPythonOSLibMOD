# pspos

The documentation for this module is being reconstructed. The accuracy of this page cannot be guaranteed.

The os module provides PSP-specific system utilities, interfacing with the PSP’s hardware and file system.

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
- **`__add__`**(...): x.<a href="#stat_result-__add__">`__add__`</a>(y) <==> x + y
- **`__contains__`**(...): x.<a href="#stat_result-__contains__">`__contains__`</a>(y) <==> y in x
- **`__eq__`**(...): x.<a href="#stat_result-__eq__">`__eq__`</a>(y) <==> x == y
- **`__ge__`**(...): x.<a href="#stat_result-__ge__">`__ge__`</a>(y) <==> x >= y
- **`__getitem__`**(...): x.<a href="#stat_result-__getitem__">`__getitem__`</a>(y) <==> x[y]
- **`__getslice__`**(...): x.<a href="#stat_result-__getslice__">`__getslice__`</a>(i, j) <==> x[i:j]  
  (Use of negative indices is not supported.)
- **`__gt__`**(...): x.<a href="#stat_result-__gt__">`__gt__`</a>(y) <==> x > y
- **`__hash__`**(...): x.<a href="#stat_result-__hash__">`__hash__`</a>() <==> hash(x)
- **`__le__`**(...): x.<a href="#stat_result-__le__">`__le__`</a>(y) <==> x <= y
- **`__len__`**(...): x.<a href="#stat_result-__len__">`__len__`</a>() <==> len(x)
- **`__lt__`**(...): x.<a href="#stat_result-__lt__">`__lt__`</a>(y) <==> x < y
- **`__mul__`**(...): x.<a href="#stat_result-__mul__">`__mul__`</a>(n) <==> x * n
- **`__ne__`**(...): x.<a href="#stat_result-__ne__">`__ne__`</a>(y) <==> x != y
- **`__reduce__`**(...): MISSING_DOC
- **`__repr__`**(...): x.<a href="#stat_result-__repr__">`__repr__`</a>() <==> repr(x)
- **`__rmul__`**(...): x.<a href="#stat_result-__rmul__">`__rmul__`</a>(n) <==> n * x

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
**`access`**(path, mode):  
- Purpose: Checks if a file exists and if the current user has the given permissions.
- Parameters: path (str) - Path to the file; mode (int) - Permissions mode.
- Return: Boolean (True if the file exists and has the required permissions).
- Notes: Raises OSError if the file does not exist or has insufficient permissions.


### [battery](#battery)
**`battery`**():  
- Description: Retrieves the current battery status.
- Returns: A tuple containing:
    - plugged: Whether the PSP is plugged in (1 if plugged, 0 if not).
    - present: Whether the battery is present (1 if present, 0 if not).
    - charging: Whether the battery is charging (1 if charging, 0 if not).
    - lifep: The battery life as a percentage (integer).
    - lifet: The estimated remaining battery time (integer, in minutes; 0 if the PSP is plugged in).
    - temp: The battery temperature (integer, in Celsius).
    - volt: The battery voltage (integer, millivolts).

### [chdir](#chdir)
**`chdir`**(path):  
- Description: Changes the current working directory.
- Parameters:
    - path: The target directory path (string).
- Returns: None on success. Raises OSError if the operation fails.

### [chmod](#chmod)
**`chmod`**(path, mode):  
- Description: Changes the file permissions of a specified file.
- Parameters:
    - path: The path of the file (string).
    - mode: The new permissions mode for the file (integer).
- Returns: None on success. Raises OSError on failure.

### [close](#close)
**`close`**(fd):  
- Description: Closes the file associated with the given file descriptor.
- Parameters:
    - fd: The file descriptor to close (integer).
- Returns: None on success. Raises OSError on failure.

### [delenv](#delenv)
**`delenv`**(...): (no full environment support)
- Description: This function would typically be used for environment variable handling.
- Details: On the PSP, these functions are either not supported or implemented as no-ops, and developers should be aware that environment variable handling is minimal or unavailable on this platform.

### [fdopen](#fdopen)
**`fdopen`**(fd, mode="r"):  
- Description: Converts a file descriptor into a Python file object.
- Parameters:
    - fd: The file descriptor (integer).
    - mode: The mode in which to open the file ("r" by default).
- Returns: A file object (file), or raises an error if the conversion fails.

### [freemem](#freemem)
**`freemem`**():
- Description: Returns the total free memory, in bytes.
- Returns: The amount of free memory (integer, in bytes).
- Details: This doesn't seem to work very well, see 'realmem' instead.

### [freemsspace](#freemsspace)
**`freemsspace`**():  
- Purpose: Returns the free space (in bytes) on the PSP’s memory stick (ms0:).
- Parameters: None
- Returns: A float representing the free space in bytes.

### [getbus](#getbus)
**`getbus`**(...):  
Returns the bus speed in MHz.

### [getclock](#getclock)
**`getclock`**():  
- Description: Retrieves the current CPU frequency.
- Returns: The current CPU frequency (integer, in MHz).

### [getclocks](#getclocks)
**`getclocks`**():  
- Description: Retrieves the current CPU and bus frequencies.
- Returns: A tuple containing the current CPU frequency and bus frequency (both integers in MHz).

### [getcwd](#getcwd)
**`getcwd`**():
- Description: Gets the current working directory.
- Parameters: None.
- Returns: The current directory as a string.
- Details: This function retrieves the current working directory of the PSP file system.

### [getenv](#getenv)
**`getenv`**(name):  
- Description: Retrieves the value of an environment variable.
- Parameters:
    - name: The name of the environment variable (string).
- Returns: The value of the environment variable as a string, or None if the variable does not exist.
- Details: This function does not interact with the PSP’s environment, as it lacks full environment variable support.

### [getenvdict](#getenvdict)
**`getenvdict`**(...): (no full environment support)
- Description: This function would typically be used for environment variable handling.
- Details: On the PSP, these functions are either not supported or implemented as no-ops, and developers should be aware that environment variable handling is minimal or unavailable on this platform.

### [getnickname](#getnickname)
**`getnickname`**():  
- Description: Retrieves the PSP’s nickname.
- Returns: The PSP’s nickname as a string.
- Details: Uses the system parameter ID for nickname.

### [getsystemparam](#getsystemparam)
**`getsystemparam`**(id):  
- Description: Retrieves a specific system parameter.
- Parameters:
    - id: The ID of the parameter to retrieve.
- Returns: The value of the requested system parameter, which could be either an integer or a string, depending on the parameter.

### [listdir](#listdir)
**`listdir`**(path):  
- Description: Lists the contents of a directory.
- Parameters:
    - path: The directory to list (string).
- Returns: A list of filenames (strings) in the directory.
- Details: This function wraps the PSP’s directory reading system calls and returns the names of files and directories inside the given directory, excluding "." and "..".

### [lstat](#lstat)
**`lstat`**(...):  
MISSING_DOC

### [mkdir](#mkdir)
**`mkdir`**(path, mode=0):  
- Description: Creates a new directory at the specified path.
- Parameters:
    - path: The directory to create (string).
    - mode: The permission mode for the directory (integer, default 0).
- Returns: None on success. Raises OSError on failure.

### [open](#open)
**`open`**(path, flags, mode=0777):  
- Description: Opens a file with the given flags and mode.
- Parameters:
    - path: The file path to open (string).
    - flags: File access flags such as O_RDONLY, O_WRONLY, etc.
    - mode: (Optional) The file mode (integer, default is 0777).
- Returns: A file descriptor (integer), or raises an OSError if the file cannot be opened.

### [powertick](#powertick)
**`powertick`**():  
- Description: Generates a power tick to prevent the PSP from going idle.
- Returns: None.

### [putenv](#putenv)
**`putenv`**(name, value):  
- Description: Sets the value of an environment variable.
- Parameters:
    - name: The name of the environment variable (string).
    - value: The new value for the variable (string).
- Returns: None.
- Details: The PSP platform does not support environment variables in the typical way, so this function has no effect.

### [realmem](#realmem)
**`realmem`**(size=4096):
- Description: Returns the actual free memory.
- Parameters:
    - size: The size of the memory blocks to allocate (integer, default is 4096 bytes).
- Returns: The total memory allocated and freed (integer).
- Details: This function works by allocating blocks of 'size' bytes until malloc() returns NULL, then freeing all the blocks.

### [remove](#remove)
**`remove`**(...):  
MISSING_DOC

### [rename](#rename)
**`rename`**(src, dst):
- Description: Renames a file or directory.
- Parameters:
    - src: The current name of the file or directory (string).
    - dst: The new name for the file or directory (string).
- Returns: None on success. Raises OSError on failure.

### [rmdir](#rmdir)
**`rmdir`**(path):  
- Description: Removes a directory.
- Parameters:
    -path: Path of the directory to remove (string).
- Returns: None on success. Raises OSError if the directory cannot be removed.

### [setbus](#setbus)
**`setbus`**(...):  
Sets the bus speed. Valid values are 1 to 167; an OSError is raised for other values.

### [setclock](#setclock)
**`setclock`**(cpufreq):  
- Description: Sets the CPU frequency.
- Parameters:
    - cpufreq: The desired CPU frequency (integer, in MHz).
- Details: Valid values are 1 to 333; an OSError is raised for other values.

### [setclocks](#setclocks)
**`setclocks`**(cpufreq, busfreq):  
- Description: Sets the CPU and bus frequencies.
- Parameters:
    - cpufreq: The desired CPU frequency (integer, in MHz).
    - busfreq: The desired bus frequency (integer, in MHz).
- Returns: None.
- Details: This function adjusts the PSP’s performance by modifying its clock frequencies. The valid CPU frequency range is 1-333 MHz, and the bus frequency is 1-167 MHz.

### [stat](#stat)
**`stat`**(path):  
- Description: Retrieves information about a file or directory.
- Parameters:
    - path: The path to the file or directory (string).
- Returns: A stat_result object that contains details such as file size, permissions, and modification times.
- Details: This function provides information about the specified file or directory. The returned object can be accessed like a tuple, with fields like st_mode, st_size, st_mtime, and more.

### [system](#system)
**`system`**(...):  
MISSING_DOC

### [unlink](#unlink)
**`unlink`**(path):  
- Description: Deletes a file at the specified path.
- Parameters:
    - path: The path of the file to remove (string).
- Returns: None on success. Raises OSError on failure.

### [utime](#utime)
**`utime`**(path, times): (not implemented)
- Description: Intended to update the access and modification times of a file.
- Details: This function is defined but not implemented, and developers should not expect it to function. It’s a placeholder for updating file times in the PSP file system.

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
