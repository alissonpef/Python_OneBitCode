class Movie:
    # Com o Construtor, podemos criar o bojeto direto na chamada dele, sem ter que fazer Classe.atributo = ...
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    # Dessa maneira, ao charmarmos print(movie) ele retorna o nome do filme, ao em vez de: <__main__.Movie object at 0x000001D7EBFF6A50>
    def __str__(self):
        return f"Filme: {self.name}"

movie = Movie("Super Mario", 2023, False, 10.0, 120)
print(movie)
print(movie.name)