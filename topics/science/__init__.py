# Import the full-featured science modules
from .ecology import ecology_page
from .genetics import genetics_page  
from .earth_science import earth_science_page

# Placeholder modules for remaining science topics
import flet as ft

def chemistry_page(page: ft.Page):
    page.title = "Chemistry - Science Hub"
    page.scroll = ft.ScrollMode.AUTO
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/science")),
        title=ft.Text("Chemistry"),
        bgcolor=ft.Colors.TEAL_700,
        center_title=True
    )
    
    content = ft.Container(
        ft.Column([
            ft.Text("🧪 Chemistry", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900, text_align=ft.TextAlign.CENTER),
            ft.Text("Discover atoms, molecules, reactions, and the periodic table", size=16, color=ft.Colors.TEAL_700, text_align=ft.TextAlign.CENTER),
            ft.Text("Full module coming soon! This will include atomic structure, chemical bonds, and reactions.", size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER)
        ], spacing=20),
        padding=30,
        expand=True
    )
    page.add(content)

def earth_science_page(page: ft.Page):
    page.title = "Earth Science - Science Hub"
    page.scroll = ft.ScrollMode.AUTO
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/science")),
        title=ft.Text("Earth Science"),
        bgcolor=ft.Colors.INDIGO_700,
        center_title=True
    )
    
    content = ft.Container(
        ft.Column([
            ft.Text("🌍 Earth Science", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900, text_align=ft.TextAlign.CENTER),
            ft.Text("Study rocks, weather, climate, and our planet's systems", size=16, color=ft.Colors.INDIGO_700, text_align=ft.TextAlign.CENTER),
            ft.Text("Full module coming soon! This will include geology, meteorology, and astronomy.", size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER)
        ], spacing=20),
        padding=30,
        expand=True
    )
    page.add(content)

def ecology_page(page: ft.Page):
    page.title = "Ecology - Science Hub"
    page.scroll = ft.ScrollMode.AUTO
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/science")),
        title=ft.Text("Ecology"),
        bgcolor=ft.Colors.CYAN_700,
        center_title=True
    )
    
    content = ft.Container(
        ft.Column([
            ft.Text("🌿 Ecology", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_900, text_align=ft.TextAlign.CENTER),
            ft.Text("Understand ecosystems, food webs, and environmental relationships", size=16, color=ft.Colors.CYAN_700, text_align=ft.TextAlign.CENTER),
            ft.Text("Full module coming soon! This will include ecosystems, biomes, and conservation.", size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER)
        ], spacing=20),
        padding=30,
        expand=True
    )
    page.add(content)

def genetics_page(page: ft.Page):
    page.title = "Genetics - Science Hub"
    page.scroll = ft.ScrollMode.AUTO
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/science")),
        title=ft.Text("Genetics"),
        bgcolor=ft.Colors.LIME_700,
        center_title=True
    )
    
    content = ft.Container(
        ft.Column([
            ft.Text("🧬 Genetics", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.LIME_900, text_align=ft.TextAlign.CENTER),
            ft.Text("Explore DNA, heredity, evolution, and genetic engineering", size=16, color=ft.Colors.LIME_700, text_align=ft.TextAlign.CENTER),
            ft.Text("Full module coming soon! This will include Mendel's laws, DNA structure, and biotechnology.", size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER)
        ], spacing=20),
        padding=30,
        expand=True
    )
    page.add(content)
