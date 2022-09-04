import os
from PIL import Image
from typing import List, Tuple
from argparse import Namespace
from mathematical_backend import Vector


def gen_image_list(arg_obj: Namespace) -> List[Image.Image]:
    images = []
    for image_path in arg_obj.input:
        images.append(Image.open(image_path))
    return images


def calculate_canvas_size(images: List[Image.Image]) -> Tuple[int, int]:
    greatest_width, greatest_height = 0, 0
    for image in images:
        greatest_width = max(greatest_width, image.width)
        greatest_height = max(greatest_height, image.height)

    if greatest_width > 1000:
        greatest_width = 1000
        greatest_height = int(greatest_height * (1000 / greatest_width))
    #
    # if greatest_height > 1000:
    #     greatest_height = 1000
    #     greatest_height = int(greatest_width * (1000 / greatest_height))

    return greatest_width, greatest_height


def resize_image_for_canvas(image: Image.Image, canvas_width: int, canvas_height: int):
    # To fit image inside canvas we can either match the new image's width to the canvas's width or the height,
    # but to figure out which (width or height) we can use some trigonometry and compare the ratio of
    # width and height (in any order, but same order for both) of the canvas and the image to each other and if the
    # canvas's ratio is higher, then we must set new image's width equal to canvas's width and scale down height
    # respecting the original aspect ratio and if image's ratio is higher we scale down width and set height equal.

    # I refuse to believe that we live in a universe where there is no better way to calculate this. Send a PR if you
    # know how to do it better please.
    canvas_ratio = canvas_height / canvas_width
    image_ratio = image.height / image.width
    if canvas_ratio > image_ratio:
        return image.resize((
            int(canvas_width),
            int(image.height * (canvas_width / image.width))
        ))
    else:
        return image.resize((
            int(image.width * (canvas_height / image.height)),
            int(canvas_height)
        ))


def add_still_image(image: Image.Image, canvas: Image.Image, args: Namespace, frame_buffer: List[Image.Image]) -> None:
    image = image.copy()
    canvas = canvas.copy()
    canvas.paste(image, (
        int(canvas.width / 2 - image.width / 2),
        int(canvas.height / 2 - image.height / 2)
    ))
    frame_buffer.extend([canvas] * int(args.fps * args.transition_duration))


def transition_image(image1: Image.Image, image2: Image.Image, canvas: Image.Image, args: Namespace,
                     frame_buffer: List[Image.Image]) -> None:
    # image 1
    initial_position1 = Vector(
        (args.canvas_width / 2 - image1.width / 2),
        (args.canvas_height / 2 - image1.height / 2)
    )
    running_position1 = initial_position1 + Vector(0, 0)

    # image 2
    initial_position2 = Vector(
        -image2.width - args.padding,
        (args.canvas_height / 2 - image2.height / 2)
    )

    final_position = Vector(
        (args.canvas_width / 2 - image2.width / 2),
        (args.canvas_height / 2 - image2.height / 2)
    )
    running_position2 = initial_position2 + Vector(0, 0)

    for frame_number in range(int(args.fps * args.transition_duration)):
        frame_canvas = canvas.copy()
        time_elapsed = (1 / args.fps) * frame_number

        # image 1
        running_position1.x += (
                (canvas.width - initial_position1.x) * args.bezier_curve(0, 1, time_elapsed, args.transition_duration)
        )
        frame_canvas.paste(image1.copy(), (
            int(running_position1.x), int(running_position1.y)
        ))

        # image 2
        running_position2.x += ((final_position.x - initial_position2.x) *
                                args.bezier_curve(0, 1, time_elapsed, args.transition_duration))
        if running_position2.x > final_position.x:
            running_position2.x = final_position.x
        frame_canvas.paste(image2.copy(), (
            int(running_position2.x),
            int(running_position2.y)
        ))

        frame_buffer.append(frame_canvas)


def gen_canvas(width: int, height: int) -> Image.Image:
    return Image.new(
        "RGBA", (width, height), (0, 0, 0, 0)
    )


def gen_frames(images: list, args: Namespace, frame_buffer: List[Image.Image]) -> None:
    main_canvas = gen_canvas(args.canvas_width, args.canvas_height)

    add_still_image(images[0], main_canvas.copy(), args, frame_buffer)
    for i in range(1, len(images)):
        canvas = main_canvas.copy()
        transition_image(images[i - 1], images[i], canvas, args, frame_buffer)
        add_still_image(images[i], canvas, args, frame_buffer)


def save_frames(frame_buffer: List[Image.Image]) -> None:
    try:
        os.mkdir("output/")
    except FileExistsError:
        pass

    for frame_number in range(len(frame_buffer)):
        frame_buffer[frame_number].save(f"output/{frame_number}.png", "PNG")
