# /**
#  * @license
#  * Copyright 2021 Google LLC
#  *
#  * Licensed under the Apache License, Version 2.0 (the "License");
#  * you may not use this file except in compliance with the License.
#  * You may obtain a copy of the License at
#  *
#  *      http://www.apache.org/licenses/LICENSE-2.0
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
#  */

from utils.color_utils import *

# /**
#  * Provides conversions needed for K-Means quantization. Converting input to
#  * points, and converting the final state of the K-Means algorithm to colors.
#  */
class LabPointProvider:
    # /**
    #  * Convert a color represented in ARGB to a 3-element array of L*a*b*
    #  * coordinates of the color.
    #  */
    def fromInt(self, argb):
        return labFromArgb(argb)

    # /**
    #  * Convert a 3-element array to a color represented in ARGB.
    #  */
    def toInt(self, point):
        return argbFromLab(point[0], point[1], point[2])

    # /**
    #  * Standard CIE 1976 delta E formula also takes the square root, unneeded
    #  * here. This method is used by quantization algorithms to compare distance,
    #  * and the relative ordering is the same, with or without a square root.
    #  *
    #  * This relatively minor optimization is helpful because this method is
    #  * called at least once for each pixel in an image.
    #  */
    # Renamed "from" to "from_v", from is reserved in Python
    def distance(self, from_v, to):
        dL = from_v[0] - to[0]
        dA = from_v[1] - to[1]
        dB = from_v[2] - to[2]
        return dL * dL + dA * dA + dB * dB
