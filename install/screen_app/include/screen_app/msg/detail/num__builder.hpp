// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from screen_app:msg/Num.idl
// generated code does not contain a copyright notice

#ifndef SCREEN_APP__MSG__DETAIL__NUM__BUILDER_HPP_
#define SCREEN_APP__MSG__DETAIL__NUM__BUILDER_HPP_

#include "screen_app/msg/detail/num__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace screen_app
{

namespace msg
{

namespace builder
{

class Init_Num_num
{
public:
  explicit Init_Num_num(::screen_app::msg::Num & msg)
  : msg_(msg)
  {}
  ::screen_app::msg::Num num(::screen_app::msg::Num::_num_type arg)
  {
    msg_.num = std::move(arg);
    return std::move(msg_);
  }

private:
  ::screen_app::msg::Num msg_;
};

class Init_Num_header
{
public:
  Init_Num_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Num_num header(::screen_app::msg::Num::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Num_num(msg_);
  }

private:
  ::screen_app::msg::Num msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::screen_app::msg::Num>()
{
  return screen_app::msg::builder::Init_Num_header();
}

}  // namespace screen_app

#endif  // SCREEN_APP__MSG__DETAIL__NUM__BUILDER_HPP_
