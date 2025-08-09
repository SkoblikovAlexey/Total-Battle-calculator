import math


class Archer():           

    def __init__(self,level):
        self.level = level
        self.name = f"archer({self.level})" 
        strength_values = {
            1: 50,
            2: 90,
            3: 160,
            4: 290,
            5: 520,
            6: 940,
            7: 1700,
            8: 3060,
            9: 5510
        }
        self.strength = strength_values.get(level, 0)     
        self.leadership = 1   
        self.hp = self.strength * 3
        self.hp_per_lead = math.floor(self.hp / self.leadership)
class Spearman():           

    def __init__(self,level):
        self.level = level
        self.name = f"spearman({self.level})" 
        strength_values = {
            1: 50,
            2: 90,
            3: 160,
            4: 290,
            5: 520,
            6: 940,
            7: 1700,
            8: 3060,
            9: 5510
        }
        self.strength = strength_values.get(level, 0)
        self.leadership = 1         
        self.hp = self.strength * 3
        self.hp_per_lead = math.floor(self.hp / self.leadership)


class Rider():           

    def __init__(self,level):
        self.level = level
        self.name = f"rider({self.level})"        
        strength_values = {
            1: 100,
            2: 180,
            3: 320,
            4: 580,
            5: 1050,
            6: 1900,
            7: 3400,
            8: 6120,
            9: 11020
        }
        self.strength = strength_values.get(level, 0)
        self.leadership = 2               
        self.hp = self.strength * 3
        self.hp_per_lead = math.floor(self.hp / self.leadership) # соотношение хп юнита к его показателю требуемого лидерства


class Battle_griffin():           

    def __init__(self,level):
        self.level = level
        self.name = f"battle_griffin({self.level})" 
        strength_values = {
            5: 10000,
            6: 19000,
            7: 34000,
            8: 61200,
            9: 110200
        }
        self.strength = strength_values.get(level, 0)
        self.leadership = 20      
        self.hp = self.strength * 3
        self.hp_per_lead = math.floor(self.hp / self.leadership)

first = Archer(7)
second = Spearman(5)
third = Rider(5)
fourth = Battle_griffin(5)
fifth = Battle_griffin(6)

squads = [first, second, third, fourth, fifth]

def get_counts(leadership, *squads, step=0, n=0):
    count_squads = len(squads)  # вычисляем количество отрядов
    lead_per_squad = math.floor(leadership / count_squads) # Вычисляем среднее количество лидерства героя на отряд 
    sum_hp_per_lead = 0 # сумма показателей юнитов (хп к лидерству) всех отрядов для вычисления их среднего арифметического
    arithmetic_mean = 0 - step # среднее арифметическое 
    for squad in squads:   
        sum_hp_per_lead += squad.hp_per_lead
    arithmetic_mean = math.floor(sum_hp_per_lead / count_squads)
    arithmetic_mean -= step
    hp_per_squad = arithmetic_mean * lead_per_squad # приблизительное суммарного хп каждого отряда, зависящее от лидерства на отряд
    required_leadership = 0 # итоговое требуемое лидерство после вычислений
    for squad in squads:
        count_warriors = math.floor(hp_per_squad / squad.hp) # кол-во юнитов в отряде (сумма хп на отряд / к хп юнита)
        required_leadership += count_warriors * squad.leadership        
        squad.count_warriors = count_warriors
        # print(squad.count_warriors)
    if required_leadership > leadership:
        n += 1
        return get_counts(leadership, *squads, step=step+10, n=n+1) # к шагу прибавляется коэф. для приближения к требуемого лидерства к заданному и возможности выйти из рекурсии
        
    return print(f"среднее арифм: {arithmetic_mean}, здоровье отряда: {hp_per_squad}, кол-во рекурсий:{n}, требуемое лидерство: {required_leadership}")
    

get_counts(3000, *squads)
for squad in squads:
    print (f"{squad.name}: {squad.count_warriors}, health: {squad.count_warriors * squad.hp}, strength: {squad.count_warriors * squad.strength}")