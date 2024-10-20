class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    videos = []
    time_video = {}
    adult_video = {}
    duration_video = {}

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        self.videos.append(self.title)
        self.time_video[title] = time_now
        self.adult_video[title] = adult_mode
        self.duration_video[title] = duration

class UrTube:
    users = []
    videos = []
    current_user = False
    age_user = {}

    def log_in(self, nickname, password):
        user_dict = {}
        user_dict[nickname] = password
        self.users.append(user_dict)
        if nickname in self.users:
            self.current_user = nickname
        print(user_dict)
        print(self.current_user)

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users.append(nickname)
            self.current_user = nickname
            self.age_user[nickname] = age
        else:
            print(f'Пользователь {nickname} уже существует')

    def add(self, *args):
        for i in range(len(args)):
            if args[i] not in self.videos:
                self.videos.append(args[i])
            else:
                pass

    def get_videos(self, name):
        name_video_list = []
        for i in range(len(Video.videos)):
            if name.lower() in Video.videos[i].lower():
                name_video_list.append(Video.videos[i])
        print(name_video_list)

    def watch_video(self, name_video):
        if name_video in Video.videos:
            if self.current_user != False:
                if Video.adult_video[name_video] == True:
                    if self.age_user[self.current_user] > 17:
                        print('1 2 3 4 5 6 7 8 9 10 Конец видео')
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    print('1 2 3 4 5 6 7 8 9 10 Конец видео')
            else:
                print('Войдите в аккаунт, чтобы смотреть видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')