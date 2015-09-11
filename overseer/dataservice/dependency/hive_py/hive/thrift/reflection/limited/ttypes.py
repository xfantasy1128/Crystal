#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None


class TTypeTag:
    T_VOID = 1
    T_BOOL = 2
    T_BYTE = 3
    T_I16 = 6
    T_I32 = 8
    T_I64 = 10
    T_DOUBLE = 4
    T_STRING = 11
    T_STRUCT = 12
    T_MAP = 13
    T_SET = 14
    T_LIST = 15
    T_ENUM = 101
    T_NOT_REFLECTED = 102


class SimpleType:

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'ttype', None, None, ),  # 1
        (2, TType.STRING, 'name', None, None, ),  # 2
    )

    def __init__(self, d=None):
        self.ttype = None
        self.name = None
        if isinstance(d, dict):
            if 'ttype' in d:
                self.ttype = d['ttype']
            if 'name' in d:
                self.name = d['name']

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.ttype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SimpleType')
        if self.ttype != None:
            oprot.writeFieldBegin('ttype', TType.I32, 1)
            oprot.writeI32(self.ttype)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ContainerType:

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'ttype', None, None, ),  # 1
        (2, TType.STRUCT, 'subtype1', (SimpleType, SimpleType.thrift_spec), None, ),  # 2
        (3, TType.STRUCT, 'subtype2', (SimpleType, SimpleType.thrift_spec), None, ),  # 3
    )

    def __init__(self, d=None):
        self.ttype = None
        self.subtype1 = None
        self.subtype2 = None
        if isinstance(d, dict):
            if 'ttype' in d:
                self.ttype = d['ttype']
            if 'subtype1' in d:
                self.subtype1 = d['subtype1']
            if 'subtype2' in d:
                self.subtype2 = d['subtype2']

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.ttype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.subtype1 = SimpleType()
                    self.subtype1.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.subtype2 = SimpleType()
                    self.subtype2.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ContainerType')
        if self.ttype != None:
            oprot.writeFieldBegin('ttype', TType.I32, 1)
            oprot.writeI32(self.ttype)
            oprot.writeFieldEnd()
        if self.subtype1 != None:
            oprot.writeFieldBegin('subtype1', TType.STRUCT, 2)
            self.subtype1.write(oprot)
            oprot.writeFieldEnd()
        if self.subtype2 != None:
            oprot.writeFieldBegin('subtype2', TType.STRUCT, 3)
            self.subtype2.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ThriftType:

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'is_container', None, None, ),  # 1
        (2, TType.STRUCT, 'simple_type', (SimpleType, SimpleType.thrift_spec), None, ),  # 2
        (3, TType.STRUCT, 'container_type', (ContainerType, ContainerType.thrift_spec), None, ),  # 3
    )

    def __init__(self, d=None):
        self.is_container = None
        self.simple_type = None
        self.container_type = None
        if isinstance(d, dict):
            if 'is_container' in d:
                self.is_container = d['is_container']
            if 'simple_type' in d:
                self.simple_type = d['simple_type']
            if 'container_type' in d:
                self.container_type = d['container_type']

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.is_container = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.simple_type = SimpleType()
                    self.simple_type.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.container_type = ContainerType()
                    self.container_type.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ThriftType')
        if self.is_container != None:
            oprot.writeFieldBegin('is_container', TType.BOOL, 1)
            oprot.writeBool(self.is_container)
            oprot.writeFieldEnd()
        if self.simple_type != None:
            oprot.writeFieldBegin('simple_type', TType.STRUCT, 2)
            self.simple_type.write(oprot)
            oprot.writeFieldEnd()
        if self.container_type != None:
            oprot.writeFieldBegin('container_type', TType.STRUCT, 3)
            self.container_type.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Argument:

    thrift_spec = (
        None,  # 0
        (1, TType.I16, 'key', None, None, ),  # 1
        (2, TType.STRING, 'name', None, None, ),  # 2
        (3, TType.STRUCT, 'type', (ThriftType, ThriftType.thrift_spec), None, ),  # 3
    )

    def __init__(self, d=None):
        self.key = None
        self.name = None
        self.type = None
        if isinstance(d, dict):
            if 'key' in d:
                self.key = d['key']
            if 'name' in d:
                self.name = d['name']
            if 'type' in d:
                self.type = d['type']

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I16:
                    self.key = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.type = ThriftType()
                    self.type.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Argument')
        if self.key != None:
            oprot.writeFieldBegin('key', TType.I16, 1)
            oprot.writeI16(self.key)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.STRUCT, 3)
            self.type.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Method:

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'name', None, None, ),  # 1
        (2, TType.STRUCT, 'return_type', (ThriftType, ThriftType.thrift_spec), None, ),  # 2
        (3, TType.LIST, 'arguments', (TType.STRUCT, (Argument, Argument.thrift_spec)), None, ),  # 3
    )

    def __init__(self, d=None):
        self.name = None
        self.return_type = None
        self.arguments = None
        if isinstance(d, dict):
            if 'name' in d:
                self.name = d['name']
            if 'return_type' in d:
                self.return_type = d['return_type']
            if 'arguments' in d:
                self.arguments = d['arguments']

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.return_type = ThriftType()
                    self.return_type.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.arguments = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = Argument()
                        _elem5.read(iprot)
                        self.arguments.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Method')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.return_type != None:
            oprot.writeFieldBegin('return_type', TType.STRUCT, 2)
            self.return_type.write(oprot)
            oprot.writeFieldEnd()
        if self.arguments != None:
            oprot.writeFieldBegin('arguments', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.arguments))
            for iter6 in self.arguments:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Service:

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'name', None, None, ),  # 1
        (2, TType.LIST, 'methods', (TType.STRUCT, (Method, Method.thrift_spec)), None, ),  # 2
        (3, TType.BOOL, 'fully_reflected', None, None, ),  # 3
    )

    def __init__(self, d=None):
        self.name = None
        self.methods = None
        self.fully_reflected = None
        if isinstance(d, dict):
            if 'name' in d:
                self.name = d['name']
            if 'methods' in d:
                self.methods = d['methods']
            if 'fully_reflected' in d:
                self.fully_reflected = d['fully_reflected']

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.methods = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = Method()
                        _elem12.read(iprot)
                        self.methods.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.fully_reflected = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Service')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.methods != None:
            oprot.writeFieldBegin('methods', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.methods))
            for iter13 in self.methods:
                iter13.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.fully_reflected != None:
            oprot.writeFieldBegin('fully_reflected', TType.BOOL, 3)
            oprot.writeBool(self.fully_reflected)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
