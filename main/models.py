from django.db import models
import uuid
from django.utils.translation import gettext as _

class content(models.Model):
    id = models.UUIDField(_("UUID"), primary_key=True,
                          default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=100)
    body = models.CharField(_("Body"),max_length=250000)
    createdAt = models.DateTimeField(_("Created At"), auto_now_add=True)
    updatedAt = models.DateTimeField(_("Updated At"), auto_now=True)
    # modifiedBy = models.ForeignKey(
    #     "authorization.User", default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    @property
    def _id(self):
        return str(self._id)