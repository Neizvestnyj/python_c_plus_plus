// example from: http://dlib.net/face_landmark_detection_ex.cpp.html

#define DLIB_JPEG_SUPPORT
#define DLIB_PNG_SUPPORT

#include "dlib/image_processing/frontal_face_detector.h"
#include "dlib/image_processing/render_face_detections.h"
#include "dlib/image_processing.h"
#include "dlib/gui_widgets.h"
#include "dlib/image_io.h"
#include "face_landmark_detection.h"

// Default constructor
DlibLandmark::DlibLandmark() {}

// Destructor
DlibLandmark::~DlibLandmark() {}


std::vector<pair<int, int>> DlibLandmark::run(char* model, char* face) {
    // We need a face detector.  We will use this to get bounding boxes for
    // each face in an image.
    frontal_face_detector detector = get_frontal_face_detector();
    // And we also need a shape_predictor.  This is the tool that will predict face
    // landmark positions given an image and face bounding box.  Here we are just
    // loading the model from the shape_predictor_68_face_landmarks.dat file you gave
    // as a command line argument.
    shape_predictor sp;
    deserialize(model) >> sp;

    // Loop over all the images provided on the command line.
    cout << "processing image " << face << endl;
    array2d<rgb_pixel> img;
    load_image(img, face);
    // Make the image larger so we can detect small faces.
    pyramid_up(img);

    // Now tell the face detector to give us a list of bounding boxes
    std::vector<rectangle> dets = detector(img);
    cout << "Number of faces detected: " << dets.size() << endl;


    full_object_detection shape = sp(img, dets[0]);

    std::vector<pair<int, int>> ret_vector;

    for (int idx = 0; idx < 68; idx++) {
        ret_vector.push_back(make_pair(shape.part(idx).x(), shape.part(idx).y()));
    }

    cout << endl;

    return ret_vector;
}
