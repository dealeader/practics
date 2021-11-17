# practics

## filter.py
![filter py](https://user-images.githubusercontent.com/85246152/142204321-f6ec18c5-915e-4f86-b74d-0dc242f1396a.png)
Наибольшее время отнял ввод данных в консоль, сами функции сделали 1296 вызовов, функция сбора фотографии сделала 1 вызов.
В сумме выполнение функций заняло ~60 миллисекунд

## old_filter.py
![old_filter py](https://user-images.githubusercontent.com/85246152/142204757-0ebb0eb2-24bb-4a9a-a87b-aba06ad58a63.png)
Функций в скрипте нет, поэтому показывается общее время выполнения скрипта, которое занимает ~1100 миллисекунд, на первый взгляд работает быстрее, без учета ввода данных, работает в десятки раз медленнее.

## filter_with_filename.py
![filter with filename py](filter_with_filename_profile.png)
Теперь данные введены напрямую в скрипте, общее время выполнения сократилось до 474 миллисекунд, что в 2 раза меньше, чем изначальная реализация

### Тест функции get_image_brightness
![get image brightness](test1.png)

### Тест функции create_img_bit
![creat img bit](test2.png)

### Тест функции create_image
![create image](test3.png)