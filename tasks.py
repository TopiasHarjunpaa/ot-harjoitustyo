from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("pytest --ignore=laskarit")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest --ignore=laskarit")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def build(ctx):
    ctx.run("python3 src/build.py")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")
