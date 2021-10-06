// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from screen_app:msg/Mouse.idl
// generated code does not contain a copyright notice

#ifndef SCREEN_APP__MSG__DETAIL__MOUSE__BUILDER_HPP_
#define SCREEN_APP__MSG__DETAIL__MOUSE__BUILDER_HPP_

#include "screen_app/msg/detail/mouse__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace screen_app
{

namespace msg
{

namespace builder
{

class Init_Mouse_right
{
public:
  explicit Init_Mouse_right(::screen_app::msg::Mouse & msg)
  : msg_(msg)
  {}
  ::screen_app::msg::Mouse right(::screen_app::msg::Mouse::_right_type arg)
  {
    msg_.right = std::move(arg);
    return std::move(msg_);
  }

private:
  ::screen_app::msg::Mouse msg_;
};

class Init_Mouse_left
{
public:
  explicit Init_Mouse_left(::screen_app::msg::Mouse & msg)
  : msg_(msg)
  {}
  Init_Mouse_right left(::screen_app::msg::Mouse::_left_type arg)
  {
    msg_.left = std::move(arg);
    return Init_Mouse_right(msg_);
  }

private:
  ::screen_app::msg::Mouse msg_;
};

class Init_Mouse_dy
{
public:
  explicit Init_Mouse_dy(::screen_app::msg::Mouse & msg)
  : msg_(msg)
  {}
  Init_Mouse_left dy(::screen_app::msg::Mouse::_dy_type arg)
  {
    msg_.dy = std::move(arg);
    return Init_Mouse_left(msg_);
  }

private:
  ::screen_app::msg::Mouse msg_;
};

class Init_Mouse_dx
{
public:
  explicit Init_Mouse_dx(::screen_app::msg::Mouse & msg)
  : msg_(msg)
  {}
  Init_Mouse_dy dx(::screen_app::msg::Mouse::_dx_type arg)
  {
    msg_.dx = std::move(arg);
    return Init_Mouse_dy(msg_);
  }

private:
  ::screen_app::msg::Mouse msg_;
};

class Init_Mouse_y
{
public:
  explicit Init_Mouse_y(::screen_app::msg::Mouse & msg)
  : msg_(msg)
  {}
  Init_Mouse_dx y(::screen_app::msg::Mouse::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Mouse_dx(msg_);
  }

private:
  ::screen_app::msg::Mouse msg_;
};

class Init_Mouse_x
{
public:
  explicit Init_Mouse_x(::screen_app::msg::Mouse & msg)
  : msg_(msg)
  {}
  Init_Mouse_y x(::screen_app::msg::Mouse::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Mouse_y(msg_);
  }

private:
  ::screen_app::msg::Mouse msg_;
};

class Init_Mouse_header
{
public:
  Init_Mouse_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Mouse_x header(::screen_app::msg::Mouse::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Mouse_x(msg_);
  }

private:
  ::screen_app::msg::Mouse msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::screen_app::msg::Mouse>()
{
  return screen_app::msg::builder::Init_Mouse_header();
}

}  // namespace screen_app

#endif  // SCREEN_APP__MSG__DETAIL__MOUSE__BUILDER_HPP_
