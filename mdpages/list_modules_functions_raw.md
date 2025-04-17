## osl Module

### osl - Classes

#### Controller
__init__(): Returns a Controller object.
##### Attributes
analogX
analogY
autoRepeatCounter
autoRepeatInit
autoRepeatInterval
autoRepeatMask
held_L
held_R
held_circle
held_cross
held_down
held_hold
held_home
held_left
held_note
held_right
held_select
held_square
held_start
held_triangle
held_up
pressed_L
pressed_R
pressed_circle
pressed_cross
pressed_down
pressed_hold
pressed_home
pressed_left
pressed_note
pressed_right
pressed_select
pressed_square
pressed_start
pressed_triangle
pressed_up
released_L
released_R
released_circle
released_cross
released_down
released_hold
released_home
released_left
released_note
released_right
released_select
released_square
released_start
released_triangle
released_up
#### Font
__init__(str): Takes a file path (e.g. "font.oft").
set(): Sets the font as the current font for text rendering.
#### Image
__init__(str, int, int): Takes a file path, memory location, and pixel format.
__init__(tuple, int, int): Takes a size tuple, memory location, and pixel format.
clear(int): Takes a color.
convert
copy(Image): Takes an Image object. Copies the source image to the target image.
correctHalfBorder()
draw(int, int): Draws the image at specified coordinates.
getpixel
lock
mirrorH
mirrorV
move
rotate(int): Takes an angle in degrees.
setFrame
setFrameSize
setRotationCenter(): Sets the rotation center to the image's center.
setpixel
swizzle
swizzleto
tile
uncache
unlock
write
##### Attributes
angle: Attribute (float). Sets rotation angle in degrees.
autoStrip
centerX: Attribute (int). Sets horizontal center for rotation/scaling.
centerY: Attribute (int). Sets vertical center for rotation/scaling.
offsetX0
offsetX1
offsetY0
offsetY1
sizeX: Attribute (int). Width of the image.
sizeY: Attribute (int). Height of the image.
stretchX: Attribute (int). Sets horizontal scaling factor.
stretchY: Attribute (int). Sets vertical scaling factor.
x: Attribute (int).
y: Attribute (int).
#### Map
__init__(Image, object, int, int): Takes an Image object, a map object, and tile dimensions.
drawSimple(): Draws the map.
##### Attributes
scrollX: Attribute (int). Sets horizontal scroll position.

#### SFont
__init__(str): Takes a file path (e.g., "sfont.png"). Loads a sprite-based font.
drawString(int, int, str): Takes x, y coordinates and text. Uses the loaded SFont.
measureText
#### Sound
__init__(str, int): Takes a file path and format.
getChannel
loop()
pause
play(int): Takes a channel number.
stop()

### osl - Functions
RGB(int, int, int): Takes red, green, blue values (0-255).
RGB12
RGB15
RGB16
RGBA(int, int, int, int): Takes red, green, blue, alpha values (0-255).
RGBA12
RGBA15
audioVSync()
clearScreen(int): Takes a color.
cls
dialogGetResult(): Returns int.  Gets result of dialog.
disableTransparentColor()
doQuit(): Signals the application to exit.
drawDialog(): Renders active dialog.
drawFillRect(int, int, int, int, int)
drawGradientRect(int, int, int, int, int, int, int, int): Takes x1, y1, x2, y2, and four colors.
drawLine(int, int, int, int, int)
drawOsk(): Renders on-screen keyboard.
drawRect(int, int, int, int, int)
drawString(int, int, str): Takes x, y coordinates and text.
drawTextBox(x0, y0, x1, y1, string, format)
endDialog(): Closes active dialog.
endDrawing(): Ends drawing operations for the frame.
endFrame(): Ends the current frame.
endGfx(): Terminates graphics system.
endOsk(): Closes on-screen keyboard.
flushDataCache
flushKey
getDialogButtonPressed
getDialogStatus(): Returns int (e.g., 0 for complete). Checks dialog status.
getDialogType(): Returns bool. Checks if a dialog is active.
getFPS(): Returns int.
getOskStatus(): Returns int (e.g., 0 for complete). Checks OSK status.
initAudio(): Initializes audio system.
initConsole(): Initializes console for text output.
initErrorDialog
initGfx(int, bool): Takes pixel format (e.g., osl.PF_8888) and fullscreen flag.
initMessageDialog(str, int): Takes message and type.
initNetDialog()
initOsk(str, str, int, int): Takes title, initial text, max length, and type.
kbhit
messageBox
moveTo
mustQuit(): Returns bool.
netInit
netTerm(): Terminates network connection.
oskGetResult(): Returns int. Gets OSK result.
oskGetText(): Returns str. Gets text entered in OSK.
oskIsActive(): Returns bool. Checks if OSK is active.
print
printxy(int, int, str): Takes x, y coordinates and text.
safeQuit
saveScreenshot(fileName)
setAlpha(effect, coeff): Takes integer (e.g. osl.FX_ALPHA) and coefficient for the effect (integer).
setBilinearFilter(int)
setBkColor(int): Takes a color.
setDithering(bool)
setDrawBuffer(Image): Takes an osl.Image or predefined constant (e.g., DEFAULT_BUFFER, SECONDARY_BUFFER). Sets rendering target.
setFrameskip(int): Takes frameskip value.
setHoldForAnalog
setKeyAnalogToDPad(int): Takes a threshold (e.g., 80). Maps analog stick to D-pad with specified sensitivity.
setKeyAutorepeat
setKeyAutorepeatInit
setKeyAutorepeatInterval
setKeyAutorepeatMask
setMaxFrameskip
setQuitOnLoadFailure(bool): Takes a boolean.
setScreenClipping
setTextColor(int): Takes a color.
setTransparentColor
startDrawing(): Begins drawing operations for the frame.
swapBuffers()
syncDrawing()
syncFrame(): Returns bool. Synchronizes frame rendering, returns skip flag.
syncFrameEx
waitKey
waitVSync

### osl - Attributes
DEFAULT_BUFFER = 145617296
DIALOG_CANCEL = 1
DIALOG_ERROR = 2
DIALOG_MESSAGE = 1
DIALOG_NETCONF = 3
DIALOG_NONE = 0
DIALOG_OK = 0
ERR_APCTL_CONNECT = -11
ERR_APCTL_GETINFO = -10
ERR_APCTL_GETSTATE = -13
ERR_APCTL_TIMEOUT = -12
ERR_RESOLVER_CREATE = -14
ERR_RESOLVER_RESOLVING = -15
ERR_WLAN_OFF = -16
FMT_NONE = 0
FMT_STREAM = 1024
FX_ADD = 3
FX_ALPHA = 2
FX_COLOR = 4096
FX_FLAT = 1
FX_NONE = 0
FX_RGBA = 256
FX_SUB = 4
IN_RAM = 2
IN_VRAM = 1
KEYMASK_CIRCLE = 8192
KEYMASK_CROSS = 16384
KEYMASK_DOWN = 64
KEYMASK_HOLD = 131072
KEYMASK_HOME = 65536
KEYMASK_L = 256
KEYMASK_LEFT = 128
KEYMASK_NOTE = 8388608
KEYMASK_R = 512
KEYMASK_RIGHT = 32
KEYMASK_SELECT = 1
KEYMASK_SQUARE = 32768
KEYMASK_START = 8
KEYMASK_TRIANGLE = 4096
KEYMASK_UP = 16
KEY_CIRCLE = 14
KEY_CROSS = 15
KEY_DOWN = 7
KEY_HOLD = 18
KEY_HOME = 17
KEY_L = 9
KEY_LEFT = 8
KEY_NOTE = 24
KEY_R = 10
KEY_RIGHT = 6
KEY_SELECT = 1
KEY_SQUARE = 16
KEY_START = 4
KEY_TRIANGLE = 13
KEY_UP = 5
MB_CANCEL = 2
MB_NO = 4
MB_OK = 1
MB_QUIT = 5
MB_YES = 3
NET_ERROR_APCTL = -4
NET_ERROR_CERT = -8
NET_ERROR_COOKIE = -9
NET_ERROR_HTTP = -6
NET_ERROR_HTTPS = -7
NET_ERROR_INET = -2
NET_ERROR_NET = -1
NET_ERROR_RESOLVER = -3
NET_ERROR_SSL = -5
OSK_CANCEL = 1
OSK_CHINESE_SIMPLIFIED = 145109972
OSK_CHINESE_TRADITIONAL = 145109948
OSK_DUTCH = 145109896
OSK_ENGLISH = 145109836
OSK_FRENCH = 145109848
OSK_GERMAN = 145109872
OSK_ITALIAN = 145109884
OSK_JAPANESE = 145109820
OSK_KOREAN = 145109936
OSK_OK = 0
OSK_PORTUGUESE = 145109908
OSK_RUSSIAN = 145109924
OSK_SPANISH = 145109860
PF_4444 = 2
PF_4BIT = 4
PF_5551 = 1
PF_5650 = 0
PF_8888 = 3
PF_8BIT = 5
SECONDARY_BUFFER = 145617380
SWIZZLED = 8
USER_ABORTED = -17

## pspmp3 Module
### pspmp3 - Functions
end
endofstream(): Returns bool.
freetune
gettime
init(int)
load(str):
pause
play(bool): Takes a loop flag.
setvolume
stop():

## pspnet Module
### pspnet - Functions
connectToAPCTL
disconnectAPCTL
enumConfigs
getAPCTLChannel
getAPCTLSignalStrength
getAPCTLState
getIP
wlanEtherAddr
wlanIsPowered
wlanSwitchState

## os (pspos) Module
### os - Functions
access
battery
chdir
chmod
close
delenv
error
execl
execle
execlp
execlpe
execvp
execvpe
fdopen
freemem
freemsspace
getbus(): Returns int.
getclock(): Returns int.
getclocks
getcwd
getenv
getenvdict
getnickname
getsystemparam
listdir(str): Takes a directory path. Returns list of files.
lstat
makedirs
mkdir
open
powertick
putenv
realmem
remove
removedirs
rename
renames
rmdir
setbus
setclock
setclocks
stat
stat_result
system
unlink
urandom
utime
walk
