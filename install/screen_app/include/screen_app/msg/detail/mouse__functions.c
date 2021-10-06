// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from screen_app:msg/Mouse.idl
// generated code does not contain a copyright notice
#include "screen_app/msg/detail/mouse__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
screen_app__msg__Mouse__init(screen_app__msg__Mouse * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    screen_app__msg__Mouse__fini(msg);
    return false;
  }
  // x
  // y
  // dx
  // dy
  // left
  // right
  return true;
}

void
screen_app__msg__Mouse__fini(screen_app__msg__Mouse * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // x
  // y
  // dx
  // dy
  // left
  // right
}

screen_app__msg__Mouse *
screen_app__msg__Mouse__create()
{
  screen_app__msg__Mouse * msg = (screen_app__msg__Mouse *)malloc(sizeof(screen_app__msg__Mouse));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(screen_app__msg__Mouse));
  bool success = screen_app__msg__Mouse__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
screen_app__msg__Mouse__destroy(screen_app__msg__Mouse * msg)
{
  if (msg) {
    screen_app__msg__Mouse__fini(msg);
  }
  free(msg);
}


bool
screen_app__msg__Mouse__Sequence__init(screen_app__msg__Mouse__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  screen_app__msg__Mouse * data = NULL;
  if (size) {
    data = (screen_app__msg__Mouse *)calloc(size, sizeof(screen_app__msg__Mouse));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = screen_app__msg__Mouse__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        screen_app__msg__Mouse__fini(&data[i - 1]);
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
screen_app__msg__Mouse__Sequence__fini(screen_app__msg__Mouse__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      screen_app__msg__Mouse__fini(&array->data[i]);
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

screen_app__msg__Mouse__Sequence *
screen_app__msg__Mouse__Sequence__create(size_t size)
{
  screen_app__msg__Mouse__Sequence * array = (screen_app__msg__Mouse__Sequence *)malloc(sizeof(screen_app__msg__Mouse__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = screen_app__msg__Mouse__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
screen_app__msg__Mouse__Sequence__destroy(screen_app__msg__Mouse__Sequence * array)
{
  if (array) {
    screen_app__msg__Mouse__Sequence__fini(array);
  }
  free(array);
}
