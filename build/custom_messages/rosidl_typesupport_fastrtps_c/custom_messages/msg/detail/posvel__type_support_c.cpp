// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from custom_messages:msg/Posvel.idl
// generated code does not contain a copyright notice
#include "custom_messages/msg/detail/posvel__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "custom_messages/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "custom_messages/msg/detail/posvel__struct.h"
#include "custom_messages/msg/detail/posvel__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _Posvel__ros_msg_type = custom_messages__msg__Posvel;

static bool _Posvel__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Posvel__ros_msg_type * ros_message = static_cast<const _Posvel__ros_msg_type *>(untyped_ros_message);
  // Field name: position1
  {
    cdr << ros_message->position1;
  }

  // Field name: velocity1
  {
    cdr << ros_message->velocity1;
  }

  // Field name: position2
  {
    cdr << ros_message->position2;
  }

  // Field name: velocity2
  {
    cdr << ros_message->velocity2;
  }

  // Field name: position3
  {
    cdr << ros_message->position3;
  }

  // Field name: velocity3
  {
    cdr << ros_message->velocity3;
  }

  // Field name: position4
  {
    cdr << ros_message->position4;
  }

  // Field name: velocity4
  {
    cdr << ros_message->velocity4;
  }

  // Field name: position5
  {
    cdr << ros_message->position5;
  }

  // Field name: velocity5
  {
    cdr << ros_message->velocity5;
  }

  // Field name: position6
  {
    cdr << ros_message->position6;
  }

  // Field name: velocity6
  {
    cdr << ros_message->velocity6;
  }

  // Field name: torque
  {
    cdr << ros_message->torque;
  }

  return true;
}

static bool _Posvel__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Posvel__ros_msg_type * ros_message = static_cast<_Posvel__ros_msg_type *>(untyped_ros_message);
  // Field name: position1
  {
    cdr >> ros_message->position1;
  }

  // Field name: velocity1
  {
    cdr >> ros_message->velocity1;
  }

  // Field name: position2
  {
    cdr >> ros_message->position2;
  }

  // Field name: velocity2
  {
    cdr >> ros_message->velocity2;
  }

  // Field name: position3
  {
    cdr >> ros_message->position3;
  }

  // Field name: velocity3
  {
    cdr >> ros_message->velocity3;
  }

  // Field name: position4
  {
    cdr >> ros_message->position4;
  }

  // Field name: velocity4
  {
    cdr >> ros_message->velocity4;
  }

  // Field name: position5
  {
    cdr >> ros_message->position5;
  }

  // Field name: velocity5
  {
    cdr >> ros_message->velocity5;
  }

  // Field name: position6
  {
    cdr >> ros_message->position6;
  }

  // Field name: velocity6
  {
    cdr >> ros_message->velocity6;
  }

  // Field name: torque
  {
    cdr >> ros_message->torque;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_messages
size_t get_serialized_size_custom_messages__msg__Posvel(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Posvel__ros_msg_type * ros_message = static_cast<const _Posvel__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name position1
  {
    size_t item_size = sizeof(ros_message->position1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name velocity1
  {
    size_t item_size = sizeof(ros_message->velocity1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name position2
  {
    size_t item_size = sizeof(ros_message->position2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name velocity2
  {
    size_t item_size = sizeof(ros_message->velocity2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name position3
  {
    size_t item_size = sizeof(ros_message->position3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name velocity3
  {
    size_t item_size = sizeof(ros_message->velocity3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name position4
  {
    size_t item_size = sizeof(ros_message->position4);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name velocity4
  {
    size_t item_size = sizeof(ros_message->velocity4);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name position5
  {
    size_t item_size = sizeof(ros_message->position5);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name velocity5
  {
    size_t item_size = sizeof(ros_message->velocity5);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name position6
  {
    size_t item_size = sizeof(ros_message->position6);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name velocity6
  {
    size_t item_size = sizeof(ros_message->velocity6);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name torque
  {
    size_t item_size = sizeof(ros_message->torque);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Posvel__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_custom_messages__msg__Posvel(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_messages
size_t max_serialized_size_custom_messages__msg__Posvel(
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

  // member: position1
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: velocity1
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: position2
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: velocity2
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: position3
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: velocity3
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: position4
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: velocity4
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: position5
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: velocity5
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: position6
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: velocity6
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: torque
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _Posvel__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_custom_messages__msg__Posvel(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Posvel = {
  "custom_messages::msg",
  "Posvel",
  _Posvel__cdr_serialize,
  _Posvel__cdr_deserialize,
  _Posvel__get_serialized_size,
  _Posvel__max_serialized_size
};

static rosidl_message_type_support_t _Posvel__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Posvel,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, custom_messages, msg, Posvel)() {
  return &_Posvel__type_support;
}

#if defined(__cplusplus)
}
#endif
