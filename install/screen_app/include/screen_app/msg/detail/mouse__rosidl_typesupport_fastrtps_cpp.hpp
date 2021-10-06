// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from screen_app:msg/Mouse.idl
// generated code does not contain a copyright notice

#ifndef SCREEN_APP__MSG__DETAIL__MOUSE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define SCREEN_APP__MSG__DETAIL__MOUSE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "screen_app/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "screen_app/msg/detail/mouse__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace screen_app
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_screen_app
cdr_serialize(
  const screen_app::msg::Mouse & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_screen_app
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  screen_app::msg::Mouse & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_screen_app
get_serialized_size(
  const screen_app::msg::Mouse & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_screen_app
max_serialized_size_Mouse(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace screen_app

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_screen_app
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, screen_app, msg, Mouse)();

#ifdef __cplusplus
}
#endif

#endif  // SCREEN_APP__MSG__DETAIL__MOUSE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
