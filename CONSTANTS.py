from enum import Enum

COLORS = ['#d53b27', '#2e7d32', '#f07c1e', '#bf5a85', '#3873a9']
SAVE_PATH = "/home/aetos/.local/share/SlayTheSpire2/steam/76561198854416655/profile1/saves/history/"
BACKUP_FLAG = ".backup"
JSON_SCHEMA = ['acts', 'ascension', 'build_id', 'game_mode', 'killed_by_encounter', 'killed_by_event', 'map_point_history', 'modifiers', 'platform_type', 'players', 'run_time', 'schema_version', 'seed', 'start_time', 'was_abandoned', 'win']

class Character(Enum):
    IRONCLAD = "CHARACTER.IRONCLAD"
    SILENT = "CHARACTER.SILENT"
    REGENT = "CHARACTER.REGENT"
    NECROBINDER = "CHARACTER.NECROBINDER"
    DEFECT = "CHARACTER.DEFECT"


# 76561198854416655 is my ID
# macSavePath = "/Users/aidenredmond/Library/Application Support/SlayTheSpire2/steam/76561198854416655/profile1/saves/history"
