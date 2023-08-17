from django.db import models

class Tag(models.Model):
    """Tag to be used for a categorizing volunteer sector such as Health, Animals or Medicine"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=500, blank=True)
    website = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    LOCATION_TYPE = [
        ('On-site', 'On-site'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
    ]

    JOB_TYPE = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]

    title = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, blank=True)
    location_type = models.CharField(choices=LOCATION_TYPE, default='On-site', max_length=100)
    job_type = models.CharField(choices=JOB_TYPE, default='Full Time', max_length=20)
    tag = models.ManyToManyField(Tag, blank=True, related_name="tags")
    image = models.ImageField(blank=True, null=True, upload_to="jobs/")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}-{self.organization}"

    def get_tags(self):
        return self.tag.all()
