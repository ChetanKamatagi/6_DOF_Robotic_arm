// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_messages:msg/Posvel.idl
// generated code does not contain a copyright notice
#include "custom_messages/msg/detail/posvel__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
custom_messages__msg__Posvel__init(custom_messages__msg__Posvel * msg)
{
  if (!msg) {
    return false;
  }
  // position1
  // velocity1
  // position2
  // velocity2
  // position3
  // velocity3
  // position4
  // velocity4
  // position5
  // velocity5
  // position6
  // velocity6
  // torque
  return true;
}

void
custom_messages__msg__Posvel__fini(custom_messages__msg__Posvel * msg)
{
  if (!msg) {
    return;
  }
  // position1
  // velocity1
  // position2
  // velocity2
  // position3
  // velocity3
  // position4
  // velocity4
  // position5
  // velocity5
  // position6
  // velocity6
  // torque
}

bool
custom_messages__msg__Posvel__are_equal(const custom_messages__msg__Posvel * lhs, const custom_messages__msg__Posvel * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // position1
  if (lhs->position1 != rhs->position1) {
    return false;
  }
  // velocity1
  if (lhs->velocity1 != rhs->velocity1) {
    return false;
  }
  // position2
  if (lhs->position2 != rhs->position2) {
    return false;
  }
  // velocity2
  if (lhs->velocity2 != rhs->velocity2) {
    return false;
  }
  // position3
  if (lhs->position3 != rhs->position3) {
    return false;
  }
  // velocity3
  if (lhs->velocity3 != rhs->velocity3) {
    return false;
  }
  // position4
  if (lhs->position4 != rhs->position4) {
    return false;
  }
  // velocity4
  if (lhs->velocity4 != rhs->velocity4) {
    return false;
  }
  // position5
  if (lhs->position5 != rhs->position5) {
    return false;
  }
  // velocity5
  if (lhs->velocity5 != rhs->velocity5) {
    return false;
  }
  // position6
  if (lhs->position6 != rhs->position6) {
    return false;
  }
  // velocity6
  if (lhs->velocity6 != rhs->velocity6) {
    return false;
  }
  // torque
  if (lhs->torque != rhs->torque) {
    return false;
  }
  return true;
}

bool
custom_messages__msg__Posvel__copy(
  const custom_messages__msg__Posvel * input,
  custom_messages__msg__Posvel * output)
{
  if (!input || !output) {
    return false;
  }
  // position1
  output->position1 = input->position1;
  // velocity1
  output->velocity1 = input->velocity1;
  // position2
  output->position2 = input->position2;
  // velocity2
  output->velocity2 = input->velocity2;
  // position3
  output->position3 = input->position3;
  // velocity3
  output->velocity3 = input->velocity3;
  // position4
  output->position4 = input->position4;
  // velocity4
  output->velocity4 = input->velocity4;
  // position5
  output->position5 = input->position5;
  // velocity5
  output->velocity5 = input->velocity5;
  // position6
  output->position6 = input->position6;
  // velocity6
  output->velocity6 = input->velocity6;
  // torque
  output->torque = input->torque;
  return true;
}

custom_messages__msg__Posvel *
custom_messages__msg__Posvel__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_messages__msg__Posvel * msg = (custom_messages__msg__Posvel *)allocator.allocate(sizeof(custom_messages__msg__Posvel), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_messages__msg__Posvel));
  bool success = custom_messages__msg__Posvel__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_messages__msg__Posvel__destroy(custom_messages__msg__Posvel * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_messages__msg__Posvel__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_messages__msg__Posvel__Sequence__init(custom_messages__msg__Posvel__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_messages__msg__Posvel * data = NULL;

  if (size) {
    data = (custom_messages__msg__Posvel *)allocator.zero_allocate(size, sizeof(custom_messages__msg__Posvel), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_messages__msg__Posvel__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_messages__msg__Posvel__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
custom_messages__msg__Posvel__Sequence__fini(custom_messages__msg__Posvel__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_messages__msg__Posvel__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

custom_messages__msg__Posvel__Sequence *
custom_messages__msg__Posvel__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_messages__msg__Posvel__Sequence * array = (custom_messages__msg__Posvel__Sequence *)allocator.allocate(sizeof(custom_messages__msg__Posvel__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_messages__msg__Posvel__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_messages__msg__Posvel__Sequence__destroy(custom_messages__msg__Posvel__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_messages__msg__Posvel__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_messages__msg__Posvel__Sequence__are_equal(const custom_messages__msg__Posvel__Sequence * lhs, const custom_messages__msg__Posvel__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_messages__msg__Posvel__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_messages__msg__Posvel__Sequence__copy(
  const custom_messages__msg__Posvel__Sequence * input,
  custom_messages__msg__Posvel__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_messages__msg__Posvel);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    custom_messages__msg__Posvel * data =
      (custom_messages__msg__Posvel *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_messages__msg__Posvel__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          custom_messages__msg__Posvel__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_messages__msg__Posvel__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
