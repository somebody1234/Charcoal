# TODO: alphabe

RotateHalfRight = {
    "|": "/", "-": "\\", "/": "-", "\\": "|", "│": "╱", "─": "╲", "╱": "─",
    "╲": "│"
}

RotateHalfLeft = {
    "|": "\\", "-": "/", "/": "|", "\\": "-", "│": "╲", "─": "╱", "╱": "│",
    "╲": "─"
}

RotateThreeHalvesRight = {
    "|": "\\", "-": "/", "/": "|", "\\": "-", "│": "╲", "─": "╱", "╱": "│",
    "╲": "─"
}

RotateThreeHalvesLeft = {
    "|": "/", "-": "\\", "/": "-", "\\": "|", "│": "╱", "─": "╲", "╱": "─",
    "╲": "│"
}

RotateRight = {
    "-": "|", "|": "-", "\\": "/", "/": "\\", "╲": "╱", "╱": "╲",
    "─": "│", "│": "─", "━": "┃", "┃": "━", "╌": "╎", "╎": "╌",
    "╍": "╏", "╏": "╍", "┄": "┆", "┆": "┄", "┅": "┇", "┇": "┅",
    "┈": "┊", "┊": "┈", "┉": "┋", "┋": "┉", "═": "║", "║": "═",
    "┐": "┘", "┘": "└", "┌": "┐", "└": "┌", "┒": "┙", "┚": "┕",
    "┎": "┑", "┖": "┍", "┑": "┚", "┙": "┖", "┍": "┒", "┕": "┎",
    "┓": "┛", "┛": "┗", "┏": "┓", "┗": "┏", "├": "┬", "┬": "┤",
    "┤": "┴", "┴": "├", "┝": "┰", "┰": "┥", "┥": "┸", "┸": "┝",
    "┞": "┮", "┮": "┧", "┧": "┵", "┵": "┞", "┟": "┭", "┭": "┦",
    "┦": "┶", "┶": "┟", "┠": "┯", "┯": "┨", "┨": "┷", "┷": "┠",
    "┡": "┲", "┲": "┪", "┪": "┹", "┹": "┡", "┢": "┱", "┱": "┩",
    "┩": "┺", "┺": "┢", "┣": "┳", "┳": "┫", "┫": "┻", "┻": "┣",
    "┽": "╀", "╀": "┾", "┾": "╁", "╁": "┽", "┿": "╂", "╂": "┿",
    "╃": "╄", "╄": "╆", "╆": "╅", "╅": "╃", "╇": "╊", "╊": "╈",
    "╈": "╉", "╉": "╇", "╒": "╖", "╖": "╛", "╛": "╙", "╙": "╒",
    "╓": "╕", "╕": "╜", "╜": "╘", "╘": "╓", "╔": "╗", "╗": "╝",
    "╝": "╚", "╚": "╔", "╞": "╥", "╥": "╡", "╡": "╨", "╨": "╞",
    "╟": "╤", "╤": "╢", "╢": "╧", "╧": "╟", "╠": "╦", "╦": "╣",
    "╣": "╩", "╩": "╠", "╪": "╫", "╫": "╪", "╭": "╮", "╮": "╯",
    "╯": "╰", "╰": "╭", "╴": "╵", "╵": "╶", "╶": "╷", "╷": "╴",
    "╸": "╹", "╹": "╺", "╺": "╻", "╻": "╸", "╼": "╽", "╽": "╾",
    "╾": "╿", "╿": "╼"
}

RotateLeft = {
    "-": "|", "|": "-", "\\": "/", "/": "\\", "╲": "╱", "╱": "╲",
    "─": "│", "│": "─", "━": "┃", "┃": "━", "╌": "╎", "╎": "╌",
    "╍": "╏", "╏": "╍", "┄": "┆", "┆": "┄", "┅": "┇", "┇": "┅",
    "┈": "┊", "┊": "┈", "┉": "┋", "┋": "┉", "═": "║", "║": "═",
    "┐": "┌", "┘": "┐", "┌": "└", "└": "┘", "┒": "┍", "┚": "┑",
    "┎": "┕", "┖": "┙", "┑": "┎", "┙": "┒", "┍": "┖", "┕": "┚",
    "┓": "┏", "┛": "┓", "┏": "┗", "┗": "┛", "├": "┴", "┬": "├",
    "┤": "┬", "┴": "┤", "┝": "┸", "┰": "┝", "┥": "┰", "┸": "┥",
    "┞": "┵", "┮": "┞", "┧": "┮", "┵": "┧", "┟": "┶", "┭": "┟",
    "┦": "┭", "┶": "┦", "┠": "┷", "┯": "┠", "┨": "┯", "┷": "┨",
    "┡": "┹", "┲": "┡", "┪": "┲", "┹": "┪", "┢": "┺", "┱": "┢",
    "┩": "┱", "┺": "┩", "┣": "┻", "┳": "┣", "┫": "┳", "┻": "┫",
    "┽": "╁", "╀": "┽", "┾": "╀", "╁": "┾", "┿": "╂", "╂": "┿",
    "╃": "╅", "╄": "╃", "╆": "╄", "╅": "╆", "╇": "╉", "╊": "╇",
    "╈": "╊", "╉": "╈", "╒": "╙", "╖": "╒", "╛": "╖", "╙": "╛",
    "╓": "╘", "╕": "╓", "╜": "╕", "╘": "╜", "╔": "╚", "╗": "╔",
    "╝": "╗", "╚": "╝", "╞": "╨", "╥": "╞", "╡": "╥", "╨": "╡",
    "╟": "╧", "╤": "╟", "╢": "╤", "╧": "╢", "╠": "╩", "╦": "╠",
    "╣": "╦", "╩": "╣", "╪": "╫", "╫": "╪", "╭": "╰", "╮": "╭",
    "╯": "╮", "╰": "╯", "╴": "╷", "╵": "╴", "╶": "╵", "╷": "╶",
    "╸": "╻", "╹": "╸", "╺": "╹", "╻": "╺", "╼": "╿", "╽": "╼",
    "╾": "╽", "╿": "╾"
}

RotateDown = {
    "b": "q", "d": "p", "p": "d", "q": "b", "6": "9", "9": "6",
    "{": "}", "}": "{", "[": "]", "]": "[", "<": ">", ">": "<",
    "(": ")", ")": "(", "┐": "└", "┘": "┌", "┌": "┘", "└": "┐",
    "┒": "┖", "┚": "┎", "┎": "┚", "┖": "┒", "┑": "┕", "┙": "┍",
    "┍": "┙", "┕": "┑", "┓": "┗", "┛": "┏", "┏": "┛", "┗": "┓",
    "├": "┤", "┬": "┴", "┤": "├", "┴": "┬", "┝": "┥", "┰": "┸",
    "┥": "┝", "┸": "┰", "┞": "┧", "┮": "┵", "┧": "┞", "┵": "┮",
    "┟": "┦", "┭": "┶", "┦": "┟", "┶": "┭", "┠": "┨", "┯": "┷",
    "┨": "┠", "┷": "┯", "┡": "┪", "┲": "┹", "┪": "┡", "┹": "┲",
    "┢": "┩", "┱": "┺", "┩": "┢", "┺": "┺", "┣": "┫", "┳": "┻",
    "┫": "┣", "┻": "┳", "┽": "┾", "╀": "╁", "┾": "┽", "╁": "╀",
    "╃": "╆", "╄": "╅", "╆": "╃", "╅": "╄", "╇": "╈", "╊": "╉",
    "╈": "╇", "╉": "╊", "╒": "╛", "╖": "╙", "╛": "╒", "╙": "╖",
    "╓": "╜", "╕": "╘", "╜": "╓", "╘": "╕", "╔": "╝", "╗": "╚",
    "╝": "╔", "╚": "╗", "╞": "╡", "╥": "╨", "╡": "╞", "╨": "╥",
    "╟": "╢", "╤": "╧", "╢": "╟", "╧": "╤", "╠": "╣", "╦": "╩",
    "╣": "╠", "╩": "╦", "╭": "╯", "╮": "╰", "╯": "╭", "╰": "╮",
    "╴": "╶", "╵": "╷", "╶": "╴", "╷": "╵", "╸": "╺", "╹": "╻",
    "╺": "╸", "╻": "╹", "╼": "╾", "╽": "╿", "╾": "╼", "╿": "╽",
    # TODO letters
    "n": "u", "u": "n", "⟓": "⟔", "⟔": "⟓",
    "⦍": "⦎", "⦎": "⦍", "⦏": "⦐", "⦐": "⦏",
    "〈": "〉", "〉": "〈", "⟨": "⟩", "⟩": "⟨", "⁅": "⁆", "⁆": "⁅",
    # "⸤": "⸥", "⸥": "⸤",
    "⟦": "⟧", "⟧": "⟦", "‹": "›", "›": "‹",
    "⌊": "⌉", "⌋": "⌈", "⌈": "⌋", "⌉": "⌊",
    # "⌜": "⌝", "⌝": "⌜",
    "⸢": "⸥", "⸥": "⸢", "⸤": "⸣", "⸣": "⸤",
    "⌜": "⌟", "⌟": "⌜", "⌞": "⌝", "⌝": "⌞",
    "⁽": "⁾", "⁾": "⁽", "₍": "₎", "₎": "₍",
    "⎸": "⎹", "⎹": "⎸",
    "⎛": "⎠", "⎠": "⎛", "⎝": "⎞", "⎞": "⎝",
    "⎡": "⎦", "⎦": "⎡", "⎣": "⎤", "⎤": "⎣",
    "⎧": "⎭", "⎭": "⎧", "⎩": "⎫", "⎫": "⎩",
    "⎬": "⎨", "⎨": "⎬", "⎱": "⎰", "⎰": "⎱",
    "⟅": "⟆", "⟆": "⟅", "⟬": "⟭", "⟭": "⟬", "⟮": "⟯", "⟯": "⟮",
    "⦃": "⦄", "⦄": "⦃", "⦅": "⦆", "⦆": "⦅", "⦇": "⦈", "⦈": "⦇",
    "⦉": "⦊", "⦊": "⦉", "⦋": "⦌", "⦌": "⦋", "⦑": "⦒", "⦒": "⦑",
    "｢": "｣", "｣": "｢", "⦓": "⦔", "⦔": "⦓", "⦕": "⦖", "⦖": "⦕",
    "⦗": "⦘", "⦘": "⦗", "⧘": "⧙", "⧙": "⧘", "⧚": "⧛", "⧛": "⧚",
    "⧼": "⧽", "⧽": "⧼", "❨": "❩", "❩": "❨", "❪": "❫", "❫": "❪",
    "❬": "❭", "❭": "❬", "❰": "❱", "❱": "❰", "❮": "❯", "❯": "❮",
    "❲": "❳", "❳": "❲", "❴": "❵", "❵": "❴", "﴿": "﴾", "﴾": "﴿",
    "᚛": "᚜", "᚜": "᚛", "⸝": "⸍", "⸍": "⸝", "⸌": "⸜", "⸜": "⸌",
    "『": "』", "』": "『", "⸦": "⸧", "⸧": "⸦", "⸨": "⸩", "⸩": "⸨",
    "〔": "〕", "〕": "〔", "〖": "〗", "〗": "〖", "〘": "〙", "〙": "〘",
    "〚": "〛", "〛": "〚", "《": "》", "》": "《", "【": "】", "】": "【",
    "（": "）", "）": "（", "［": "］", "］": "［", "＜": "＞", "＞": "＜",
    "｛": "｝", "｝": "｛", "｟": "｠", "｠": "｟"
}

HorizontalFlip = {
    "b": "d", "d": "b", "p": "q", "q": "p",
    "{": "}", "}": "{", "[": "]", "]": "[", "<": ">", ">": "<",
    "(": ")", ")": "(", "\\": "/", "/": "\\", "╲": "╱", "╱": "╲",
    "┐": "┌", "┘": "└", "┌": "┐", "└": "┘", "┒": "┎", "┚": "┖",
    "┎": "┒", "┖": "┚", "┑": "┍", "┙": "┕", "┍": "┑", "┕": "┙",
    "┓": "┏", "┛": "┗", "┏": "┓", "┗": "┛", "├": "┤", "┤": "├",
    "┝": "┥", "┥": "┝", "┞": "┦", "┮": "┭", "┧": "┟", "┵": "┶",
    "┟": "┧", "┭": "┮", "┦": "┞", "┶": "┵", "┠": "┨", "┨": "┠",
    "┡": "┩", "┲": "┱", "┪": "┢", "┹": "┺", "┢": "┪", "┱": "┲",
    "┩": "┡", "┺": "┹", "┣": "┫", "┫": "┣", "┽": "┾", "┾": "┽",
    "╃": "╄", "╄": "╃", "╆": "╅", "╅": "╆", "╊": "╉", "╉": "╊",
    "╒": "╕", "╖": "╓", "╛": "╘", "╙": "╜", "╓": "╖", "╕": "╒",
    "╜": "╙", "╘": "╛", "╔": "╗", "╗": "╔", "╝": "╚", "╚": "╝",
    "╞": "╡", "╡": "╞", "╟": "╢", "╢": "╟", "╠": "╣", "╣": "╠",
    "╭": "╮", "╮": "╭", "╯": "╰", "╰": "╯", "╸": "╺", "╺": "╸",
    "╼": "╾", "╾": "╼", "〈": "〉", "〉": "〈", "⟨": "⟩", "⟩": "⟨",
    "‹": "›", "›": "‹", "⁅": "⁆", "⁆": "⁅", "｢": "｣", "｣": "｢",
    "⟦": "⟧", "⟧": "⟦", "⌊": "⌋", "⌋": "⌊", "⌈": "⌉", "⌉": "⌈",
    "⸢": "⸣", "⸣": "⸢", "⸤": "⸥", "⸥": "⸤", "⌜": "⌝", "⌝": "⌜",
    "⌞": "⌟", "⌟": "⌞", "⁽": "⁾", "⁾": "⁽", "₍": "₎", "₎": "₍",
    "⎸": "⎹", "⎹": "⎸", "⎛": "⎞", "⎞": "⎛", "⎝": "⎠", "⎠": "⎝",
    "⎡": "⎤", "⎤": "⎡", "⎣": "⎦", "⎦": "⎣", "⎧": "⎫", "⎫": "⎧",
    "⎩": "⎭", "⎭": "⎩", "⎬": "⎨", "⎨": "⎬", "⎱": "⎰", "⎰": "⎱",
    "⟅": "⟆", "⟆": "⟅", "⟬": "⟭", "⟭": "⟬", "⟮": "⟯", "⟯": "⟮",
    "⦃": "⦄", "⦄": "⦃", "⦅": "⦆", "⦆": "⦅", "⦇": "⦈", "⦈": "⦇",
    "⦉": "⦊", "⦊": "⦉", "⦋": "⦌", "⦌": "⦋", "⦍": "⦐", "⦐": "⦍",
    "⦏": "⦎", "⦎": "⦏", "⦑": "⦒", "⦒": "⦑", "⦓": "⦔", "⦔": "⦓",
    "⦕": "⦖", "⦖": "⦕", "⦗": "⦘", "⦘": "⦗", "⧘": "⧙", "⧙": "⧘",
    "⧚": "⧛", "⧛": "⧚", "⧼": "⧽", "⧽": "⧼", "❨": "❩", "❩": "❨",
    "❪": "❫", "❫": "❪", "❬": "❭", "❭": "❬", "❰": "❱", "❱": "❰",
    "❮": "❯", "❯": "❮", "❲": "❳", "❳": "❲", "❴": "❵", "❵": "❴",
    "﴿": "﴾", "﴾": "﴿", "᚛": "᚜", "᚜": "᚛", "⸜": "⸝", "⸝": "⸜",
    "⸌": "⸍", "⸍": "⸌", "⸂": "⸃", "⸃": "⸂", "⸄": "⸅", "⸅": "⸄",
    "⸉": "⸊", "⸊": "⸉", "༺": "༻", "༻": "༺", "༼": "༽", "༽": "༼",
    "⸦": "⸧", "⸧": "⸦", "⸨": "⸩", "⸩": "⸨", "〔": "〕", "〕": "〔",
    "〖": "〗", "〗": "〖", "〘": "〙", "〙": "〘", "〚": "〛", "〛": "〚",
    "《": "》", "》": "《", "【": "】", "】": "【", "（": "）", "）": "（",
    "［": "］", "］": "［", "＜": "＞", "＞": "＜", "｛": "｝", "｝": "｛",
    "｟": "｠", "｠": "｟"
}

VerticalFlip = {
    "b": "p", "d": "q", "p": "b", "q": "d",
    "\\": "/", "/": "\\", "╲": "╱", "╱": "╲",
    "┐": "┘", "┘": "┐", "┌": "└", "└": "┌",
    "┒": "┚", "┚": "┒", "┎": "┖", "┖": "┎", "┑": "┙", "┙": "┑",
    "┍": "┕", "┕": "┍",
    "┓": "┛", "┛": "┓", "┏": "┗", "┗": "┏",
    "┬": "┴", "┴": "┬", "┰": "┸", "┸": "┰",
    "┞": "┟", "┮": "┶", "┧": "┦", "┵": "┭", "┟": "┞", "┭": "┵",
    "┦": "┧", "┶": "┮",
    "┯": "┷", "┷": "┯",
    "┡": "┢", "┲": "┺", "┪": "┩", "┹": "┱", "┢": "┡", "┱": "┹",
    "┩": "┪", "┺": "┲",
    "┳": "┻", "┻": "┳", "╀": "╁", "╁": "╀",
    "╃": "╅", "╄": "╆", "╆": "╄", "╅": "╃",
    "╇": "╈", "╈": "╇",
    "╒": "╘", "╖": "╜", "╛": "╕", "╙": "╓", "╓": "╙", "╕": "╛",
    "╜": "╖", "╘": "╒",
    "╔": "╚", "╗": "╝", "╝": "╗", "╚": "╔",
    "╥": "╨", "╨": "╥", "╤": "╧", "╧": "╤", "╦": "╩", "╩": "╦",
    "╭": "╰", "╮": "╯", "╯": "╮", "╰": "╭",
    "╹": "╻", "╻": "╹", "╽": "╿", "╿": "╽",
    "︿": "﹀", "﹀": "︿", "︽": "︾", "︾": "︽", "⎛": "⎝", "⎝": "⎛",
    "⎞": "⎠", "⎠": "⎞", "⎡": "⎣", "⎣": "⎡", "⎤": "⎦", "⎦": "⎤",
    "⎧": "⎩", "⎩": "⎧", "⎫": "⎭", "⎭": "⎫", "⎱": "⎰", "⎰": "⎱",
    "⎴": "⎵", "⎵": "⎴", "⏜": "⏝", "⏝": "⏜", "⏞": "⏟", "⏟": "⏞",
    "⏠": "⏡", "⏡": "⏠", "⦍": "⦏", "⦏": "⦍", "⦐": "⦎", "⦎": "⦐",
    "⸜": "⸍", "⸍": "⸜", "⸝": "⸌", "⸌": "⸝", "⸉": "⸊", "⸊": "⸉",
}

NWSEFlip = {
    "-": "|", "|": "-",
    "─": "│", "│": "─", "━": "┃", "┃": "━", "╌": "╎", "╎": "╌",
    "╍": "╏", "╏": "╍", "┄": "┆", "┆": "┄", "┅": "┇", "┇": "┅",
    "┈": "┊", "┊": "┈", "┉": "┋", "┋": "┉", "═": "║", "║": "═",
    "┐": "└", "└": "┐",
    "┒": "┕", "┚": "┙", "┎": "┍", "┖": "┑", "┑": "┖", "┙": "┚",
    "┍": "┎", "┕": "┒",
    "┓": "┗", "┗": "┓", "├": "┬", "┬": "├", "┤": "┴", "┴": "┤",
    "┝": "┸", "┰": "┥", "┥": "┰", "┸": "┝",
    "┞": "┭", "┮": "┟", "┧": "┶", "┵": "┦", "┟": "┮", "┭": "┞",
    "┦": "┵", "┶": "┧",
    "┠": "┯", "┯": "┠", "┨": "┷", "┷": "┨",
    "┡": "┱", "┲": "┢", "┪": "┺", "┹": "┩", "┢": "┲", "┱": "┡",
    "┩": "┹", "┺": "┪",
    "┣": "┳", "┳": "┣", "┫": "┻", "┻": "┫",
    "┽": "╀", "╀": "┽", "┾": "╁", "╁": "┾",
    "┿": "╂", "╂": "┿", "╄": "╅", "╅": "╄",
    "╇": "╉", "╊": "╈", "╈": "╊", "╉": "╇",
    "╒": "╓", "╖": "╘", "╛": "╜", "╙": "╕", "╓": "╒", "╕": "╙",
    "╜": "╛", "╘": "╖",
    "╗": "╚", "╚": "╗", "╞": "╥", "╥": "╞", "╡": "╨", "╨": "╡",
    "╟": "╤", "╤": "╟", "╢": "╧", "╧": "╢",
    "╠": "╦", "╦": "╠", "╣": "╩", "╩": "╣", "╪": "╫", "╫": "╪",
    "╮": "╰", "╰": "╮", "╸": "╹", "╹": "╸", "╺": "╻", "╻": "╺",
    "╼": "╽", "╽": "╼", "╾": "╿", "╿": "╾"
}

NESWFlip = {
    "-": "|", "|": "-",
    "─": "│", "│": "─", "━": "┃", "┃": "━", "╌": "╎", "╎": "╌",
    "╍": "╏", "╏": "╍", "┄": "┆", "┆": "┄", "┅": "┇", "┇": "┅",
    "┈": "┊", "┊": "┈", "┉": "┋", "┋": "┉", "═": "║", "║": "═",
    "┘": "┌", "┌": "┘", "┒": "┑", "┚": "┍", "┎": "┍", "┖": "┕",
    "┑": "┒", "┙": "┎", "┍": "┚", "┕": "┖", "┛": "┏", "┏": "┛",
    "├": "┴", "┬": "┤", "┤": "┬", "┴": "├", "┝": "┰", "┰": "┝",
    "┥": "┸", "┸": "┥", "┞": "┶", "┮": "┦", "┧": "┭", "┵": "┟",
    "┟": "┵", "┭": "┧", "┦": "┮", "┶": "┞", "┠": "┷", "┯": "┨",
    "┨": "┯", "┷": "┠", "┡": "┺", "┲": "┩", "┪": "┱", "┹": "┢",
    "┢": "┹", "┱": "┪", "┩": "┲", "┺": "┡", "┣": "┻", "┳": "┫",
    "┫": "┳", "┻": "┣", "┽": "╁", "╀": "┾", "┾": "╀", "╁": "┽",
    "┿": "╂", "╂": "┿", "╃": "╆", "╆": "╃", "╇": "╊", "╊": "╇",
    "╈": "╉", "╉": "╈", "╒": "╜", "╖": "╕", "╛": "╓", "╙": "╘",
    "╓": "╛", "╕": "╖", "╜": "╒", "╘": "╙", "╔": "╝", "╝": "╔",
    "╞": "╨", "╥": "╡", "╡": "╥", "╨": "╞", "╟": "╧", "╤": "╢",
    "╢": "╤", "╧": "╟", "╠": "╩", "╦": "╣", "╣": "╦", "╩": "╠",
    "╪": "╫", "╫": "╪", "╭": "╯", "╯": "╭", "╸": "╻", "╹": "╺",
    "╺": "╹", "╻": "╸", "╼": "╿", "╽": "╾", "╾": "╽", "╿": "╼"
}
