#include <pybind11/pybind11.h>
#include "logic.h"

namespace py = pybind11;

PYBIND11_MODULE(logic, m) {
    m.def("get_productivity", &get_productivity);
    m.def("get_motivation", &get_motivation);
};