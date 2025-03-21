from pkgmt.github import get_repo_and_branch_for_readthedocs

repository_url, repository_branch = get_repo_and_branch_for_readthedocs(
    repository_url="https://github.com/ploomber/jupysql",
    default_branch="master",
)

###############################################################################
# Auto-generated by `jupyter-book config`
# If you wish to continue using _config.yml, make edits to that file and
# re-generate this one.
###############################################################################
author = "Ploomber"
comments_config = {"hypothesis": False, "utterances": False}
copyright = "2023"
exclude_patterns = ["**.ipynb_checkpoints", ".DS_Store", "Thumbs.db", "_build"]
execution_allow_errors = False
execution_excludepatterns = ["howto/*-connect.ipynb", "integrations/mindsdb.ipynb"]
execution_in_temp = False
execution_show_tb = True
execution_timeout = 90
extensions = [
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "myst_nb",
    "jupyter_book",
    "sphinx_thebe",
    "sphinx_comments",
    "sphinx_external_toc",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_book_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "matplotlib.sphinxext.plot_directive",
    "sphinx_jupyterbook_latex",
]
external_toc_exclude_missing = False
external_toc_path = "_toc.yml"
html_baseurl = ""
html_favicon = ""
html_logo = "square-no-bg-small.png"
html_sourcelink_suffix = ""
html_theme = "sphinx_book_theme"
html_theme_options = {
    "search_bar_text": "Search this book...",
    "launch_buttons": {
        "notebook_interface": "jupyterlab",
        "binderhub_url": "https://binder.ploomber.io",
        "jupyterhub_url": "",
        "thebe": False,
        "colab_url": "",
    },
    "path_to_docs": "doc",
    "repository_url": repository_url,
    "repository_branch": repository_branch,
    "google_analytics_id": "G-JBZ8NNQSLN",
    "extra_navbar": 'Join us on <a href="https://ploomber.io/community/">Slack!</a>',
    "extra_footer": "",
    "home_page_in_toc": True,
    "announcement": "To launch any tutorial in JupyterLab, \
        click on the 🚀 button below!",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": True,
}
html_title = "JupySQL"
jupyter_cache = ""
jupyter_execute_notebooks = "force"
latex_engine = "pdflatex"
myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "linkify",
    "substitution",
    "tasklist",
]
myst_url_schemes = ["mailto", "http", "https"]
nb_output_stderr = "show"
numfig = True
plot_html_show_formats = False
plot_html_show_source_link = False
plot_include_source = True
pygments_style = "sphinx"
suppress_warnings = ['misc.highlighting_failure']
use_jupyterbook_latex = True
use_multitoc_numbering = True
