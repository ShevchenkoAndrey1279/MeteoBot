def replacitinator(city_name: str) -> str:
    return city_name.replace('х', 'kh')\
                    .replace(' ', '_')\
                    .replace('ь', '')\
                    .replace('ж', 'zh')\
                    .replace('ю', 'yu')\
                    .replace('ы', 'y')\
                    .replace('й', 'y')
