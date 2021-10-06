// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from screen_app:msg/Key.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "screen_app/msg/detail/key__rosidl_typesupport_introspection_c.h"
#include "screen_app/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "screen_app/msg/detail/key__functions.h"
#include "screen_app/msg/detail/key__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `symbol`
// Member `modifiers`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void Key__rosidl_typesupport_introspection_c__Key_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  screen_app__msg__Key__init(message_memory);
}

void Key__rosidl_typesupport_introspection_c__Key_fini_function(void * message_memory)
{
  screen_app__msg__Key__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Key__rosidl_typesupport_introspection_c__Key_message_member_array[3] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(screen_app__msg__Key, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "symbol",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(screen_app__msg__Key, symbol),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "modifiers",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(screen_app__msg__Key, modifiers),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Key__rosidl_typesupport_introspection_c__Key_message_members = {
  "screen_app__msg",  // message namespace
  "Key",  // message name
  3,  // number of fields
  sizeof(screen_app__msg__Key),
  Key__rosidl_typesupport_introspection_c__Key_message_member_array,  // message members
  Key__rosidl_typesupport_introspection_c__Key_init_function,  // function to initialize message memory (memory has to be allocated)
  Key__rosidl_typesupport_introspection_c__Key_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Key__rosidl_typesupport_introspection_c__Key_message_type_support_handle = {
  0,
  &Key__rosidl_typesupport_introspection_c__Key_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_screen_app
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, screen_app, msg, Key)() {
  Key__rosidl_typesupport_introspection_c__Key_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!Key__rosidl_typesupport_introspection_c__Key_message_type_support_handle.typesupport_identifier) {
    Key__rosidl_typesupport_introspection_c__Key_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Key__rosidl_typesupport_introspection_c__Key_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
