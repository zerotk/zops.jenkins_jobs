# -*- coding: utf-8 -*-
import glob
from tempfile import NamedTemporaryFile

import click


click.disable_unicode_literals_warning = True


@click.group('jenkins-jobs')
def main():
    pass


@main.command()
def create():
    """
    Create jobs.
    """
    click.echo('Jenkins-jobs create')
    for i_filename in glob.glob('jenkins-jobs/*.yml'):
        template = open(i_filename, 'r').read()
        with NamedTemporaryFile(mode='w') as oss:
            content = template.format(branch='master')
            oss.write(content)
            _jenkins_jobs(
                '--conf=jenkins-jobs/jenkins-jobs.ini',
                'update',
                oss.name
            )


def _jenkins_jobs(*args):
    from jenkins_jobs.cli.entry import JenkinsJobs

    click.echo('$ jenkins-jobs {}'.format(' '.join(args)))
    jjb = JenkinsJobs(args)
    jjb.execute()


if __name__ == '__main__':
    main()
