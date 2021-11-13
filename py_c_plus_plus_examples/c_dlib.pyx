# distutils: language = c++

from libcpp.vector cimport vector
from libcpp.pair cimport pair

cdef extern from "c_dlib/face_landmark_detection.cpp":
    pass


cdef extern from "c_dlib/face_landmark_detection.h":
    cdef cppclass DlibLandmark:
        DlibLandmark() except +
        vector[pair[int, int]] run(char*, char*)


cdef class PyDlibLandmark:
    cdef DlibLandmark c_dlib

    def __init__(self):
        self.c_dlib = DlibLandmark()

    def run(self, model, face):
        return self.c_dlib.run(model, face)
