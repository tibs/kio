Notes on setting up experimental GitHub pages support
=====================================================

https://docs.github.com/en/pages/getting-started-with-github-pages

I'm going to work with a user site, for simplicity.

https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

First, I need a repository called tibs.github.io

Then setup (my fork of kio) https://github.com/tibs/kio

Let's setup to publish when changes are pushed to main.

Follow
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

Select ``main`` as the branch and ``/docs`` as the folder

Add an `index.md` file into the `docs` folder.

Commit and push (to main)

And lo, there's https://tibs.github.io/kio/ which shows the content of that `index.md`

*However* all the reStructuredText docs for use with sphinx is stored in
`docs`, so I *probably* want to have a `builds` directory as my source of publ


.. code:: shell

  cd docs
  python -m venv venv
  source venv/bin/activate.fish
  pip install -r requirements.txt
  make html

I get problems importing from kio - presumably because I've not created a
virtual environment at the top level to allow kio to work. Let's ignore that
for one moment and look at the output in ``_build/html``

Oh, of course, I need to remove the extra ``index.md`` file and ``make clean; make html``

OK, basic structure is there, but not the introspection we want of the source
code.

.. code:: shell

  deactivate
  rm -rf venv
  cd ..                 # back to the main kio directory
  python -m venv venv
  source venv/bin/activate.fish
  pip install --require-virtualenv -e .[all]

Ah, I need Python 3.11

.. code:: shell

  deactivate
  rm -rf venv
  pyenv install 3.11    # it's building 3.11.7
  pyenv local 3.11
  python -m venv venv
  source venv/bin/activate.fish
  pip install --require-virtualenv -e .[all]

and that completes. *Now* let's go back into the ``docs`` directory and try
again:

.. code:: shell

  cd docs
  pip install -r requirements.txt
  make html

and *now* all the API documentation is present and accounted for within
``_build/html``.

Since the Settings for the repository allows me to choose either ``/`` or
``/docs`` as the place to publish documentation from, let's do some hackery:

.. code:: shell

  cd ..               # back to the main directory
  mv docs docs-source
  cp -a docs-source/_build/html docs

  git add docs docs-source

Then commit and push - and that *does* publish stuff to
https://tibs.github.io/kio/ but I've mucked up all the theming

Ah - it's a limitation of Pages. I need to use a GitHub action to publish.

So let's put the ``docs-source`` back as ``docs`` again..

.. code:: shell

  git rm -rf docs
  git mv docs-source docs

Let's try using the workflow action at
https://github.com/marketplace/actions/sphinx-to-github-pages,
putting the action in ``.github/workflows/sphinx.yml``
and setting up the GitHub Pages setting for the repository as indicated.

Add, commit and push the action.
