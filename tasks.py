"""Management tasks."""
from typing import List

from invoke import Exit, Failure, Result, UnexpectedExit, task


class _CollectFailures:
    def __init__(self, ctx):
        self._failed: List[Result] = []
        self._ctx = ctx

    def run(self, command: str, **kwargs):
        kwargs.setdefault("warn", True)
        cmd_result: Result = self._ctx.run(command, **kwargs)
        if cmd_result.ok:
            self._ctx.run("echo Ok")
        else:
            self._failed.append(cmd_result)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._failed:
            raise UnexpectedExit(self._failed[0])


@task
def build_for_mac(ctx):
    ctx.run("pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' "
            "--add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py", pty=True)


@task
def build_for_windows(ctx):
    ctx.run("pyinstaller part_manager.py --onefile --windowed --noconsole", pty=True)


# ========
# def _get_changed_files(ctx, extension=".py"):
#     output = ctx.run("git diff --name-only", hide=True).stdout
#     return " ".join(f for f in output.splitlines() if extension and f.endswith(extension))
#
#
# @task
# def test(ctx):
#     """Run tests."""
#     # Note: use commandline arguments instead of using `adopts` in `setup.cfg`,
#     # since pytest-cov breaks Intellij IDEA debugger.
#     ctx.run("poetry run pytest --cov=app -vv .", pty=True)
#
#
# @task
# def check(ctx):
#     """Run all static checks."""
#     ok = True
#     for check_task in (check_code, check_safety):
#         try:
#             check_task(ctx)
#         except Failure:
#             ok = False
#
#     if ok:
#         print("All checks passed.")
#     else:
#         raise Exit("One or more checks failed.")
#
#
# @task(help={"diff": "Check only the changed files."})
# def check_code(ctx, diff=False):
#     """Run static checks on Python code."""
#     files_to_check = _get_changed_files(ctx) if diff else ""
#     if diff and not files_to_check:
#         print("No changed files, skipping.")
#         return
#
#     with _CollectFailures(ctx) as new_ctx:
#         print("Checking Black formatting.")
#         new_ctx.run(f"poetry run black  --check -- { files_to_check or '.' }")
#
#         print("Checking the style.")
#         new_ctx.run(f"poetry run flake8 -- { files_to_check }")
#
#         print("Checking type safety.")
#         new_ctx.run(f"poetry run mypy { files_to_check or '.' }")
#
#
# @task(help={"diff": "Check only the changed files."})
# def fmt(ctx, diff=False):
#     """Apply automatic code formatting."""
#     files_to_check = _get_changed_files(ctx) if diff else "."
#     if not files_to_check:
#         print("No changed files, skipping.")
#         return
#
#     with _CollectFailures(ctx) as new_ctx:
#         new_ctx.run(f"poetry run isort -rc { files_to_check }")
#         new_ctx.run(f"poetry run black { files_to_check }")
#
#
# @task
# def run_dev(ctx):
#     """Run the app in development mode."""
#     ctx.run("poetry run uvicorn app.main:app --reload", pty=True)
#
#
# @task(
#     iterable=["tags"],
#     help={
#         "tags": "(List[str]): tags for images to be build",
#         "image": "(str): image name",
#         "registry": "(str): docker registry",
#     },
# )
# def build_and_push(ctx, tags, image, registry):
#     """Build image(s) and push to the docker hub.
#
#     Note: you should previously be logged in to the docker registry
#
#     Examples:
#         >> poetry run inv build-and-push --tags latest --tags sha --image name --registry address
#     """
#     image_constructor = f"{registry}/{image}"
#
#     # build the images
#     tags_commands = [f"-t {image_constructor}:{tag}" for tag in tags]
#     tags_to_execute = " ".join(tags_commands)
#     ctx.run(f"docker build {tags_to_execute} .")
#
#     # push the images
#     for tag in tags:
#         ctx.run(f"docker push {image_constructor}:{tag}")
