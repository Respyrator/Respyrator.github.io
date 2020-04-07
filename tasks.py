# Copyright (C) 2020 Respyrador
# This file is part of Respyrador <https://respyrator.github.io/respirador/>.
#
# Respyrador is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Respyrador is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Respyrador.  If not, see <http://www.gnu.org/licenses/>.

from invoke import task

@task
def install(c):
    c.run("pipenv install")

@task
def shell(c):
    c.run("pipenv shell")

@task
def test(c):
    c.run("pipenv run test")

@task
def lint(c):
    c.run("pydocstyle src")
    c.run("mypy src")
    c.run("flake8 src")
    # Disable bad-continuation because there is a conflict between pylint and
    # black:
    #   - https://github.com/psf/black/issues/48
    #   - https://github.com/PyCQA/pylint/issues/289
    c.run("pylint --didable=bad-continuation src")

@task
def format(c):
    # It is not possible to install black using pipenv because how psf (the 
    # developers of the black package) name their versions:
    # - https://github.com/psf/black/issues/822
    try:
        import black
    except ImportError:
        c.run("pip install black")
    c.run("black -l 79 src")
