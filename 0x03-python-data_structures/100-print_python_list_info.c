#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - function that prints the list
 * @p: pointer to objects in a python list
 * Return: void
*/
void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyListObject *list;

	list = (PyListObject *)p;
	if PyList_Check(p)
	{
		printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
		printf("[*] Allocated = %ld\n", list->allocated);
		for (; i < PyList_Size(p); i++)
			printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
	}
}
