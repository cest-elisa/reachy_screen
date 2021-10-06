// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from screen_app:msg/Key.idl
// generated code does not contain a copyright notice

#ifndef SCREEN_APP__MSG__DETAIL__KEY__TRAITS_HPP_
#define SCREEN_APP__MSG__DETAIL__KEY__TRAITS_HPP_

#include "screen_app/msg/detail/key__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<screen_app::msg::Key>()
{
  return "screen_app::msg::Key";
}

template<>
inline const char * name<screen_app::msg::Key>()
{
  return "screen_app/msg/Key";
}

template<>
struct has_fixed_size<screen_app::msg::Key>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<screen_app::msg::Key>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<screen_app::msg::Key>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SCREEN_APP__MSG__DETAIL__KEY__TRAITS_HPP_
