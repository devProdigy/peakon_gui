"""Management tasks."""
from invoke import task


@task
def build_for_mac(ctx):
    ctx.run(
        "pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' "
        "--add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py",
        pty=True,
    )


@task
def build(ctx):
    ctx.run("pyinstaller part_manager.py --onefile --windowed --noconsole", pty=True)
