import uuid

def upload_image_formater(instance, filename):
    print(instance)
    return f'{str(uuid.uuid4())}-{filename}' 