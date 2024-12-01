from ..app import client
from time import sleep

def images_exists(image_name):
    images = client.images.list()
    for image in images:
        if image_name in image.tags:
            return True
    return False

def install_image(target):
    image_tags = {
        "basic": "bcBasic",
        "normal": "bcNormal",
        "pro": "bcPro"
    }
    
    image_name = image_tags.get(target)
    
    if image_name and not images_exists(image_name):
        try:
            client.images.build(path=".", tag=image_name)
            sleep(30)  # 考慮使用回調或事件來確認構建完成
        except Exception as e:
            print(f"不能建立映像 {image_name}: 錯誤： {e}")
            return None
    return image_name

def install_mach(image_name):
    try:
        container = client.containers.get(image_name)
    except Exception:
        container = None

    if image_name == "bcBasic":
        if not container:
            container = client.containers.create(image_name, command="apt update && mkdir files")
        return container
    elif image_name == "bcNormal":
        if not container:
            container = client.containers.create(image_name, command="apt update && mkdir files")
        return container
    elif image_name == "bcPro":
        if not container:
            container = client.containers.create(image_name, command="apt update && mkdir files")
        return container
    return None

__all__ = ["install_image","install_mach"]
