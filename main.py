import flet as ft
import aiohttp as aio
import asyncio as asio


async def main(pg: ft.Page):
    #Atributos de nuestra pagina
    pg.window_width = 720
    pg.window_height = 1280
    pg.window_resizable = False
    pg.padding = 0
    pg.fonts = {
        "dungeon": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.8/zpix.ttf"   
    }
    pg.theme = ft.Theme(font_family = "dungeon")

    pokemon_actual 

    async def peticion(url):
        async with aio.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    async def evento_empty(e: ft.ContainerTapEvent):
        print("evento",e)
        resultado = await peticion("https://pokeapi.co/api/v2/pokemon/{pokemon_actual}")
        print(resultado)


    boton_azul = ft.Stack([
        ft.Container(
            width=80, height=80, 
            bgcolor=ft.colors.WHITE, 
            border_radius=50
        ),

        ft.Container(
            width=70, height=70, 
            left=5, top=5, 
            bgcolor=ft.colors.BLUE, 
            border_radius=50
        )

    ])

    items_superior = [

        ft.Container(
            boton_azul,
            width=80, height=80
        ),

        ft.Container(
            width=40, height=40,
            bgcolor=ft.colors.RED_300,
            border_radius=50
        ),

        ft.Container(
            width=40, height=40,
            bgcolor=ft.colors.YELLOW_300,
            border_radius=50
        ),

        ft.Container(
            width=40, height=40,
            bgcolor=ft.colors.BROWN_400,
            border_radius=50
        ),
    ]

    stack_central = ft.Stack([
        ft.Container(width=600, height=400, bgcolor=ft.colors.WHITE),
        ft.Container(width=550, height=350, bgcolor=ft.colors.BLACK, top=25, left=25),
        ft.Image(
            src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/122.png",
            scale=10,
            width=50,
            height=50,
            top=350/2,
            right=550/2
        )
    ])

    triangulo = ft.canvas.Canvas([
        ft.canvas.Path
        (
            [
                ft.canvas.Path.MoveTo(40,0),
                ft.canvas.Path.LineTo(0,50),
                ft.canvas.Path.LineTo(80,50),
            ],

        paint = ft.Paint(style=ft.PaintingStyle.FILL),
        ),
    ],
    width=80,
    height=50,
    
    )


    flechas = ft.Column(
        [
            ft.Container(triangulo,width=80, height=50, on_click=evento_empty),

            ft.Container(triangulo,rotate=ft.Rotate(angle=3.14159),width=80, height=50),
        ]
    )

    texto = ft.Text(
        value="Hola mucho gusto",
        color=ft.colors.BLACK
    )
    items_inferior = [
        ft.Container(width=50, border=ft.border.all()), #Margen Izquierdo

        ft.Container(texto,padding=10,width=400, height=300, bgcolor=ft.colors.GREEN,border_radius=20),

        ft.Container(flechas, width=80, height=120),

        ft.Container(width=50, border=ft.border.all()), #Margen derecho

        
    ]



    superior = ft.Container(
        content=ft.Row(items_superior), 
        width=600, height=80, 
        margin=ft.margin.only(top=40), 
        #border=ft.border.all()
    )
    centro = ft.Container(
        content=stack_central,
        width=600, height=400, 
        margin=ft.margin.only(top=40), 
        alignment=ft.alignment.center
        #border=ft.border.all()
    )
    
    inferior = ft.Container(
        content=ft.Row(items_inferior),
        width=600, height=400, 
        margin=ft.margin.only(top=40), 
        #border=ft.border.all()
    )

    col = ft.Column(spacing=0,controls=[
        superior,
        centro,
        inferior
    ])


    contenedor = ft.Container(col, width=720,height=1280, bgcolor=ft.colors.CYAN_ACCENT, alignment=ft.alignment.top_center)


    await pg.add_async(contenedor)

ft.app(target=main)