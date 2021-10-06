// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from screen_app:msg/Key.idl
// generated code does not contain a copyright notice

#ifndef SCREEN_APP__MSG__DETAIL__KEY__BUILDER_HPP_
#define SCREEN_APP__MSG__DETAIL__KEY__BUILDER_HPP_

#include "screen_app/msg/detail/key__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace screen_app
{

namespace msg
{

namespace builder
{

class Init_Key_modifiers
{
public:
  explicit Init_Key_modifiers(::screen_app::msg::Key & msg)
  : msg_(msg)
  {}
  ::screen_app::msg::Key modifiers(::screen_app::msg::Key::_modifiers_type arg)
  {
    msg_.modifiers = std::move(arg);
    return std::move(msg_);
  }

private:
  ::screen_app::msg::Key msg_;
};

class Init_Key_symbol
{
public:
  explicit Init_Key_symbol(::screen_app::msg::Key & msg)
  : msg_(msg)
  {}
  Init_Key_modifiers symbol(::screen_app::msg::Key::_symbol_type arg)
  {
    msg_.symbol = std::move(arg);
    return Init_Key_modifiers(msg_);
  }

private:
  ::screen_app::msg::Key msg_;
};

class Init_Key_header
{
public:
  Init_Key_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Key_symbol header(::screen_app::msg::Key::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Key_symbol(msg_);
  }

private:
  ::screen_app::msg::Key msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::screen_app::msg::Key>()
{
  return screen_app::msg::builder::Init_Key_header();
}

}  // namespace screen_app

#endif  // SCREEN_APP__MSG__DETAIL__KEY__BUILDER_HPP_
