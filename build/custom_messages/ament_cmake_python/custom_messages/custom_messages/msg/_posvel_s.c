// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from custom_messages:msg/Posvel.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "custom_messages/msg/detail/posvel__struct.h"
#include "custom_messages/msg/detail/posvel__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool custom_messages__msg__posvel__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[35];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("custom_messages.msg._posvel.Posvel", full_classname_dest, 34) == 0);
  }
  custom_messages__msg__Posvel * ros_message = _ros_message;
  {  // position1
    PyObject * field = PyObject_GetAttrString(_pymsg, "position1");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position1 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // velocity1
    PyObject * field = PyObject_GetAttrString(_pymsg, "velocity1");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->velocity1 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // position2
    PyObject * field = PyObject_GetAttrString(_pymsg, "position2");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position2 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // velocity2
    PyObject * field = PyObject_GetAttrString(_pymsg, "velocity2");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->velocity2 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // position3
    PyObject * field = PyObject_GetAttrString(_pymsg, "position3");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position3 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // velocity3
    PyObject * field = PyObject_GetAttrString(_pymsg, "velocity3");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->velocity3 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // position4
    PyObject * field = PyObject_GetAttrString(_pymsg, "position4");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position4 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // velocity4
    PyObject * field = PyObject_GetAttrString(_pymsg, "velocity4");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->velocity4 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // position5
    PyObject * field = PyObject_GetAttrString(_pymsg, "position5");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position5 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // velocity5
    PyObject * field = PyObject_GetAttrString(_pymsg, "velocity5");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->velocity5 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // position6
    PyObject * field = PyObject_GetAttrString(_pymsg, "position6");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position6 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // velocity6
    PyObject * field = PyObject_GetAttrString(_pymsg, "velocity6");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->velocity6 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // torque
    PyObject * field = PyObject_GetAttrString(_pymsg, "torque");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->torque = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * custom_messages__msg__posvel__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Posvel */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("custom_messages.msg._posvel");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Posvel");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  custom_messages__msg__Posvel * ros_message = (custom_messages__msg__Posvel *)raw_ros_message;
  {  // position1
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position1);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // velocity1
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->velocity1);
    {
      int rc = PyObject_SetAttrString(_pymessage, "velocity1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position2
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // velocity2
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->velocity2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "velocity2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position3
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position3);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // velocity3
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->velocity3);
    {
      int rc = PyObject_SetAttrString(_pymessage, "velocity3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position4
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position4);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position4", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // velocity4
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->velocity4);
    {
      int rc = PyObject_SetAttrString(_pymessage, "velocity4", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position5
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position5);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position5", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // velocity5
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->velocity5);
    {
      int rc = PyObject_SetAttrString(_pymessage, "velocity5", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position6
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position6);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position6", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // velocity6
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->velocity6);
    {
      int rc = PyObject_SetAttrString(_pymessage, "velocity6", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // torque
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->torque);
    {
      int rc = PyObject_SetAttrString(_pymessage, "torque", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
