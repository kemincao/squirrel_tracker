from django.db import models
from django.utils.translation import gettext as _

class Squirrels(models, Model):
    X =models.DecimalField(
            max_digits=100,
            decimal_places = 20,
            help_text = _("Longtitude"),
    )

    Y =models.DecimalField(
            max_digits=100,
            decimal_places = 20,
            help_text = _("Latitude"),
    )

    Unique_squirrel_id = models.CharField(
            max_length = 100,
            help_text =_("Unique Squiirel ID"),
            unique = True,
            primary_key=True,
    )

    PM = "PM"
    AM = "AM"
    Shift_choices=[
            (PM, _("PM")),
            (AM, _"AM")),
    ]
    Shift = models.CharField(
            max_length = 15,
            help_text = _("Shift"),
            choices = Shift_choices,
    )

    Date = models.DateField(
            help_text = _("Date: MMDDYYYY"),
    )

    Adult="Adult"
    Juvenile="Juvenile"
    Other="Other"
    Age_choices = [
            (Adult, _("Adult")),
            (Juvenile, _("Juvenile")),
            (Other, _("Other")),
    ]
    Age=models.CharField(
            max_length=15,
            null=True
            help_text=_("Age"),
            choices = Age_choices,
    )

    Gray="Gray"
    Cinnamon = "Cinnamon"
    Black="Black"
    Other="Other"
    Primary_fur_color_choices = [
            (Gray, _("Gray")),
            (Cinnamon, _("Cinnamon")),
            (Black, _("Black")),
            (Other, _("Other")),
    ]
    Fur = models.CharField(
            max_length=15,
            null=True
            help_text=_("Primary Fur Color"),
            choices=Primary_fur_color_choices,
    )

    Ground_Plane='Ground_Plane'
    Above_Ground='Above_Ground'
    Other='Other'
    Location_choices=[
            (Ground_Plane,_('Ground Plane')),
            (Above_Ground,_('Above_Ground')),
            (Other,_('Other')),
    ]
    Location=models.CharField(
            max_length=15,
            null=True
            choices=Location_choices,
    )






Create your models here.
