#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 *
 *@p: python object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size, list_alloc_size, i;
	PyObject *ele_p;

	if (PyList_Check(p))
	{
		list_size = PyList_Size(p);
		list_alloc_size = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %zu\n", list_size);
		printf("[*] Allocated = %zu\n", list_alloc_size);
		for (i = 0; i < list_size; i++)
		{
			ele_p = PyList_GET_ITEM(p, i);
			printf("Element %zu: %s\n", i, Py_TYPE(ele_p)->tp_name);
		}
	}
}
