//To compile :
// g++ -I/usr/include/python -lpython demo.cpp -o demo

#include "Python/Python.h"
#include <time.h>

PyObject *pName, *pModule, *pDict, *pClass, *pInstance, *pValue;
PyObject *sys_path; 
PyObject *path; 


/* FUNCTION PROTOTYPES */
int callPy();

int main(int argc, char *argv[])
{
    clock_t begin, end;
    double time_spent;

    ////////////// INITIALIZATIONS START  ////////////
    if (argc < 4) 
    {
        fprintf(stderr,"Usage: call python_filename class_name function_name\n");
        return 1;
    }

    Py_Initialize();
    pName = PyString_FromString(argv[1]);


    sys_path = PySys_GetObject("path"); 
    if (sys_path == NULL) 
        return NULL; 
    path = PyString_FromString(".");
    if (path == NULL) 
        return NULL; 
    if (PyList_Append(sys_path, path) < 0) 
        return NULL;


    pModule = PyImport_Import(pName);
    pDict = PyModule_GetDict(pModule);
   
    // Build the name of a callable class 
    pClass = PyDict_GetItemString(pDict, argv[2]);

    // Create an instance of the class
    if (PyCallable_Check(pClass))
    {
        pInstance = PyObject_CallObject(pClass, NULL); 
    }
    ////////////// INITIALIZATIONS ENDS  ////////////


    begin = clock();
    callPy();
    end = clock();
    printf("Elapsed 1: %f seconds\n", (double)(end - begin) / CLOCKS_PER_SEC);

    begin = clock();
    callPy();
    end = clock();
    printf("Elapsed 2: %f seconds\n", (double)(end - begin) / CLOCKS_PER_SEC);

    // Clean up
    Py_DECREF(pValue);
    Py_DECREF(pModule);
    Py_DECREF(pName);
    Py_Finalize();

    return 0;
}


int callPy() {
    pValue = PyObject_CallMethod(pInstance, "multiply2", "(ii)", 10,5);
   
    if (pValue != NULL) 
    {
        printf("Return of call : %d\n", PyInt_AsLong(pValue));
    }
    else 
    {
        PyErr_Print();
    }
    
    return 0;
}
