classDiagram
    App --* Django
    Django -- Models
    Django -- Forms
    Django -- Views
    
    Django -- Templates
    Usuario -- App

    Forms <.. ModelForm
    ModelForm <|-- ProfileForm
    CrearPerfil --> ProfileForm : Usa
    
    Home --> Templates : usa
    PerfilList --> Templates  : usa
    CrearPerfil --> Templates : usa
    PeliculaList --> Templates : usa
    DetallePelicula --> Templates : usa
    RepoPeli --> Templates : usa 

    Models <|-- Perfil
    Models <|-- Pelicula
    Models <|-- Video

    Views <|-- CrearPerfil
    Views <|-- PerfilList
    Views <|-- Home
    Views <|-- PeliculaList
    Views <|-- DetallePelicula
    Views <|-- RepoPeli

    class Perfil {
        +nombre : CharField
        +edad_limmite : CharField
        +uuid : UUIDField
        +__str__()
    }

    class Pelicula {
        +titulo : CharField
        +descripcion : TextField
        +fecha_creacion: DateTimeField
        +uuid : UUIDField
        +categorias: CharField
        +idioma: CharField
        +video: Video
        +imagen: ImageField
        +edad_limmite: CharField
        +__str__()
    }

    class Video {
        +__str__()
        +titulo: CharField
        +archivo: FileField
    }

    class Home {
        +get(request, *args)
    }
    class PerfilList {
        +get(request, *args)
    }
    class CrearPerfil {
        +get(request, *args)
        +post(request, *args)
    }
    class PeliculaList {
        +get(request, *args)
    }
    class DetallePelicula {
        +get(request, *args)
    }
    class RepoPeli {
        +get(request, *args)
    }