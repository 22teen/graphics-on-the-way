import  struct
try:
    bytes('', 'ascii')
    def strtobytes(x):
        return bytes(x, 'iso8859-1')
    def bytestostr(x):
        return str(x, 'iso8859-1')
except (NameError, TypeError):
    # We get NameError when bytes() does not exist (most Python
    # 2.x versions), and TypeError when bytes() exists but is on
    # Python 2.x (when it is an alias for str() and takes at most
    # one argument).
    strtobytes = str
    bytestostr = str

global  _t
_t = [0, 0x1db71064, 0x3b6e20c8, 0x26d930ac, 0x76dc4190, 0x6b6b51f4, 0x4db26158, 0x5005713c,0xedb88320, 0xf00f9344, 0xd6d6a3e8, 0xcb61b38c, 0x9b64c2b0, 0x86d3d2d4, 0xa00ae278, 0xbdbdf21c ]

class svpng :
    def __init__(self, f, w, h, alpha = 0):
        self.a = 1
        self.b = 0
        self.c = None
        self.p = w * (3 if alpha == 0 else 4) + 1
        self.f = f
        self.w = w
        self.h = h
        self.alpha = alpha

    def svpng_put(self, u):
        self.f.write(struct.pack("B", u))

    def svpng_u8a(self, ua):
        self.f.write(strtobytes(ua))

    def svpng_u32(self, u):
        self.svpng_put(u>>24)
        self.svpng_put((u >> 16) & 255)
        self.svpng_put((u >> 8) & 255)
        self.svpng_put(u & 255)

    def svpng_u8c(self,u):
        self.svpng_put(u)
        self.c ^= u
        self.c = (self.c >> 4)^_t[self.c & 15]
        self.c = (self.c >> 4)^_t[self.c & 15]

    def svpng_u8ac(self, ua):
        byteArray = strtobytes(ua)
        for u in byteArray:
            self.svpng_u8c(u)

    def svpng_u16lc(self, u):
        self.svpng_u8c(u & 255)
        self.svpng_u8c((u >> 8) & 255)

    def svpng_u32c(self, u):
        self.svpng_u8c(u >> 24)
        self.svpng_u8c((u >> 16) & 255)
        self.svpng_u8c( (u >>8) & 255)
        self.svpng_u8c(u & 255)

    def svpng_u8adler(self, u):
        self.svpng_u8c(u)
        self.a = (self.a + u) % 65521
        self.b = (self.b + self.a) %65521

    def svpng_begin(self, s, l):
        self.svpng_u32(l)
        self.c =~0
        self.svpng_u8ac(s)

    def svpng_end(self):
        self.svpng_u32(~self.c)

    def save(self, data):
        self.svpng_u8a("\x89PNG\r\n\32\n")
        self.svpng_begin("IHDR", 13)
        self.svpng_u32c(self.w)
        self.svpng_u32c(self.h)
        self.svpng_u8c(8)
        self.svpng_u8c(2 if self.alpha == 0 else 4)
        self.svpng_u8ac("\0\0\0")
        self.svpng_end()
        self.svpng_begin("IDAT", 2 + self.h * (5 + self.p) +4)
        self.svpng_u8ac("\x78\1")
        for y in range(self.h):
            self.svpng_u8c(int(y == self.h - 1))
            self.svpng_u16lc(self.p)
            self.svpng_u16lc(~self.p)
            self.svpng_u8adler(0)
            for x in range(self.p - 1):
                self.svpng_u8adler(data[y* (self.p-1) + x])
        self.svpng_u32c(self.b << 16 | self.a)
        self.svpng_end()
        self.svpng_begin("IEND", 0)
        self.svpng_end()