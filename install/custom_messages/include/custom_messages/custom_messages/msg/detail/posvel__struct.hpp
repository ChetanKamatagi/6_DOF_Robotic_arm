// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from custom_messages:msg/Posvel.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__STRUCT_HPP_
#define CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__custom_messages__msg__Posvel __attribute__((deprecated))
#else
# define DEPRECATED__custom_messages__msg__Posvel __declspec(deprecated)
#endif

namespace custom_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Posvel_
{
  using Type = Posvel_<ContainerAllocator>;

  explicit Posvel_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->position1 = 0.0;
      this->velocity1 = 0.0;
      this->position2 = 0.0;
      this->velocity2 = 0.0;
      this->position3 = 0.0;
      this->velocity3 = 0.0;
      this->position4 = 0.0;
      this->velocity4 = 0.0;
      this->position5 = 0.0;
      this->velocity5 = 0.0;
      this->position6 = 0.0;
      this->velocity6 = 0.0;
      this->torque = 0l;
    }
  }

  explicit Posvel_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->position1 = 0.0;
      this->velocity1 = 0.0;
      this->position2 = 0.0;
      this->velocity2 = 0.0;
      this->position3 = 0.0;
      this->velocity3 = 0.0;
      this->position4 = 0.0;
      this->velocity4 = 0.0;
      this->position5 = 0.0;
      this->velocity5 = 0.0;
      this->position6 = 0.0;
      this->velocity6 = 0.0;
      this->torque = 0l;
    }
  }

  // field types and members
  using _position1_type =
    double;
  _position1_type position1;
  using _velocity1_type =
    double;
  _velocity1_type velocity1;
  using _position2_type =
    double;
  _position2_type position2;
  using _velocity2_type =
    double;
  _velocity2_type velocity2;
  using _position3_type =
    double;
  _position3_type position3;
  using _velocity3_type =
    double;
  _velocity3_type velocity3;
  using _position4_type =
    double;
  _position4_type position4;
  using _velocity4_type =
    double;
  _velocity4_type velocity4;
  using _position5_type =
    double;
  _position5_type position5;
  using _velocity5_type =
    double;
  _velocity5_type velocity5;
  using _position6_type =
    double;
  _position6_type position6;
  using _velocity6_type =
    double;
  _velocity6_type velocity6;
  using _torque_type =
    int32_t;
  _torque_type torque;

  // setters for named parameter idiom
  Type & set__position1(
    const double & _arg)
  {
    this->position1 = _arg;
    return *this;
  }
  Type & set__velocity1(
    const double & _arg)
  {
    this->velocity1 = _arg;
    return *this;
  }
  Type & set__position2(
    const double & _arg)
  {
    this->position2 = _arg;
    return *this;
  }
  Type & set__velocity2(
    const double & _arg)
  {
    this->velocity2 = _arg;
    return *this;
  }
  Type & set__position3(
    const double & _arg)
  {
    this->position3 = _arg;
    return *this;
  }
  Type & set__velocity3(
    const double & _arg)
  {
    this->velocity3 = _arg;
    return *this;
  }
  Type & set__position4(
    const double & _arg)
  {
    this->position4 = _arg;
    return *this;
  }
  Type & set__velocity4(
    const double & _arg)
  {
    this->velocity4 = _arg;
    return *this;
  }
  Type & set__position5(
    const double & _arg)
  {
    this->position5 = _arg;
    return *this;
  }
  Type & set__velocity5(
    const double & _arg)
  {
    this->velocity5 = _arg;
    return *this;
  }
  Type & set__position6(
    const double & _arg)
  {
    this->position6 = _arg;
    return *this;
  }
  Type & set__velocity6(
    const double & _arg)
  {
    this->velocity6 = _arg;
    return *this;
  }
  Type & set__torque(
    const int32_t & _arg)
  {
    this->torque = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_messages::msg::Posvel_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_messages::msg::Posvel_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_messages::msg::Posvel_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_messages::msg::Posvel_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_messages::msg::Posvel_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_messages::msg::Posvel_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_messages::msg::Posvel_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_messages::msg::Posvel_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_messages::msg::Posvel_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_messages::msg::Posvel_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_messages__msg__Posvel
    std::shared_ptr<custom_messages::msg::Posvel_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_messages__msg__Posvel
    std::shared_ptr<custom_messages::msg::Posvel_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Posvel_ & other) const
  {
    if (this->position1 != other.position1) {
      return false;
    }
    if (this->velocity1 != other.velocity1) {
      return false;
    }
    if (this->position2 != other.position2) {
      return false;
    }
    if (this->velocity2 != other.velocity2) {
      return false;
    }
    if (this->position3 != other.position3) {
      return false;
    }
    if (this->velocity3 != other.velocity3) {
      return false;
    }
    if (this->position4 != other.position4) {
      return false;
    }
    if (this->velocity4 != other.velocity4) {
      return false;
    }
    if (this->position5 != other.position5) {
      return false;
    }
    if (this->velocity5 != other.velocity5) {
      return false;
    }
    if (this->position6 != other.position6) {
      return false;
    }
    if (this->velocity6 != other.velocity6) {
      return false;
    }
    if (this->torque != other.torque) {
      return false;
    }
    return true;
  }
  bool operator!=(const Posvel_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Posvel_

// alias to use template instance with default allocator
using Posvel =
  custom_messages::msg::Posvel_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace custom_messages

#endif  // CUSTOM_MESSAGES__MSG__DETAIL__POSVEL__STRUCT_HPP_
