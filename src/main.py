from cli_parser import get_args
from renderer import *

args = get_args()
images = gen_image_list(args)
canvas_width, canvas_height = calculate_canvas_size(images)

images = [
    resize_image_for_canvas(image, canvas_width, canvas_height) for image in images
]
images += [images[0]]
args.canvas_width = canvas_width
args.canvas_height = canvas_width

frame_buffer = []
gen_frames(images, args, frame_buffer)
save_frames(frame_buffer)
