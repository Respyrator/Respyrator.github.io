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
