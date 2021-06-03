# automatically generated by the FlatBuffers compiler, do not modify

# namespace: zkinterface

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# A single R1CS constraint between variables.
#
# - Represents the linear combinations of variables A, B, C such that:
#       (A) * (B) = (C)
# - A linear combination is given as a sequence of (variable ID, coefficient).
class BilinearConstraint(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BilinearConstraint()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBilinearConstraint(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def BilinearConstraintBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x7A\x6B\x69\x66", size_prefixed=size_prefixed)

    # BilinearConstraint
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BilinearConstraint
    def LinearCombinationA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from zkinterface.Variables import Variables
            obj = Variables()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BilinearConstraint
    def LinearCombinationB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from zkinterface.Variables import Variables
            obj = Variables()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BilinearConstraint
    def LinearCombinationC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from zkinterface.Variables import Variables
            obj = Variables()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Start(builder): builder.StartObject(3)
def BilinearConstraintStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddLinearCombinationA(builder, linearCombinationA): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(linearCombinationA), 0)
def BilinearConstraintAddLinearCombinationA(builder, linearCombinationA):
    """This method is deprecated. Please switch to AddLinearCombinationA."""
    return AddLinearCombinationA(builder, linearCombinationA)
def AddLinearCombinationB(builder, linearCombinationB): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(linearCombinationB), 0)
def BilinearConstraintAddLinearCombinationB(builder, linearCombinationB):
    """This method is deprecated. Please switch to AddLinearCombinationB."""
    return AddLinearCombinationB(builder, linearCombinationB)
def AddLinearCombinationC(builder, linearCombinationC): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(linearCombinationC), 0)
def BilinearConstraintAddLinearCombinationC(builder, linearCombinationC):
    """This method is deprecated. Please switch to AddLinearCombinationC."""
    return AddLinearCombinationC(builder, linearCombinationC)
def End(builder): return builder.EndObject()
def BilinearConstraintEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)