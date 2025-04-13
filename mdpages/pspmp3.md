# pspmp3

The documentation for this module is being reconstructed. The accuracy of this page cannot be guaranteed.

---

## Table of Contents
1. [Functions](#functions)
   - [end](#end)
   - [endofstream](#endofstream)
   - [freetune](#freetune)
   - [gettime](#gettime)
   - [init](#init)
   - [load](#load)
   - [pause](#pause)
   - [play](#play)
   - [setvolume](#setvolume)
   - [stop](#stop)

---

## Functions

### [end](#end)
**`end`**():  
- Description: Stops the current MP3 playback and calls freetune() to release resources used by the MP3 subsystem.
- Parameters: None
- Returns: None

### [endofstream](#endofstream)
**`endofstream`**():  
- Description: Checks if the MP3 playback has reached the end of the stream.
- Parameters: None
- Returns: Integer (1 if the stream has ended, 0 if it is still playing).

### [freetune](#freetune)
**`freetune`**():  
- Description: Frees up memory used by the MP3 file and subsystem.
- Parameters: None
- Returns: None

### [gettime](#gettime)
**`gettime`**():  
- Description: Retrieves the current playback time of the MP3 in the format HH:MM:SS.
- Parameters: None
- Returns: A string representing the playback time in HH:MM:SS format.

### [init](#init)
**`init`**(chan):
- Description: Initializes the MP3 subsystem.
- Parameters:
    - chan: The audio channel to be used for playback (integer).
- Returns: None
- Details: This function initializes the MP3 subsystem for playback, using the specified audio channel. It should be called before any MP3 files are loaded or played. 

### [load](#load)
**`load`**(path):  
- Description: Loads an MP3 file for playback.
- Parameters:
    - path: The path to the MP3 file (string).
- Returns: None
- Details: This function attempts to open the specified MP3 file at the given path and load it into memory for playback. If the file cannot be opened, it raises an IOError.

### [pause](#pause)
**`pause`**():  
- Description: Pauses MP3 playback, call again to unpause.
- Parameters: None
- Returns: None
- Details: Pauses the current MP3 playback. Calling this function again will resume playback from where it was paused.

### [play](#play)
**`play`**(loop):  
- Description: Play a loaded MP3 file.
- Parameters:
    - loop: An integer indicating whether the MP3 should loop when it finishes. 0 means no loop, while any non-zero value enables looping.
- Returns: None
- Details: Starts playing the loaded MP3 file. If loop is set to a non-zero value, the MP3 will loop continuously.

### [setvolume](#setvolume)
**`setvolume`**(...):  
Sets the volume in percentage.

### [stop](#stop)
**`stop`**():  
- Description: Stops MP3 playback.
- Parameters: None
- Returns: None
- Details: Stops any ongoing MP3 playback, halting the audio output.

---
