"""




    /** Key code constant: Number modifier key.
     * Used to enter numeric symbols.
     * This key is not Num Lock; it is more like {@link #KEYCODE_ALT_LEFT} and is
     * interpreted as an ALT key by {@link android.text.method.MetaKeyKeyListener}. */
    public static final int KEYCODE_NUM             = 78;
    /** Key code constant: Headset Hook key.
     * Used to hang up calls and stop media. */
    public static final int KEYCODE_HEADSETHOOK     = 79;
    /** Key code constant: Camera Focus key.
     * Used to focus the camera. */
    public static final int KEYCODE_FOCUS           = 80;   // *Camera* focus
    /** Key code constant: '+' key. */
    public static final int KEYCODE_PLUS            = 81;
    /** Key code constant: Menu key. */
    public static final int KEYCODE_MENU            = 82;
    /** Key code constant: Notification key. */
    public static final int KEYCODE_NOTIFICATION    = 83;
    /** Key code constant: Search key. */
    public static final int KEYCODE_SEARCH          = 84;
    /** Key code constant: Play/Pause media key. */
    public static final int KEYCODE_MEDIA_PLAY_PAUSE= 85;
    /** Key code constant: Stop media key. */
    public static final int KEYCODE_MEDIA_STOP      = 86;
    /** Key code constant: Play Next media key. */
    public static final int KEYCODE_MEDIA_NEXT      = 87;
    /** Key code constant: Play Previous media key. */
    public static final int KEYCODE_MEDIA_PREVIOUS  = 88;
    /** Key code constant: Rewind media key. */
    public static final int KEYCODE_MEDIA_REWIND    = 89;
    /** Key code constant: Fast Forward media key. */
    public static final int KEYCODE_MEDIA_FAST_FORWARD = 90;
    /** Key code constant: Mute key.
     * Mutes the microphone, unlike {@link #KEYCODE_VOLUME_MUTE}. */
    public static final int KEYCODE_MUTE            = 91;
    /** Key code constant: Page Up key. */
    public static final int KEYCODE_PAGE_UP         = 92;
    /** Key code constant: Page Down key. */
    public static final int KEYCODE_PAGE_DOWN       = 93;
    /** Key code constant: Picture Symbols modifier key.
     * Used to switch symbol sets (Emoji, Kao-moji). */
    public static final int KEYCODE_PICTSYMBOLS     = 94;   // switch symbol-sets (Emoji,Kao-moji)
    /** Key code constant: Switch Charset modifier key.
     * Used to switch character sets (Kanji, Katakana). */
    public static final int KEYCODE_SWITCH_CHARSET  = 95;   // switch char-sets (Kanji,Katakana)
    /** Key code constant: A Button key.
     * On a game controller, the A button should be either the button labeled A
     * or the first button on the bottom row of controller buttons. */
    public static final int KEYCODE_BUTTON_A        = 96;
    /** Key code constant: B Button key.
     * On a game controller, the B button should be either the button labeled B
     * or the second button on the bottom row of controller buttons. */
    public static final int KEYCODE_BUTTON_B        = 97;
    /** Key code constant: C Button key.
     * On a game controller, the C button should be either the button labeled C
     * or the third button on the bottom row of controller buttons. */
    public static final int KEYCODE_BUTTON_C        = 98;
    /** Key code constant: X Button key.
     * On a game controller, the X button should be either the button labeled X
     * or the first button on the upper row of controller buttons. */
    public static final int KEYCODE_BUTTON_X        = 99;
    /** Key code constant: Y Button key.
     * On a game controller, the Y button should be either the button labeled Y
     * or the second button on the upper row of controller buttons. */
    public static final int KEYCODE_BUTTON_Y        = 100;
    /** Key code constant: Z Button key.
     * On a game controller, the Z button should be either the button labeled Z
     * or the third button on the upper row of controller buttons. */
    public static final int KEYCODE_BUTTON_Z        = 101;
    /** Key code constant: L1 Button key.
     * On a game controller, the L1 button should be either the button labeled L1 (or L)
     * or the top left trigger button. */
    public static final int KEYCODE_BUTTON_L1       = 102;
    /** Key code constant: R1 Button key.
     * On a game controller, the R1 button should be either the button labeled R1 (or R)
     * or the top right trigger button. */
    public static final int KEYCODE_BUTTON_R1       = 103;
    /** Key code constant: L2 Button key.
     * On a game controller, the L2 button should be either the button labeled L2
     * or the bottom left trigger button. */
    public static final int KEYCODE_BUTTON_L2       = 104;
    /** Key code constant: R2 Button key.
     * On a game controller, the R2 button should be either the button labeled R2
     * or the bottom right trigger button. */
    public static final int KEYCODE_BUTTON_R2       = 105;
    /** Key code constant: Left Thumb Button key.
     * On a game controller, the left thumb button indicates that the left (or only)
     * joystick is pressed. */
    public static final int KEYCODE_BUTTON_THUMBL   = 106;
    /** Key code constant: Right Thumb Button key.
     * On a game controller, the right thumb button indicates that the right
     * joystick is pressed. */
    public static final int KEYCODE_BUTTON_THUMBR   = 107;
    /** Key code constant: Start Button key.
     * On a game controller, the button labeled Start. */
    public static final int KEYCODE_BUTTON_START    = 108;
    /** Key code constant: Select Button key.
     * On a game controller, the button labeled Select. */
    public static final int KEYCODE_BUTTON_SELECT   = 109;
    /** Key code constant: Mode Button key.
     * On a game controller, the button labeled Mode. */
    public static final int KEYCODE_BUTTON_MODE     = 110;
    /** Key code constant: Escape key. */
    public static final int KEYCODE_ESCAPE          = 111;
    /** Key code constant: Forward Delete key.
     * Deletes characters ahead of the insertion point, unlike {@link #KEYCODE_DEL}. */
    public static final int KEYCODE_FORWARD_DEL     = 112;
    /** Key code constant: Left Control modifier key. */
    public static final int KEYCODE_CTRL_LEFT       = 113;
    /** Key code constant: Right Control modifier key. */
    public static final int KEYCODE_CTRL_RIGHT      = 114;
    /** Key code constant: Caps Lock key. */
    public static final int KEYCODE_CAPS_LOCK       = 115;
    /** Key code constant: Scroll Lock key. */
    public static final int KEYCODE_SCROLL_LOCK     = 116;
    /** Key code constant: Left Meta modifier key. */
    public static final int KEYCODE_META_LEFT       = 117;
    /** Key code constant: Right Meta modifier key. */
    public static final int KEYCODE_META_RIGHT      = 118;
    /** Key code constant: Function modifier key. */
    public static final int KEYCODE_FUNCTION        = 119;
    /** Key code constant: System Request / Print Screen key. */
    public static final int KEYCODE_SYSRQ           = 120;
    /** Key code constant: Break / Pause key. */
    public static final int KEYCODE_BREAK           = 121;
    /** Key code constant: Home Movement key.
     * Used for scrolling or moving the cursor around to the start of a line
     * or to the top of a list. */
    public static final int KEYCODE_MOVE_HOME       = 122;
    /** Key code constant: End Movement key.
     * Used for scrolling or moving the cursor around to the end of a line
     * or to the bottom of a list. */
    public static final int KEYCODE_MOVE_END        = 123;
    /** Key code constant: Insert key.
     * Toggles insert / overwrite edit mode. */
    public static final int KEYCODE_INSERT          = 124;
    /** Key code constant: Forward key.
     * Navigates forward in the history stack.  Complement of {@link #KEYCODE_BACK}. */
    public static final int KEYCODE_FORWARD         = 125;
    /** Key code constant: Play media key. */
    public static final int KEYCODE_MEDIA_PLAY      = 126;
    /** Key code constant: Pause media key. */
    public static final int KEYCODE_MEDIA_PAUSE     = 127;
    /** Key code constant: Close media key.
     * May be used to close a CD tray, for example. */
    public static final int KEYCODE_MEDIA_CLOSE     = 128;
    /** Key code constant: Eject media key.
     * May be used to eject a CD tray, for example. */
    public static final int KEYCODE_MEDIA_EJECT     = 129;
    /** Key code constant: Record media key. */
    public static final int KEYCODE_MEDIA_RECORD    = 130;
    /** Key code constant: F1 key. */
    public static final int KEYCODE_F1              = 131;
    /** Key code constant: F2 key. */
    public static final int KEYCODE_F2              = 132;
    /** Key code constant: F3 key. */
    public static final int KEYCODE_F3              = 133;
    /** Key code constant: F4 key. */
    public static final int KEYCODE_F4              = 134;
    /** Key code constant: F5 key. */
    public static final int KEYCODE_F5              = 135;
    /** Key code constant: F6 key. */
    public static final int KEYCODE_F6              = 136;
    /** Key code constant: F7 key. */
    public static final int KEYCODE_F7              = 137;
    /** Key code constant: F8 key. */
    public static final int KEYCODE_F8              = 138;
    /** Key code constant: F9 key. */
    public static final int KEYCODE_F9              = 139;
    /** Key code constant: F10 key. */
    public static final int KEYCODE_F10             = 140;
    /** Key code constant: F11 key. */
    public static final int KEYCODE_F11             = 141;
    /** Key code constant: F12 key. */
    public static final int KEYCODE_F12             = 142;
    /** Key code constant: Num Lock key.
     * This is the Num Lock key; it is different from {@link #KEYCODE_NUM}.
     * This key alters the behavior of other keys on the numeric keypad. */
    public static final int KEYCODE_NUM_LOCK        = 143;
    /** Key code constant: Numeric keypad '0' key. */
    public static final int KEYCODE_NUMPAD_0        = 144;
    /** Key code constant: Numeric keypad '1' key. */
    public static final int KEYCODE_NUMPAD_1        = 145;
    /** Key code constant: Numeric keypad '2' key. */
    public static final int KEYCODE_NUMPAD_2        = 146;
    /** Key code constant: Numeric keypad '3' key. */
    public static final int KEYCODE_NUMPAD_3        = 147;
    /** Key code constant: Numeric keypad '4' key. */
    public static final int KEYCODE_NUMPAD_4        = 148;
    /** Key code constant: Numeric keypad '5' key. */
    public static final int KEYCODE_NUMPAD_5        = 149;
    /** Key code constant: Numeric keypad '6' key. */
    public static final int KEYCODE_NUMPAD_6        = 150;
    /** Key code constant: Numeric keypad '7' key. */
    public static final int KEYCODE_NUMPAD_7        = 151;
    /** Key code constant: Numeric keypad '8' key. */
    public static final int KEYCODE_NUMPAD_8        = 152;
    /** Key code constant: Numeric keypad '9' key. */
    public static final int KEYCODE_NUMPAD_9        = 153;
    /** Key code constant: Numeric keypad '/' key (for division). */
    public static final int KEYCODE_NUMPAD_DIVIDE   = 154;
    /** Key code constant: Numeric keypad '*' key (for multiplication). */
    public static final int KEYCODE_NUMPAD_MULTIPLY = 155;
    /** Key code constant: Numeric keypad '-' key (for subtraction). */
    public static final int KEYCODE_NUMPAD_SUBTRACT = 156;
    /** Key code constant: Numeric keypad '+' key (for addition). */
    public static final int KEYCODE_NUMPAD_ADD      = 157;
    /** Key code constant: Numeric keypad '.' key (for decimals or digit grouping). */
    public static final int KEYCODE_NUMPAD_DOT      = 158;
    /** Key code constant: Numeric keypad ',' key (for decimals or digit grouping). */
    public static final int KEYCODE_NUMPAD_COMMA    = 159;
    /** Key code constant: Numeric keypad Enter key. */
    public static final int KEYCODE_NUMPAD_ENTER    = 160;
    /** Key code constant: Numeric keypad '=' key. */
    public static final int KEYCODE_NUMPAD_EQUALS   = 161;
    /** Key code constant: Numeric keypad '(' key. */
    public static final int KEYCODE_NUMPAD_LEFT_PAREN = 162;
    /** Key code constant: Numeric keypad ')' key. */
    public static final int KEYCODE_NUMPAD_RIGHT_PAREN = 163;
    /** Key code constant: Volume Mute key.
     * Mutes the speaker, unlike {@link #KEYCODE_MUTE}.
     * This key should normally be implemented as a toggle such that the first press
     * mutes the speaker and the second press restores the original volume. */
    public static final int KEYCODE_VOLUME_MUTE     = 164;
    /** Key code constant: Info key.
     * Common on TV remotes to show additional information related to what is
     * currently being viewed. */
    public static final int KEYCODE_INFO            = 165;
    /** Key code constant: Channel up key.
     * On TV remotes, increments the television channel. */
    public static final int KEYCODE_CHANNEL_UP      = 166;
    /** Key code constant: Channel down key.
     * On TV remotes, decrements the television channel. */
    public static final int KEYCODE_CHANNEL_DOWN    = 167;
    /** Key code constant: Zoom in key. */
    public static final int KEYCODE_ZOOM_IN         = 168;
    /** Key code constant: Zoom out key. */
    public static final int KEYCODE_ZOOM_OUT        = 169;
    /** Key code constant: TV key.
     * On TV remotes, switches to viewing live TV. */
    public static final int KEYCODE_TV              = 170;
    /** Key code constant: Window key.
     * On TV remotes, toggles picture-in-picture mode or other windowing functions. */
    public static final int KEYCODE_WINDOW          = 171;
    /** Key code constant: Guide key.
     * On TV remotes, shows a programming guide. */
    public static final int KEYCODE_GUIDE           = 172;
    /** Key code constant: DVR key.
     * On some TV remotes, switches to a DVR mode for recorded shows. */
    public static final int KEYCODE_DVR             = 173;
    /** Key code constant: Bookmark key.
     * On some TV remotes, bookmarks content or web pages. */
    public static final int KEYCODE_BOOKMARK        = 174;
    /** Key code constant: Toggle captions key.
     * Switches the mode for closed-captioning text, for example during television shows. */
    public static final int KEYCODE_CAPTIONS        = 175;
    /** Key code constant: Settings key.
     * Starts the system settings activity. */
    public static final int KEYCODE_SETTINGS        = 176;
    /** Key code constant: TV power key.
     * On TV remotes, toggles the power on a television screen. */
    public static final int KEYCODE_TV_POWER        = 177;
    /** Key code constant: TV input key.
     * On TV remotes, switches the input on a television screen. */
    public static final int KEYCODE_TV_INPUT        = 178;
    /** Key code constant: Set-top-box power key.
     * On TV remotes, toggles the power on an external Set-top-box. */
    public static final int KEYCODE_STB_POWER       = 179;
    /** Key code constant: Set-top-box input key.
     * On TV remotes, switches the input mode on an external Set-top-box. */
    public static final int KEYCODE_STB_INPUT       = 180;
    /** Key code constant: A/V Receiver power key.
     * On TV remotes, toggles the power on an external A/V Receiver. */
    public static final int KEYCODE_AVR_POWER       = 181;
    /** Key code constant: A/V Receiver input key.
     * On TV remotes, switches the input mode on an external A/V Receiver. */
    public static final int KEYCODE_AVR_INPUT       = 182;
    /** Key code constant: Red "programmable" key.
     * On TV remotes, acts as a contextual/programmable key. */
    public static final int KEYCODE_PROG_RED        = 183;
    /** Key code constant: Green "programmable" key.
     * On TV remotes, actsas a contextual/programmable key. */
    public static final int KEYCODE_PROG_GREEN      = 184;
    /** Key code constant: Yellow "programmable" key.
     * On TV remotes, acts as a contextual/programmable key. */
    public static final int KEYCODE_PROG_YELLOW     = 185;
    /** Key code constant: Blue "programmable" key.
     * On TV remotes, acts as a contextual/programmable key. */
    public static final int KEYCODE_PROG_BLUE       = 186;
    /** Key code constant: App switch key.
     * Should bring up the application switcher dialog. */
    public static final int KEYCODE_APP_SWITCH      = 187;
    /** Key code constant: Generic Game Pad Button #1.*/
    public static final int KEYCODE_BUTTON_1        = 188;
    /** Key code constant: Generic Game Pad Button #2.*/
    public static final int KEYCODE_BUTTON_2        = 189;
    /** Key code constant: Generic Game Pad Button #3.*/
    public static final int KEYCODE_BUTTON_3        = 190;
    /** Key code constant: Generic Game Pad Button #4.*/
    public static final int KEYCODE_BUTTON_4        = 191;
    /** Key code constant: Generic Game Pad Button #5.*/
    public static final int KEYCODE_BUTTON_5        = 192;
    /** Key code constant: Generic Game Pad Button #6.*/
    public static final int KEYCODE_BUTTON_6        = 193;
    /** Key code constant: Generic Game Pad Button #7.*/
    public static final int KEYCODE_BUTTON_7        = 194;
    /** Key code constant: Generic Game Pad Button #8.*/
    public static final int KEYCODE_BUTTON_8        = 195;
    /** Key code constant: Generic Game Pad Button #9.*/
    public static final int KEYCODE_BUTTON_9        = 196;
    /** Key code constant: Generic Game Pad Button #10.*/
    public static final int KEYCODE_BUTTON_10       = 197;
    /** Key code constant: Generic Game Pad Button #11.*/
    public static final int KEYCODE_BUTTON_11       = 198;
    /** Key code constant: Generic Game Pad Button #12.*/
    public static final int KEYCODE_BUTTON_12       = 199;
    /** Key code constant: Generic Game Pad Button #13.*/
    public static final int KEYCODE_BUTTON_13       = 200;
    /** Key code constant: Generic Game Pad Button #14.*/
    public static final int KEYCODE_BUTTON_14       = 201;
    /** Key code constant: Generic Game Pad Button #15.*/
    public static final int KEYCODE_BUTTON_15       = 202;
    /** Key code constant: Generic Game Pad Button #16.*/
    public static final int KEYCODE_BUTTON_16       = 203;
    /** Key code constant: Language Switch key.
     * Toggles the current input language such as switching between English and Japanese on
     * a QWERTY keyboard.  On some devices, the same function may be performed by
     * pressing Shift+Spacebar. */
    public static final int KEYCODE_LANGUAGE_SWITCH = 204;
    /** Key code constant: Manner Mode key.
     * Toggles silent or vibrate mode on and off to make the device behave more politely
     * in certain settings such as on a crowded train.  On some devices, the key may only
     * operate when long-pressed. */
    public static final int KEYCODE_MANNER_MODE     = 205;
    /** Key code constant: 3D Mode key.
     * Toggles the display between 2D and 3D mode. */
    public static final int KEYCODE_3D_MODE         = 206;
    /** Key code constant: Contacts special function key.
     * Used to launch an address book application. */
    public static final int KEYCODE_CONTACTS        = 207;
    /** Key code constant: Calendar special function key.
     * Used to launch a calendar application. */
    public static final int KEYCODE_CALENDAR        = 208;
    /** Key code constant: Music special function key.
     * Used to launch a music player application. */
    public static final int KEYCODE_MUSIC           = 209;
    /** Key code constant: Calculator special function key.
     * Used to launch a calculator application. */
    public static final int KEYCODE_CALCULATOR      = 210;
    /** Key code constant: Japanese full-width / half-width key. */
    public static final int KEYCODE_ZENKAKU_HANKAKU = 211;
    /** Key code constant: Japanese alphanumeric key. */
    public static final int KEYCODE_EISU            = 212;
    /** Key code constant: Japanese non-conversion key. */
    public static final int KEYCODE_MUHENKAN        = 213;
    /** Key code constant: Japanese conversion key. */
    public static final int KEYCODE_HENKAN          = 214;
    /** Key code constant: Japanese katakana / hiragana key. */
    public static final int KEYCODE_KATAKANA_HIRAGANA = 215;
    /** Key code constant: Japanese Yen key. */
    public static final int KEYCODE_YEN             = 216;
    /** Key code constant: Japanese Ro key. */
    public static final int KEYCODE_RO              = 217;
    /** Key code constant: Japanese kana key. */
    public static final int KEYCODE_KANA            = 218;
    /** Key code constant: Assist key.
     * Launches the global assist activity.  Not delivered to applications. */
    public static final int KEYCODE_ASSIST          = 219;
    /** Key code constant: Brightness Down key.
     * Adjusts the screen brightness down. */
    public static final int KEYCODE_BRIGHTNESS_DOWN = 220;
    /** Key code constant: Brightness Up key.
     * Adjusts the screen brightness up. */
    public static final int KEYCODE_BRIGHTNESS_UP   = 221;
    /** Key code constant: Audio Track key.
     * Switches the audio tracks. */
    public static final int KEYCODE_MEDIA_AUDIO_TRACK = 222;
    /** Key code constant: Sleep key.
     * Puts the device to sleep.  Behaves somewhat like {@link #KEYCODE_POWER} but it
     * has no effect if the device is already asleep. */
    public static final int KEYCODE_SLEEP           = 223;
    /** Key code constant: Wakeup key.
     * Wakes up the device.  Behaves somewhat like {@link #KEYCODE_POWER} but it
     * has no effect if the device is already awake. */
    public static final int KEYCODE_WAKEUP          = 224;
    /** Key code constant: Pairing key.
     * Initiates peripheral pairing mode. Useful for pairing remote control
     * devices or game controllers, especially if no other input mode is
     * available. */
    public static final int KEYCODE_PAIRING         = 225;
    /** Key code constant: Media Top Menu key.
     * Goes to the top of media menu. */
    public static final int KEYCODE_MEDIA_TOP_MENU  = 226;
    /** Key code constant: '11' key. */
    public static final int KEYCODE_11              = 227;
    /** Key code constant: '12' key. */
    public static final int KEYCODE_12              = 228;
    /** Key code constant: Last Channel key.
     * Goes to the last viewed channel. */
    public static final int KEYCODE_LAST_CHANNEL    = 229;
    /** Key code constant: TV data service key.
     * Displays data services like weather, sports. */
    public static final int KEYCODE_TV_DATA_SERVICE = 230;
    /** Key code constant: Voice Assist key.
     * Launches the global voice assist activity. Not delivered to applications. */
    public static final int KEYCODE_VOICE_ASSIST = 231;
    /** Key code constant: Radio key.
     * Toggles TV service / Radio service. */
    public static final int KEYCODE_TV_RADIO_SERVICE = 232;
    /** Key code constant: Teletext key.
     * Displays Teletext service. */
    public static final int KEYCODE_TV_TELETEXT = 233;
    /** Key code constant: Number entry key.
     * Initiates to enter multi-digit channel nubmber when each digit key is assigned
     * for selecting separate channel. Corresponds to Number Entry Mode (0x1D) of CEC
     * User Control Code. */
    public static final int KEYCODE_TV_NUMBER_ENTRY = 234;
    /** Key code constant: Analog Terrestrial key.
     * Switches to analog terrestrial broadcast service. */
    public static final int KEYCODE_TV_TERRESTRIAL_ANALOG = 235;
    /** Key code constant: Digital Terrestrial key.
     * Switches to digital terrestrial broadcast service. */
    public static final int KEYCODE_TV_TERRESTRIAL_DIGITAL = 236;
    /** Key code constant: Satellite key.
     * Switches to digital satellite broadcast service. */
    public static final int KEYCODE_TV_SATELLITE = 237;
    /** Key code constant: BS key.
     * Switches to BS digital satellite broadcasting service available in Japan. */
    public static final int KEYCODE_TV_SATELLITE_BS = 238;
    /** Key code constant: CS key.
     * Switches to CS digital satellite broadcasting service available in Japan. */
    public static final int KEYCODE_TV_SATELLITE_CS = 239;
    /** Key code constant: BS/CS key.
     * Toggles between BS and CS digital satellite services. */
    public static final int KEYCODE_TV_SATELLITE_SERVICE = 240;
    /** Key code constant: Toggle Network key.
     * Toggles selecting broacast services. */
    public static final int KEYCODE_TV_NETWORK = 241;
    /** Key code constant: Antenna/Cable key.
     * Toggles broadcast input source between antenna and cable. */
    public static final int KEYCODE_TV_ANTENNA_CABLE = 242;
    /** Key code constant: HDMI #1 key.
     * Switches to HDMI input #1. */
    public static final int KEYCODE_TV_INPUT_HDMI_1 = 243;
    /** Key code constant: HDMI #2 key.
     * Switches to HDMI input #2. */
    public static final int KEYCODE_TV_INPUT_HDMI_2 = 244;
    /** Key code constant: HDMI #3 key.
     * Switches to HDMI input #3. */
    public static final int KEYCODE_TV_INPUT_HDMI_3 = 245;
    /** Key code constant: HDMI #4 key.
     * Switches to HDMI input #4. */
    public static final int KEYCODE_TV_INPUT_HDMI_4 = 246;
    /** Key code constant: Composite #1 key.
     * Switches to composite video input #1. */
    public static final int KEYCODE_TV_INPUT_COMPOSITE_1 = 247;
    /** Key code constant: Composite #2 key.
     * Switches to composite video input #2. */
    public static final int KEYCODE_TV_INPUT_COMPOSITE_2 = 248;
    /** Key code constant: Component #1 key.
     * Switches to component video input #1. */
    public static final int KEYCODE_TV_INPUT_COMPONENT_1 = 249;
    /** Key code constant: Component #2 key.
     * Switches to component video input #2. */
    public static final int KEYCODE_TV_INPUT_COMPONENT_2 = 250;
    /** Key code constant: VGA #1 key.
     * Switches to VGA (analog RGB) input #1. */
    public static final int KEYCODE_TV_INPUT_VGA_1 = 251;
    /** Key code constant: Audio description key.
     * Toggles audio description off / on. */
    public static final int KEYCODE_TV_AUDIO_DESCRIPTION = 252;
    /** Key code constant: Audio description mixing volume up key.
     * Louden audio description volume as compared with normal audio volume. */
    public static final int KEYCODE_TV_AUDIO_DESCRIPTION_MIX_UP = 253;
    /** Key code constant: Audio description mixing volume down key.
     * Lessen audio description volume as compared with normal audio volume. */
    public static final int KEYCODE_TV_AUDIO_DESCRIPTION_MIX_DOWN = 254;
    /** Key code constant: Zoom mode key.
     * Changes Zoom mode (Normal, Full, Zoom, Wide-zoom, etc.) */
    public static final int KEYCODE_TV_ZOOM_MODE = 255;
    /** Key code constant: Contents menu key.
     * Goes to the title list. Corresponds to Contents Menu (0x0B) of CEC User Control
     * Code */
    public static final int KEYCODE_TV_CONTENTS_MENU = 256;
    /** Key code constant: Media context menu key.
     * Goes to the context menu of media contents. Corresponds to Media Context-sensitive
     * Menu (0x11) of CEC User Control Code. */
    public static final int KEYCODE_TV_MEDIA_CONTEXT_MENU = 257;
    /** Key code constant: Timer programming key.
     * Goes to the timer recording menu. Corresponds to Timer Programming (0x54) of
     * CEC User Control Code. */
    public static final int KEYCODE_TV_TIMER_PROGRAMMING = 258;
    /** Key code constant: Help key. */
    public static final int KEYCODE_HELP = 259;
    /** Key code constant: Navigate to previous key.
     * Goes backward by one item in an ordered collection of items. */
    public static final int KEYCODE_NAVIGATE_PREVIOUS = 260;
    /** Key code constant: Navigate to next key.
     * Advances to the next item in an ordered collection of items. */
    public static final int KEYCODE_NAVIGATE_NEXT   = 261;
    /** Key code constant: Navigate in key.
     * Activates the item that currently has focus or expands to the next level of a navigation
     * hierarchy. */
    public static final int KEYCODE_NAVIGATE_IN     = 262;
    /** Key code constant: Navigate out key.
     * Backs out one level of a navigation hierarchy or collapses the item that currently has
     * focus. */
    public static final int KEYCODE_NAVIGATE_OUT    = 263;
    /** Key code constant: Skip forward media key. */
    public static final int KEYCODE_MEDIA_SKIP_FORWARD = 272;
    /** Key code constant: Skip backward media key. */
    public static final int KEYCODE_MEDIA_SKIP_BACKWARD = 273;
    /** Key code constant: Step forward media key.
     * Steps media forward, one frame at a time. */
    public static final int KEYCODE_MEDIA_STEP_FORWARD = 274;
    /** Key code constant: Step backward media key.
     * Steps media backward, one frame at a time. */
    public static final int KEYCODE_MEDIA_STEP_BACKWARD = 275;


keycode    含义
3    HOME 键
4    返回键
5    打开拨号应用
6    挂断电话
24    增加音量
25    降低音量
26    电源键
27    拍照（需要在相机应用里）
64    打开浏览器
82    菜单键
85    播放/暂停
86    停止播放
87    播放下一首
88    播放上一首
122    移动光标到行首或列表顶部
123    移动光标到行末或列表底部
126    恢复播放
127    暂停播放
164    静音
176    打开系统设置
187    切换应用
207    打开联系人
208    打开日历
209    打开音乐
210    打开计算器
220    降低屏幕亮度
221    提高屏幕亮度
223    系统休眠
224    点亮屏幕
231    打开语音助手
276    如果没有 wakelock 则让系统休眠



"""
KEYCODE_UNKNOWN = 0  # 未知按键
KEYCODE_SOFT_LEFT = 1  # 左下角显示选择软件定义功能的功能键
KEYCODE_SOFT_RIGHT = 2  # 右下角显示选择软件定义功能的功能键
KEYCODE_HOME = 3  # HOME 按键
KEYCODE_BACK = 4  # 键码常量:返回键
KEYCODE_CALL = 5  # 打开拨号应用
KEYCODE_ENDCALL = 6  # 挂断电话

KEYCODE_0 = 7  # 按键 0
KEYCODE_1 = 8  # 按键 1
KEYCODE_2 = 9  # 按键 2
KEYCODE_3 = 10  # 按键 3
KEYCODE_4 = 11  # 按键 4
KEYCODE_5 = 12  # 按键 5
KEYCODE_6 = 13  # 按键 6
KEYCODE_7 = 14  # 按键 7
KEYCODE_8 = 15  # 按键 8
KEYCODE_9 = 16  # 按键 9
KEYCODE_STAR = 17  # 按键 * * * * * * * * *
KEYCODE_POUND = 18  # 按键 # # # # # # # # #
KEYCODE_DPAD_UP = 19  # 方向向上键
KEYCODE_DPAD_DOWN = 20  # 方向向下键
KEYCODE_DPAD_LEFT = 21  # 方向键左键  也可以由轨迹球运动合成
KEYCODE_DPAD_RIGHT = 22  # 方向键右键  也可以由轨迹球运动合成
KEYCODE_DPAD_CENTER = 23  # 方向Pad中心键  也可以由轨迹球运动合成

KEYCODE_VOLUME_UP = 24  # 音量上升键
KEYCODE_VOLUME_DOWN = 25  # 音量下升键
KEYCODE_POWER = 26  # 电源键
KEYCODE_CAMERA = 27  # 拍照（需要在相机应用里）
KEYCODE_CLEAR = 28  # 清除键

KEYCODE_A = 29  # 按键 'A'键
KEYCODE_B = 30  # 按键 'B'键
KEYCODE_C = 31  # 按键 'C'键
KEYCODE_D = 32  # 按键 'D'键
KEYCODE_E = 33  # 按键 'E'键
KEYCODE_F = 34  # 按键 'F'键
KEYCODE_G = 35  # 按键 'G'键
KEYCODE_H = 36  # 按键 'H'键
KEYCODE_I = 37  # 按键 'I'键
KEYCODE_J = 38  # 按键 'J'键
KEYCODE_K = 39  # 按键 'K'键
KEYCODE_L = 40  # 按键 'L'键
KEYCODE_M = 41  # 按键 'M'键
KEYCODE_N = 42  # 按键 'N'键
KEYCODE_O = 43  # 按键 'O'键
KEYCODE_P = 44  # 按键 'P'键
KEYCODE_Q = 45  # 按键 'Q'键
KEYCODE_R = 46  # 按键 'R'键
KEYCODE_S = 47  # 按键 'S'键
KEYCODE_T = 48  # 按键 'T'键
KEYCODE_U = 49  # 按键 'U'键
KEYCODE_V = 50  # 按键 'V'键
KEYCODE_W = 51  # 按键 'W'键
KEYCODE_X = 52  # 按键 'X'键
KEYCODE_Y = 53  # 按键 'Y'键
KEYCODE_Z = 54  # 按键 'Z'键

KEYCODE_COMMA = 55  # 按键 ',' 键
KEYCODE_PERIOD = 56  # 按键 '.' 键
KEYCODE_ALT_LEFT = 57  # 左Alt修改键
KEYCODE_ALT_RIGHT = 58  # 右Alt修改键
KEYCODE_SHIFT_LEFT = 59  # 左Shift修改键
KEYCODE_SHIFT_RIGHT = 60  # 右Shift修改键
KEYCODE_TAB = 61  # 按键 Tab
KEYCODE_SPACE = 62  # 按键 Space key
KEYCODE_SYM = 63  # 符号修改键。 *用于输入替代符号
KEYCODE_EXPLORER = 64  # 浏览器的特殊功能键 启动浏览器
KEYCODE_ENVELOPE = 65  # 信封特殊功能键。 *用于启动邮件应用程序
KEYCODE_ENTER = 66  # 回车 输入键
KEYCODE_DEL = 67  # 退格键。 *删除插入点之前的字符
KEYCODE_GRAVE = 68  # (反勾)键

KEYCODE_MINUS = 69  # 按键 '-'键
KEYCODE_EQUALS = 70  # 按键 '='键
KEYCODE_LEFT_BRACKET = 71  # 按键 '['键
KEYCODE_RIGHT_BRACKET = 72  # 按键 ']'键
KEYCODE_BACKSLASH = 73  # 按键 '\'键
KEYCODE_SEMICOLON = 74  # 按键 ';'键
KEYCODE_APOSTROPHE = 75  # 按键 '''键
KEYCODE_SLASH = 76  # 按键 '/'键
KEYCODE_AT = 77  # 按键 '@'键









