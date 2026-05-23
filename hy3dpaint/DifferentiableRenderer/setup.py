from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext = Pybind11Extension(
    "mesh_inpaint_processor",
    ["mesh_inpaint_processor.cpp"],
    extra_compile_args=["/O2", "/std:c++17"],
)

setup(
    name="mesh_inpaint_processor",
    ext_modules=[ext],
    cmdclass={"build_ext": build_ext},
)
