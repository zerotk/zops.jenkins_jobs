# -*- coding: utf-8 -*-
import click


click.disable_unicode_literals_warning = True


@click.group()
def jobs():
    pass


@jobs.command()
def create():
    """
    Create jobs.
    """
    click.echo('Jenkins-jobs create')


if __name__ == '__main__':
    jobs()
