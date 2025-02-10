import heapq

def merge_cables(cables):
    """
    Обчислює мінімальні загальні витрати на об'єднання кабелів.
    Кожне з'єднання двох кабелів має вартість, що дорівнює сумі їхніх довжин.
    Алгоритм використовує купу для завжди вибору двох найкоротших кабелів.
    """
    if not cables:
        return 0
    if len(cables) == 1:
        return 0
    
    heapq.heapify(cables)  # Створюємо мін купу
    total_cost = 0
    
    while len(cables) > 1:
        # Вибираємо два найменші кабелі
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)
        cost = a + b
        total_cost += cost
        # Об'єднуємо кабелі і повертаємо нову довжину в купу
        heapq.heappush(cables, cost)
    
    return total_cost

if __name__ == "__main__":
    try:
        input_cables = input("Введіть довжини кабелів через пробіл: ").strip()
        if input_cables:
            cables = list(map(int, input_cables.split()))
            result = merge_cables(cables)
            print("Мінімальні загальні витрати:", result)
        else:
            print("Не надано довжин кабелів!")
    except ValueError:
        print("Будь ласка, введіть правильні числові значення.")