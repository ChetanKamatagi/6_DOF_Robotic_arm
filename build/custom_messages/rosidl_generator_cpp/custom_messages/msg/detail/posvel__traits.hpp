// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_messages:msg/Posvel.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__TRAITS_HPP_
#define CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "custom_messages/msg/detail/posvel__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace custom_messages
{

namespace msg
{

inline void to_flow_style_yaml(
  const Posvel & msg,
  std::ostream & out)
{
  out << "{";
  // member: position1
  {
    out << "position1: ";
    rosidl_generator_traits::value_to_yaml(msg.position1, out);
    out << ", ";
  }

  // member: velocity1
  {
    out << "velocity1: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity1, out);
    out << ", ";
  }

  // member: position2
  {
    out << "position2: ";
    rosidl_generator_traits::value_to_yaml(msg.position2, out);
    out << ", ";
  }

  // member: velocity2
  {
    out << "velocity2: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity2, out);
    out << ", ";
  }

  // member: position3
  {
    out << "position3: ";
    rosidl_generator_traits::value_to_yaml(msg.position3, out);
    out << ", ";
  }

  // member: velocity3
  {
    out << "velocity3: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity3, out);
    out << ", ";
  }

  // member: position4
  {
    out << "position4: ";
    rosidl_generator_traits::value_to_yaml(msg.position4, out);
    out << ", ";
  }

  // member: velocity4
  {
    out << "velocity4: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity4, out);
    out << ", ";
  }

  // member: position5
  {
    out << "position5: ";
    rosidl_generator_traits::value_to_yaml(msg.position5, out);
    out << ", ";
  }

  // member: velocity5
  {
    out << "velocity5: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity5, out);
    out << ", ";
  }

  // member: position6
  {
    out << "position6: ";
    rosidl_generator_traits::value_to_yaml(msg.position6, out);
    out << ", ";
  }

  // member: velocity6
  {
    out << "velocity6: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity6, out);
    out << ", ";
  }

  // member: torque
  {
    out << "torque: ";
    rosidl_generator_traits::value_to_yaml(msg.torque, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Posvel & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: position1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position1: ";
    rosidl_generator_traits::value_to_yaml(msg.position1, out);
    out << "\n";
  }

  // member: velocity1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity1: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity1, out);
    out << "\n";
  }

  // member: position2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position2: ";
    rosidl_generator_traits::value_to_yaml(msg.position2, out);
    out << "\n";
  }

  // member: velocity2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity2: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity2, out);
    out << "\n";
  }

  // member: position3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position3: ";
    rosidl_generator_traits::value_to_yaml(msg.position3, out);
    out << "\n";
  }

  // member: velocity3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity3: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity3, out);
    out << "\n";
  }

  // member: position4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position4: ";
    rosidl_generator_traits::value_to_yaml(msg.position4, out);
    out << "\n";
  }

  // member: velocity4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity4: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity4, out);
    out << "\n";
  }

  // member: position5
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position5: ";
    rosidl_generator_traits::value_to_yaml(msg.position5, out);
    out << "\n";
  }

  // member: velocity5
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity5: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity5, out);
    out << "\n";
  }

  // member: position6
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position6: ";
    rosidl_generator_traits::value_to_yaml(msg.position6, out);
    out << "\n";
  }

  // member: velocity6
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity6: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity6, out);
    out << "\n";
  }

  // member: torque
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "torque: ";
    rosidl_generator_traits::value_to_yaml(msg.torque, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Posvel & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace custom_messages

namespace rosidl_generator_traits
{

[[deprecated("use custom_messages::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const custom_messages::msg::Posvel & msg,
  std::ostream & out, size_t indentation = 0)
{
  custom_messages::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use custom_messages::msg::to_yaml() instead")]]
inline std::string to_yaml(const custom_messages::msg::Posvel & msg)
{
  return custom_messages::msg::to_yaml(msg);
}

template<>
inline const char * data_type<custom_messages::msg::Posvel>()
{
  return "custom_messages::msg::Posvel";
}

template<>
inline const char * name<custom_messages::msg::Posvel>()
{
  return "custom_messages/msg/Posvel";
}

template<>
struct has_fixed_size<custom_messages::msg::Posvel>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<custom_messages::msg::Posvel>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<custom_messages::msg::Posvel>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__TRAITS_HPP_
