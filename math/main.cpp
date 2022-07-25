#include <pybind11/pybind11.h>
#include "logic.h"

namespace py = pybind11;


PYBIND11_MODULE(logic, m) {

    py::class_<Productivity>(m, "Productivity")
        .def(py::init<>())
        .def("set_qualification", &Productivity::set_qualification)
        .def("set_count", &Productivity::set_count)
        .def("calc_motivation", &Productivity::calc_motivation)
        .def("calc_productivity", &Productivity::calc_productivity)
        .def("update_productivity", &Productivity::update_productivity)
        .def("get_productivity", &Productivity::get_productivity);

};
