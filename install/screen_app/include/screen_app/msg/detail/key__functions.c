// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from screen_app:msg/Key.idl
// generated code does not contain a copyright notice
#include "screen_app/msg/detail/key__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `symbol`
// Member `modifiers`
#include "rosidl_runtime_c/string_functions.h"

bool
screen_app__msg__Key__init(screen_app__msg__Key * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    screen_app__msg__Key__fini(msg);
    return false;
  }
  // symbol
  if (!rosidl_runtime_c__String__init(&msg->symbol)) {
    screen_app__msg__Key__fini(msg);
    return false;
  }
  // modifiers
  if (!rosidl_runtime_c__String__init(&msg->modifiers)) {
    screen_app__msg__Key__fini(msg);
    return false;
  }
  return true;
}

void
screen_app__msg__Key__fini(screen_app__msg__Key * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // symbol
  rosidl_runtime_c__String__fini(&msg->symbol);
  // modifiers
  rosidl_runtime_c__String__fini(&msg->modifiers);
}

screen_app__msg__Key *
screen_app__msg__Key__create()
{
  screen_app__msg__Key * msg = (screen_app__msg__Key *)malloc(sizeof(screen_app__msg__Key));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(screen_app__msg__Key));
  bool success = screen_app__msg__Key__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
screen_app__msg__Key__destroy(screen_app__msg__Key * msg)
{
  if (msg) {
    screen_app__msg__Key__fini(msg);
  }
  free(msg);
}


bool
screen_app__msg__Key__Sequence__init(screen_app__msg__Key__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  screen_app__msg__Key * data = NULL;
  if (size) {
    data = (screen_app__msg__Key *)calloc(size, sizeof(screen_app__msg__Key));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = screen_app__msg__Key__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        screen_app__msg__Key__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
screen_app__msg__Key__Sequence__fini(screen_app__msg__Key__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      screen_app__msg__Key__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

screen_app__msg__Key__Sequence *
screen_app__msg__Key__Sequence__create(size_t size)
{
  screen_app__msg__Key__Sequence * array = (screen_app__msg__Key__Sequence *)malloc(sizeof(screen_app__msg__Key__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = screen_app__msg__Key__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
screen_app__msg__Key__Sequence__destroy(screen_app__msg__Key__Sequence * array)
{
  if (array) {
    screen_app__msg__Key__Sequence__fini(array);
  }
  free(array);
}
