// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from screen_app:msg/Mouse.idl
// generated code does not contain a copyright notice

#ifndef SCREEN_APP__MSG__DETAIL__MOUSE__STRUCT_HPP_
#define SCREEN_APP__MSG__DETAIL__MOUSE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__screen_app__msg__Mouse __attribute__((deprecated))
#else
# define DEPRECATED__screen_app__msg__Mouse __declspec(deprecated)
#endif

namespace screen_app
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Mouse_
{
  using Type = Mouse_<ContainerAllocator>;

  explicit Mouse_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0;
      this->y = 0;
      this->dx = 0;
      this->dy = 0;
      this->left = false;
      this->right = false;
    }
  }

  explicit Mouse_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0;
      this->y = 0;
      this->dx = 0;
      this->dy = 0;
      this->left = false;
      this->right = false;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _x_type =
    int16_t;
  _x_type x;
  using _y_type =
    int16_t;
  _y_type y;
  using _dx_type =
    int16_t;
  _dx_type dx;
  using _dy_type =
    int16_t;
  _dy_type dy;
  using _left_type =
    bool;
  _left_type left;
  using _right_type =
    bool;
  _right_type right;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__x(
    const int16_t & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const int16_t & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__dx(
    const int16_t & _arg)
  {
    this->dx = _arg;
    return *this;
  }
  Type & set__dy(
    const int16_t & _arg)
  {
    this->dy = _arg;
    return *this;
  }
  Type & set__left(
    const bool & _arg)
  {
    this->left = _arg;
    return *this;
  }
  Type & set__right(
    const bool & _arg)
  {
    this->right = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    screen_app::msg::Mouse_<ContainerAllocator> *;
  using ConstRawPtr =
    const screen_app::msg::Mouse_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<screen_app::msg::Mouse_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<screen_app::msg::Mouse_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      screen_app::msg::Mouse_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<screen_app::msg::Mouse_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      screen_app::msg::Mouse_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<screen_app::msg::Mouse_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<screen_app::msg::Mouse_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<screen_app::msg::Mouse_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__screen_app__msg__Mouse
    std::shared_ptr<screen_app::msg::Mouse_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__screen_app__msg__Mouse
    std::shared_ptr<screen_app::msg::Mouse_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Mouse_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->dx != other.dx) {
      return false;
    }
    if (this->dy != other.dy) {
      return false;
    }
    if (this->left != other.left) {
      return false;
    }
    if (this->right != other.right) {
      return false;
    }
    return true;
  }
  bool operator!=(const Mouse_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Mouse_

// alias to use template instance with default allocator
using Mouse =
  screen_app::msg::Mouse_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace screen_app

#endif  // SCREEN_APP__MSG__DETAIL__MOUSE__STRUCT_HPP_
