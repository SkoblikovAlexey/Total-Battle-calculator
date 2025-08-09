import math

# ==== Вынесенные данные о типах войск ====

UNIT_STATS = {
    "Archer": {
        "leadership": 1,
        "strength_by_level": {
            1: 50, 2: 90, 3: 160, 4: 290, 5: 520,
            6: 940, 7: 1700, 8: 3060, 9: 5510
        }
    },
    "Spearman": {
        "leadership": 1,
        "strength_by_level": {
            1: 50, 2: 90, 3: 160, 4: 290, 5: 520,
            6: 940, 7: 1700, 8: 3060, 9: 5510
        }
    },
    "Rider": {
        "leadership": 2,
        "strength_by_level": {
            1: 100, 2: 180, 3: 320, 4: 580, 5: 1050,
            6: 1900, 7: 3400, 8: 6120, 9: 11020
        }
    },
    "BattleGriffin": {
        "leadership": 20,
        "strength_by_level": {
            5: 10000, 6: 19000, 7: 34000, 8: 61200, 9: 110200
        }
    }
}


# ==== Универсальный класс для юнита ====

class Unit:
    def __init__(self, unit_type: str, level: int):
        stats = UNIT_STATS[unit_type]
        self.unit_type = unit_type
        self.level = level
        self.name = f"{unit_type}({level})"
        self.leadership = stats["leadership"]
        self.strength = stats["strength_by_level"].get(level, 0)
        self.hp = self.strength * 3
        self.hp_per_lead = math.floor(self.hp / self.leadership)
        self.count = 0  # будет рассчитано позже


# ==== Логика подбора армии ====

def get_unit_counts(total_leadership, units, step=0, recursion_depth=0):
    num_units = len(units)
    leadership_per_unit = math.floor(total_leadership / num_units)
    
    avg_hp_per_lead = math.floor(sum(unit.hp_per_lead for unit in units) / num_units) - step
    squad_hp = avg_hp_per_lead * leadership_per_unit

    required_leadership = 0

    for unit in units:
        unit.count = math.floor(squad_hp / unit.hp)
        required_leadership += unit.count * unit.leadership

    if required_leadership > total_leadership:
        return get_unit_counts(total_leadership, units, step + 10, recursion_depth + 1)

    print(f"\n=== Расчёт завершён ===")
    print(f"Средний hp/lead: {avg_hp_per_lead}")
    print(f"Ожидаемое HP на отряд: {squad_hp}")
    print(f"Итоговое потребление лидерства: {required_leadership}")
    print(f"Количество итераций: {recursion_depth}\n")

    return units


# ==== Основной запуск ====

if __name__ == "__main__":
    user_input = int(input("Введите общее значение лидерства: "))

    # Создание армии
    army = [
        Unit("Archer", 7),
        Unit("Spearman", 5),
        Unit("Rider", 5),
        Unit("BattleGriffin", 5),
        Unit("BattleGriffin", 6)
    ]

    # Расчёт
    army = get_unit_counts(user_input, army)

    # Вывод результатов
    print("Состав армии:")
    for unit in army:
        total_hp = unit.count * unit.hp
        total_strength = unit.count * unit.strength
        print(f"{unit.name:20} | Кол-во: {unit.count:3} | HP: {total_hp:7} | Сила: {total_strength}")
