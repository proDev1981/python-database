from ast import Lambda
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk , Gdk

id = "id"
value = "value"
title = "title"
className = "className"
width = "width"
height = "height"
spacing = "spacing"
orientation = "orientatio" # Gtk.Orientation.(VERTICAL , HORIZONTAL)
visible = "visible" # boolean
xalign = "xalign"  #float
yalign = "yalign"
padding = "padding"
opacity = "opacity"
#package child in box
expand = "expand" # boolean
fill = "fill" # boolean
position = "position"
# window
decorated = "decorated"
transparent = "transparent"
placeholder = "placeholder"
# eventos
onClick = "onClick"
onChange = "onChange"
onSubmit = "onSubmit"

def btn_on(e):
    print("press")

def move(e):
    win = e.get_parent()
    while win.get_name() != "GtkWindow":
        win = win.get_parent()
        print(win.get_name())
    win.set_decorated(not win.get_decorated())

def prueba(e):
    print(e.get_text())
    Gtk.main_quit()

def win(props,body):

    global colors

    def draw(widget,cr):
        Gdk.cairo_set_source_rgba(cr, Gdk.RGBA(red= colors[0],green= colors[1],blue= colors[2],alpha= colors[3]))
        cr.paint()
        return False
    def getTrasparent(str):
        colors = str.split(",")
        cont = 0
        for color in colors:
            colors[cont] = float(color)
            cont = cont+1
        return colors

    win = Gtk.Window()

    if position in props:
        if props[position] == "center":
            win.set_position(Gtk.WindowPosition.CENTER)
        if props[position] == "mouse":
             win.set_position(Gtk.WindowPosition.MOUSE)

    if transparent in props:
        colors = getTrasparent(props[transparent])
        win.set_app_paintable(True)
        screen = win.get_screen()
        visual = screen.get_rgba_visual()
        win.set_visual(visual)
        win.connect('draw', draw )
    if opacity in props:
        win.set_opacity(props[opacity])
    if decorated in props:
        win.set_decorated(props[decorated])
    if className in props:
        win.get_style_context().add_class(props[className])
    if id in props:
        win.set_name(props[id])
    if title in props:
        win.set_title(props[title])
    if body != None:
        win.add(body)
    win.show_all()
    return win

def button(props):

    btn = Gtk.Button()
    if xalign in props:
        btn.set_xalign(props[xalign])
    if yalign in props:
        btn.set_yalign(props[yalign])
    if opacity in props:
        btn.set_opacity(props[opacity])
    if visible in props:         
        btn.set_visible(props[visible])
    if value in props:
        btn.set_label(props[value])
    if id in props:
        btn.set_name(props[id])
    if className in props:
        btn.get_style_context().add_class(props[className])
    if width in props and height in props:
        btn.set_size_request(props[width], props[height])
    if onClick in props:
        btn.connect("clicked",props[onClick])
    return btn

def label(props):
    label=Gtk.Label()
    if xalign in props:
        label.set_xalign(props[xalign])
    if yalign in props:
        label.set_yalign(props[yalign])
    if opacity in props:
        label.set_opacity(props[opacity])
    if visible in props:         
        label.set_visible(props[visible])
    if  value in props:
        label.set_label(props[value])
    if width in props and height in props:
        label.set_size_request(props[width],props[height])
    if className in props:
        label.get_style_context().add_class(props[className])
    if id in props:
        label.set_name(props[id]) 
    return label

def entry(props):
    entry=Gtk.Entry()
    if placeholder in props:
        entry.set_placeholder_text(props[placeholder])
    if xalign in props:
        entry.set_xalign(props[xalign])
    if yalign in props:
        entry.set_yalign(props[yalign])
    if opacity in props:
        entry.set_opacity(props[opacity])
    if visible in props:         
        entry.set_visible(props[visible])
    if  value in props:
        entry.set_entry(props[value])
    if width in props and height in props:
        entry.set_size_request(props[width],props[height])
    if className in props:
        entry.get_style_context().add_class(props[className])
    if id in props:
        entry.set_name(props[id]) 
    if onSubmit in props:
        entry.connect("activate",props[onSubmit])
    if onChange in props:
        entry.connect("changed",props[onChange])
    return entry

def box(props,childs):
    
    fi = False
    exp = False
    pos = 0
    if expand in props:
        exp = props[expand]
    if fill in props:
        fi = props[fill]
    if position in props:
        pos = props[position]
    box = Gtk.Box()
    if orientation in props:
        if props[orientation] == "vertical":
            box.set_orientation(Gtk.Orientation.VERTICAL)
        elif props[orientation] == "horizontal":
            box.set_orientation(Gtk.Orientation.HORIZONTAL)
    if spacing in props:
        box.set_spacing(props[spacing])
    if id in props:
        box.set_name(props[id])
    if className in props:
        box.get_style_context().add_class(props[className])
    for child in childs:
        box.pack_start(child,exp,fi,pos)
    return box

def setCss(css):
    
    style_provider = Gtk.CssProvider()
    style_provider.load_from_data(css)
 
    Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),style_provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

setCss(b""" 
    .btn{
        border-radius:10px;
        color:gray;
        background:black;
        }
    .btn:hover{
            color:white;
            border:3px solid white;
            }
    .container{
        background:transparent;
        }
    .body{
        background:none;
        }
    .label{
        color:yellow;
        font-size:50px;
    }
""")


win({className:"body",title:"app",transparent:"0,0,0,0",decorated:0,position:"mouse"},
    box({className:"container",spacing:10,orientation:"vertical"},[
      entry({className:"entry",placeholder:"algo..",onSubmit:prueba}),
        ])
)


Gtk.main()



