# Vk_bot
Этот бот позволит автоматически отправлять сообщения определенному человеку для того что бы все получилось нужно 
# Установить
pip install -r requirements.txt
создать .env файл с воем IDE что бы хранить переменные окружения
# Пример .env
ACCESS_TOKEN="Много много символов"
USER_ID="1234567890"

для того что бы получить токен https://vkhost.github.io/ перейдите в найстройки выберите права например "отправка сообщений", "доступ в любое время" нажмите получить и готово. Вы получите токен в адресной строке и в конце свой айди. Для тестов можете пока вставить свой USER_ID
# Пример получения токена и айди
https://oauth.vk.com/blank.html#access_token=****************************************&expires_in=0&user_id=1234567890
# Помните USER_ID
Для того что бы отпрявлять сообщения другому человеку в вк нужен его айди. Обычно заходя на страницу в адресной показан айди пользователя, но многие его меняют поэтому что бы быстро найти USER_ID откройте любую фотогорафию пользователя и в адресной строке вы можете найти айди числовой айди пользователя
# Пример 
                                   👇🏻                            👇🏻
https://vk.com/1s2g4as4?z=photo1234567890_451234247355%2Fphotos1234567890
                                   
