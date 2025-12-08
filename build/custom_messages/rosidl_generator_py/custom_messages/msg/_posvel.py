# generated from rosidl_generator_py/resource/_idl.py.em
# with input from custom_messages:msg/Posvel.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Posvel(type):
    """Metaclass of message 'Posvel'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('custom_messages')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'custom_messages.msg.Posvel')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__posvel
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__posvel
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__posvel
            cls._TYPE_SUPPORT = module.type_support_msg__msg__posvel
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__posvel

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Posvel(metaclass=Metaclass_Posvel):
    """Message class 'Posvel'."""

    __slots__ = [
        '_position1',
        '_velocity1',
        '_position2',
        '_velocity2',
        '_position3',
        '_velocity3',
        '_position4',
        '_velocity4',
        '_position5',
        '_velocity5',
        '_position6',
        '_velocity6',
        '_torque',
    ]

    _fields_and_field_types = {
        'position1': 'double',
        'velocity1': 'double',
        'position2': 'double',
        'velocity2': 'double',
        'position3': 'double',
        'velocity3': 'double',
        'position4': 'double',
        'velocity4': 'double',
        'position5': 'double',
        'velocity5': 'double',
        'position6': 'double',
        'velocity6': 'double',
        'torque': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.position1 = kwargs.get('position1', float())
        self.velocity1 = kwargs.get('velocity1', float())
        self.position2 = kwargs.get('position2', float())
        self.velocity2 = kwargs.get('velocity2', float())
        self.position3 = kwargs.get('position3', float())
        self.velocity3 = kwargs.get('velocity3', float())
        self.position4 = kwargs.get('position4', float())
        self.velocity4 = kwargs.get('velocity4', float())
        self.position5 = kwargs.get('position5', float())
        self.velocity5 = kwargs.get('velocity5', float())
        self.position6 = kwargs.get('position6', float())
        self.velocity6 = kwargs.get('velocity6', float())
        self.torque = kwargs.get('torque', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.position1 != other.position1:
            return False
        if self.velocity1 != other.velocity1:
            return False
        if self.position2 != other.position2:
            return False
        if self.velocity2 != other.velocity2:
            return False
        if self.position3 != other.position3:
            return False
        if self.velocity3 != other.velocity3:
            return False
        if self.position4 != other.position4:
            return False
        if self.velocity4 != other.velocity4:
            return False
        if self.position5 != other.position5:
            return False
        if self.velocity5 != other.velocity5:
            return False
        if self.position6 != other.position6:
            return False
        if self.velocity6 != other.velocity6:
            return False
        if self.torque != other.torque:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def position1(self):
        """Message field 'position1'."""
        return self._position1

    @position1.setter
    def position1(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'position1' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'position1' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._position1 = value

    @builtins.property
    def velocity1(self):
        """Message field 'velocity1'."""
        return self._velocity1

    @velocity1.setter
    def velocity1(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'velocity1' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'velocity1' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._velocity1 = value

    @builtins.property
    def position2(self):
        """Message field 'position2'."""
        return self._position2

    @position2.setter
    def position2(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'position2' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'position2' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._position2 = value

    @builtins.property
    def velocity2(self):
        """Message field 'velocity2'."""
        return self._velocity2

    @velocity2.setter
    def velocity2(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'velocity2' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'velocity2' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._velocity2 = value

    @builtins.property
    def position3(self):
        """Message field 'position3'."""
        return self._position3

    @position3.setter
    def position3(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'position3' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'position3' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._position3 = value

    @builtins.property
    def velocity3(self):
        """Message field 'velocity3'."""
        return self._velocity3

    @velocity3.setter
    def velocity3(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'velocity3' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'velocity3' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._velocity3 = value

    @builtins.property
    def position4(self):
        """Message field 'position4'."""
        return self._position4

    @position4.setter
    def position4(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'position4' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'position4' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._position4 = value

    @builtins.property
    def velocity4(self):
        """Message field 'velocity4'."""
        return self._velocity4

    @velocity4.setter
    def velocity4(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'velocity4' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'velocity4' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._velocity4 = value

    @builtins.property
    def position5(self):
        """Message field 'position5'."""
        return self._position5

    @position5.setter
    def position5(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'position5' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'position5' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._position5 = value

    @builtins.property
    def velocity5(self):
        """Message field 'velocity5'."""
        return self._velocity5

    @velocity5.setter
    def velocity5(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'velocity5' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'velocity5' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._velocity5 = value

    @builtins.property
    def position6(self):
        """Message field 'position6'."""
        return self._position6

    @position6.setter
    def position6(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'position6' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'position6' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._position6 = value

    @builtins.property
    def velocity6(self):
        """Message field 'velocity6'."""
        return self._velocity6

    @velocity6.setter
    def velocity6(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'velocity6' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'velocity6' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._velocity6 = value

    @builtins.property
    def torque(self):
        """Message field 'torque'."""
        return self._torque

    @torque.setter
    def torque(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'torque' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'torque' field must be an integer in [-2147483648, 2147483647]"
        self._torque = value
