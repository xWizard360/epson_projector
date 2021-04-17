"""Const helpers of Epson projector module."""

HTTP_OK = 200

ACCEPT_ENCODING = "gzip, deflate"
ACCEPT_HEADER = "application/json, text/javascript"

ESCVPNET_HELLO_COMMAND = "ESC/VP.net\x10\x03\x00\x00\x00\x00"
ESCVPNETNAME = "ESC/VP.net"
ESCVPNAME = "ESC/VP"
ERROR = "ERR"

ESCVP_HELLO_COMMAND = "\r"
COLON = ":"
CR = "\r"
CR_COLON = CR+COLON
GET_CR = "?"+CR

POWER = "PWR"
CMODE = "CMODE"
SOURCE = "SOURCE"
VOLUME = "VOLUME"
MUTE = "MUTE"
VOL_UP = "VOL_UP"
VOL_DOWN = "VOL_DOWN"
PLAY = "PLAY"
PAUSE = "PAUSE"
FAST = "FAST"
BACK = "BACK"
TURN_ON = "PWR ON"
PWR_ON = "PWR ON"
TURN_OFF = "PWR OFF"
PWR_OFF = "PWR OFF"
ALL = "ALL"
IMGPROC_FINE = "IMGPROC_FINE"
IMGPROC_FAST = "IMGPROC_FAST"
MEMORY_1 = "MEMORY_1"
MEMORY_2 = "MEMORY_2"
MEMORY_3 = "MEMORY_3"
MEMORY_4 = "MEMORY_4"
MEMORY_5 = "MEMORY_5"
MEMORY_6 = "MEMORY_6"
MEMORY_7 = "MEMORY_7"
MEMORY_8 = "MEMORY_8"
MEMORY_9 = "MEMORY_9"
MEMORY_10 = "MEMORY_10"
BUSY = 2

EPSON_CODES = {
    'PWR': '01'
}

EPSON_KEY_COMMANDS = {
    "PWR ON": [('KEY', '3B')],
    "PWR OFF": [('KEY', '3B'), ('KEY', '3B')],
    "HDMILINK": [('jsoncallback', 'HDMILINK?')],
    "PWR": [('jsoncallback', 'PWR?')],
    "SOURCE": [('jsoncallback', 'SOURCE?')],
    "CMODE": [('jsoncallback', 'CMODE?')],
    "VOLUME": [('jsoncallback', 'VOL?')],
    "CMODE_AUTO": [('CMODE', '00')],
    "CMODE_CINEMA": [('CMODE', '15')],
    "CMODE_NATURAL": [('CMODE', '07')],
    "CMODE_BRIGHT": [('CMODE', '0C')],
    "CMODE_DYNAMIC": [('CMODE', '06')],
    "CMODE_3DDYNAMIC": [('CMODE', '18')],
    "CMODE_3DCINEMA": [('CMODE', '17')],
    "CMODE_3DTHX": [('CMODE', '19')],
    "CMODE_BWCINEMA": [('CMODE', '20')],
    "CMODE_ARGB": [('CMODE', '21')],
    "CMODE_DCINEMA": [('CMODE', '22')],
    "CMODE_THX": [('CMODE', '13')],
    "CMODE_GAME": [('CMODE', '0D')],
    "CMODE_STAGE": [('CMODE', '16')],
    "CMODE_AUTOCOLOR": [('CMODE', 'C1')],
    "CMODE_XV": [('CMODE', '0B')],
    "CMODE_THEATRE": [('CMODE', '05')],
    "CMODE_THEATREBLACK": [('CMODE', '09')],
    "CMODE_THEATREBLACK2": [('CMODE', '0A')],
    "VOL_UP": [('KEY', '56')],
    "VOL_DOWN": [('KEY', '57')],
    "MUTE": [('KEY', 'D8')],
    "HDMI1": [('KEY', '4D')],
    "HDMI2": [('KEY', '40')],
    "PC": [('KEY', '44')],
    "VIDEO": [('KEY', '46')],
    "USB": [('KEY', '85')],
    "LAN": [('KEY', '53')],
    "WFD": [('KEY', '56')],
    "PLAY": [('KEY', 'D1')],
    "PAUSE": [('KEY', 'D3')],
    "STOP": [('KEY', 'D2')],
    "BACK": [('KEY', 'D4')],
    "FAST": [('KEY', 'D5')],
    "IMGPROC_FINE": [('IMGPROC', '01')],
    "IMGPROC_FAST": [('IMGPROC', '02')],
    "MEMORY_1": [('POPMEM', '02 01')],
    "MEMORY_2": [('POPMEM', '02 02')],
    "MEMORY_3": [('POPMEM', '02 03')],
    "MEMORY_4": [('POPMEM', '02 04')],
    "MEMORY_5": [('POPMEM', '02 05')],
    "MEMORY_6": [('POPMEM', '02 06')],
    "MEMORY_7": [('POPMEM', '02 07')],
    "MEMORY_8": [('POPMEM', '02 08')],
    "MEMORY_9": [('POPMEM', '02 09')],
    "MEMORY_10": [('POPMEM', '02 0A')]
}

TIMEOUT_TIMES = {
    'PWR ON': 40,
    'PWR OFF': 10,
    'SOURCE': 5,
    'ALL': 3
}

DEFAULT_SOURCES = {
    'HDMI1': 'HDMI1',
    'HDMI2': 'HDMI2',
    'HDMI3': 'HDMI3',
    'LAN': 'LAN'
}

SOURCE_LIST = {
    '32': 'HDMI1',
    '33': 'HDMI2',
    '36': 'HDMI3',
    '52': 'LAN'
}

INV_SOURCES = {v: k for k, v in DEFAULT_SOURCES.items()}

CMODE_LIST = {
    '15': 'Cinema',
    '0C': 'Bright Cinema',
    '06': 'Dynamic',
    '0D': 'Game'
}

CMODE_LIST_SET = {
    'cinema': 'CMODE_CINEMA', 'Cinema': 'CMODE_CINEMA',
    'bright cinema': 'CMODE_BRIGHT', 'Bright Cinema': 'CMODE_BRIGHT',
    'dynamic': 'CMODE_DYNAMIC', 'Dynamic': 'CMODE_DYNAMIC',
    'game': 'CMODE_GAME', 'Game': 'CMODE_GAME'
}


STATE_UNAVAILABLE = 'unavailable' 