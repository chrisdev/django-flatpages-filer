from django.core.files import File as DjangoFile
from filer.models.imagemodels import Image


def create_filer_image(filename, image_name, owner):
    file_obj = DjangoFile(open(filename), name=image_name)
    image = Image.objects.create(owner=owner,
                                 original_filename=image_name,
                                 file=file_obj)
    return image
