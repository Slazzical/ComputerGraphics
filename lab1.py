import cairo

WIDTH, HEIGHT = 700, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)
context.set_source_rgb(1, 1, 1)
context.paint()

# Draw the main house body
context.set_source_rgb(0, 0, 0)
context.set_line_width(2)
context.move_to(150, 150)
context.line_to(150, 300)
context.line_to(500, 300)
context.line_to(500, 150)
context.line_to(330, 150)
context.stroke()

# Draw the bottom rectangle under the main house
context.set_source_rgb(0, 0, 0)  # Black outline
context.set_line_width(2)
context.rectangle(145, 300, 360, 20)  # (x, y, width, height)
context.stroke()

# Draw the roof (triangular shape)
context.move_to(140, 160)  # Left corner of roof
context.line_to(230, 50)   # Roof peak
context.line_to(325, 160)  # Right corner of roof
context.line_to(335, 155)
context.line_to(230, 35)
context.line_to(130, 155)
context.close_path()
context.stroke()

# Draw the remaining roof
context.move_to(500, 150)
context.line_to(515, 150)
context.line_to(410, 50)
context.line_to(245, 50)
context.stroke()

# Draw the door (window shape)
context.rectangle(190, 190, 80, 60)  # Small window (left)
context.stroke()

# Draw the door (window shape)
context.rectangle(185, 250, 90, 10)  # Small window (left)
context.stroke()

# Draw the right window
context.rectangle(390, 190, 80, 60)  # Small window (right)
context.stroke()

# Draw the right window bottom
context.rectangle(385, 250, 90, 10)  # Small window (right)
context.stroke()

context.move_to(315, 300)
context.line_to(315, 150)
context.stroke()

# Draw the upper window (small square)
context.rectangle(205, 110, 50, 50)  # Window under the roof
context.stroke()

# Draw the base (ground) line
context.move_to(150, 300)
context.line_to(450, 300)
context.stroke()

# Draw a crescent moon in the sky
context.arc(600, 80, 40, 0, 2 * 3.14)  # Full circle
context.set_source_rgb(0.9, 0.9, 0.9)  # Light gray moon
context.fill()

context.arc(590, 60, 40, 0, 2 * 3.14)  # Offset circle to create crescent
context.set_source_rgb(1, 1, 1)  # Erase part of the moon (white color)
context.fill()

# Save the image as a PNG file
surface.write_to_png("2d_house.png")

print("2D house drawing saved as '2d_house.png'")
