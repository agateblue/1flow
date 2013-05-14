#
# Include your development machines hostnames here.
#
# NOTE: this is not strictly needed, as Django doesn't enforce
# the check if DEBUG==True. But Just in case you wanted to disable
# it temporarily, this could be a good thing to have your hostname
# here.
#
# If you connect via http://localhost:8000/, everything is already OK.

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.debug',
)


ALLOWED_HOSTS += [
    'localhost',
    'chani.licorn.org',
    'leto.licorn.org',
    'gurney.licorn.org'
]

INSTALLED_APPS += ('django_nose', )

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

