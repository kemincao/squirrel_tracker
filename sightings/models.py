from django.db import models
from django.utils.translation import gettext as _

class Squirrels(models.Model):
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
            (AM, _("AM")),
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
            null=True,
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
            null=True,
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
            null=True,
            choices=Location_choices,
    )

    Specific_location=models.CharField(
            max_length=100,
            null=True,
    )

    Running = models.BooleanField(
        help_text = _('Running or not?'),
        default = False,
    )
    
    Chasing = models.BooleanField(
        help_text = _('Chasing or not?'),
        default = False,
    )
    
    Climbing = models.BooleanField(
        help_text =_('Climbing or not?'),
        default = False,
    )
    
    Eating = models.BooleanField(
        help_text = _('Eating or not?'),
        default = False,
    )
    
    Foraging = models.BooleanField(
        help_text = _('Foraging or not?'),
        default = False,
    )
   
    Other_Activities = models.CharField(
        help_text = _('Other Activities'),
        max_length =100,
        null = True,
    )
    
    Kuks = models.BooleanField(
        help_text =_('Kuks or not?'),
        default = False,
    )
    
    Quaas = models.BooleanField(
        help_text =_('Quaas or not?'),
        default = False,
    )
    
    Moans = models.BooleanField(
            help_text=_('Moans or not?'),
            default = False,
    )   
    
    Tail_Flags = models.BooleanField(
        help_text = _('Tail flags or nots?'),
        default = False,
    )

    Tail_Twitches = models.BooleanField(
        help_text = _('Tail Twitches or nots?'),
        default = False,
    )
    
    Approaches = models.BooleanField(
        help_text = _('Approaches or not?'),
        default = False,
    )
    
    Indifferent = models.BooleanField(
        help_text =_('Indifferent or not?'),
        default = False,
    )

    Runs_From = models.BooleanField(
        help_text = _('Runs From?'),
        default = False
    )

    def __str__(self):
        return self.Unique_squirrel_id

