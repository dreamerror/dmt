#include <pybind11/pybind11.h>
#include "logic.h"

namespace py = pybind11;


PYBIND11_MODULE(logic, m) {

    py::class_<Productivity>(m, "Productivity")
        .def(py::init<>())

        .def("set_qualification", &Productivity::set_qualification)
        .def("get_qualification", &Productivity::get_qualification)
        .def_property("qualification", &Productivity::get_qualification, &Productivity::set_qualification)

        .def("set_count", &Productivity::set_count)
        .def("get_count", &Productivity::get_count)
        .def_property("count", &Productivity::get_count, &Productivity::set_count)

        .def("get_motivation", &Productivity::get_motivation)
        .def_property_readonly("motivation", &Productivity::get_motivation)

        .def("get_productivity", &Productivity::get_productivity)
        .def_property_readonly("productivity", &Productivity::get_productivity);

};
