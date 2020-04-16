"""Management tasks."""
from invoke import task


@task
def build_for_mac(ctx):
    ctx.run(
        "pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' "
        "--add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' app/run.py",
        pty=True,
    )


@task
def build(ctx):
    ctx.run("pyinstaller app/run.py --onefile --windowed --noconsole", pty=True)
