// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from screen_app:msg/Num.idl
// generated code does not contain a copyright notice

#ifndef SCREEN_APP__MSG__DETAIL__NUM__STRUCT_H_
#define SCREEN_APP__MSG__DETAIL__NUM__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

// Struct defined in msg/Num in the package screen_app.
typedef struct screen_app__msg__Num
{
  std_msgs__msg__Header header;
  int64_t num;
} screen_app__msg__Num;

// Struct for a sequence of screen_app__msg__Num.
typedef struct screen_app__msg__Num__Sequence
{
  screen_app__msg__Num * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} screen_app__msg__Num__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SCREEN_APP__MSG__DETAIL__NUM__STRUCT_H_
