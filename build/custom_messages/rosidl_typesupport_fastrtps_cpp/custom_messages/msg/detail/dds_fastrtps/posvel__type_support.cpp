// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from custom_messages:msg/Posvel.idl
// generated code does not contain a copyright notice
#include "custom_messages/msg/detail/posvel__rosidl_typesupport_fastrtps_cpp.hpp"
#include "custom_messages/msg/detail/posvel__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace custom_messages
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_custom_messages
cdr_serialize(
  const custom_messages::msg::Posvel & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: position1
  cdr << ros_message.position1;
  // Member: velocity1
  cdr << ros_message.velocity1;
  // Member: position2
  cdr << ros_message.position2;
  // Member: velocity2
  cdr << ros_message.velocity2;
  // Member: position3
  cdr << ros_message.position3;
  // Member: velocity3
  cdr << ros_message.velocity3;
  // Member: position4
  cdr << ros_message.position4;
  // Member: velocity4
  cdr << ros_message.velocity4;
  // Member: position5
  cdr << ros_message.position5;
  // Member: velocity5
  cdr << ros_message.velocity5;
  // Member: position6
  cdr << ros_message.position6;
  // Member: velocity6
  cdr << ros_message.velocity6;
  // Member: torque
  cdr << ros_message.torque;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_custom_messages
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  custom_messages::msg::Posvel & ros_message)
{
  // Member: position1
  cdr >> ros_message.position1;

  // Member: velocity1
  cdr >> ros_message.velocity1;

  // Member: position2
  cdr >> ros_message.position2;

  // Member: velocity2
  cdr >> ros_message.velocity2;

  // Member: position3
  cdr >> ros_message.position3;

  // Member: velocity3
  cdr >> ros_message.velocity3;

  // Member: position4
  cdr >> ros_message.position4;

  // Member: velocity4
  cdr >> ros_message.velocity4;

  // Member: position5
  cdr >> ros_message.position5;

  // Member: velocity5
  cdr >> ros_message.velocity5;

  // Member: position6
  cdr >> ros_message.position6;

  // Member: velocity6
  cdr >> ros_message.velocity6;

  // Member: torque
  cdr >> ros_message.torque;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_custom_messages
get_serialized_size(
  const custom_messages::msg::Posvel & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: position1
  {
    size_t item_size = sizeof(ros_message.position1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: velocity1
  {
    size_t item_size = sizeof(ros_message.velocity1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: position2
  {
    size_t item_size = sizeof(ros_message.position2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: velocity2
  {
    size_t item_size = sizeof(ros_message.velocity2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: position3
  {
    size_t item_size = sizeof(ros_message.position3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: velocity3
  {
    size_t item_size = sizeof(ros_message.velocity3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: position4
  {
    size_t item_size = sizeof(ros_message.position4);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: velocity4
  {
    size_t item_size = sizeof(ros_message.velocity4);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: position5
  {
    size_t item_size = sizeof(ros_message.position5);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: velocity5
  {
    size_t item_size = sizeof(ros_message.velocity5);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: position6
  {
    size_t item_size = sizeof(ros_message.position6);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: velocity6
  {
    size_t item_size = sizeof(ros_message.velocity6);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: torque
  {
    size_t item_size = sizeof(ros_message.torque);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_custom_messages
max_serialized_size_Posvel(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: position1
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: velocity1
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: position2
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: velocity2
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: position3
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: velocity3
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: position4
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: velocity4
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: position5
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: velocity5
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: position6
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: velocity6
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: torque
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static bool _Posvel__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const custom_messages::msg::Posvel *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Posvel__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<custom_messages::msg::Posvel *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Posvel__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const custom_messages::msg::Posvel *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Posvel__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_Posvel(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _Posvel__callbacks = {
  "custom_messages::msg",
  "Posvel",
  _Posvel__cdr_serialize,
  _Posvel__cdr_deserialize,
  _Posvel__get_serialized_size,
  _Posvel__max_serialized_size
};

static rosidl_message_type_support_t _Posvel__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Posvel__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace custom_messages

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_custom_messages
const rosidl_message_type_support_t *
get_message_type_support_handle<custom_messages::msg::Posvel>()
{
  return &custom_messages::msg::typesupport_fastrtps_cpp::_Posvel__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, custom_messages, msg, Posvel)() {
  return &custom_messages::msg::typesupport_fastrtps_cpp::_Posvel__handle;
}

#ifdef __cplusplus
}
#endif
