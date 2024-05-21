from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    founded = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Full name
    in_game_name = models.CharField(max_length=50)  # In-game name
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_wiki_url(self):
        base_url = "https://liquipedia.net/valorant/"
        return base_url + self.in_game_name

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    prize_pool = models.DecimalField(max_digits=10, decimal_places=2)
    teams = models.ManyToManyField(Team, related_name='tournaments')

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
