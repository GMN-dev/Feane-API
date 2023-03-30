import uuid

def upload_image_formater(instance, filename):
    return f'{str(uuid.uuid4())}-{filename}'