# Thetford Forest Analysis

Near where I grew up lies Thetford Forest, a working forest that I used to go for walks around.

The forest itself is cordoned off into sections which undergo cycles of processing - from planting, to eventually being cut down.

The script in this repo processes satellite data from Thetford forest using the Visible Band-Difference Vegetation Index, then compares the result year on year. This way you can see where sectors of the pine have been removed.

The resulting image from running this script will black out any areas with a large VDVI difference.

## TODO

* Look at other indices for a better estimate of what's been cleared
* Write CLI wrapper  
* Look at public datasets to fetch new TIFFs automatically