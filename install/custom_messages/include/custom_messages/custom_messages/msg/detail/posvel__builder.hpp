// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_messages:msg/Posvel.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__BUILDER_HPP_
#define CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_messages/msg/detail/posvel__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_messages
{

namespace msg
{

namespace builder
{

class Init_Posvel_torque
{
public:
  explicit Init_Posvel_torque(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  ::custom_messages::msg::Posvel torque(::custom_messages::msg::Posvel::_torque_type arg)
  {
    msg_.torque = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_velocity6
{
public:
  explicit Init_Posvel_velocity6(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  Init_Posvel_torque velocity6(::custom_messages::msg::Posvel::_velocity6_type arg)
  {
    msg_.velocity6 = std::move(arg);
    return Init_Posvel_torque(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_position6
{
public:
  explicit Init_Posvel_position6(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  Init_Posvel_velocity6 position6(::custom_messages::msg::Posvel::_position6_type arg)
  {
    msg_.position6 = std::move(arg);
    return Init_Posvel_velocity6(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_velocity5
{
public:
  explicit Init_Posvel_velocity5(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  Init_Posvel_position6 velocity5(::custom_messages::msg::Posvel::_velocity5_type arg)
  {
    msg_.velocity5 = std::move(arg);
    return Init_Posvel_position6(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_position5
{
public:
  explicit Init_Posvel_position5(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  Init_Posvel_velocity5 position5(::custom_messages::msg::Posvel::_position5_type arg)
  {
    msg_.position5 = std::move(arg);
    return Init_Posvel_velocity5(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_velocity4
{
public:
  explicit Init_Posvel_velocity4(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  Init_Posvel_position5 velocity4(::custom_messages::msg::Posvel::_velocity4_type arg)
  {
    msg_.velocity4 = std::move(arg);
    return Init_Posvel_position5(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_position4
{
public:
  explicit Init_Posvel_position4(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  Init_Posvel_velocity4 position4(::custom_messages::msg::Posvel::_position4_type arg)
  {
    msg_.position4 = std::move(arg);
    return Init_Posvel_velocity4(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_velocity3
{
public:
  explicit Init_Posvel_velocity3(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  Init_Posvel_position4 velocity3(::custom_messages::msg::Posvel::_velocity3_type arg)
  {
    msg_.velocity3 = std::move(arg);
    return Init_Posvel_position4(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_position3
{
public:
  explicit Init_Posvel_position3(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  Init_Posvel_velocity3 position3(::custom_messages::msg::Posvel::_position3_type arg)
  {
    msg_.position3 = std::move(arg);
    return Init_Posvel_velocity3(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_velocity2
{
public:
  explicit Init_Posvel_velocity2(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  Init_Posvel_position3 velocity2(::custom_messages::msg::Posvel::_velocity2_type arg)
  {
    msg_.velocity2 = std::move(arg);
    return Init_Posvel_position3(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_position2
{
public:
  explicit Init_Posvel_position2(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  Init_Posvel_velocity2 position2(::custom_messages::msg::Posvel::_position2_type arg)
  {
    msg_.position2 = std::move(arg);
    return Init_Posvel_velocity2(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_velocity1
{
public:
  explicit Init_Posvel_velocity1(::custom_messages::msg::Posvel & msg)
  : msg_(msg)
  {}
  Init_Posvel_position2 velocity1(::custom_messages::msg::Posvel::_velocity1_type arg)
  {
    msg_.velocity1 = std::move(arg);
    return Init_Posvel_position2(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

class Init_Posvel_position1
{
public:
  Init_Posvel_position1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Posvel_velocity1 position1(::custom_messages::msg::Posvel::_position1_type arg)
  {
    msg_.position1 = std::move(arg);
    return Init_Posvel_velocity1(msg_);
  }

private:
  ::custom_messages::msg::Posvel msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_messages::msg::Posvel>()
{
  return custom_messages::msg::builder::Init_Posvel_position1();
}

}  // namespace custom_messages

#endif  // CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__BUILDER_HPP_
