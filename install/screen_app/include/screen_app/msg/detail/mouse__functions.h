// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from screen_app:msg/Mouse.idl
// generated code does not contain a copyright notice

#ifndef SCREEN_APP__MSG__DETAIL__MOUSE__FUNCTIONS_H_
#define SCREEN_APP__MSG__DETAIL__MOUSE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "screen_app/msg/rosidl_generator_c__visibility_control.h"

#include "screen_app/msg/detail/mouse__struct.h"

/// Initialize msg/Mouse message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * screen_app__msg__Mouse
 * )) before or use
 * screen_app__msg__Mouse__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_screen_app
bool
screen_app__msg__Mouse__init(screen_app__msg__Mouse * msg);

/// Finalize msg/Mouse message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_screen_app
void
screen_app__msg__Mouse__fini(screen_app__msg__Mouse * msg);

/// Create msg/Mouse message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * screen_app__msg__Mouse__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_screen_app
screen_app__msg__Mouse *
screen_app__msg__Mouse__create();

/// Destroy msg/Mouse message.
/**
 * It calls
 * screen_app__msg__Mouse__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_screen_app
void
screen_app__msg__Mouse__destroy(screen_app__msg__Mouse * msg);


/// Initialize array of msg/Mouse messages.
/**
 * It allocates the memory for the number of elements and calls
 * screen_app__msg__Mouse__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_screen_app
bool
screen_app__msg__Mouse__Sequence__init(screen_app__msg__Mouse__Sequence * array, size_t size);

/// Finalize array of msg/Mouse messages.
/**
 * It calls
 * screen_app__msg__Mouse__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_screen_app
void
screen_app__msg__Mouse__Sequence__fini(screen_app__msg__Mouse__Sequence * array);

/// Create array of msg/Mouse messages.
/**
 * It allocates the memory for the array and calls
 * screen_app__msg__Mouse__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_screen_app
screen_app__msg__Mouse__Sequence *
screen_app__msg__Mouse__Sequence__create(size_t size);

/// Destroy array of msg/Mouse messages.
/**
 * It calls
 * screen_app__msg__Mouse__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_screen_app
void
screen_app__msg__Mouse__Sequence__destroy(screen_app__msg__Mouse__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // SCREEN_APP__MSG__DETAIL__MOUSE__FUNCTIONS_H_
