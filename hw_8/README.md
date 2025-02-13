# Comparison of Change-Making Algorithms

## Greedy Algorithm (`find_coins_greedy`)

- **Approach:**  
  The greedy algorithm always picks the largest coin denomination available until the remaining amount is zero.

- **Time Complexity:**  
  O(n) where n is the number of coin denominations.  
  This is very efficient even for large sums because the algorithm depends only on the number of denominations.

- **Pros & Cons:**
  - **Pros:**  
    Simple and fast.
  - **Cons:**  
    May not always produce an optimal solution for arbitrary coin systems.  
    However, for the coin set [50, 25, 10, 5, 2, 1], it provides a valid optimal solution.

## Dynamic Programming (`find_min_coins`)

- **Approach:**  
  Uses a bottom-up approach to build a table of the minimum coins needed for every value from 0 to the target amount.

- **Time Complexity:**  
  O(amount \* n) where n is the number of coin denominations.  
  This can be slower for very large amounts because every intermediate value is computed.

- **Pros & Cons:**
  - **Pros:**  
    Always finds the optimal solution for any coin system.
  - **Cons:**  
    Higher time complexity with respect to the target amount, which may impact performance for very large sums.

## Conclusion

- **For small to moderate sums:**  
  Both algorithms perform well and yield optimal results with the given coin denominations.

- **For very large sums:**  
  The greedy algorithm is likely preferred due to its constant dependency on the number of denominations rather than the target amount.  
  Dynamic programming gives a guaranteed optimal result for arbitrary denominations but might be less efficient for extremely large targets.

This analysis shows that when the coin set has specific properties (like the one provided), the greedy algorithm can be both optimal and efficient. For more generalized coin systems, dynamic programming is a sure way to guarantee minimal coin usage.

# Порівняння алгоритмів видачі решти

## Жадібний алгоритм (`find_coins_greedy`)

- **Підхід:**  
  Жадібний алгоритм завжди вибирає найбільший доступний номінал монети, поки залишок не стане нулем.

- **Часова складність:**  
  O(n), де n – кількість номіналів монет.  
  Це дуже ефективно навіть для великих сум, оскільки алгоритм залежить лише від кількості номіналів.

- **Плюси та мінуси:**
  - **Плюси:**  
    Простий та швидкий.
  - **Мінуси:**  
    Не завжди забезпечує оптимальне рішення для довільних систем монет.  
    Проте для набору монет [50, 25, 10, 5, 2, 1] він забезпечує коректне оптимальне рішення.

## Динамічне програмування (`find_min_coins`)

- **Підхід:**  
  Використовує підхід "знизу вгору" для побудови таблиці мінімальної кількості монет, необхідних для кожного значення від 0 до цільової суми.

- **Часова складність:**  
  O(сума \* n), де n – кількість номіналів монет.  
  Це може працювати повільніше для дуже великих сум, оскільки обчислюється кожне проміжне значення.

- **Плюси та мінуси:**
  - **Плюси:**  
    Завжди знаходить оптимальне рішення для будь-якої системи монет.
  - **Мінуси:**  
    Вища часова складність щодо цільової суми, що може вплинути на продуктивність при дуже великих сумах.

## Висновок

- **Для невеликих та середніх сум:**  
  Обидва алгоритми працюють добре та дають оптимальні результати з заданими номіналами монет.

- **Для дуже великих сум:**  
  Ймовірно, перевага буде на користь жадібного алгоритму, адже він залежить лише від кількості номіналів, а не від цільової суми.  
  Динамічне програмування гарантує оптимальне рішення для довільних систем монет, але може бути менш ефективним при надзвичайно великих сумах.

Цей аналіз показує, що коли система монет має специфічні властивості (як у даному випадку), жадібний алгоритм може бути оптимальним і ефективним. Для більш узагальнених систем монет динамічне програмування є надійним способом гарантувати мінімальне використання монет.
