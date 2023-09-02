from django.test import TestCase
from django.contrib.auth import get_user_model
from moneyed import Money
from .models import Job, Tag, Organization
from profiles.models import Profile, Jobapplication
from django.test import Client

# Create your tests here.
class TagTests(TestCase):

    def test_create_tag(self):
        name = 'Animal'
        tag = Tag.objects.create(name=name)
        self.assertEqual(tag.name, name)

class OrganizationTests(TestCase):

    def test_create_organization(self):
        name = 'UNESCO'
        website = 'www.unesco.com'
        location = 'France'
        organization = Organization.objects.create(name=name, website=website, location=location)
        self.assertEqual(organization.name, name)
        self.assertEqual(organization.website, website)
        self.assertEqual(organization.location, location)


class JobTests(TestCase):

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        username = "testuser_1001"
        password = "s897yuP&&+?12"
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password,
        )
        self.client.force_login(self.user)

    def test_create_job(self):
        title = 'Test title'
        description = 'Test description'
        job_type = 'Full Time'
        organization = Organization.objects.create(name='UNESCO')
        tag1 = Tag.objects.create(name='Health')
        tag2 = Tag.objects.create(name='Doctor')
        location = 'Greece'
        location_type = 'On-site'

        job = Job.objects.create(title=title, description=description, job_type=job_type,
                                organization=organization, location=location,
                                location_type=location_type)

        # add many to many fields
        # one job might have be related to more than one tag and one tag might be related to more than one job
        job.tag.add(tag1)
        job.tag.add(tag2)

        self.assertEqual(job.title, title)
        self.assertEqual(job.description, description)
        self.assertEqual(job.job_type, job_type)
        self.assertEqual(job.organization, organization)
        self.assertEqual(job.get_tags()[0], tag1)
        self.assertEqual(job.get_tags()[1], tag2)
        self.assertEqual(job.location, location)
        self.assertEqual(job.location_type, location_type)


class JobApplicationTests(TestCase):

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        username = "testuser_1001"
        password = "s897yuP&&+?12"
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password,
        )
        self.client.force_login(self.user)

    def test_apply_job_application(self):
        # get user profile
        profile = Profile.objects.get(user=self.user)
        # create organization
        organization = Organization.objects.create(name='Test Organization')
        # create job object
        job = Job.objects.create(title='Test title', description='Test description', job_type='Full Time', organization=organization)
        # create job application
        job_application = Jobapplication.objects.create(job=job, applicant=profile)

        self.assertEqual(job_application.job, job)
        self.assertEqual(profile.get_applied_jobs()[0], job)
        self.assertEqual(profile.get_applied_jobs_count(), 1)
        self.assertEqual(job_application.applicant, profile)
        # make sure default application status is waiting
        self.assertEqual(job_application.status, 'Waiting')

    def test_withdraw_job_application(self):
        # get user profile
        profile = Profile.objects.get(user=self.user)
        # create organization
        organization = Organization.objects.create(name='Test Organization')
        # create job object
        job = Job.objects.create(title='Test title', description='Test description', job_type='Full Time', organization=organization)
        # create job application
        Jobapplication.objects.create(job=job, applicant=profile)

        # remove job instance from applied_jobs of related Profile
        profile.applied_job.remove(job)

        self.assertEqual(len(profile.applied_job.all()), 0)


