from flet import AppBar, ElevatedButton, Text, colors, Row

def Style_AppBar(title, btn_name, route):
    return [
            AppBar(bgcolor=colors.SURFACE_VARIANT,
                   leading=Text(title),
                   center_title=True,
                   title=Row([ElevatedButton(btn_name, 
                                               on_click=route,
                                             ),
                                ElevatedButton(btn_name, 
                                               on_click=route
                                             ),
                                ElevatedButton(btn_name, 
                                               on_click=route
                                             ),
                                ElevatedButton(btn_name, 
                                               on_click=route
                                             ),
                                ElevatedButton(btn_name, 
                                               on_click=route
                                             ),
                              ]),
                  ),
           ]