# CADE: Reverb Timing Calculator

Это репозиторий с несколькими реализациями калькулятора таймингов реверберации.

## HTML версия

Файл `index.html` представляет собой автономное приложение на чистом HTML/JS. При открытии в браузере страница загружает `genre_presets.json` прямо из GitHub и позволяет вычислять пресеты по BPM и жанру. Двойное нажатие по экрану переключает тему.

## Python версия

Оригинальное приложение на `Tkinter` находится в каталоге `CADE_ReverbCalc`.

### Запуск
```bash
python3 CADE_ReverbCalc/main.py
```
Требуется Python 3.11+ с модулем Tkinter.

## Возможности
- Расчёт задержек 1/4, 1/8, 1/16, dotted и триоль
- Выбор жанра и отображение пресетов из `genre_presets.json`
- Поддержка светлой и тёмной темы (HTML и Tkinter)
- Жанровые советы для Hip-Hop/Trap, Pop, Rock, EDM, Jazz, Reggae, Country, Metal, Classical и других

## License
MIT License. See [LICENSE](LICENSE).

GitHub: <https://github.com/CadeMind/Cade_Reverb>

---

## English

CADE: Reverb Timing Calculator contains two implementations to help you pick reverb settings.

### HTML version
Open `index.html` in a browser. It fetches `genre_presets.json` from GitHub and lets you compute presets by BPM and genre. Double click anywhere to toggle the theme.

### Python version
The original Tkinter application lives in `CADE_ReverbCalc`.

#### Run
```bash
python3 CADE_ReverbCalc/main.py
```
Requires Python 3.11+ with Tkinter.

### Features
- Delay times for 1/4, 1/8, 1/16, dotted and triplet
- Presets for various genres from `genre_presets.json`
- Light and dark themes (HTML & Tkinter)
- Tips for Hip-Hop/Trap, Pop, Rock, EDM, Jazz, Reggae, Country, Metal, Classical and more
