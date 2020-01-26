## Чек-листы команды WAO на почту https://e.mail.ru
===

### Гурин Влад и Можаев Дмитрий. Страница регистрации

#### После ввода корректных имен, фамилии и логина, выбора поля (мужского/женского), существующей прошедшей даты, нажатия на кнопку регистрации должен происходить переход на страницу ввода капчи https://account.mail.ru/signup/verify


* Выбор домена mail, пол: мужской
* Выбор домена inbox, пол: женский
* Выбор домена list, пол: мужской
* Выбор домена bk, пол: женский, дата из високосного года (29.02.16)


* После вводе месяца и года на форме регистрации не возможно выбрать день, которого в этом месяце и году нет (например, 30.02.2016)
* Если выбрать в качестве дня рождения 31 число, а потом выбрать месяц, в котором такого числа нет (ноябрь), то день сненится на максимально возможный для этого месяца (на 30 ноября)


#### Проверка на превышение максимального размера поля (40 символов)

* После ввода в поле имени 41 символа
* После ввода в поле фамилии 41 символа


* При нажатии на кнопку регистрации у пустых полей формы регистрации должны появляться сообщения с просьбой заполнить поле
* При указании в дате дня из будущего и нажатии на кнопку регистрации должно появиться сообщение о невозможности зарегистрироваться из будущего


##### Попытка регистрации (всплывает сообщение об ошибке)

* С уже занятым логином всплывает сообщение об ошибке, что логин уже занят
* С логином, содержащим хотя бы один недопустимый символ (любой, кроме букв и цифр), всплывает сообщение об ошибке из-за использования недопустимых символов
* С логином, содержащим кириллические символы, всплывает сообщение об ошибке из-за использования кириллических символов
* С паролем, длиной менее 8-ми символов, должно появиться сообщение об ошибке регистрации со слишком коротким паролем
* Со слабым паролем должно появиться сообщение об ошибке, что выбран слабый пароль
* С паролем, совпадающим с логином, должно появиться сообщение об ошибке регистрации из-за использования личных данных в пароле
* С незаполненной капчей возникнет ошибка, что поле для ввода пустое
* С неверной капчей возникает ошибка ввода неверных данных

##### При нажатии на

* ссылку "условия использования" открывается новая вкладка с адресом "https://help.mail.ru/legal/terms/mail"
* "Не вижу код" => должна обновиться капча

###### кнопку "Назад" в окне ввода капчи должен произойти переход на страницу регистрации

* Введенные ранее данные должны сохраниться
* Должна быть возможность отредактировать введенные ранее данные и затем продолжить регистрацию


#### Вход на почту, Редактирование в форме письма

* После ввода правильной почты и пароля пользователь попадает на страницу почты с письмами
* После ввода корректной почты и неверного пароля пользователю выдается ошибка ввода неверного пароля

##### Ввод почты с определенным доменом

* Yandex
* Gmail
* Yahoo
* Rambler
* Нестандартный домен пользователя
=> После ввода почты пользователя переадресовывают на страницу почты соответствующего домена


* После ввода корректной почты и пустого пароля пользователю выдается ошибка незаполненной формы пароля


#### Проверка выхода из почты

* После ввода корректной почты и пароля пользователю отображается страница почты, после нажатия на кнопку выйти пользователя переадресовывают на 'https://mail.ru'

#### Редактирование в форме письма

##### Написать письмо, выделить это письмо, сменить:
* Шрифт на Заголовок1
* Выравнивание на "по центру"
* Отступ (увеличив)
* Отступ (2 раза увеличив и 1 раз уменьшив)


#### Устинов Игорь. Операции с письмами

##### Ввод электронной почты и проверка темы и текста письма, попадания письма в папку "Входящие" введенного адресата

* Почты данного аккаунта
* Почты другого аккаунта


* После получения нового письма в папку "Входящие" и при нажатии "кружок" слева от аватарки письма его статус изменится на "Прочитан", а всплывающее сообщение при наведении курсором на него будет "Пометить непрочитанным"
* После удаления письма (нажатием на кнопку удаления на тулбаре) оно оказывается в корзине
* После перемещения письма из корзины в папку "Входящие" оно оказывается в папке "Входящие"
* После отправки письма оно окажется в папке "Отправленные".
* При нажатии на письмо оно откроется, показав свое содержимое
* После получения письма из другого аккаунта, ответив на него, письмо придет на тот аккаунт с добавленным текстом ответа на первоначальное письмо
* После отправления письма нескольким существующим адресатам оно окажется в папке "Входящие" у каждого из этих адресатов


##### Проверка форматирования текста (после получения письма адресатом текст в письме окажется соответствующего форматирования)

* Жирное форматирование
* Курсив
* Подчеркнутое
* Зачеркнутое
* Изменение цвета:
    - Текста
    - Фона текста


#### Прищеп Дмитрий. Папки с письмами

* После создания письма и перемещения его в архив письмо должно переместиться в архив
* Если переместить только что созданное письмо в архив, а потом переместить во "Входящие", то письмо должно оказаться в папке "Входящие"


##### Cоздание письма и выделение его как важное

* Письмо должно выделиться как важное
* После снятия маркера важности письмо должно быть не выделено

##### После перемещения письма в определенную папку оно должно в ней оказаться

* "Архив"
* "Архив", а потом переместить во "Входящие"
* "Социальные сети"
* "Социальные сети", а потом переместить во "Входящие"
* "Рассылки"
* "Черновики"


##### При создании писем и попытке их отправления должна появиться ошибка отправки письма
* Пустое письмо
* Письмо без получателя
* Письмо без темы

* Если создать письмо и сохранить его как черновик, а потом открыть его в папке "Черновики" и дозаполнить, а после чего отправить, то письмо должно отправиться


##### Написание письма. Изменение формата текста. При отмене действия/форматирования письмо должно принять исходное форматирование

* Жирный формат текста
* Курсив, потом изменить на жирный, потом на подчеркнутый, а потом на зачеркнутый


* Если при написании письма добавить в него ссылку, заполнив ее свойства, то в письме должна появиться эта ссылка
