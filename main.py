import cv2
from typing import Any
from pathlib import Path

def get_color(event: int, x: int, y: int, flags: int, param: Any) -> None:
    """
    Обработчик событий мыши для окна OpenCV. Извлекает и выводит цвет пикселя по клику.

    Args:
        event (int): Код произошедшего события мыши.
        x (int): Координата X курсора в окне в момент события.
        y (int): Координата Y курсора в окне в момент события.
        flags (int): Дополнительные флаги OpenCV, связанные с событием.
        param (Any): Пользовательские данные, переданные при регистрации функции 
                     (в данном случае - загруженное изображение).

    Returns:
        None
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        image = param
        b, g, r = image[y, x]
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        
        print(f"Координаты: ({x}, {y}) | RGB: ({r}, {g}, {b}) | HEX: {hex_color}")

def run_eyedropper(file_path: Path) -> None:
    """
    Загружает изображение и открывает интерактивное окно пипетки.
    
    Args:
        file_path (Path): Путь к файлу изображения.

    Returns:
        None
    """
    try:
        image = cv2.imread(str(file_path))
        cv2.imshow("RefBoard eyedropper", image)
        cv2.setMouseCallback("RefBoard eyedropper", get_color, param=image)

        print("Кликайте по изображению для захвата цвета. Нажмите 'q' или ESC для выхода.")

        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord('q'):
                break

        cv2.destroyAllWindows()

    except cv2.error:
        print(f"Ошибка: не удалось загрузить или отобразить изображение по пути:\n{file_path}")
        return
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return

if __name__ == '__main__':
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    
    target_image_path = data_dir / "YOUR_IMG.jpg"
    
    run_eyedropper(target_image_path)