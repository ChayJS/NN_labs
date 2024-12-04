import cv2

# Загрузка изображения
image = cv2.imread('1.png')
cv2.namedWindow('Image')

if image is None: 
    print(f"Не удалось загрузить изображение по пути") 
    exit()

def get_batch_size():
    while True:
        batch_size = int(input("Введите размер батча (30-80 пикселей): "))
        if 30 <= batch_size <= 80:
            return batch_size
        else:
            print("Недопустимый ввод. Пожалуйста, введите значение в диапазоне от 30 до 80 пикселей.")

batch_size = get_batch_size()

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Координаты точки: x={x}, y={y}")
        
        # Вычисление границ батча
        x_start = max(0, x - batch_size // 2)
        y_start = max(0, y - batch_size // 2)
        x_end = min(image.shape[1], x + batch_size // 2)
        y_end = min(image.shape[0], y + batch_size // 2)

        # Извлечение батча и расчет средней интенсивности
        batch = image[y_start:y_end, x_start:x_end]
        mean_intensity = cv2.mean(batch)

        # Показ координат и средней интенсивности на изображении
        cv2.putText(image, f"({x},{y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.putText(image, f"Mean: {mean_intensity[:3]}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.imshow('Image', image)
        print(f"Средняя интенсивность по каналам (BGR): {mean_intensity[:3]}")

cv2.setMouseCallback('Image', mouse_callback)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
