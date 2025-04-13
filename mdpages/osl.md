# osl

The documentation for this module is being reconstructed. The accuracy of this page cannot be guaranteed.

---

## Table of Contents
1. [Classes](#classes)
   - [Controller](#controller)
   - [Error](#error)
   - [Font](#font)
   - [Image](#image)
   - [Map](#map)
   - [SFont](#sfont)
   - [Sound](#sound)
2. [Functions](#functions)
3. [Data](#data)

---

## Classes

### [Controller](#controller)
#### Methods
- **`__init__`(...):** x.<a href="#Controller-__init__">`__init__`</a>(...) initializes x; see x.__class__.__doc__ for signature

#### Data Descriptors
- **analogX**
- **analogY**
- **autoRepeatCounter**
- **autoRepeatInit**
- **autoRepeatInterval**
- **autoRepeatMask**
- **held_L**
- **held_R**
- **held_circle**
- **held_cross**
- **held_down**
- **held_hold**
- **held_home**
- **held_left**
- **held_note**
- **held_right**
- **held_select**
- **held_square**
- **held_start**
- **held_triangle**
- **held_up**
- **pressed_L**
- **pressed_R**
- **pressed_circle**
- **pressed_cross**
- **pressed_down**
- **pressed_hold**
- **pressed_home**
- **pressed_left**
- **pressed_note**
- **pressed_right**
- **pressed_select**
- **pressed_square**
- **pressed_start**
- **pressed_triangle**
- **pressed_up**
- **released_L**
- **released_R**
- **released_circle**
- **released_cross**
- **released_down**
- **released_hold**
- **released_home**
- **released_left**
- **released_note**
- **released_right**
- **released_select**
- **released_square**
- **released_start**
- **released_triangle**
- **released_up**

#### Data and other attributes
- **`__new__`** = `<built-in method __new__ of type object at 0x8ac9380>`
---

### [Error](#error)

#### Method resolution order:
- [Error](#Error)
- [exceptions.Exception](#Exception)
- [exceptions.BaseException](#BaseException)
- [__builtin__.object](#__builtin__.object)

#### Data descriptors
- **`__weakref__`**: list of weak references to the object (if defined)

#### Methods inherited from [exceptions.Exception](#Exception):
- **`__init__`(...):** x.<a href="#Error-__init__">`__init__`</a>(...) initializes x; see x.__class__.__doc__ for signature

#### Data and other attributes inherited from [exceptions.Exception](#Exception):
- **`__new__`** = `<built-in method __new__ of type object at 0x8abb148>`

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

### [Font](#font)

#### Methods
- **`__init__`(...):** x.<a href="#Font-__init__">`__init__`</a>(filename) Loads a font from a file.
- **set**(...): Sets this font as the current font.

#### Data and other attributes
- **`__new__`** = `<built-in method __new__ of type object at 0x8ac9e5c>`
---

### [Image](#image)

The image module provides PSP-specific image manipulation and rendering, leveraging the OSLib graphics library for hardware-accelerated operations.

#### Methods
- **`__init__`(...):** x.<a href="#Image-__init__">`__init__`</a> initializes the image from a file or creates an image.
- **clear**(color): Clears the image with a given color.
- **convert**(newLocation, newFormat): 
    - Purpose: Converts an image to a new memory location and pixel format on the PSP.
    - Parameters: 
        - newLocation: Integer specifying memory location (e.g., osl.IN_RAM, osl.IN_VRAM).
        - newFormat: Integer specifying pixel format (e.g., OSL_PF_8888, OSL_PF_5650).
    - Returns: A new image object with the converted image, or raises an exception on failure.
    - Notes:
        - Use PSP-specific constants (e.g., osl.IN_VRAM) defined in the OSLib module.
        - VRAM conversions optimize rendering performance.
- **copy**(...): Copies another image into this one.
- **correctHalfBorder**(...): Wraps oslCorrectImageHalfBorder().
- **draw**(...): Wraps oslDrawImage().
- **getpixel**(...): MISSING_DOC
- **lock**(...): oslLockImage()
- **mirrorH**(...): MISSING_DOC
- **mirrorV**(...): MISSING_DOC
- **move**(newLocation):
    - Purpose: Moves an image to a different memory location (e.g., RAM to VRAM).
    - Parameters:
        - newLocation: Integer specifying target memory location (e.g., osl.IN_RAM, osl.IN_VRAM).
    - Returns: None
    - Notes:
        - Useful for optimizing memory usage or rendering speed.
- **rotate**(...): MISSING_DOC
- **setFrame**(...): MISSING_DOC
- **setFrameSize**(...): MISSING_DOC
- **setRotationCenter**(...): MISSING_DOC
- **setpixel**(...): MISSING_DOC
- **swizzle**(dst): oslSwizzleImage(dst, self)
- **swizzleto**(...): MISSING_DOC
- **tile**(x0, y0, x1, y1): oslCreateImageTile()
- **uncache**(...): Wraps oslUncacheImage().
- **unlock**(...): oslUnlockImage()
- **write**(...): Writes the image to a file.

#### Data descriptors
- **angle**
- **autoStrip**
- **centerX**
- **centerY**
- **offsetX0**
- **offsetX1**
- **offsetY0**
- **offsetY1**
- **sizeX**
- **sizeY**
- **stretchX**
- **stretchY**
- **x**
- **y**

#### Data and other attributes
- **`__new__`** = `<built-in method __new__ of type object at 0x8ac8ef4>`
---

### [Map](#map)

#### Methods
- **`__init__`(...):** x.<a href="#Map-__init__">`__init__`</a>(img, data, tileX, tileY) 'img' must be an instance of osl.Image.
- **draw**(...): Wraps oslDrawMap().
- **drawSimple**(...): Wraps oslDrawMapSimple().

#### Data descriptors
- **scrollX**
- **scrollY**

#### Data and other attributes
- **`__new__`** = `<built-in method __new__ of type object at 0x8ac9bf0>`
---

### [SFont](#sfont)

#### Methods
- **`__init__`(...):** x.<a href="#SFont-__init__">`__init__`</a>(...) initializes x.
- **drawString**(...): MISSING_DOC
- **measureText**(...): MISSING_DOC

#### Data and other attributes
- **`__new__`** = `<built-in method __new__ of type object at 0x8aca07c>`
---

### [Sound](#sound)

#### Methods
- **`__init__`(...):** x.<a href="#Sound-__init__">`__init__`</a>(...) initializes x.
- **getChannel**(...): Returns the channel used for this sound.
- **loop**(loop=1): Sets looping on/off.
- **pause**(pause=1): Pauses the playback.
- **play**(voice=0): Plays the sound.
- **stop**(...): Stops playing.

#### Data and other attributes
- **`__new__`** = `<built-in method __new__ of type object at 0x8ac9990>`
---

## Functions

- **`RGB`**(...): MISSING_DOC
- **`RGB12`**(...): MISSING_DOC
- **`RGB15`**(...): MISSING_DOC
- **`RGB16`**(...): MISSING_DOC
- **`RGBA`**(...): MISSING_DOC
- **`RGBA12`**(...): MISSING_DOC
- **`RGBA15`**(...): MISSING_DOC
- **`audioVSync`**(...): MISSING_DOC
- **`clearScreen`**(...): MISSING_DOC
- **`cls`**(...): MISSING_DOC
- **`dialogGetResult`**(...): MISSING_DOC
- **`disableTransparentColor`**(...): MISSING_DOC
- **`doQuit`**(...): MISSING_DOC
- **`drawDialog`**(...): MISSING_DOC
- **`drawFillRect`**(...): MISSING_DOC
- **`drawGradientRect`**(...): MISSING_DOC
- **`drawLine`**(...): MISSING_DOC
- **`drawOsk`**(...): MISSING_DOC
- **`drawRect`**(...): MISSING_DOC
- **`drawString`**(x, y, string): Draws a string using the current font
- **`drawTextBox`**(x0, y0, x1, y1, string, format): oslDrawTextBox
- **`endDialog`**(...): MISSING_DOC
- **`endDrawing`**(...): MISSING_DOC
- **`endFrame`**(...): MISSING_DOC
- **`endGfx`**(...): MISSING_DOC
- **`endOsk`**(...): MISSING_DOC
- **`flushDataCache`**(...): MISSING_DOC
- **`flushKey`**(...): MISSING_DOC
- **`getDialogButtonPressed`**(...): MISSING_DOC
- **`getDialogStatus`**(...): MISSING_DOC
- **`getDialogType`**(...): MISSING_DOC
- **`getFPS`**(...): MISSING_DOC
- **`getOskStatus`**(...): MISSING_DOC
- **`initAudio`**(...): MISSING_DOC
- **`initConsole`**(...): MISSING_DOC
- **`initErrorDialog`**(...): MISSING_DOC
- **`initGfx`**(...): MISSING_DOC
- **`initMessageDialog`**(...): MISSING_DOC
- **`initNetDialog`**(...): MISSING_DOC
- **`initOsk`**(...): MISSING_DOC
- **`intraFontInit`**(...): MISSING_DOC
- **`intraFontSetStyle`**(...): MISSING_DOC
- **`intraFontShutdown`**(...): MISSING_DOC
- **`kbhit`**(...): MISSING_DOC
- **`messageBox`**(...): MISSING_DOC
- **`moveTo`**(...): MISSING_DOC
- **`mustQuit`**(...): MISSING_DOC
- **`netInit`**(...): MISSING_DOC
- **`netTerm`**(...): MISSING_DOC
- **`oskGetResult`**(...): MISSING_DOC
- **`oskGetText`**(...): MISSING_DOC
- **`oskIsActive`**(...): MISSING_DOC
- **`print`**(...): MISSING_DOC
- **`printxy`**(...): MISSING_DOC
- **`safeQuit`**(...): MISSING_DOC
- **`saveScreenshot`**(...): MISSING_DOC
- **`setAlpha`**(...): MISSING_DOC
- **`setBilinearFilter`**(...): MISSING_DOC
- **`setBkColor`**(...): MISSING_DOC
- **`setDithering`**(...): MISSING_DOC
- **`setDrawBuffer`**(...): MISSING_DOC
- **`setFrameskip`**(...): MISSING_DOC
- **`setHoldForAnalog`**(...): MISSING_DOC
- **`setKeyAnalogToDPad`**(...): MISSING_DOC
- **`setKeyAutorepeat`**(...): MISSING_DOC
- **`setKeyAutorepeatInit`**(...): MISSING_DOC
- **`setKeyAutorepeatInterval`**(...): MISSING_DOC
- **`setKeyAutorepeatMask`**(...): MISSING_DOC
- **`setMaxFrameskip`**(...): MISSING_DOC
- **`setQuitOnLoadFailure`**(...): MISSING_DOC
- **`setScreenClipping`**(...): MISSING_DOC
- **`setTextColor`**(...): MISSING_DOC
- **`setTransparentColor`**(...): MISSING_DOC
- **`startDrawing`**(...): MISSING_DOC
- **`swapBuffers`**(...): MISSING_DOC
- **`syncDrawing`**(...): MISSING_DOC
- **`syncFrame`**(...): MISSING_DOC
- **`syncFrameEx`**(...): MISSING_DOC
- **`waitKey`**(...): MISSING_DOC
- **`waitVSync`**(...): MISSING_DOC

---

## Data

- **DEFAULT_BUFFER** = 145617296
- **DIALOG_CANCEL** = 1
- **DIALOG_ERROR** = 2
- **DIALOG_MESSAGE** = 1
- **DIALOG_NETCONF** = 3
- **DIALOG_NONE** = 0
- **DIALOG_OK** = 0
- **ERR_APCTL_CONNECT** = -11
- **ERR_APCTL_GETINFO** = -10
- **ERR_APCTL_GETSTATE** = -13
- **ERR_APCTL_TIMEOUT** = -12
- **ERR_RESOLVER_CREATE** = -14
- **ERR_RESOLVER_RESOLVING** = -15
- **ERR_WLAN_OFF** = -16
- **FMT_NONE** = 0
- **FMT_STREAM** = 1024
- **FX_ADD** = 3
- **FX_ALPHA** = 2
- **FX_COLOR** = 4096
- **FX_FLAT** = 1
- **FX_NONE** = 0
- **FX_RGBA** = 256
- **FX_SUB** = 4
- **INTRAFONT_ACTIVE** = 145110268
- **INTRAFONT_ADVANCE_H** = 145109992
- **INTRAFONT_ADVANCE_V** = 145110012
- **INTRAFONT_ALIGN_CENTER** = 145110056
- **INTRAFONT_ALIGN_FULL** = 145110104
- **INTRAFONT_ALIGN_LEFT** = 145110032
- **INTRAFONT_ALIGN_RIGHT** = 145110080
- **INTRAFONT_CACHE_ALL** = 145110356
- **INTRAFONT_CACHE_ASCII** = 145110332
- **INTRAFONT_CACHE_LARGE** = 145110308
- **INTRAFONT_CACHE_MED** = 145110288
- **INTRAFONT_SCROLL_LEFT** = 145110128
- **INTRAFONT_SCROLL_RIGHT** = 145110176
- **INTRAFONT_SCROLL_SEESAW** = 145110152
- **INTRAFONT_SCROLL_THROUGH** = 145110200
- **INTRAFONT_STRING_ASCII** = 145110376
- **INTRAFONT_STRING_BIG5** = 145110544
- **INTRAFONT_STRING_CP1251** = 145110568
- **INTRAFONT_STRING_CP1252** = 145110592
- **INTRAFONT_STRING_CP437** = 145110400
- **INTRAFONT_STRING_CP850** = 145110424
- **INTRAFONT_STRING_CP866** = 145110448
- **INTRAFONT_STRING_GBK** = 145110496
- **INTRAFONT_STRING_KOR** = 145110520
- **INTRAFONT_STRING_SJIS** = 145110472
- **INTRAFONT_STRING_UTF8** = 145110616
- **INTRAFONT_WIDTH_FIX** = 145110248
- **INTRAFONT_WIDTH_VAR** = 145110228
- **IN_RAM** = 2
- **IN_VRAM** = 1
- **KEYMASK_CIRCLE** = 8192
- **KEYMASK_CROSS** = 16384
- **KEYMASK_DOWN** = 64
- **KEYMASK_HOLD** = 131072
- **KEYMASK_HOME** = 65536
- **KEYMASK_L** = 256
- **KEYMASK_LEFT** = 128
- **KEYMASK_NOTE** = 8388608
- **KEYMASK_R** = 512
- **KEYMASK_RIGHT** = 32
- **KEYMASK_SELECT** = 1
- **KEYMASK_SQUARE** = 32768
- **KEYMASK_START** = 8
- **KEYMASK_TRIANGLE** = 4096
- **KEYMASK_UP** = 16
- **KEY_CIRCLE** = 14
- **KEY_CROSS** = 15
- **KEY_DOWN** = 7
- **KEY_HOLD** = 18
- **KEY_HOME** = 17
- **KEY_L** = 9
- **KEY_LEFT** = 8
- **KEY_NOTE** = 24
- **KEY_R** = 10
- **KEY_RIGHT** = 6
- **KEY_SELECT** = 1
- **KEY_SQUARE** = 16
- **KEY_START** = 4
- **KEY_TRIANGLE** = 13
- **KEY_UP** = 5
- **MB_CANCEL** = 2
- **MB_NO** = 4
- **MB_OK** = 1
- **MB_QUIT** = 5
- **MB_YES** = 3
- **NET_ERROR_APCTL** = -4
- **NET_ERROR_CERT** = -8
- **NET_ERROR_COOKIE** = -9
- **NET_ERROR_HTTP** = -6
- **NET_ERROR_HTTPS** = -7
- **NET_ERROR_INET** = -2
- **NET_ERROR_NET** = -1
- **NET_ERROR_RESOLVER** = -3
- **NET_ERROR_SSL** = -5
- **OSK_CANCEL** = 1
- **OSK_CHINESE_SIMPLIFIED** = 145109972
- **OSK_CHINESE_TRADITIONAL** = 145109948
- **OSK_DUTCH** = 145109896
- **OSK_ENGLISH** = 145109836
- **OSK_FRENCH** = 145109848
- **OSK_GERMAN** = 145109872
- **OSK_ITALIAN** = 145109884
- **OSK_JAPANESE** = 145109820
- **OSK_KOREAN** = 145109936
- **OSK_OK** = 0
- **OSK_PORTUGUESE** = 145109908
- **OSK_RUSSIAN** = 145109924
- **OSK_SPANISH** = 145109860
- **PF_4444** = 2
- **PF_4BIT** = 4
- **PF_5551** = 1
- **PF_5650** = 0
- **PF_8888** = 3
- **PF_8BIT** = 5
- **SECONDARY_BUFFER** = 145617380
- **SWIZZLED** = 8
- **USER_ABORTED** = -17
