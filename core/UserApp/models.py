from django.db import models

from services.user_services import QueryService, CSVExporter


class Player(models.Model):
    player_id = models.CharField(max_length=100)

    def __str__(self):
        return self.player_id


class Boost(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()

    def __str__(self):
        return self.name


class PlayerBoost(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    boost = models.ForeignKey(Boost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Буст {self.boost.name} для {self.player.player_id}"


class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Prize(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Игрок {self.player.player_id} - {self.level.title}"

    @staticmethod
    def export_to_csv():
        query_set = QueryService.get_player_level()
        CSVExporter.export_player_levels(query_set=query_set)


class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateField()

    def __str__(self):
        return f"{self.level} - {self.prize}"
