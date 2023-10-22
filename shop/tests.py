from django.test import TestCase


def func(an):
    return 12


@func
def ll(x):
    return x

ll(12)