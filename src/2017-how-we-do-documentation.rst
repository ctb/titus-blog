How we do documentation (2017 version)
######################################

:author: C\. Titus Brown
:tags: 
:date: 2017-04-26
:slug: 2017-how-we-do-documentation
:category: teaching

In brief,

* import a copy of https://github.com/ctb/labibi into a new repo, using
  `GitHub Importer <https://help.github.com/articles/importing-a-repository-with-github-importer/>`__

* clone it to your local computer

* change into the directory

* run::

      python -m virtualenv -p python3 env

* run::

      . env/bin/activate
      pip install -r requirements.txt

* now, run::

      make

  to update html content in ``html/``, and ``make clean html`` to rebuild
  from scratch.

* add new pages to ``toc.rst``

* build your custom site off of ``index.md``.

Voila!

--titus
