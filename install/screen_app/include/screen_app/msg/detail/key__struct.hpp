// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from screen_app:msg/Key.idl
// generated code does not contain a copyright notice

#ifndef SCREEN_APP__MSG__DETAIL__KEY__STRUCT_HPP_
#define SCREEN_APP__MSG__DETAIL__KEY__STRUCT_HPP_

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
# define DEPRECATED__screen_app__msg__Key __attribute__((deprecated))
#else
# define DEPRECATED__screen_app__msg__Key __declspec(deprecated)
#endif

namespace screen_app
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Key_
{
  using Type = Key_<ContainerAllocator>;

  explicit Key_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->symbol = "";
      this->modifiers = "";
    }
  }

  explicit Key_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    symbol(_alloc),
    modifiers(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->symbol = "";
      this->modifiers = "";
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _symbol_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _symbol_type symbol;
  using _modifiers_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _modifiers_type modifiers;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__symbol(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->symbol = _arg;
    return *this;
  }
  Type & set__modifiers(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->modifiers = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    screen_app::msg::Key_<ContainerAllocator> *;
  using ConstRawPtr =
    const screen_app::msg::Key_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<screen_app::msg::Key_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<screen_app::msg::Key_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      screen_app::msg::Key_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<screen_app::msg::Key_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      screen_app::msg::Key_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<screen_app::msg::Key_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<screen_app::msg::Key_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<screen_app::msg::Key_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__screen_app__msg__Key
    std::shared_ptr<screen_app::msg::Key_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__screen_app__msg__Key
    std::shared_ptr<screen_app::msg::Key_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Key_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->symbol != other.symbol) {
      return false;
    }
    if (this->modifiers != other.modifiers) {
      return false;
    }
    return true;
  }
  bool operator!=(const Key_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Key_

// alias to use template instance with default allocator
using Key =
  screen_app::msg::Key_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace screen_app

#endif  // SCREEN_APP__MSG__DETAIL__KEY__STRUCT_HPP_
