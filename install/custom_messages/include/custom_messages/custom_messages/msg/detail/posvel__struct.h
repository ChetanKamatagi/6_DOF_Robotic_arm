// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_messages:msg/Posvel.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__STRUCT_H_
#define CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Posvel in the package custom_messages.
typedef struct custom_messages__msg__Posvel
{
  double position1;
  double velocity1;
  double position2;
  double velocity2;
  double position3;
  double velocity3;
  double position4;
  double velocity4;
  double position5;
  double velocity5;
  double position6;
  double velocity6;
  int32_t torque;
} custom_messages__msg__Posvel;

// Struct for a sequence of custom_messages__msg__Posvel.
typedef struct custom_messages__msg__Posvel__Sequence
{
  custom_messages__msg__Posvel * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_messages__msg__Posvel__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__STRUCT_H_
