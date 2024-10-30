import csv
from datetime import date

from django.db.models import Prefetch, F, QuerySet


class QueryService:

    @staticmethod
    def get_player_level():
        """
        Получение QuerySet для модели PlayerLevel
        :return: QuerySet
        """
        from UserApp.models import LevelPrize, PlayerLevel
        level_prizes = LevelPrize.objects.select_related('prize')

        return PlayerLevel.objects.prefetch_related(
            Prefetch('level__levelprize', queryset=level_prizes)
        ).annotate(
            playerid=F('player__player_id'),
            level_title=F('level__title'),
            prize_title=F('level__levelprize__prize__title')
        ).values('playerid', 'level_title', 'is_completed', 'prize_title')


class CSVExporter:

    @staticmethod
    def export_player_levels(query_set: QuerySet):
        """
       Экспорт данных в файл CSV.
       """

        with open("player_levels_info.csv", mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["Player ID", "Level Title", "Is Completed", "Prize"])

            for player in query_set:
                writer.writerow([
                    player['playerid'],
                    player['level_title'],
                    player['is_completed'],
                    player['prize_title'] or "No Prize"
                ])


class UserPrize:
    def __init__(self, player_id, level_id, prize):
        self.player_id = player_id
        self.level_id = level_id
        self.prize = prize

    def give_prize(self):
        """
        Выдачи приза игроку за завершение уровня.

        """

        from UserApp.models import PlayerLevel, LevelPrize
        player_level = PlayerLevel.objects.filter(
            player__player_id=self.player_id,
            level__id=self.level_id,
            is_completed=True
        ).first()

        if player_level:
            LevelPrize.objects.create(
                level=player_level.level,
                prize=self.prize,
                received=date.today()
            )
            return True
        return False
