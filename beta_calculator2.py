import math

# ==== Классы юнитов ====

class Unit:
    def __init__(self, level: int, name: str, strength_table: dict, leadership: int):
        self.level = level
        self.name = f"{name}({level})"
        self.strength = strength_table.get(level, 0)
        self.leadership = leadership
        self.hp = self.strength * 3
        self.hp_per_lead = math.floor(self.hp / self.leadership)
        self.count = 0  # будет рассчитано позже

class Archer(Unit):
    def __init__(self, level):
        super().__init__(level, "Archer", {
            1: 50, 2: 90, 3: 160, 4: 290, 5: 520,
            6: 940, 7: 1700, 8: 3060, 9: 5510
        }, leadership=1)

class Spearman(Unit):
    def __init__(self, level):
        super().__init__(level, "Spearman", {
            1: 50, 2: 90, 3: 160, 4: 290, 5: 520,
            6: 940, 7: 1700, 8: 3060, 9: 5510
        }, leadership=1)

class Rider(Unit):
    def __init__(self, level):
        super().__init__(level, "Rider", {
            1: 100, 2: 180, 3: 320, 4: 580, 5: 1050,
            6: 1900, 7: 3400, 8: 6120, 9: 11020
        }, leadership=2)

class BattleGriffin(Unit):
    def __init__(self, level):
        super().__init__(level, "BattleGriffin", {
            5: 10000, 6: 19000, 7: 34000, 8: 61200, 9: 110200
        }, leadership=20)


# ==== Функция подбора состава армии ====

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


# ==== Основной код ====

if __name__ == "__main__":
    user_input = int(input("Введите общее значение лидерства: "))

    army = [
        Archer(7),
        Spearman(5),
        Rider(5),
        BattleGriffin(5),
        BattleGriffin(6)
    ]

    army = get_unit_counts(user_input, army)

    print("Состав армии:")
    for unit in army:
        total_hp = unit.count * unit.hp
        total_strength = unit.count * unit.strength
        print(f"{unit.name:20} | Кол-во: {unit.count:3} | HP: {total_hp:7} | Сила: {total_strength}")

