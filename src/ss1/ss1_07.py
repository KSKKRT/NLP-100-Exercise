def template(x: int, y: str, z: float) -> str:
    return f'{x}時の{y}は{z}'

if __name__ == '__main__':
    x: int = 12
    y: str = '気温'
    z: float = 22.4
    print(template(x, y, z))