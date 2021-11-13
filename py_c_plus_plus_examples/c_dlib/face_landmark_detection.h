#pragma once

#include "dlib/image_processing/full_object_detection.h"

// <vector> imported in dlib `.h`

using namespace std;
using namespace dlib;

class DlibLandmark {
public:
     DlibLandmark();
    ~DlibLandmark();
    std::vector<pair<int, int>> run(char* model, char* face);
};
