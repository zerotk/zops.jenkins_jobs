# -*- coding: utf-8 -*-
import glob
from contextlib import contextmanager
from tempfile import NamedTemporaryFile

import click


click.disable_unicode_literals_warning = True


@click.group('jenkins-jobs')
def main():
    pass


@main.command()
@click.option('--branch', default='master', help='The job branch.')
def create(branch):
    """
    Create jobs.
    """
    click.echo('Jenkins-jobs create')
    for i_filename in glob.glob('jenkins-jobs/*.yml'):
        click.echo(i_filename)
        with _temp_file(_template(i_filename, branch=branch)) as oss:
            _jenkins_jobs('update', oss.name)


def _jenkins_jobs(*args):
    from jenkins_jobs.cli.entry import JenkinsJobs

    click.echo('$ jenkins-jobs {}'.format(' '.join(args)))
    jjb = JenkinsJobs(args)
    jjb.execute()


def _template(filename, **kwargs):
    import pkg_resources
    setup = pkg_resources.require('.')
    kwargs['setup.project_name'] = setup.project_name
    kwargs['setup.url'] = setup.url

    template = open(filename, 'r').read()
    return template.format(**kwargs)


@contextmanager
def _temp_file(content):
    import os
    with NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as oss:
        oss.write(content)
        oss.close()
    yield oss
    os.unlink(oss.name)
