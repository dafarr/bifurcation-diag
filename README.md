**Chaos diagram video generator**

**chaosvid-make-images.py**

  This is the python script for generating the images
  as a sequence of png files. It is Python 2.7 compatible but
  use a 2.7 compatible version of the Pypy jit-compiler to run
  it so that it completes in 20 minutes rather than 20 hours.
  Tested on Ubuntu -- and uses Ubuntu's location of its fonts.

**chaosvid-add-reverse.sh**

  Bash script to add the reversed sequence to the images, created
  from the existing images.

**chaosvid-make-vid.sh**

  Bash script to convert png image sequence to mp4 video.
  Needs the "real" ffmpeg that's in most very recent
  Linux distros but not the "fake" ffmpeg that's a front-end to
  avconv that was in many distros until just recently.


