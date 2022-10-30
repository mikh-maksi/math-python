# Дійсні числа
<img src = "img/numbers01.png">

## Натуральні числа
**Натуральні числа** - це ті, якими ми рахуємо предмети: 1,2,3,4....  
Вони нам потрібні, щоб розраховувати кількість предметів, а також площу, час, відстань, температуру, тощо.

Що дозволяють зробити натуральні числа?  
Вони необхідні, щоб закодувати кількість предметів, записати це кодування, для того, щоб зберегти значення.  
Ви можете записти кількість яблук, конфет або олівців.  


Скільки яблук?  
<img src = "img/numbers08.png">

Відповідь:
**7**

|Зображення|Кількість яблук|
|:---:|:---:|
|<img src = "img/Apples02.png"> | 2 |
|<img src = "img/Apples03.png"> | 3 |
|<img src = "img/Apples04.png"> | 4 |
|<img src = "img/Apples05.png"> |  |
|<img src = "img/Apples03.png"> |  |
|<img src = "img/Apples07.png"> |  |
|<img src = "img/Apples14.png"> |  |
|<img src = "img/Apples12.png"> |  |
|<img src = "img/Apples11.png"> |  |
|<img src = "img/Apples08.png"> |  |


## Python-програма
```python
import random

while True:
    a = random.randint(1, 10)
    strn = ''
    for i in range (a):
        strn +='.'
    si = input("Please, enter number of points. For stop enter .\n"+strn+"\n")
    if si == '.':
        break
    if a==int(si):
        print("true")
    else:
        print("false")
```
<img src = "img/numbers13.gif">





