class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0

# Primeiro Filme
movie = Movie()
movie.name = "Wicked"
movie.yearLaunch = 2024
movie.includedPlan = False
movie.note = 4.0
movie.durationMinutes = 210
print("-----Dados do Filme-----")
print(f"Nome do Filme: {movie.name} - Ano de Lançamento: {movie.yearLaunch}")
