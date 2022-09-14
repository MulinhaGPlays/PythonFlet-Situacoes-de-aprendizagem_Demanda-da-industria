from flet import AppBar, ElevatedButton, Text, colors, Row

def Style_AppBar(title, btn1_name, btn2_name="", btn3_name="", btn4_name="", btn1_route="", btn2_route="", btn3_route="", btn4_route=""):
    return [
            AppBar(bgcolor=colors.SURFACE_VARIANT,
                   leading=Text(title),
                   title=Row([ElevatedButton(btn1_name, 
                                             on_click=btn1_route,
                                            ),
                              ElevatedButton(btn2_name, 
                                             on_click=btn2_route,
                                            ),
                              ElevatedButton(btn3_name, 
                                             on_click=btn3_route,
                                            ),
                              ElevatedButton(btn4_name, 
                                             on_click=btn4_route,
                                            ),
                            ]),
                  ),
           ]