# -*- coding: utf-8 -*-
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


if __name__ == '__main__':
    main()
