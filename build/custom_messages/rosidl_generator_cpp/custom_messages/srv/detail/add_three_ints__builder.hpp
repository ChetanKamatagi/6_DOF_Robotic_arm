// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_messages:srv/AddThreeInts.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__SRV__DETAIL__ADD_THREE_INTS__BUILDER_HPP_
#define CUSTOM_MESSAGES__SRV__DETAIL__ADD_THREE_INTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_messages/srv/detail/add_three_ints__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_messages
{

namespace srv
{

namespace builder
{

class Init_AddThreeInts_Request_c
{
public:
  explicit Init_AddThreeInts_Request_c(::custom_messages::srv::AddThreeInts_Request & msg)
  : msg_(msg)
  {}
  ::custom_messages::srv::AddThreeInts_Request c(::custom_messages::srv::AddThreeInts_Request::_c_type arg)
  {
    msg_.c = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_messages::srv::AddThreeInts_Request msg_;
};

class Init_AddThreeInts_Request_b
{
public:
  explicit Init_AddThreeInts_Request_b(::custom_messages::srv::AddThreeInts_Request & msg)
  : msg_(msg)
  {}
  Init_AddThreeInts_Request_c b(::custom_messages::srv::AddThreeInts_Request::_b_type arg)
  {
    msg_.b = std::move(arg);
    return Init_AddThreeInts_Request_c(msg_);
  }

private:
  ::custom_messages::srv::AddThreeInts_Request msg_;
};

class Init_AddThreeInts_Request_a
{
public:
  Init_AddThreeInts_Request_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddThreeInts_Request_b a(::custom_messages::srv::AddThreeInts_Request::_a_type arg)
  {
    msg_.a = std::move(arg);
    return Init_AddThreeInts_Request_b(msg_);
  }

private:
  ::custom_messages::srv::AddThreeInts_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_messages::srv::AddThreeInts_Request>()
{
  return custom_messages::srv::builder::Init_AddThreeInts_Request_a();
}

}  // namespace custom_messages


namespace custom_messages
{

namespace srv
{

namespace builder
{

class Init_AddThreeInts_Response_sum
{
public:
  Init_AddThreeInts_Response_sum()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_messages::srv::AddThreeInts_Response sum(::custom_messages::srv::AddThreeInts_Response::_sum_type arg)
  {
    msg_.sum = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_messages::srv::AddThreeInts_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_messages::srv::AddThreeInts_Response>()
{
  return custom_messages::srv::builder::Init_AddThreeInts_Response_sum();
}

}  // namespace custom_messages

#endif  // CUSTOM_MESSAGES__SRV__DETAIL__ADD_THREE_INTS__BUILDER_HPP_
