from button import Button
from paint_module import *
import webcolors

paint = Paint(canvas_dim, canvas_dim, width, height, BLACK)
paint.make_Grid(WHITE)
paint.draw_Grid()
paint.make_menu_panel()
paint.current_color_display(paint.brush_color)

button_lis = [
    Button(screen, "White", width - (width // 3) - 93, paint.height + 10, 30, 30, 1, "1", 30, False, brush_one_icon),
    Button(screen, "White", width - (width // 3) - 61, paint.height + 10, 30, 30, 1, "2", 30, False, brush_two_icon),
    Button(screen, "White", width - (width // 3) - 29, paint.height + 10, 30, 30, 1, "3", 30, False, brush_three_icon),
    Button(screen, "White", width - (width // 3) + 3, paint.height + 10, 30, 30, 1, "4", 30, False, brush_four_icon),

    Button(screen, "White", width - (width // 3) - 29, paint.height + 42, 30, 30, 1, "Erase", 30, False, eraser_icon),
    Button(screen, "White", width - (width // 3) + 3, paint.height + 42, 30, 30, 1, "Reset", 30, False, reset_icon),
    Button(screen, "White", width - (width // 3) - 61, paint.height + 42, 30, 30, 1, "Fill", 30, False, fill_icon),
    Button(screen, "White", width - (width // 3) - 93, paint.height + 42, 30, 30, 1, "Grid", 30, False, grid_icon),
    Button(screen, "White", width - (width // 3) + 35, paint.height + 42, 30, 30, 1, "BlackWhite", 30, False, blackwhite_icon),
    Button(screen, "White", width - (width // 3) + 35, paint.height + 10, 30, 30, 1, "ColorPick", 30, False, pick_icon),
    Button(screen, "White", width - (width // 3) + 67, paint.height + 42, 30, 30, 1, "Invert", 30, False, invert_icon),

    Button(screen, "White", width - (width // 3) - 125, paint.height + 10, 30, 30, 1, "Save", 30, False,
           save_file_icon),
    Button(screen, "White", width - (width // 3) - 125, paint.height + 42, 30, 30, 1, "Open", 30, False,
           open_file_icon),

    # Row 1
    Button(screen, "Red", (width - 590), paint.height + 10, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "Orange", (width - 570), paint.height + 10, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "Yellow", (width - 550), paint.height + 10, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "GreenYellow", (width - 530), paint.height + 10, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "LawnGreen", (width - 510), paint.height + 10, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "SpringGreen", (width - 490), paint.height + 10, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "Cyan", (width - 470), paint.height + 10, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "DeepSkyBlue", (width - 450), paint.height + 10, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "Blue", (width - 430), paint.height + 10, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "DarkOrchid", (width - 410), paint.height + 10, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "Magenta", (width - 390), paint.height + 10, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "DeepPink", (width - 370), paint.height + 10, color_button_width, color_button_height, 0, "", 20),

    # Row 2
    Button(screen, "DarkRed", (width - 590), paint.height + 30, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "SaddleBrown", (width - 570), paint.height + 30, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "DarkGoldenRod", (width - 550), paint.height + 30, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "OliveDrab", (width - 530), paint.height + 30, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "ForestGreen", (width - 510), paint.height + 30, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "SeaGreen", (width - 490), paint.height + 30, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "Teal", (width - 470), paint.height + 30, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "SteelBlue", (width - 450), paint.height + 30, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "MediumBlue", (width - 430), paint.height + 30, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "BlueViolet", (width - 410), paint.height + 30, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "DarkMagenta", (width - 390), paint.height + 30, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "MediumVioletRed", (width - 370), paint.height + 30, color_button_width, color_button_height, 0, "", 20),

    # Row 3
    Button(screen, "Salmon", (width - 590), paint.height + 50, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "Bisque", (width - 570), paint.height + 50, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "LemonChiffon", (width - 550), paint.height + 50, color_button_width, color_button_height, 0, "",20),
    Button(screen, "YellowGreen", (width - 530), paint.height + 50, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "PaleGreen", (width - 510), paint.height + 50, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "Aquamarine", (width - 490), paint.height + 50, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "PaleTurquoise", (width - 470), paint.height + 50, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "CornflowerBlue", (width - 450), paint.height + 50, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "MediumPurple", (width - 430), paint.height + 50, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "MediumOrchid", (width - 410), paint.height + 50, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "HotPink", (width - 390), paint.height + 50, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "LightPink", (width - 370), paint.height + 50, color_button_width, color_button_height, 0, "", 20),

    # Row 4
    Button(screen, "Black", (width - 590), paint.height + 70, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "DimGrey", (width - 570), paint.height + 70, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "LightSlateGrey", (width - 550), paint.height + 70, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "Gray", (width - 530), paint.height + 70, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "WhiteSmoke", (width - 510), paint.height + 70, color_button_width, color_button_height, 0, "", 20),
    Button(screen, "White", (width - 490), paint.height + 70, color_button_width, color_button_height, 0, "", 20)
]

while running:
    clock.tick(120)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            if paint.isSaved is False:
                save_ans = ask_save("Save?", "Would you like to save your work before exiting?")
                if save_ans == "yes":
                    paint.image_save()
                else:
                    running = False
            else:
                running = False

        pos = pygame.mouse.get_pos()
        mouse_state = pygame.mouse.get_pressed()

        paint.mouse_coords(pos[0], pos[1])

        if mouse_state[0] is True and mouse_released is False:
            try:
                paint.draw_pixel(paint.brush_color, pos)
            except IndexError:
                for button in button_lis:
                    if button.click(pos):
                        # --------------MenuButtons----------------#
                        if button.text == "1":
                            paint.thickness = 1
                            paint.is_Fill = False
                            paint.isPicked = False
                            button.scale = 2

                        if button.text == "2":
                            paint.thickness = 2
                            paint.is_Fill = False
                            paint.isPicked = False

                        if button.text == "3":
                            paint.thickness = 3
                            paint.is_Fill = False
                            paint.isPicked = False

                        if button.text == "4":
                            paint.thickness = 4
                            paint.is_Fill = False
                            paint.isPicked = False

                        if button.text == "Erase":
                            paint.brush_color = WHITE
                            paint.thickness = 1
                            paint.isPicked = False
                            paint.current_color_display(paint.brush_color)

                        if button.text == "Reset":
                            paint.isPicked = False
                            reset_ans = ask_save("Reset", "Reset Canvas? \n (Cannot undo this action)")
                            if reset_ans == "yes":
                                paint.reset_canvas()
                                pygame.display.update()

                        if button.text == "Fill":
                            paint.is_Fill = True
                            paint.isPicked = False

                        if button.text == "Grid":
                            paint.grid_visible = not paint.grid_visible
                            paint.draw_Grid()
                            pygame.time.wait(100)

                        if button.text == "BlackWhite":
                            bw_ans = blackwhite_warn()
                            if bw_ans is True:
                                paint.image_save()
                            elif bw_ans is False:
                                paint.black_white()

                        if button.text == "Invert":
                            paint.invert_image()
                            pygame.time.wait(100)

                        if button.text == "Save":
                            paint.image_save()

                        if button.text == "Open":
                            paint.image_open()
                            paint.is_Fill = False

                        if button.text == "ColorPick":
                            paint.color_pick()
                            pygame.time.wait(100)

                        if c := button.is_color():
                            paint.brush_color = webcolors.name_to_rgb(c)
                            paint.current_color_display(paint.brush_color)

pygame.quit()
