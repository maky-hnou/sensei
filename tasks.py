from invoke import run, task


@task
def safety():
    run('safety check')


@task
def pep8():
    run('pep8 .')


@task
def pylint():
    run('pylint *.py')


@task
def pyflakes():
    run('pyflakes .')


@task
def flake8():
    run('flake8 .')


@task
def editorconfig():
    run('git ls-files -z | grep -av patch | xargs -0 -r -n 100 $(shell npm bin)/eclint check')


@task
def xmllint():
    run('find . -name "*.xml" -exec xmllint --noout {} 2>&1 \\;')


@task
def bandit():
    run('find . -name \'*.py\' | xargs bandit')


@task(pre=[safety, pep8, pylint, pyflakes, flake8, editorconfig, xmllint, bandit])
def lint():
    pass
