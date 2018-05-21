from django.db import models
from django.conf import settings

class Zert_jumys(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    number = models.CharField(max_length=100)
    opisanie =  models.CharField(max_length=100,default='SOME STRING')
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('subject-detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.opisanie)

class Lit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    literature_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    izdanie = models.CharField(max_length=100, blank=True)
    stranica = models.CharField(max_length=100, blank=True)
    god = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('Н', 'Негізгі'),
        ('Қ', 'Қосымша'),
    )
    typee = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('subject-detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.literature_name)


class Literature(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    literature_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    izdanie = models.CharField(max_length=100, blank=True)
    stranica = models.CharField(max_length=100, blank=True)
    god = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('Н', 'Негізгі'),
        ('Қ', 'Қосымша'),
    )
    typee = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('subject-detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.literature_name)



class Takyryp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    number = models.CharField(max_length=100)
    takyryp_aty = models.CharField(max_length=100)
    opisanie = models.TextField(blank=True, null=True)
    zert_jumys = models.ForeignKey('Zert_jumys', on_delete=models.SET_NULL, null=True)


    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('subject-detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.takyryp_aty)


class Subject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    subject_name = models.CharField(max_length=100)
    credit = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    outcome = models.TextField(blank=True, null=True)
    takyryp = models.ManyToManyField(Takyryp, help_text="Select a genre for this book")
    literature = models.ManyToManyField(Literature, help_text="Select a genre for this book")


    def display_takyryp(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ takyryp.takyryp_aty for takyryp in self.takyryp.all()[:3] ])
    display_takyryp.short_description = 'Takyryp'

    def display_literature(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ literature.literature_name for literature in self.literature.all()[:3] ])
    display_literature.short_description = 'Literature'


    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('subject-detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.subject_name)



class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    email = models. EmailField()
    phone_numbers = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, help_text="Select a genre for this book")

    def display_subject(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ subject.subject_name for subject in self.subject.all()[:3] ])
    display_subject.short_description = 'Subject'

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('teacher-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)




class Keste(models.Model):
    apta = models.CharField(max_length=100,blank=True)
    lekcia = models.CharField(max_length=100,blank=True)
    zert = models.CharField(max_length=100,blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('keste-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.apta, self.zert)

