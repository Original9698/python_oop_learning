import json


# Напишите определение класса AppConfig
class AppConfig:
    @classmethod
    def load_config(cls, json_file):
        with open(json_file, 'r') as file:
            cls.data = json.load(file)

    @classmethod
    def get_config(self, key):
        if not hasattr(self, 'data'):
            raise Exception("Config not loaded. Please call load_config() first.")

        keys = key.split(".")
        config = self.data
        for key in keys:
            if key not in config:
                return None
            config = config[key]

        return config


# Загрузка конфигурации при запуске приложения


AppConfig.load_config('app_config.json')

# Получение значения конфигурации
assert AppConfig.get_config('database') == {
    'host': '127.0.0.1', 'port': 5432,
    'database_name': 'postgres_db',
    'user': 'owner',
    'password': 'ya_vorona_ya_vorona'}
assert AppConfig.get_config('database.user') == 'owner'
assert AppConfig.get_config('database.password') == 'ya_vorona_ya_vorona'
assert AppConfig.get_config('database.pass') is None
assert AppConfig.get_config('password.database') is None

config = AppConfig()
assert config.get_config('max_connections') == 10
assert config.get_config('min_connections') is None

conf = AppConfig()
assert conf.get_config('max_connections') == 10
assert conf.get_config('database.user') == 'owner'
assert conf.get_config('database.host') == '127.0.0.1'
assert conf.get_config('host') is None

print('Good')
