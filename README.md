![demo](https://github.com/sujaldev/gmsg/blob/main/docs/images/video.gif)

# GitHub Markdown Slideshow Generator

Some garbage code I quickly put together to create image slideshows in my GitHub
readme files. Although this does not generate a GIF file, just outputs an image sequence
then you can you use whatever tool you like to create a GIF file. I use
[gifski](https://gif.ski), you could use ffmpeg, but I didn't get good results from it.


### Usage
```
usage: gmsg [-h] -i INPUT [-f FPS] [-d DELAY] [-t TRANSITION_DURATION] [-p PADDING] [-b BEZIER_CURVE]

Utility to create slideshows for GitHub markdown.

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        A directory containing all the input images and nothing else.
  -f FPS, --fps FPS     Frames per second
  -d DELAY, --delay DELAY
                        How long for each picture to stay on screen
  -t TRANSITION_DURATION, --transition-duration TRANSITION_DURATION
                        Duration for transition animation
  -p PADDING, --padding PADDING
                        Distance between sliding images
  -b BEZIER_CURVE, --bezier-curve BEZIER_CURVE
                        Choose from: [ease, ease-in, ease-out]
```