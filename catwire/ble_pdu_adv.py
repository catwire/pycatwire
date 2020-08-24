# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class BlePduAdv(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.ensure_fixed_contents(b"\xD6\xBE\x89\x8E")
        self.header = self._root.PduHeader(self._io, self, self._root)
        self.adv_a = self._io.read_bytes(6)
        self.adv_data = [None] * (3)
        for i in range(3):
            self.adv_data[i] = self._root.AdStructure(self._io, self, self._root)

        self.crc = self._io.read_bytes(3)

    class AdStructure(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.adv_size = self._io.read_u1()
            self.ad_type = self._io.read_u1()
            _on = self.ad_type
            if _on == 1:
                self._raw_ad_data = self._io.read_bytes((self.adv_size - 1))
                io = KaitaiStream(BytesIO(self._raw_ad_data))
                self.ad_data = self._root.AdType0x01(io, self, self._root)
            elif _on == 10:
                self._raw_ad_data = self._io.read_bytes((self.adv_size - 1))
                io = KaitaiStream(BytesIO(self._raw_ad_data))
                self.ad_data = self._root.AdType0x0a(io, self, self._root)
            elif _on == 255:
                self._raw_ad_data = self._io.read_bytes((self.adv_size - 1))
                io = KaitaiStream(BytesIO(self._raw_ad_data))
                self.ad_data = self._root.AdType0xff(io, self, self._root)
            else:
                self._raw_ad_data = self._io.read_bytes((self.adv_size - 1))
                io = KaitaiStream(BytesIO(self._raw_ad_data))
                self.ad_data = self._root.AdTypeDefault(io, self, self._root)


    class PduHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pdu_type = self._io.read_bits_int(4)
            self.rfu = self._io.read_bits_int(1) != 0
            self.ch_sel = self._io.read_bits_int(1) != 0
            self.tx_add = self._io.read_bits_int(1) != 0
            self.rx_add = self._io.read_bits_int(1) != 0
            self._io.align_to_byte()
            self.pdu_length = self._io.read_bytes(1)


    class AdTypeDefault(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = []
            i = 0
            while not self._io.is_eof():
                self.data.append(self._io.read_bytes(1))
                i += 1



    class AdType0x01(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = self._io.read_bytes(1)


    class AdType0xff(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.company_id = self._io.read_bytes(2)
            self.data = []
            i = 0
            while not self._io.is_eof():
                self.data.append(self._io.read_bytes(1))
                i += 1



    class AdType0x0a(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = self._io.read_bytes(1)



