"""Management tasks."""
from invoke import task


@task
def build_for_mac(ctx):
    ctx.run(
        "pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' "
        "--add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' run.py",
        pty=True,
    )


@task
def build(ctx):
    ctx.run("pyinstaller run.py --onefile --windowed --noconsole", pty=True)


@task
def clear_build_data(ctx):
    ctx.run("rm run.spec", pty=True)
    ctx.run("rm -r dist build", pty=True)
